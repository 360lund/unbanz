// Returns the visitor's country code from Vercel's IP geo header (CTA note + contact policy).
// Nov 20 2026, strict WhatsApp gate. The WhatsApp number is returned ONLY when BOTH are true:
//   1. Vercel's IP country header (set by Vercel's edge, clients cannot override it) is exactly US, CA, GB, NL or AE;
//   2. the browser's IANA time zone (?tz=, from Intl) is a time zone of one of those five countries.
// A VPN exit in the US/UK/NL from Pakistan, India, Iran, Morocco etc. still reports Asia/Karachi, Asia/Kolkata...
// so it gets no number. Missing/unknown country or time zone (including UTC) = no number (fail closed).
// No URL, cookie or header override exists. The number never ships in static HTML/JS.
const WA_COUNTRIES = new Set(["US", "CA", "GB", "NL", "AE"]);
// Every tzdb zone for US, CA, GB, NL and AE (zone.tab) plus their legacy aliases (US/*, Canada/*, GB, Europe/Belfast,
// America/Indianapolis, America/Montreal...). Nothing else, so Asia/Muscat, Caribbean or Latin American zones fail.
const WA_TZ = new Set(["America/Adak", "America/Anchorage", "America/Atikokan", "America/Atka", "America/Blanc-Sablon", "America/Boise", "America/Cambridge_Bay", "America/Chicago", "America/Coral_Harbour", "America/Creston", "America/Dawson", "America/Dawson_Creek", "America/Denver", "America/Detroit", "America/Edmonton", "America/Fort_Nelson", "America/Fort_Wayne", "America/Glace_Bay", "America/Goose_Bay", "America/Halifax", "America/Indiana/Indianapolis", "America/Indiana/Knox", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Tell_City", "America/Indiana/Vevay", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Indianapolis", "America/Inuvik", "America/Iqaluit", "America/Juneau", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/Knox_IN", "America/Los_Angeles", "America/Louisville", "America/Menominee", "America/Metlakatla", "America/Moncton", "America/Montreal", "America/New_York", "America/Nipigon", "America/Nome", "America/North_Dakota/Beulah", "America/North_Dakota/Center", "America/North_Dakota/New_Salem", "America/Pangnirtung", "America/Phoenix", "America/Rainy_River", "America/Rankin_Inlet", "America/Regina", "America/Resolute", "America/Shiprock", "America/Sitka", "America/St_Johns", "America/Swift_Current", "America/Thunder_Bay", "America/Toronto", "America/Vancouver", "America/Whitehorse", "America/Winnipeg", "America/Yakutat", "America/Yellowknife", "Asia/Dubai", "Canada/Atlantic", "Canada/Central", "Canada/Eastern", "Canada/Mountain", "Canada/Newfoundland", "Canada/Pacific", "Canada/Saskatchewan", "Canada/Yukon", "Europe/Amsterdam", "Europe/Belfast", "Europe/London", "GB", "GB-Eire", "Navajo", "Pacific/Honolulu", "US/Alaska", "US/Aleutian", "US/Arizona", "US/Central", "US/East-Indiana", "US/Eastern", "US/Hawaii", "US/Indiana-Starke", "US/Michigan", "US/Mountain", "US/Pacific"]);
const WA_NUMBER = "447723162824";
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
  const body = { c };
  if (c && WA_COUNTRIES.has(c) && WA_TZ.has(tz)) body.wa = WA_NUMBER;
  res.status(200).json(body);
}
