import { json, sameOrigin, readJson } from "../../_lib/auth.mjs";
import { checkUsername, issueU } from "../../_lib/uauth.mjs";
import { limit, audit } from "../../_lib/guard.mjs";
export default async function handler(req, res) {
  if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
  if (!sameOrigin(req)) return json(res, 403, { error: "forbidden" });
  if (!(await limit(req, "login", 10, 600))) return json(res, 429, { error: "too_many_attempts" });
  let b; try { b = await readJson(req, 2000); } catch { return json(res, 400, { error: "bad_request" }); }
  if (!checkUsername(b && b.username)) { await audit(req, "login", "", false); await new Promise((r) => setTimeout(r, 400)); return json(res, 401, { error: "invalid" }); }
  await audit(req, "login", "", true);
  const token = issueU(res);
  return json(res, 200, { ok: true, token });
}
