import { hasValidSession, issueSession, json } from "../_lib/auth.mjs";
import { sql } from "../_lib/db.mjs";
const TZ = "Asia/Karachi";
const day = (s) => (/^\d{4}-\d{2}-\d{2}$/.test(s || "") ? s : null);
export default async function handler(req, res) {
  if (req.method !== "GET") return json(res, 405, { error: "method_not_allowed" });
  if (!hasValidSession(req)) return json(res, 401, { error: "unauthorized" });
  issueSession(res); // sliding: every authenticated request extends the year
  const q = new URL(req.url, "http://x").searchParams;
  const range = q.get("range") || "7d";
  // date window in Karachi local days: [from, to] inclusive
  let fromExpr, toExpr, p = [];
  const now = `(now() at time zone '${TZ}')::date`;
  if (range === "custom" && day(q.get("from"))) {
    p.push(day(q.get("from")), day(q.get("to")) || day(q.get("from")));
    fromExpr = `$1::date`; toExpr = `$2::date`;
  } else {
    const n = { today: 0, "7d": 6, "30d": 29, "90d": 89 }[range] ?? 6;
    fromExpr = `(${now} - ${n})`; toExpr = now;
  }
  // previous period of the same length, right before the window
  const lenExpr = `(${toExpr} - ${fromExpr} + 1)`;
  const prevWin = `(started_at at time zone '${TZ}')::date between ${fromExpr} - ${lenExpr} and ${fromExpr} - 1`;
  const local = `(started_at at time zone '${TZ}')::date`;
  const win = `${local} between ${fromExpr} and ${toExpr}`;
  const fp = [...p];
  let f = win;
  if (q.get("group")) { fp.push(q.get("group").slice(0, 20)); f += ` and source_group = $${fp.length}`; }
  if (q.get("source")) { fp.push(q.get("source").slice(0, 40)); f += ` and source = $${fp.length}`; }
  if (q.get("clicked") === "1") f += ` and (clicked_whatsapp or clicked_email)`;
  try {
    const pf = f.replace(win, prevWin);
    const [kpi, inRange, prev, sources, recent, landing, countries, daily, devices] = await Promise.all([
      sql(`select count(*) filter (where ${local} = ${now}) as today, count(*) filter (where ${local} = ${now} - 1) as yesterday, count(*) filter (where ${local} > ${now} - 7) as d7, count(*) filter (where ${local} between ${now} - 13 and ${now} - 7) as p7, count(*) filter (where ${local} > ${now} - 30) as d30, count(*) filter (where ${local} between ${now} - 59 and ${now} - 30) as p30 from visits where started_at > now() - interval '62 days'`),
      sql(`select count(*) as visitors, count(*) filter (where clicked_whatsapp) as wa, count(*) filter (where clicked_email) as email, count(*) filter (where opened_popup) as popup, count(*) filter (where clicked_whatsapp or clicked_email) as converted, coalesce(avg(page_count),0)::float as pages from visits where ${f}`, fp),
      sql(`select count(*) as visitors, count(*) filter (where clicked_whatsapp) as wa, count(*) filter (where clicked_email or clicked_whatsapp) as converted from visits where ${pf}`, fp),
      sql(`select source_group as g, source as s, count(*)::int as n, count(*) filter (where clicked_whatsapp or clicked_email)::int as c, array_agg(distinct ref_domain) filter (where source_group='Other' and ref_domain is not null) as domains from visits where ${win} group by 1,2 order by n desc`, p),
      sql(`select id, started_at, last_at, source, source_group as g, medium, ref_domain, utm_campaign, search_term, landing, pages, page_count, country, city, device, browser, os, clicked_whatsapp, clicked_email, opened_popup, platform, service from visits where ${f} order by started_at desc limit 150`, fp),
      sql(`select landing as k, count(*)::int as n, count(*) filter (where clicked_whatsapp or clicked_email)::int as c from visits where ${f} group by 1 order by n desc limit 10`, fp),
      sql(`select coalesce(country,'??') as k, count(*)::int as n, count(*) filter (where clicked_whatsapp or clicked_email)::int as c from visits where ${f} group by 1 order by n desc limit 5`, fp),
      sql(`select to_char(${local},'YYYY-MM-DD') as d, count(*)::int as n, count(*) filter (where clicked_whatsapp or clicked_email)::int as c, count(*) filter (where clicked_whatsapp)::int as w from visits where ${f} group by 1 order by 1`, fp),
      sql(`select device as k, count(*)::int as n from visits where ${f} group by 1 order by n desc`, fp),
    ]);
    return json(res, 200, { kpi: kpi[0], range: inRange[0], prev: prev[0], sources, recent, landing, countries, daily, devices, now: new Date().toISOString() });
  } catch (e) {
    return json(res, 500, { error: "db_error" });
  }
}
