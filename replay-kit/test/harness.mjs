// Local test harness: serves ../.. (the static site) and runs the REAL api/*.mjs handlers against an in-process
// Postgres (pglite) through a fake Neon HTTP endpoint. No network, no production data.
//   node test/harness.mjs [port]      env for the fake session: USERS_USERNAME / USERS_SESSION_SECRET are set here to test values
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { PGlite } from "@electric-sql/pglite";

const here = path.dirname(fileURLToPath(import.meta.url));
const SITE = path.resolve(here, process.env.SITE_ROOT || "../..");
process.env.DATABASE_URL = "postgres://test:test@neon.test/db";
process.env.USERS_USERNAME = "harness-user";
process.env.USERS_SESSION_SECRET = "harness-secret-harness-secret-harness-secret";

export const db = new PGlite();
await db.exec(`create table visits (
  id text primary key, source text, source_group text, medium text, ref_domain text, utm_source text, utm_medium text, utm_campaign text, search_term text,
  landing text, pages jsonb not null default '[]', page_count int not null default 1, country text, city text, device text, browser text, os text,
  started_at timestamptz not null default now(), last_at timestamptz not null default now(),
  clicked_whatsapp boolean not null default false, clicked_email boolean not null default false, opened_popup boolean not null default false,
  platform text, service text)`);

// fake Neon: https://neon.test/sql
const realFetch = globalThis.fetch;
const norm = (v) => (typeof v === "bigint" ? String(v) : v);
globalThis.fetch = async (url, opt) => {
  if (String(url).startsWith("https://neon.test/sql")) {
    const { query, params } = JSON.parse(opt.body);
    try {
      const r = await db.query(query, params);
      const rows = r.rows.map((row) => Object.fromEntries(Object.entries(row).map(([k, v]) => [k, norm(v)])));
      return new Response(JSON.stringify({ rows }), { status: 200, headers: { "content-type": "application/json" } });
    } catch (e) { return new Response(JSON.stringify({ message: String(e.message) }), { status: 400 }); }
  }
  return realFetch(url, opt);
};

const MIME = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".mjs": "text/javascript", ".css": "text/css", ".svg": "image/svg+xml", ".woff": "font/woff", ".woff2": "font/woff2", ".png": "image/png", ".webp": "image/webp", ".jpg": "image/jpeg", ".json": "application/json", ".txt": "text/plain", ".xml": "application/xml", ".ico": "image/x-icon" };
const cache = new Map();
const handler = async (file) => (cache.get(file) || cache.set(file, (await import(pathToFileURL(file).href)).default).get(file));

export function start(port = 0) {
  const srv = http.createServer(async (req, res) => {
    try {
      const u = new URL(req.url, "http://x");
      let p = decodeURIComponent(u.pathname);
      if (p.startsWith("/api/")) {
        const f = path.join(SITE, p.replace(/\/$/, "") + ".mjs");
        if (!f.startsWith(path.join(SITE, "api")) || !fs.existsSync(f)) { res.statusCode = 404; return res.end(); }
        return (await handler(f))(req, res);
      }
      let f = path.join(SITE, p);
      if (!f.startsWith(SITE)) { res.statusCode = 403; return res.end(); }
      if (fs.existsSync(f) && fs.statSync(f).isDirectory()) {
        if (!p.endsWith("/")) { res.statusCode = 308; res.setHeader("Location", p + "/" + u.search); return res.end(); }
        f = path.join(f, "index.html");
      }
      if (!fs.existsSync(f)) { res.statusCode = 404; return res.end("not found"); }
      res.setHeader("Content-Type", MIME[path.extname(f)] || "application/octet-stream");
      res.setHeader("Cache-Control", "no-store");
      fs.createReadStream(f).pipe(res);
    } catch (e) { console.error("harness error", e); res.statusCode = 500; res.end(); }
  });
  return new Promise((ok) => srv.listen(port, "127.0.0.1", () => ok({ srv, port: srv.address().port })));
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  const { port } = await start(Number(process.argv[2]) || 8099);
  console.log("harness on http://127.0.0.1:" + port);
}
