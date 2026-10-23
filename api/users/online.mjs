// Live "Online now" for the /users dashboard: distinct visitors whose heartbeat landed in the last 60s (excluding /users).
import { json } from "../_lib/auth.mjs";
import { gated, sessionEmail } from "../_lib/gauth.mjs";
import { sql } from "../_lib/db.mjs";
export default async function handler(req, res) {
  if (req.method !== "GET") return json(res, 405, { error: "method_not_allowed" });
  if (gated() && !sessionEmail(req)) return json(res, 401, { error: "unauthorized" });
  try {
    const rows = await sql(`select path, country from presence where last_seen > now() - interval '60 seconds' and path not like '/users%'`);
    const tally = (k) => Object.entries(rows.reduce((m, r) => ((m[r[k] || "??"] = (m[r[k] || "??"] || 0) + 1), m), {})).map(([k, n]) => ({ k, n })).sort((a, b) => b.n - a.n).slice(0, 8);
    sql(`delete from presence where last_seen < now() - interval '1 day'`).catch(() => {});
    return json(res, 200, { online: rows.length, pages: tally("path"), countries: tally("country"), now: new Date().toISOString() });
  } catch (e) {
    if (/does not exist/.test(e.message)) return json(res, 200, { online: 0, pages: [], countries: [] });
    return json(res, 500, { error: "db_error" });
  }
}
