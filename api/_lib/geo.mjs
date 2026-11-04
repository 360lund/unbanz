// Sender origin from mail headers + IP geolocation (ipwho.is, no key), cached per IP in Postgres and in memory.
// Never guesses: if the only public IP belongs to a big mail provider's server, the result is "unknown (sent via X)".
import net from "node:net";
import { sql } from "./db.mjs";

const PROVIDERS = [
  [/google\.com|gmail|googlemail/i, "Gmail"], [/outlook\.com|hotmail|protection\.outlook|microsoft\.com|office365/i, "Outlook / Microsoft"],
  [/yahoo|yahoodns|aol\.com/i, "Yahoo / AOL"], [/icloud|apple\.com|\bme\.com|mac\.com/i, "iCloud"], [/zoho/i, "Zoho"], [/proton(mail)?\./i, "Proton"],
  [/amazonses|amazonaws/i, "Amazon SES"], [/sendgrid/i, "SendGrid"], [/mailgun/i, "Mailgun"], [/mcsv\.net|mcdlv\.net|rsgsv\.net|mailchimp|mandrillapp/i, "Mailchimp"],
  [/sparkpost/i, "SparkPost"], [/mtasv\.net|postmarkapp/i, "Postmark"], [/mailjet/i, "Mailjet"], [/sendinblue|brevo/i, "Brevo"], [/hubspot/i, "HubSpot"],
  [/exacttarget|salesforce/i, "Salesforce"], [/gmx\.|web\.de/i, "GMX"], [/yandex/i, "Yandex"], [/mail\.ru/i, "Mail.ru"], [/messagingengine|fastmail/i, "Fastmail"],
  [/smtp2go/i, "SMTP2GO"], [/zendesk/i, "Zendesk"], [/facebookmail|facebook\.com/i, "Facebook"], [/linkedin/i, "LinkedIn"], [/qq\.com/i, "QQ Mail"],
  [/163\.com|126\.com|netease/i, "NetEase"], [/titan\.email|flockmail/i, "Titan"], [/privateemail|namecheap/i, "Namecheap"], [/secureserver\.net|godaddy/i, "GoDaddy"],
];
const OWN = /spacemail/i;
const provider = (s) => (PROVIDERS.find(([r]) => r.test(s)) || [])[1] || "";

export function isPublic(ip) {
  ip = String(ip || "").replace(/^::ffff:/i, "");
  const v = net.isIP(ip);
  if (v === 4) {
    const [a, b] = ip.split(".").map(Number);
    return !(a === 0 || a === 10 || a === 127 || a >= 224 || (a === 100 && b >= 64 && b < 128) || (a === 169 && b === 254) || (a === 172 && b >= 16 && b < 32) || (a === 192 && b === 168) || (a === 192 && b === 0) || (a === 198 && (b === 18 || b === 19)));
  }
  if (v === 6) { const l = ip.toLowerCase(); return !(l === "::1" || l === "::" || /^f[cd]/.test(l) || /^fe[89ab]/.test(l) || /^ff/.test(l) || /^2001:db8/.test(l)); }
  return false;
}
const ipsIn = (s) => {
  const out = [];
  for (const m of s.matchAll(/\[(?:IPv6:)?([0-9a-fA-F:.]+)\]/g)) out.push(m[1]);
  if (!out.length) for (const m of s.matchAll(/\b(\d{1,3}(?:\.\d{1,3}){3})\b/g)) out.push(m[1]);
  return out.filter((x) => net.isIP(x.replace(/^::ffff:/i, ""))).map((x) => x.replace(/^::ffff:/i, ""));
};
// Unfolded header lines from raw header text.
export function headerLines(raw) {
  const t = String(raw || "").split(/\r?\n\r?\n/)[0].replace(/\r?\n[ \t]+/g, " ");
  return t.split(/\r?\n/).map((l) => { const i = l.indexOf(":"); return i > 0 ? [l.slice(0, i).trim().toLowerCase(), l.slice(i + 1).trim()] : null; }).filter(Boolean);
}
// Returns { kind: client|server|provider|none, ip?, via? }
export function originOf(raw) {
  const H = headerLines(raw);
  for (const k of ["x-originating-ip", "x-sender-ip", "x-client-ip", "x-real-ip", "x-forwarded-for", "x-yahoo-post-ip"]) {
    for (const [n, v] of H) if (n === k) { const ip = ipsIn(v.includes("[") ? v : `[${v.split(",")[0].trim()}]`).find(isPublic); if (ip) return { kind: "client", ip, src: k }; }
  }
  const rec = H.filter(([n]) => n === "received").map(([, v]) => v).reverse(); // oldest first
  for (const r of rec) {
    const fromPart = (r.match(/^\s*from\s+([\s\S]*?)(?=\s+by\s|;|$)/i) || [])[1] || "";
    const byPart = (r.match(/\sby\s+([\s\S]*?)(?=\s+(with|id|for)\s|;|$)/i) || [])[1] || "";
    if (!fromPart) continue;
    const ip = ipsIn(fromPart).find(isPublic);
    if (!ip) continue;
    if (OWN.test(fromPart)) continue; // our own Spacemail relay hop
    const pv = provider(fromPart);
    if (pv) return { kind: "provider", ip, via: pv };
    // Authenticated submission / webmail into the sender's provider: the "from" IP is the sender's own device.
    if (/ESMTPSA|ESMTPA|authenticated|HTTP|webmail|submission/i.test(r) || provider(byPart)) return { kind: "client", ip, src: "received" };
    return { kind: "server", ip, src: "received" };
  }
  const pv = rec.map((r) => provider(r)).find(Boolean);
  return pv ? { kind: "provider", via: pv } : { kind: "none" };
}

let ready;
const migrate = () => (ready ||= sql(`create table if not exists ip_geo (ip text primary key, d jsonb not null, at timestamptz default now())`).catch((e) => { ready = null; throw e; }));
const MEM = new Map();
async function lookupMany(ips) {
  const want = [...new Set(ips.filter(Boolean))], out = {};
  const miss = want.filter((ip) => (MEM.has(ip) ? ((out[ip] = MEM.get(ip)), false) : true));
  if (miss.length) {
    try { await migrate(); for (const r of await sql(`select ip, d from ip_geo where ip = any($1) and at > now() - interval '60 days'`, [miss])) { out[r.ip] = r.d; MEM.set(r.ip, r.d); } } catch {}
    const need = miss.filter((ip) => !out[ip]).slice(0, 25);
    await Promise.all(need.map(async (ip) => {
      try {
        const r = await fetch(`https://ipwho.is/${encodeURIComponent(ip)}?fields=success,country,country_code,region,city,connection`, { signal: AbortSignal.timeout(3500) });
        const j = await r.json();
        if (!j.success || !j.country_code) return;
        const d = { country: j.country, code: j.country_code, region: j.region || "", city: j.city || "", org: j.connection?.org || j.connection?.isp || "" };
        out[ip] = d; MEM.set(ip, d);
        await sql(`insert into ip_geo (ip, d) values ($1, $2) on conflict (ip) do update set d = excluded.d, at = now()`, [ip, JSON.stringify(d)]).catch(() => {});
      } catch {}
    }));
  }
  return out;
}
const DN = new Intl.DisplayNames(["en"], { type: "region" });
const GENERIC = new Set(["io", "co", "ai", "me", "tv", "cc", "ws", "fm", "am", "gg", "ly", "to", "is", "it", "so", "sh", "app", "dev"]);
function tldHint(addr) {
  let t = (String(addr || "").toLowerCase().match(/\.([a-z]{2})>?\s*$/) || [])[1];
  if (!t || GENERIC.has(t)) return null;
  if (t === "uk") t = "gb";
  try { const n = DN.of(t.toUpperCase()); return n && n !== t.toUpperCase() ? { code: t.toUpperCase(), country: n } : null; } catch { return null; }
}
// items: [{ raw, fromAddr }] -> array of geo labels
export async function geoLabels(items) {
  const o = items.map((x) => originOf(x.raw));
  const g = await lookupMany(o.filter((x) => x.ip && x.kind !== "provider").map((x) => x.ip));
  return o.map((x, i) => {
    const hint = tldHint(items[i].fromAddr);
    if (x.kind === "provider") return { kind: "provider", via: x.via, hint };
    const d = x.ip && g[x.ip];
    if (!d) return { kind: "none", hint, ip: x.ip || undefined };
    return { kind: x.kind, ip: x.ip, country: d.country, code: d.code, region: d.region, city: d.city, org: d.org, hint };
  });
}
