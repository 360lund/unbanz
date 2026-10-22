import { json, readJson, sameOrigin } from "../../_lib/auth.mjs";
import { allowed, gated, issue, verifyGoogle } from "../../_lib/gauth.mjs";
export default async function handler(req, res) {
  if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
  if (!sameOrigin(req)) return json(res, 403, { error: "forbidden" });
  if (!gated()) return json(res, 404, { error: "not_enabled" });
  if (!process.env.USERS_SESSION_SECRET) return json(res, 503, { error: "not_configured" });
  let b; try { b = await readJson(req); } catch { return json(res, 400, { error: "bad_request" }); }
  let email; try { email = await verifyGoogle(b.credential); } catch { return json(res, 503, { error: "google_unavailable" }); }
  if (!email) return json(res, 401, { error: "invalid_token" });
  if (!allowed().includes(email)) return json(res, 403, { error: "not_allowed" });
  issue(res, email);
  return json(res, 200, { ok: true, email });
}
