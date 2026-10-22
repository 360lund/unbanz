// First-party visit tracker. One row per browser session. No IPs, no user agents, no personal data stored.
import { sql } from "./_lib/db.mjs";
const S = (v, n = 200) => (typeof v === "string" ? v.slice(0, n) : null);
const GROUPS = new Set(["AI", "Search", "Social", "Ads", "Messaging", "Direct", "Other"]);
function ua(s) {
  s = String(s || "");
  const device = /iPad|Tablet/i.test(s) ? "Tablet" : /Mobi|iPhone|Android/i.test(s) ? "Mobile" : "Desktop";
  const browser = /Edg\//.test(s) ? "Edge" : /OPR\/|Opera/.test(s) ? "Opera" : /SamsungBrowser/.test(s) ? "Samsung" : /FBAN|FBAV|Instagram/.test(s) ? (/Instagram/.test(s) ? "Instagram app" : "Facebook app") : /CriOS|Chrome\//.test(s) ? "Chrome" : /FxiOS|Firefox\//.test(s) ? "Firefox" : /Safari\//.test(s) ? "Safari" : "Other";
  const os = /iPhone|iPad|iOS/.test(s) ? "iOS" : /Android/.test(s) ? "Android" : /Windows/.test(s) ? "Windows" : /Mac OS X/.test(s) ? "macOS" : /Linux/.test(s) ? "Linux" : "Other";
  return { device, browser, os };
}
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
  try {
    if (b.e === "view") {
      const path = S(b.p, 300) || "/";
      const g = GROUPS.has(b.g) ? b.g : "Other";
      const u = ua(req.headers["user-agent"]);
      const city = req.headers["x-vercel-ip-city"] ? decodeURIComponent(req.headers["x-vercel-ip-city"]) : null;
      await sql(
        `insert into visits(id, source, source_group, medium, ref_domain, utm_source, utm_medium, utm_campaign, search_term, landing, pages, country, city, device, browser, os)
         values($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,jsonb_build_array($10::text),$11,$12,$13,$14,$15)
         on conflict (id) do update set pages = case when jsonb_array_length(visits.pages) < 60 then visits.pages || jsonb_build_array($10::text) else visits.pages end,
           page_count = visits.page_count + 1, last_at = now()`,
        [id, S(b.s, 40) || "Direct", g, S(b.m, 20), S(b.d, 100), S(b.us, 100), S(b.um, 60), S(b.uc, 100), S(b.q, 120), path,
         S(req.headers["x-vercel-ip-country"], 2), S(city, 80), u.device, u.browser, u.os],
      );
    } else if (b.e === "click") {
      const k = b.k === "whatsapp" ? "clicked_whatsapp" : b.k === "email" ? "clicked_email" : b.k === "popup" ? "opened_popup" : null;
      if (k) await sql(`update visits set ${k} = true, platform = coalesce($2, platform), service = coalesce($3, service), last_at = now() where id = $1`, [id, S(b.pl, 20), S(b.sv, 20)]);
    }
    res.statusCode = 204; res.end();
  } catch { res.statusCode = 500; res.end(); }
}
