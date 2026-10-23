import { json, sameOrigin } from "../../_lib/auth.mjs";
import { clearU } from "../../_lib/uauth.mjs";
export default function handler(req, res) {
  if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
  if (!sameOrigin(req)) return json(res, 403, { error: "forbidden" });
  res.setHeader("Set-Cookie", clearU());
  return json(res, 200, { ok: true });
}
