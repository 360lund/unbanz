import { clearSession, json, sameOrigin } from "./_lib/auth.mjs";
export default function handler(req, res) {
  if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
  if (!sameOrigin(req)) return json(res, 403, { error: "forbidden" });
  clearSession(res);
  return json(res, 200, { ok: true });
}
