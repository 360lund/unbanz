// Logs AI and search crawler page fetches, posted by middleware.js (waitUntil). No IPs or raw user agents stored.
import { json, readJson } from "./_lib/auth.mjs";
import { sql } from "./_lib/db.mjs";
let ready;
const table = () => (ready ||= sql(`create table if not exists crawler_hits (id bigserial primary key, at timestamptz not null default now(), bot text not null, path text not null, country text, is_test boolean not null default false)`).then(() => sql(`alter table crawler_hits add column if not exists is_test boolean not null default false`)).catch((e) => { ready = null; throw e; }));
export default async function handler(req, res) {
  if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
  if (req.headers["x-ubz-mw"] !== "1") return json(res, 403, { error: "forbidden" });
  let b; try { b = await readJson(req, 2000); } catch { return json(res, 400, { error: "bad_json" }); }
  const bot = String(b.bot || "").slice(0, 40), path = String(b.path || "").slice(0, 300), country = String(b.country || "").slice(0, 4);
  if (!bot || !path.startsWith("/")) return json(res, 400, { error: "bad_input" });
  try {
    await table();
    await sql(`insert into crawler_hits(bot, path, country, is_test) values($1, $2, $3, $4)`, [bot, path, country, !!b.test]);
    return json(res, 200, { ok: true });
  } catch (e) { console.error("crawl insert failed", e.message); return json(res, 500, { error: "db_error" }); }
}
