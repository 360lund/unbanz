// Private API for the Recordings panel in the /users Ads tab. Same auth as the rest of /users (cookie or X-Users-Token); 401 otherwise.
//   GET ?list=1[&test=1]   sessions (meta + length + contact flag)     GET ?sid=<id>   all rrweb events (JSON array)
//   DELETE ?sid=<id>       remove a recording.  Recordings older than 30 days are deleted on list loads.
import { list, get, del } from "@vercel/blob";
import { authed } from "../_lib/uauth.mjs";
import zlib from "node:zlib";
import { PREFIX, SID, RETENTION_DAYS } from "../_lib/adrec.mjs";
const send = (res, code, obj) => { res.statusCode = code; res.setHeader("Content-Type", "application/json"); res.end(JSON.stringify(obj)); };
async function all(prefix) { const out = []; let cursor; do { const r = await list({ prefix, cursor, limit: 1000 }); out.push(...r.blobs); cursor = r.hasMore ? r.cursor : undefined; } while (cursor && out.length < 20000); return out; }
async function readBuf(pathname) { const r = await get(pathname, { access: "private", useCache: false }); if (!r || !r.stream) return null; return Buffer.from(await new Response(r.stream).arrayBuffer()); }
export default async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store"); res.setHeader("X-Robots-Tag", "noindex, nofollow"); res.setHeader("Referrer-Policy", "no-referrer");
  if (!authed(req, res)) return send(res, 401, { error: "unauthorized" });
  const q = new URL(req.url, "http://x").searchParams, sid = q.get("sid") || "";
  try {
    if (req.method === "DELETE") {
      if (!SID.test(sid)) return send(res, 400, { error: "bad_sid" });
      const b = await all(`${PREFIX}${sid}/`); if (b.length) await del(b.map((x) => x.url));
      return send(res, 200, { ok: true, deleted: b.length });
    }
    if (req.method !== "GET") return send(res, 405, { error: "method_not_allowed" });
    if (sid) {
      if (!SID.test(sid)) return send(res, 400, { error: "bad_sid" });
      const chunks = (await all(`${PREFIX}${sid}/c-`)).sort((a, b) => a.pathname.localeCompare(b.pathname));
      let evs = [];
      for (const c of chunks.slice(0, 600)) {
        const buf = await readBuf(c.pathname); if (!buf) continue;
        try { const z = c.pathname.split("-")[4] === "1"; evs = evs.concat(JSON.parse((z ? zlib.gunzipSync(buf) : buf).toString("utf8"))); } catch {}
      }
      const body = zlib.gzipSync(JSON.stringify(evs));
      res.statusCode = 200; res.setHeader("Content-Type", "application/json"); res.setHeader("Content-Encoding", "gzip"); return res.end(body);
    }
    const blobs = await all(PREFIX), by = new Map();
    for (const b of blobs) {
      const m = b.pathname.match(/^rec\/([a-z0-9]+)\/(.+)$/); if (!m) continue;
      const s = by.get(m[1]) || { sid: m[1], chunks: 0, t1: 0, tmin: 0, cta: false, meta: null, urls: [] }; by.set(m[1], s); s.urls.push(b.url);
      const c = m[2].match(/^c-(\d+)-[a-z0-9]+-\d+-[01]-([01])\.bin$/);
      if (c) { s.chunks++; const t = +c[1]; s.tmin = s.tmin ? Math.min(s.tmin, t) : t; s.t1 = Math.max(s.t1, t, +new Date(b.uploadedAt)); if (c[2] === "1") s.cta = true; }
      else if (m[2] === "meta.json") s.meta = b.pathname;
    }
    const cutoff = Date.now() - RETENTION_DAYS * 864e5, old = [], out = [];
    for (const s of by.values()) {
      if ((s.tmin || s.t1) && (s.tmin || s.t1) < cutoff) { old.push(...s.urls); continue; }
      let meta = {}; if (s.meta) { try { meta = JSON.parse((await readBuf(s.meta)).toString("utf8")); } catch {} }
      if (meta.test && q.get("test") !== "1") continue;
      out.push({ sid: s.sid, t0: meta.t0 || s.tmin, t1: s.t1, chunks: s.chunks, cta: s.cta, test: !!meta.test, country: meta.country || "", city: meta.city || "", device: meta.device || "", browser: meta.browser || "", os: meta.os || "", visit: meta.visit || "", landing: meta.landing || "", src: meta.src || "", ref: meta.ref || "" });
    }
    if (old.length) { try { await del(old.slice(0, 1000)); } catch {} }
    out.sort((a, b) => b.t0 - a.t0);
    return send(res, 200, { sessions: out });
  } catch (e) { return send(res, 500, { error: "storage_error" }); }
}
