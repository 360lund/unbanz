// Nov 20 2026: storage for Google Ads visitor replays in the private Vercel Blob store "unbanz-ad-replays"
// (BLOB_READ_WRITE_TOKEN). Never touches the Neon DB. Layout:
//   rec/<sid>/meta.json                      visit facts written on the first chunk (time, geo, device, landing, ad params)
//   rec/<sid>/c-<t0>-<pg>-<i>-<z>-<cta>.bin   rrweb event chunks (gzip when z=1)
export const PREFIX = "rec/";
export const SID = /^[a-z0-9]{12,32}$/, PG = /^[a-z0-9]{4,8}$/;
export const RETENTION_DAYS = 30;
export function uaInfo(s) {
  s = String(s || "");
  const device = /iPad|Tablet/i.test(s) ? "Tablet" : /Mobi|iPhone|Android/i.test(s) ? "Mobile" : "Desktop";
  const browser = /Edg\//.test(s) ? "Edge" : /OPR\/|Opera/.test(s) ? "Opera" : /SamsungBrowser/.test(s) ? "Samsung Internet" : /CriOS|Chrome\//.test(s) ? "Chrome" : /FxiOS|Firefox\//.test(s) ? "Firefox" : /Safari\//.test(s) ? "Safari" : "Other";
  const os = /iPhone|iPad|iOS/.test(s) ? "iOS" : /Android/.test(s) ? "Android" : /Windows/.test(s) ? "Windows" : /Mac OS X/.test(s) ? "macOS" : /Linux/.test(s) ? "Linux" : "Other";
  return { device, browser, os };
}
export function adSource(landing) {
  try {
    const q = new URL(landing, "https://unbanz.com").searchParams, o = [];
    for (const k of ["gclid", "gbraid", "wbraid", "gad_source", "gad_campaignid", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"]) if (q.get(k)) o.push(k + "=" + (k === "gclid" || k.endsWith("braid") ? q.get(k).slice(0, 10) + "…" : q.get(k).slice(0, 60)));
    return o.join(" ");
  } catch { return ""; }
}
export async function rawBody(req, max) {
  const chunks = []; let n = 0;
  for await (const c of req) { n += c.length; if (n > max) throw new Error("too_big"); chunks.push(c); }
  return Buffer.concat(chunks);
}
