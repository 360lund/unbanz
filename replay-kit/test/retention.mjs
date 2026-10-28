// Retention check: backdated rows are removed by cleanup(); fresh ones stay. Run: node test/retention.mjs
import { PGlite } from "@electric-sql/pglite";
import { createReplay } from "../server/core.mjs";
const db = new PGlite();
const sql = async (t, p = []) => (await db.query(t, p)).rows;
const r = createReplay({ sql, authed: () => true, brand: "t", retentionDays: 14 });
await r.schema();
const ins = (sid, days, test = false, hrs = 0) => sql(`insert into session_replay_index(sid,host,is_test,created_at,updated_at) values($1,'t',$2, now() - ($3||' days')::interval - ($4||' hours')::interval, now())`, [sid, test, days, hrs])
  .then(() => sql(`insert into session_replays(sid,pg,idx,host,payload,gz,bytes,ev,is_test,created_at) values($1,'p',0,'t','\\x00',false,1,1,$2, now() - ($3||' days')::interval - ($4||' hours')::interval)`, [sid, test, days, hrs]));
await ins("old15d", 15); await ins("new1d", 1); await ins("test30h", 0, true, 30); await ins("test2h", 0, true, 2);
await r.cleanup(true);
const left = (await sql("select sid from session_replay_index order by sid")).map((x) => x.sid);
const left2 = (await sql("select distinct sid from session_replays order by sid")).map((x) => x.sid);
console.log("index:", left.join(","), "| chunks:", left2.join(","));
const ok = left.join() === "new1d,test2h" && left2.join() === "new1d,test2h";
console.log(ok ? "RETENTION OK" : "RETENTION FAIL"); process.exit(ok ? 0 : 1);
