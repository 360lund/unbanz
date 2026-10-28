// Unbanz wiring for the session-replay module (replay-kit/). Everything site-specific lives here.
import { createReplay } from "../../replay-kit/server/core.mjs";
import { sql } from "./db.mjs";
import { authed } from "./uauth.mjs";
export default createReplay({
  sql,
  authed,                                              // same cookie / X-Users-Token session as the rest of /users
  brand: process.env.REPLAY_BRAND || "unbanz.com",     // host column value
  visitsTable: "visits",
  retentionDays: Number(process.env.REPLAY_RETENTION_DAYS) || 14,
});
