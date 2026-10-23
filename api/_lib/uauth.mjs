// Username-only gate for /users. USERS_USERNAME (exact, case-sensitive) + USERS_SESSION_SECRET (HMAC key) live in Vercel env.
import crypto from "node:crypto";
export const UCOOKIE = "__Secure-unbanz_u";
const PATH = "/api/users", DAYS = 30;
const b64u = (b) => Buffer.from(b).toString("base64url");
function sign(p) {
  const k = process.env.USERS_SESSION_SECRET;
  if (!k || k.length < 32) throw new Error("no secret");
  return b64u(crypto.createHmac("sha256", k).update(p).digest());
}
export function checkUsername(u) {
  const want = process.env.USERS_USERNAME || "";
  const a = crypto.createHash("sha256").update(String(u ?? "")).digest(), b = crypto.createHash("sha256").update(want).digest();
  return !!want && crypto.timingSafeEqual(a, b);
}
export function issueU(res) {
  const max = DAYS * 86400, exp = Date.now() + max * 1000;
  const p = `u1.${exp}.${b64u(crypto.randomBytes(12))}`;
  res.setHeader("Set-Cookie", `${UCOOKIE}=${p}.${sign(p)}; Path=${PATH}; Max-Age=${max}; HttpOnly; Secure; SameSite=Lax`);
}
export const clearU = () => `${UCOOKIE}=; Path=${PATH}; Max-Age=0; HttpOnly; Secure; SameSite=Lax`;
export function authed(req) {
  for (const c of String(req.headers.cookie || "").split(";").map((s) => s.trim())) {
    if (!c.startsWith(UCOOKIE + "=")) continue;
    const t = c.slice(UCOOKIE.length + 1), i = t.lastIndexOf(".");
    if (i < 0) continue;
    let s; try { s = sign(t.slice(0, i)); } catch { return false; }
    const a = Buffer.from(t.slice(i + 1)), b = Buffer.from(s);
    if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) continue;
    const [v, exp] = t.split(".");
    if (v === "u1" && +exp > Date.now()) return true;
  }
  return false;
}
