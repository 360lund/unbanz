// Returns the visitor's country code from Vercel's IP geo header (CTA note + contact policy).
// Nov 19 2026: WhatsApp contact is returned ONLY for US, CA, GB, NL and AE visitors.
// The number never ships in static HTML/JS, so other countries never receive it.
const WA_COUNTRIES = new Set(["US", "CA", "GB", "NL", "AE"]);
const WA_NUMBER = "447723162824";
const WA_DISPLAY = "+44 7723 162824";
export default function handler(req, res) {
  const c = String(req.headers["x-vercel-ip-country"] || "").slice(0, 2).toUpperCase();
  res.setHeader("Cache-Control", "private, no-store");
  res.setHeader("Vary", "x-vercel-ip-country");
  res.setHeader("X-Robots-Tag", "noindex");
  const body = { c };
  if (WA_COUNTRIES.has(c)) { body.wa = WA_NUMBER; body.wd = WA_DISPLAY; }
  res.status(200).json(body);
}
