import { json } from "../../_lib/auth.mjs";
import { authed } from "../../_lib/uauth.mjs";
export default function handler(req, res) { return json(res, 200, { gated: true, authed: authed(req) }); }
