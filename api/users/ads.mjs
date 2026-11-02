import { json } from "../_lib/auth.mjs";
import { authed } from "../_lib/uauth.mjs";
import { sql } from "../_lib/db.mjs";
const TZ = "Asia/Karachi";
// Rolling windows: 24h is exactly the last 24 hours (not 7 days).
const WIN = { "24h": "24 hours", "7d": "7 days", "30d": "30 days" };
let migrated;
const migrate = () => (migrated ||= sql(`alter table visits add column if not exists utm_content text, add column if not exists utm_term text, add column if not exists fbclid text, add column if not exists gclid text, add column if not exists ttclid text, add column if not exists landing_url text, add column if not exists ad_paid boolean, add column if not exists ad_platform text, add column if not exists is_bot boolean, add column if not exists is_test boolean, add column if not exists active_s int, add column if not exists scroll_max int`).catch((e) => { migrated = null; throw e; }));
// Older rows (before the ads columns) fall back to the client classifier's 'Ads' group / paid utm_medium.
const PAID = `coalesce(ad_paid, source_group = 'Ads' or coalesce(utm_medium,'') ~* '^(cpc|ppc|paid|paid_?social|paidsocial|ads?|display|cpm|sponsored)$')`;
const PLAT = `coalesce(ad_platform, case when source ilike 'Google%' then 'Google' when source ilike 'TikTok%' then 'TikTok' when source ilike 'ChatGPT%' then 'ChatGPT ads' when source ilike 'Instagram%' then 'Instagram' when source ilike any(array['Facebook%','Meta%']) then 'Facebook' else 'Other' end)`;
const LEAD = `(coalesce(clicked_whatsapp,false) or coalesce(clicked_email,false))`;
export default async function handler(req, res) {
  if (req.method !== "GET") return json(res, 405, { error: "method_not_allowed" });
  if (!authed(req, res)) return json(res, 401, { error: "unauthorized" });
  const q = new URL(req.url, "http://x").searchParams;
  const range = WIN[q.get("range")] ? q.get("range") : "7d";
  const NT = q.get("test") === "1" ? `true` : `coalesce(is_test, false) = false`;
  const f = `started_at > now() - interval '${WIN[range]}' and ${NT} and coalesce(is_bot, false) = false and ${PAID}`;
  const g = (k) => `select ${k} as k, count(*)::int as n, count(*) filter (where ${LEAD})::int as c from visits where ${f} group by 1 order by c desc, n desc limit 25`;
  try {
    await migrate();
    const [tot, platform, campaign, ad, landing, country, daily, leads, bots] = await Promise.all([
      sql(`select count(*)::int as n, count(*) filter (where ${LEAD})::int as c, count(*) filter (where clicked_whatsapp)::int as wa, count(*) filter (where clicked_email)::int as em, count(*) filter (where coalesce(active_s,0) >= 5 or coalesce(scroll_max,0) >= 25)::int as engaged, min(started_at) as first from visits where ${f}`),
      sql(g(PLAT)), sql(g(`coalesce(utm_campaign,'(none)')`)), sql(g(`coalesce(utm_content,'(none)')`)), sql(g(`landing`)),
      sql(`select coalesce(country,'??') as k, count(*)::int as n, count(*) filter (where ${LEAD})::int as c from visits where ${f} group by 1 order by c desc, n desc limit 60`),
      sql(`select to_char((started_at at time zone '${TZ}')::date,'YYYY-MM-DD') as d, count(*)::int as n, count(*) filter (where ${LEAD})::int as c from visits where ${f} group by 1 order by 1`),
      sql(`select started_at, last_at, ${PLAT} as platform, utm_campaign, utm_content, utm_term, landing, country, city, device, clicked_whatsapp as wa, clicked_email as em, platform as acct, service from visits where ${f} and ${LEAD} order by started_at desc limit 50`),
      sql(`select count(*)::int as n from visits where started_at > now() - interval '${WIN[range]}' and ${NT} and is_bot and ${PAID}`),
    ]);
    return json(res, 200, { range, tot: tot[0], platform, campaign, ad, landing, country, daily, leads, bots: bots[0].n, now: new Date().toISOString() });
  } catch (e) {
    return json(res, 500, { error: "db_error" });
  }
}
