// Google Sign-In gate for /users. Activates only when GOOGLE_CLIENT_ID and USERS_ALLOWED_EMAILS are both set.
import crypto from "node:crypto";
export const GCOOKIE = "__Secure-unbanz_users_g";
const PATH = "/api/users", DAYS = 30;
const b64u = (b) => Buffer.from(b).toString("base64url");
export const allowed = () => String(process.env.USERS_ALLOWED_EMAILS || "").split(",").map((s) => s.trim().toLowerCase()).filter(Boolean);
export const gated = () => !!(process.env.GOOGLE_CLIENT_ID && allowed().length);
function sign(p) {
  const k = process.env.USERS_SESSION_SECRET;
  if (!k || k.length < 32) throw new Error("no secret");
  return b64u(crypto.createHmac("sha256", k).update(p).digest());
}
export function issue(res, email) {
  const max = DAYS * 86400, exp = Date.now() + max * 1000;
  const p = `g1.${exp}.${b64u(email)}.${b64u(crypto.randomBytes(12))}`;
  res.setHeader("Set-Cookie", `${GCOOKIE}=${p}.${sign(p)}; Path=${PATH}; Max-Age=${max}; HttpOnly; Secure; SameSite=Lax`);
}
export function clear(res) { res.setHeader("Set-Cookie", `${GCOOKIE}=; Path=${PATH}; Max-Age=0; HttpOnly; Secure; SameSite=Lax`); }
/** returns the signed-in, still-allowed email or null */
export function sessionEmail(req) {
  for (const c of String(req.headers.cookie || "").split(";").map((s) => s.trim())) {
    if (!c.startsWith(GCOOKIE + "=")) continue;
    const t = c.slice(GCOOKIE.length + 1), i = t.lastIndexOf(".");
    if (i < 0) continue;
    let s; try { s = sign(t.slice(0, i)); } catch { return null; }
    const a = Buffer.from(t.slice(i + 1)), b = Buffer.from(s);
    if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) continue;
    const [v, exp, e] = t.split(".");
    const email = Buffer.from(e || "", "base64url").toString();
    if (v === "g1" && +exp > Date.now() && allowed().includes(email)) return email;
  }
  return null;
}
let jwks = null, jwksAt = 0;
async function keys() {
  if (jwks && Date.now() - jwksAt < 3600e3) return jwks;
  const r = await fetch("https://www.googleapis.com/oauth2/v3/certs", { signal: AbortSignal.timeout(6000) });
  if (!r.ok) throw new Error("jwks");
  jwks = (await r.json()).keys; jwksAt = Date.now(); return jwks;
}
/** verifies a Google ID token; returns verified lowercase email or null */
export async function verifyGoogle(token) {
  const parts = String(token || "").split(".");
  if (parts.length !== 3) return null;
  let h, c; try { h = JSON.parse(Buffer.from(parts[0], "base64url")); c = JSON.parse(Buffer.from(parts[1], "base64url")); } catch { return null; }
  if (h.alg !== "RS256") return null;
  const jwk = (await keys()).find((k) => k.kid === h.kid);
  if (!jwk) return null;
  const ok = crypto.verify("RSA-SHA256", Buffer.from(parts[0] + "." + parts[1]), crypto.createPublicKey({ key: jwk, format: "jwk" }), Buffer.from(parts[2], "base64url"));
  if (!ok) return null;
  const now = Date.now() / 1000;
  if (c.aud !== process.env.GOOGLE_CLIENT_ID) return null;
  if (!["accounts.google.com", "https://accounts.google.com"].includes(c.iss)) return null;
  if (!(c.exp > now - 60) || (c.iat && c.iat > now + 300)) return null;
  if (c.email_verified !== true && c.email_verified !== "true") return null;
  return String(c.email || "").toLowerCase() || null;
}
