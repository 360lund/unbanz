// First-party visit tracker. One row per browser session, tagged with a persistent anonymous visitor id.
// Raw user agents are not stored; old cached scripts without an id get a one-way hash of IP+UA instead.
// For the 'Likely VPN' flag we keep the IP and Vercel's IP geo headers next to the browser's IANA time zone.
import { sql } from "./_lib/db.mjs";
import crypto from "node:crypto";
let migrated;
const migrate = () => (migrated ||= sql(`alter table visits add column if not exists visitor_id text, add column if not exists tz text, add column if not exists ip text, add column if not exists ip_country text, add column if not exists ip_region text, add column if not exists ip_city text, add column if not exists ip_tz text, add column if not exists vpn boolean, add column if not exists vpn_reason text, add column if not exists is_test boolean`).catch((e) => { migrated = null; throw e; }));
let presenceReady;
const presenceTable = () => (presenceReady ||= sql(`create table if not exists presence (visitor_id text primary key, last_seen timestamptz not null default now(), path text, country text)`).catch((e) => { presenceReady = null; throw e; }));
// Live "online now": last-seen per visitor. /users views never count.
async function touch(vid, path, country) {
  if (!path || path.startsWith("/users")) return;
  await presenceTable();
  await sql(`insert into presence(visitor_id, last_seen, path, country) values($1, now(), $2, $3) on conflict (visitor_id) do update set last_seen = now(), path = excluded.path, country = coalesce(excluded.country, presence.country)`, [vid, path, country]);
}
const S = (v, n = 200) => (typeof v === "string" ? v.slice(0, n) : null);
const GROUPS = new Set(["AI", "Search", "Social", "Ads", "Messaging", "Direct", "Other"]);
function ua(s) {
  s = String(s || "");
  const device = /iPad|Tablet/i.test(s) ? "Tablet" : /Mobi|iPhone|Android/i.test(s) ? "Mobile" : "Desktop";
  const browser = /Edg\//.test(s) ? "Edge" : /OPR\/|Opera/.test(s) ? "Opera" : /SamsungBrowser/.test(s) ? "Samsung" : /FBAN|FBAV|Instagram/.test(s) ? (/Instagram/.test(s) ? "Instagram app" : "Facebook app") : /CriOS|Chrome\//.test(s) ? "Chrome" : /FxiOS|Firefox\//.test(s) ? "Firefox" : /Safari\//.test(s) ? "Safari" : "Other";
  const os = /iPhone|iPad|iOS/.test(s) ? "iOS" : /Android/.test(s) ? "Android" : /Windows/.test(s) ? "Windows" : /Mac OS X/.test(s) ? "macOS" : /Linux/.test(s) ? "Linux" : "Other";
  return { device, browser, os };
}
// Current UTC offset (minutes) of an IANA zone; null if unknown.
const offset = (tz) => { try { const d = new Date(); const p = Object.fromEntries(new Intl.DateTimeFormat("en-US", { timeZone: tz, hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" }).formatToParts(d).map((x) => [x.type, x.value])); return Math.round((Date.UTC(+p.year, p.month - 1, +p.day, +p.hour % 24, +p.minute) - d.getTime()) / 60000); } catch { return null; } };
const dec = (v) => { try { return v ? decodeURIComponent(v) : null; } catch { return v || null; } };
export default async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");
  if (req.method !== "POST") { res.statusCode = 405; return res.end(); }
  if (/bot|crawl|spider|slurp|preview|headless|lighthouse/i.test(req.headers["user-agent"] || "")) { res.statusCode = 204; return res.end(); }
  let b;
  try {
    if (req.body && typeof req.body === "object" && !Buffer.isBuffer(req.body)) { b = req.body; if (!b.id) { const k = Object.keys(b)[0]; if (k && k.startsWith("{")) b = JSON.parse(k); } }
    else if (Buffer.isBuffer(req.body)) b = JSON.parse(req.body.toString("utf8") || "{}");
    else { let s = typeof req.body === "string" ? req.body : ""; if (!s) { for await (const c of req) { s += c; if (s.length > 4000) break; } } b = JSON.parse(s || "{}"); }
  } catch { res.statusCode = 400; return res.end(); }
  const id = S(b.id, 40);
  if (!id || !/^[a-z0-9]{8,40}$/i.test(id)) { res.statusCode = 400; return res.end(); }
  const vid = /^[a-z0-9]{8,40}$/i.test(b.v || "") ? "v:" + b.v : "h:" + crypto.createHash("sha256").update("ubz|" + String(req.headers["x-forwarded-for"] || "").split(",")[0].trim() + "|" + (req.headers["user-agent"] || "")).digest("hex").slice(0, 20);
  try {
    if (b.e !== "hb") await migrate();
    if (b.e === "hb") {
      await touch(vid, S(b.p, 300), S(req.headers["x-vercel-ip-country"], 2));
    } else if (b.e === "view") {
      await touch(vid, S(b.p, 300) || "/", S(req.headers["x-vercel-ip-country"], 2)).catch(() => {});
      const path = S(b.p, 300) || "/";
      const g = GROUPS.has(b.g) ? b.g : "Other";
      const u = ua(req.headers["user-agent"]);
      const city = dec(req.headers["x-vercel-ip-city"]);
      const tz = /^[A-Za-z_]+(\/[A-Za-z0-9_+\-]+){0,2}$|^UTC$/.test(b.tz || "") ? S(b.tz, 64) : null;
      const iptz = S(req.headers["x-vercel-ip-timezone"], 64);
      const o1 = tz ? offset(tz) : null, o2 = iptz ? offset(iptz) : null;
      // Compare current UTC offsets so same-offset zones (e.g. Asia/Karachi vs Asia/Tashkent) don't false-flag.
      const vpn = o1 != null && o2 != null ? Math.abs(o1 - o2) >= 60 : null;
      const ip = S(String(req.headers["x-real-ip"] || req.headers["x-forwarded-for"] || "").split(",")[0].trim(), 64) || null;
      await sql(
        `insert into visits(id, source, source_group, medium, ref_domain, utm_source, utm_medium, utm_campaign, search_term, landing, pages, country, city, device, browser, os, visitor_id, tz, ip, ip_country, ip_region, ip_city, ip_tz, vpn, vpn_reason, is_test)
         values($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,jsonb_build_array($10::text),$11,$12,$13,$14,$15,$16,$17,$18,$11,$19,$12,$20,$21,$22,$23)
         on conflict (id) do update set pages = case when jsonb_array_length(visits.pages) < 60 then visits.pages || jsonb_build_array($10::text) else visits.pages end,
           page_count = visits.page_count + 1, last_at = now(), visitor_id = coalesce(visits.visitor_id, $16),
           tz = coalesce(visits.tz, $17), ip = coalesce(visits.ip, $18), ip_region = coalesce(visits.ip_region, $19), ip_tz = coalesce(visits.ip_tz, $20),
           vpn = case when visits.vpn or $21::boolean then true else coalesce(visits.vpn, $21::boolean) end, vpn_reason = coalesce(visits.vpn_reason, $22), is_test = coalesce(visits.is_test, false) or $23::boolean`,
        [id, S(b.s, 40) || "Direct", g, S(b.m, 20), S(b.d, 100), S(b.us, 100), S(b.um, 60), S(b.uc, 100), S(b.q, 120), path,
         S(req.headers["x-vercel-ip-country"], 2), S(city, 80), u.device, u.browser, u.os, vid,
         tz, ip, S(dec(req.headers["x-vercel-ip-country-region"]), 20), iptz, vpn, vpn ? `Browser time zone ${tz} vs IP time zone ${iptz}` : null, b.x === 1],
      );
    } else if (b.e === "click") {
      const k = b.k === "whatsapp" ? "clicked_whatsapp" : b.k === "email" ? "clicked_email" : b.k === "popup" ? "opened_popup" : null;
      if (k) await sql(`update visits set ${k} = true, platform = coalesce($2, platform), service = coalesce($3, service), last_at = now() where id = $1`, [id, S(b.pl, 20), S(b.sv, 20)]);
    }
    res.statusCode = 204; res.end();
  } catch { res.statusCode = 500; res.end(); }
}
