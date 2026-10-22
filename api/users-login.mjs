import { checkCredentials, issueSession, json, readJson, sameOrigin } from "./_lib/auth.mjs";
const fails = new Map(); // per-instance soft throttle (Kredos also rate-limits its side)
export default async function handler(req, res) {
  if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
  if (!sameOrigin(req)) return json(res, 403, { error: "forbidden" });
  if (!process.env.USERS_SESSION_SECRET) return json(res, 503, { error: "not_configured" });
  const ip = String(req.headers["x-real-ip"] || "x");
  const f = fails.get(ip);
  if (f && f.n >= 5 && f.t > Date.now()) return json(res, 429, { error: "too_many_attempts" });
  let b; try { b = await readJson(req); } catch { return json(res, 400, { error: "bad_request" }); }
  const u = typeof b.username === "string" ? b.username.slice(0, 100) : "";
  const p = typeof b.password === "string" ? b.password.slice(0, 200) : "";
  const ok = await checkCredentials(u, p);
  if (ok === "locked") return json(res, 429, { error: "too_many_attempts" });
  if (ok === "unavailable") return json(res, 503, { error: "auth_unavailable" });
  if (!ok) {
    fails.set(ip, { n: (f && f.t > Date.now() ? f.n : 0) + 1, t: Date.now() + 15 * 60000 });
    await new Promise((r) => setTimeout(r, 400 + Math.random() * 300));
    return json(res, 401, { error: "invalid_credentials" });
  }
  fails.delete(ip);
  issueSession(res);
  return json(res, 200, { ok: true });
}
