import { json, sameOrigin, readJson } from "../../_lib/auth.mjs";
import { checkUsername, issueU } from "../../_lib/uauth.mjs";
export default async function handler(req, res) {
  if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
  if (!sameOrigin(req)) return json(res, 403, { error: "forbidden" });
  let b; try { b = await readJson(req, 2000); } catch { return json(res, 400, { error: "bad_request" }); }
  if (!checkUsername(b && b.username)) { await new Promise((r) => setTimeout(r, 400)); return json(res, 401, { error: "invalid" }); }
  issueU(res);
  return json(res, 200, { ok: true });
}
