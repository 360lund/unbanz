// Public ingest for Google Ads visitor replays (POST only). Chunks go to the private Blob store; nothing else is stored.
import { put } from "@vercel/blob";
import { PREFIX, SID, PG, uaInfo, adSource, rawBody } from "./_lib/adrec.mjs";
const BOT = /bot|crawl|spider|slurp|preview|headless|lighthouse|mediapartners|adsbot/i;
const hits = new Map(); // per-instance rate limit: 40 chunks / minute / IP
export default async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store"); res.setHeader("X-Robots-Tag", "noindex");
  if (req.method !== "POST") { res.statusCode = 405; return res.end(); }
  if (!process.env.BLOB_READ_WRITE_TOKEN) { res.statusCode = 503; return res.end(); }
  const ua = req.headers["user-agent"] || "";
  if (BOT.test(ua)) { res.statusCode = 204; return res.end(); }
  const q = new URL(req.url, "http://x").searchParams;
  const s = q.get("s") || "", g = q.get("g") || "", i = +q.get("i"), z = q.get("z") === "1" ? 1 : 0, a = +q.get("a"), c = q.get("c") === "1" ? 1 : 0;
  if (!SID.test(s) || !PG.test(g) || !Number.isInteger(i) || i < 0 || i > 400 || !(a > 1.7e12 && a < 2.2e12)) { res.statusCode = 400; return res.end(); }
  const ip = String(req.headers["x-forwarded-for"] || "").split(",")[0].trim(), now = Date.now();
  const h = (hits.get(ip) || []).filter((t) => now - t < 60000); h.push(now); hits.set(ip, h);
  if (hits.size > 5000) hits.clear();
  if (h.length > 40) { res.statusCode = 429; return res.end(); }
  let body; try { body = await rawBody(req, 400_000); } catch { res.statusCode = 413; return res.end(); }
  if (!body.length) { res.statusCode = 400; return res.end(); }
  if (z && !(body[0] === 0x1f && body[1] === 0x8b)) { res.statusCode = 400; return res.end(); }
  if (!z && body[0] !== 0x5b) { res.statusCode = 400; return res.end(); }
  try {
    const opts = { access: "private", addRandomSuffix: false, allowOverwrite: true, contentType: "application/octet-stream" };
    await put(`${PREFIX}${s}/c-${a}-${g}-${String(i).padStart(3, "0")}-${z}-${c}.bin`, body, opts);
    if (q.get("f") === "1") {
      const H = (k) => { try { return decodeURIComponent(String(req.headers[k] || "")); } catch { return ""; } };
      const landing = (q.get("l") || "").slice(0, 400), ref = (q.get("r") || "").slice(0, 200);
      const meta = { sid: s, t0: a, test: q.get("x") === "1", country: H("x-vercel-ip-country").slice(0, 2), region: H("x-vercel-ip-country-region").slice(0, 40), city: H("x-vercel-ip-city").slice(0, 60), ...uaInfo(ua), visit: /^[a-z0-9]{8,40}$/i.test(q.get("v") || "") ? q.get("v") : "", landing: landing.split("?")[0], src: adSource(landing), ref };
      await put(`${PREFIX}${s}/meta.json`, JSON.stringify(meta), { ...opts, contentType: "application/json" });
    }
  } catch (e) { res.statusCode = 500; return res.end(); }
  res.statusCode = 204; res.end();
}
