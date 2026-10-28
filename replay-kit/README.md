# replay-kit — self-hosted session replay

A small, copy-able session replay (Clarity-style) for static sites on Vercel + Neon Postgres.

| Part | File | Runs where | Size |
|---|---|---|---|
| Recorder | `src/recorder.js` (+ vendored rrweb `record`, MIT) → `assets/rec.<hash>.js` | public pages | ~22 KB gz |
| API core | `server/core.mjs` (no npm deps) | serverless | – |
| Player UI | `src/player.js`, `src/player.css` (+ rrweb `replay`) → `assets/rpv.<hash>.js` | dashboard only | ~76 KB gz |
| Build | `build.mjs` (esbuild; hashed output + `dist-*.txt`) | dev machine | – |
| Tools | `tools/inject-tag.mjs`, `tools/rebuild.sh` | dev machine | – |
| Test | `test/harness.mjs` (pglite fake Neon + real handlers), `test/e2e/*.py` (Playwright) | dev machine | – |

## Wiring (3 tiny files in the host repo)
```js
// api/_lib/replay.mjs
import { createReplay } from "../../replay-kit/server/core.mjs";
export default createReplay({ sql, authed, brand: "unbanz.com", visitsTable: "visits", retentionDays: 14 });
// api/users/rp.mjs        (public)  export default (req,res) => replay.ingest(req,res)
// api/users/replays.mjs   (private) export default (req,res) => replay.replays(req,res)
```
* `sql(text, params)` → array of row objects. `authed(req)` → boolean (the same check as the rest of the dashboard).
* `brand` is written to the `host` column of every row and the dashboard lists only that brand, so several sites can share one DB.
* `visitsTable` must have `id` (tracker session id) and the columns the list joins (source, device, country, pages, started_at, saw_cta, … — see `core.mjs`).

## Data / retention / privacy
* New tables only (created on demand): `session_replays` (PK sid,pg,idx; gzip payload), `session_replay_index`. Existing tables are never altered.
* Retention: 14 days (`retentionDays`), test sessions 24 h. Cleanup is cron-free: runs on a session's first chunk and on dashboard list loads (≤ once / 10 min).
* Caps: 10 min / 1.5 MB per session on the client; server: 400 KB per request, 2 MB per session, 24 chunks/min/session, 40 new sessions/IP-hash/hour, 250 MB global.
* All form values masked, passwords never captured, `/users` and `/api` pages never recorded, bots / `ubz_test=1` / owner browsers (`ubz_norec=1`) skipped.

## Build & tag
```
cd replay-kit && npm i && tools/rebuild.sh ..    # builds rec + rpv, tags every *.html after the site*.js script, updates the rpv ref in users/index.html
```
See `PORTING.md` for reusing it on another site.
