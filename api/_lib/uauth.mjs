// Username-only gate for /users. USERS_USERNAME (exact, case-sensitive) + USERS_SESSION_SECRET (HMAC key) live in Vercel env.
import crypto from "node:crypto";
export const UCOOKIE = "__Secure-unbanz_u";
const PATH = "/", DAYS = 30;
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
  return setU(res, `${p}.${sign(p)}`, exp);
}
// (Re)sets the cookie for a token; also expires the old Path=/api/users cookie so only one copy exists.
export function setU(res, token, exp) {
  const max = Math.max(0, Math.floor((exp - Date.now()) / 1000));
  res.setHeader("Set-Cookie", [`${UCOOKIE}=${token}; Path=${PATH}; Max-Age=${max}; HttpOnly; Secure; SameSite=Lax`, `${UCOOKIE}=; Path=/api/users; Max-Age=0; HttpOnly; Secure; SameSite=Lax`]);
  return token;
}
export const clearU = () => [`${UCOOKIE}=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Lax`, `${UCOOKIE}=; Path=/api/users; Max-Age=0; HttpOnly; Secure; SameSite=Lax`];
export function validToken(t) {
  t = String(t || ""); const i = t.lastIndexOf(".");
  if (i < 0) return 0;
  let s; try { s = sign(t.slice(0, i)); } catch { return 0; }
  const a = Buffer.from(t.slice(i + 1)), b = Buffer.from(s);
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) return 0;
  const [v, exp] = t.split(".");
  return v === "u1" && +exp > Date.now() ? +exp : 0;
}
/** Valid session from the cookie, or from the X-Users-Token header (localStorage fallback). A header-only hit re-sets the cookie. */
export function authed(req, res) {
  for (const c of String(req.headers.cookie || "").split(";").map((s) => s.trim()))
    if (c.startsWith(UCOOKIE + "=") && validToken(c.slice(UCOOKIE.length + 1))) return true;
  const h = req.headers["x-users-token"], exp = validToken(h);
  if (exp) { if (res) setU(res, h, exp); return true; }
  return false;
}
