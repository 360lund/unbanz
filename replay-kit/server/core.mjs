// Session replay: server core (framework-free, no npm dependencies).
//
//   createReplay({ sql, authed, brand, ... }) -> { ingest, replays }
//     ingest   public  POST  chunk of recorded events (called by the recorder)
//     replays  private GET   list / ids / one session's chunks   DELETE one session
//
// Everything site-specific (DB client, auth check, brand/host, table names, limits) is injected,
// so this file can be copied to another repo unchanged. See ../README.md.
import crypto from "node:crypto";
import zlib from "node:zlib";

const DEFAULTS = {
  brand: "default",              // value written to the `host` column; the dashboard only lists this brand
  visitsTable: "visits",         // existing analytics table; must have an `id` (the tracker session id) column
  chunkTable: "session_replays",
  indexTable: "session_replay_index",
  retentionDays: 14,             // replay data older than this is deleted on write / on dashboard load
  testRetentionHours: 24,        // sessions tagged as test (x=1) are kept only this long
  maxChunkBytes: 400_000,        // one request body (compressed)
  maxInflatedBytes: 8_000_000,   // zip-bomb guard for one chunk
  maxEventsPerChunk: 40_000,
  maxSessionBytes: 2_000_000,    // per session, compressed (client stops at ~1.5MB)
  maxSessionChunks: 220,
  maxChunksPerMinute: 24,        // per session
  maxSessionsPerIpHour: 40,      // new replay sessions per IP hash per hour
  maxTotalBytes: 250_000_000,    // global storage cap: new data is refused above this
  tz: "Asia/Karachi",            // dashboard "today" boundary
};

const SID = /^[a-z0-9]{8,40}$/i;
const PG = /^[a-z0-9]{3,12}$/i;
const BOT = /bot|crawl|spider|slurp|preview|headless|lighthouse/i;
const int = (v, lo, hi, d = null) => { const n = parseInt(v, 10); return Number.isFinite(n) && n >= lo && n <= hi ? n : d; };

export function createReplay(options) {
  const C = { ...DEFAULTS, ...options };
  const { sql, authed } = C;
  if (typeof sql !== "function" || typeof authed !== "function") throw new Error("createReplay: sql and authed are required");
  for (const k of ["visitsTable", "chunkTable", "indexTable"]) if (!/^[a-z_][a-z0-9_]*$/i.test(C[k])) throw new Error("bad table name " + k);
  const T = C.chunkTable, X = C.indexTable, V = C.visitsTable;

  // ---------- schema (new tables only; existing analytics tables are never touched) ----------
  let ready;
  const schema = () => (ready ||= (async () => {
    await sql(`create table if not exists ${T} (
      sid text not null, pg text not null, idx int not null, host text, payload bytea not null, gz boolean not null,
      bytes int not null, ev int not null, t0 bigint, t1 bigint, is_test boolean not null default false,
      created_at timestamptz not null default now(), primary key (sid, pg, idx))`);
    await sql(`create index if not exists ${T}_created on ${T}(created_at)`);
    await sql(`create table if not exists ${X} (
      sid text primary key, host text, is_test boolean not null default false, ih text,
      chunks int not null default 0, bytes int not null default 0, events int not null default 0, t0 bigint, t1 bigint,
      rn int not null default 0, rt timestamptz, created_at timestamptz not null default now(), updated_at timestamptz not null default now())`);
    await sql(`create index if not exists ${X}_created on ${X}(created_at)`);
    await sql(`create index if not exists ${X}_ih on ${X}(ih, created_at)`);
  })().catch((e) => { ready = null; throw e; }));

  // ---------- retention (cron-free): runs from ingest of a session's first chunk and from dashboard loads ----------
  let lastClean = 0;
  async function cleanup(force) {
    const now = Date.now();
    if (!force && now - lastClean < 10 * 60_000) return;
    lastClean = now;
    const d = `${C.retentionDays} days`, h = `${C.testRetentionHours} hours`;
    await sql(`delete from ${T} where created_at < now() - $1::interval or (is_test and created_at < now() - $2::interval)`, [d, h]);
    await sql(`delete from ${X} where created_at < now() - $1::interval or (is_test and created_at < now() - $2::interval)`, [d, h]);
  }

  const send = (res, status, body, type = "application/json; charset=utf-8") => {
    res.statusCode = status;
    res.setHeader("Cache-Control", "no-store, max-age=0");
    res.setHeader("X-Robots-Tag", "noindex, nofollow");
    res.setHeader("X-Content-Type-Options", "nosniff");
    if (body === undefined) return res.end();
    res.setHeader("Content-Type", type);
    return res.end(typeof body === "string" || Buffer.isBuffer(body) ? body : JSON.stringify(body));
  };

  async function readRaw(req, limit) {
    // Never touch req.body: the platform would try to parse it. Read the raw stream with a hard cap.
    const parts = []; let n = 0;
    for await (const c of req) { n += c.length; if (n > limit) return null; parts.push(c); }
    return Buffer.concat(parts);
  }

  // ---------- POST: ingest one chunk (public) ----------
  async function ingest(req, res) {
    if (req.method !== "POST") return send(res, 405);
    if (BOT.test(req.headers["user-agent"] || "")) return send(res, 204);
    const q = new URL(req.url, "http://x").searchParams;
    const sid = q.get("s"), pg = q.get("g"), idx = int(q.get("i"), 0, 9999), gz = q.get("z") === "1", test = q.get("x") === "1";
    const t0 = int(q.get("a"), 1e12, 4e12), t1 = int(q.get("b"), 1e12, 4e12), n = int(q.get("n"), 1, C.maxEventsPerChunk);
    if (!SID.test(sid || "") || !PG.test(pg || "") || idx == null || t0 == null || t1 == null || t1 < t0 || n == null) return send(res, 400, { error: "bad_request" });
    if (Math.abs(Date.now() - t1) > 36 * 3600e3) return send(res, 400, { error: "bad_time" });
    const cl = parseInt(req.headers["content-length"] || "0", 10);
    if (cl > C.maxChunkBytes) return send(res, 413, { error: "too_large" });
    let body;
    try { body = await readRaw(req, C.maxChunkBytes); } catch { return send(res, 400, { error: "bad_request" }); }
    if (!body) return send(res, 413, { error: "too_large" });
    if (body.length < 10) return send(res, 400, { error: "bad_request" });
    // Validate: it must really be a JSON array of rrweb-like events with the declared count.
    try {
      const txt = gz ? zlib.gunzipSync(body, { maxOutputLength: C.maxInflatedBytes }).toString("utf8") : body.toString("utf8");
      const evs = JSON.parse(txt);
      if (!Array.isArray(evs) || evs.length !== n) throw new Error("shape");
      for (const e of evs) if (!e || typeof e.type !== "number" || typeof e.timestamp !== "number") throw new Error("event");
    } catch { return send(res, 400, { error: "bad_payload" }); }

    const ip = String(req.headers["x-real-ip"] || req.headers["x-forwarded-for"] || "").split(",")[0].trim();
    const ih = crypto.createHash("sha256").update("rp|" + ip).digest("hex").slice(0, 16);
    try {
      await schema();
      const rows = await sql(
        `with up as (
           insert into ${X} as x (sid, host, is_test, ih, chunks, bytes, events, t0, t1, rn, rt)
           select $1::text, $2::text, $3::boolean, $4::text, 1, $5::int, $6::int, $7::bigint, $8::bigint, 1, now()
           where exists (select 1 from ${V} where id = $1::text)
             and (select coalesce(sum(bytes), 0) from ${X}) < $9::bigint
             and (exists (select 1 from ${X} where sid = $1::text)
                  or (select count(*) from ${X} where ih = $4::text and created_at > now() - interval '1 hour') < $10::int)
           on conflict (sid) do update set
             chunks = x.chunks + 1, bytes = x.bytes + $5::int, events = x.events + $6::int,
             t0 = least(x.t0, $7::bigint), t1 = greatest(x.t1, $8::bigint), updated_at = now(),
             rn = case when x.rt > now() - interval '1 minute' then x.rn + 1 else 1 end,
             rt = case when x.rt > now() - interval '1 minute' then x.rt else now() end
           where x.bytes + $5::int <= $11::int and x.chunks < $12::int and (x.rt <= now() - interval '1 minute' or x.rn < $13::int)
           returning sid)
         insert into ${T} (sid, pg, idx, host, payload, gz, bytes, ev, t0, t1, is_test)
         select sid, $14::text, $15::int, $2::text, decode($16::text, 'base64'), $17::boolean, $5::int, $6::int, $7::bigint, $8::bigint, $3::boolean from up
         on conflict do nothing returning 1 as ok`,
        [sid, C.brand, test, ih, body.length, n, t0, t1, C.maxTotalBytes, C.maxSessionsPerIpHour, C.maxSessionBytes, C.maxSessionChunks, C.maxChunksPerMinute, pg, idx, body.toString("base64"), gz],
      );
      if (idx === 0) cleanup().catch(() => {});
      if (rows.length) return send(res, 204);
      // Distinguish "visit row not there yet" (client retries) from a hard refusal (client stops).
      const v = await sql(`select 1 as ok from ${V} where id = $1::text`, [sid]);
      return send(res, v.length ? 429 : 404, { error: v.length ? "limit" : "no_visit" });
    } catch { return send(res, 500, { error: "server_error" }); }
  }

  // ---------- dashboard API (private) ----------
  const win = (range) => {
    const n = { today: 0, "7d": 6, "14d": 13, "30d": 29 }[range] ?? 6;
    return `r.created_at >= ((now() at time zone '${C.tz}')::date - ${n})::timestamp at time zone '${C.tz}'`;
  };
  async function replays(req, res) {
    if (!authed(req, res)) return send(res, 401, { error: "unauthorized" });
    const q = new URL(req.url, "http://x").searchParams;
    const sid = q.get("sid");
    try {
      await schema();
      if (req.method === "DELETE") {
        const o = req.headers.origin;
        if (o) { let ok = false; try { ok = new URL(o).host === req.headers.host; } catch {} if (!ok) return send(res, 403, { error: "forbidden" }); }
        if (!SID.test(sid || "")) return send(res, 400, { error: "bad_request" });
        await sql(`delete from ${T} where sid = $1::text and host = $2::text`, [sid, C.brand]);
        await sql(`delete from ${X} where sid = $1::text and host = $2::text`, [sid, C.brand]);
        return send(res, 200, { ok: true });
      }
      if (req.method !== "GET") return send(res, 405, { error: "method_not_allowed" });
      if (sid) {
        if (!SID.test(sid)) return send(res, 400, { error: "bad_request" });
        const rows = await sql(`select gz, encode(payload, 'base64') as d from ${T} where sid = $1::text and host = $2::text order by t0, pg, idx`, [sid, C.brand]);
        if (!rows.length) return send(res, 404, { error: "not_found" });
        // Binary framing: repeated [u8 gz][u32be length][bytes]. The browser inflates with DecompressionStream.
        const bufs = [];
        for (const r of rows) { const b = Buffer.from(r.d, "base64"), h = Buffer.alloc(5); h[0] = r.gz ? 1 : 0; h.writeUInt32BE(b.length, 1); bufs.push(h, b); }
        return send(res, 200, Buffer.concat(bufs), "application/octet-stream");
      }
      cleanup().catch(() => {});
      if (q.get("ids") === "1") {
        const rows = await sql(`select r.sid from ${X} r where r.host = $1::text and r.created_at > now() - $2::interval and not r.is_test`, [C.brand, `${C.retentionDays} days`]);
        return send(res, 200, { ids: rows.map((r) => r.sid) });
      }
      const p = [C.brand];
      let f = `r.host = $1 and ${win(q.get("range"))}`;
      if (q.get("test") !== "1") f += ` and not r.is_test`;
      if (q.get("source")) { p.push(q.get("source").slice(0, 40)); f += ` and v.source = $${p.length}`; }
      if (q.get("device")) { p.push(q.get("device").slice(0, 20)); f += ` and v.device = $${p.length}`; }
      if (q.get("clicked") === "1") f += ` and (v.clicked_whatsapp or v.opened_popup)`;
      if (q.get("converted") === "1") f += ` and (v.clicked_whatsapp or v.clicked_email)`;
      const rows = await sql(
        `select r.sid, r.chunks, r.bytes, r.events, r.t0, r.t1, r.is_test, r.created_at, v.started_at, v.last_at, v.source, v.source_group as g, v.country, v.city, v.device, v.browser, v.os,
                v.landing, v.pages, v.page_count, v.clicked_whatsapp, v.clicked_email, v.opened_popup, v.platform, v.service, v.scroll_max, v.active_s, v.vpn
         from ${X} r left join ${V} v on v.id = r.sid where ${f} order by r.created_at desc limit 300`, p);
      const meta = await sql(`select count(*)::int as sessions, coalesce(sum(bytes), 0)::bigint as bytes from ${X} where host = $1::text`, [C.brand]);
      return send(res, 200, { replays: rows, stats: meta[0], retentionDays: C.retentionDays, now: new Date().toISOString() });
    } catch { return send(res, 500, { error: "db_error" }); }
  }

  return { ingest, replays, cleanup, schema, config: C };
}
