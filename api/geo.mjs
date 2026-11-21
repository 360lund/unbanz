// Returns the visitor's country code from Vercel's IP geo header (CTA note + contact policy).
// Nov 21 2026: WhatsApp contact is removed. This API never returns a WhatsApp number.
// contactAllowed is false for India, Pakistan and Iran (IP country or browser time zone).
// No URL, cookie or header override exists (the ubz_noc cookie can only ADD a block, never unlock contact).
const EMAIL = "team@unbanz.com";
// Nov 21 2026: NO contact at all (no email) for India, Pakistan and Iran, by IP country OR browser time zone
// (so VPN users from those countries are blocked too). Pages/SEO content are unchanged; only contact UI is removed client-side.
const NO_CONTACT = new Set(["IN", "PK", "IR"]);
const NO_CONTACT_TZ = new Set(["Asia/Karachi", "Asia/Kolkata", "Asia/Calcutta", "Asia/Tehran", "Iran"]);
export default function handler(req, res) {
  const raw = String(req.headers["x-vercel-ip-country"] || "").trim().toUpperCase();
  const c = /^[A-Z]{2}$/.test(raw) ? raw : "";
  let tz = "";
  try { tz = String(new URL(req.url || "/", "https://unbanz.com").searchParams.get("tz") || "").slice(0, 64); } catch (e) { tz = ""; }
  res.setHeader("Cache-Control", "private, no-store, no-cache, must-revalidate, max-age=0");
  res.setHeader("CDN-Cache-Control", "no-store");
  res.setHeader("Vercel-CDN-Cache-Control", "no-store");
  res.setHeader("Pragma", "no-cache");
  res.setHeader("Expires", "0");
  res.setHeader("Vary", "x-vercel-ip-country");
  res.setHeader("X-Robots-Tag", "noindex, nofollow");
  const blocked = NO_CONTACT.has(c) || NO_CONTACT_TZ.has(tz);
  const body = { c, contactAllowed: !blocked, email: blocked ? null : EMAIL };
  if (blocked) res.setHeader("Set-Cookie", "ubz_noc=1; Path=/; Max-Age=2592000; SameSite=Lax; Secure");
  res.status(200).json(body);
}
