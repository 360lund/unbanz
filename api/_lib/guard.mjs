// Rate limits and audit log for the private /users APIs (Neon Postgres, no extra deps).
import { sql } from "./db.mjs";
let ready;
const migrate = () => (ready ||= Promise.all([sql(`create table if not exists api_rl (k text not null, win bigint not null, n int not null default 0, primary key (k, win))`), sql(`create table if not exists api_audit (id bigserial primary key, at timestamptz default now(), ip text, op text, target text, ok boolean, detail text)`)]).catch((e) => { ready = null; throw e; }));
export const ipOf = (req) => String(req.headers["x-real-ip"] || String(req.headers["x-forwarded-for"] || "").split(",")[0] || "").trim().slice(0, 64);
/** true when allowed. Fails open on DB errors so the dashboard keeps working. */
export async function limit(req, bucket, max, winSec) {
  try {
    await migrate();
    const win = Math.floor(Date.now() / 1000 / winSec);
    const r = await sql(`insert into api_rl (k, win, n) values ($1, $2, 1) on conflict (k, win) do update set n = api_rl.n + 1 returning n`, [`${bucket}:${ipOf(req)}`, win]);
    if (Math.random() < 0.02) sql(`delete from api_rl where win < $1`, [win - 2]).catch(() => {});
    return r[0].n <= max;
  } catch { return true; }
}
export async function audit(req, op, target, ok, detail = "") {
  try { await migrate(); await sql(`insert into api_audit (ip, op, target, ok, detail) values ($1,$2,$3,$4,$5)`, [ipOf(req), String(op).slice(0, 40), String(target || "").slice(0, 200), !!ok, String(detail || "").slice(0, 300)]); } catch {}
}
export async function auditList(n = 100) { await migrate(); return sql(`select at, ip, op, target, ok, detail from api_audit order by id desc limit $1`, [n]); }
