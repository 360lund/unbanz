import { json } from "../../_lib/auth.mjs";
import { gated, sessionEmail } from "../../_lib/gauth.mjs";
export default function handler(req, res) {
  if (!gated()) return json(res, 200, { gated: false });
  const email = sessionEmail(req);
  return json(res, 200, { gated: true, clientId: process.env.GOOGLE_CLIENT_ID, authed: !!email, email });
}
