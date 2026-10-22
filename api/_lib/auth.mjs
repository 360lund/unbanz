// Server-only auth for the private /users dashboard. Nothing here ships to the browser.
// Env (encrypted in Vercel):
//   USERS_SESSION_SECRET  random key that signs session cookies (rotate to log everyone out)
//   USERS_AUTH_HASH       optional: scrypt hash in the same format as Kredos LEADS_AUTH_HASH
//                         (scrypt$N$r$p$saltB64$hashB64 of "USERNAME\n" + password). When it is not set,
//                         the login is verified server-to-server against kredosmedia.com/api/leads-login,
//                         so it is exactly the same login (BOSS + the Kredos password). No password is stored here.
import crypto from "node:crypto";

export const COOKIE = "__Secure-unbanz_users";
const COOKIE_PATH = "/api/users";
const SESSION_DAYS = 365;
const KREDOS_LOGIN = "https://www.kredosmedia.com/api/leads-login";
const b64url = (b) => Buffer.from(b).toString("base64url");

export function securityHeaders(res) {
  res.setHeader("Cache-Control", "no-store, max-age=0");
  res.setHeader("X-Robots-Tag", "noindex, nofollow");
  res.setHeader("Referrer-Policy", "no-referrer");
  res.setHeader("X-Content-Type-Options", "nosniff");
}
export function json(res, status, body) {
  securityHeaders(res);
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.end(JSON.stringify(body));
}
const scrypt = (s, salt, N, r, p, len) => new Promise((ok, no) => crypto.scrypt(s, salt, len, { N, r, p, maxmem: 256 * 1024 * 1024 }, (e, k) => (e ? no(e) : ok(k))));

async function localCheck(stored, username, password) {
  const parts = stored.split("$");
  const [, n, r, p, salt, hash] = parts.length === 6 ? parts : ["", "16384", "8", "1", "AAAAAAAAAAAAAAAAAAAAAA==", "AAAA"];
  const expected = Buffer.from(hash, "base64");
  const got = await scrypt(`${String(username).trim().toUpperCase()}\n${password}`, Buffer.from(salt, "base64"), +n, +r, +p, expected.length || 32);
  return parts.length === 6 && expected.length === got.length && crypto.timingSafeEqual(expected, got);
}
async function kredosCheck(username, password) {
  try {
    const r = await fetch(KREDOS_LOGIN, { method: "POST", headers: { "Content-Type": "application/json", "User-Agent": "unbanz-users-auth" }, body: JSON.stringify({ username, password }), signal: AbortSignal.timeout(8000) });
    if (r.status === 429) return "locked";
    return r.status === 200;
  } catch { return "unavailable"; }
}
/** true | false | "locked" | "unavailable" */
export async function checkCredentials(username, password) {
  if (String(username).trim().toUpperCase() !== "BOSS") { await localCheck("", username, password); return false; }
  const stored = process.env.USERS_AUTH_HASH;
  return stored ? localCheck(stored, username, password) : kredosCheck("BOSS", password);
}
function sign(payload) {
  const key = process.env.USERS_SESSION_SECRET;
  if (!key || key.length < 32) throw new Error("USERS_SESSION_SECRET missing");
  return b64url(crypto.createHmac("sha256", key).update(payload).digest());
}
export function issueSession(res) {
  const maxAge = SESSION_DAYS * 86400, exp = Date.now() + maxAge * 1000;
  const payload = `v1.${exp}.${b64url(crypto.randomBytes(16))}`;
  res.setHeader("Set-Cookie", `${COOKIE}=${payload}.${sign(payload)}; Path=${COOKIE_PATH}; Max-Age=${maxAge}; Expires=${new Date(exp).toUTCString()}; HttpOnly; Secure; SameSite=Lax`);
}
export function clearSession(res) {
  res.setHeader("Set-Cookie", `${COOKIE}=; Path=${COOKIE_PATH}; Max-Age=0; Expires=Thu, 01 Jan 1970 00:00:00 GMT; HttpOnly; Secure; SameSite=Lax`);
}
function valid(token) {
  const i = token.lastIndexOf(".");
  if (i < 0) return false;
  let exp; try { exp = sign(token.slice(0, i)); } catch { return false; }
  const a = Buffer.from(token.slice(i + 1)), b = Buffer.from(exp);
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) return false;
  const [v, e] = token.split(".");
  return v === "v1" && +e > Date.now();
}
export function hasValidSession(req) {
  return String(req.headers.cookie || "").split(";").map((s) => s.trim()).filter((s) => s.startsWith(COOKIE + "=")).some((s) => valid(s.slice(COOKIE.length + 1)));
}
export function sameOrigin(req) {
  const o = req.headers.origin;
  if (!o) return true;
  try { return new URL(o).host === req.headers.host; } catch { return false; }
}
export async function readJson(req, limit = 10000) {
  if (req.body && typeof req.body === "object") return req.body;
  if (typeof req.body === "string") return JSON.parse(req.body || "{}");
  const chunks = []; let size = 0;
  for await (const c of req) { size += c.length; if (size > limit) throw new Error("too large"); chunks.push(c); }
  return JSON.parse(Buffer.concat(chunks).toString("utf8") || "{}");
}
