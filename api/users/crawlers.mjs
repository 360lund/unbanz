// /users dashboard: AI and search crawler hits per page and per bot.
import { json } from "../_lib/auth.mjs";
import { authed } from "../_lib/uauth.mjs";
import { sql } from "../_lib/db.mjs";
export default async function handler(req, res) {
  if (req.method === "DELETE") {
    if (!authed(req, res)) return json(res, 401, { error: "unauthorized" });
    try { const r = await sql(`delete from crawler_hits where is_test returning id`); return json(res, 200, { deleted: r.length }); } catch (e) { return json(res, 500, { error: "db_error" }); }
  }
  if (req.method !== "GET") return json(res, 405, { error: "method_not_allowed" });
  if (!authed(req, res)) return json(res, 401, { error: "unauthorized" });
  const days = Math.max(1, Math.min(90, parseInt(new URL(req.url, "http://x").searchParams.get("days"), 10) || 7));
  try {
    const bots = await sql(`select bot, count(*)::int n, max(at) last from crawler_hits where not coalesce(is_test,false) and at > now() - ($1 || ' days')::interval group by bot order by n desc`, [String(days)]);
    const pages = await sql(`select path, count(*)::int n, count(distinct bot)::int bots, string_agg(distinct bot, ', ') names from crawler_hits where not coalesce(is_test,false) and at > now() - ($1 || ' days')::interval group by path order by n desc limit 50`, [String(days)]);
    sql(`delete from crawler_hits where at < now() - interval '120 days'`).catch(() => {});
    return json(res, 200, { days, bots, pages });
  } catch (e) {
    if (/does not exist/.test(e.message)) return json(res, 200, { days, bots: [], pages: [] });
    return json(res, 500, { error: "db_error" });
  }
}
