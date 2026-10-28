# Porting notes — reusing replay-kit on another site (e.g. atclaim.com / ogclaim.com / usernm.com, the "pofofo" project)

No secrets live in this kit. Env vars are named only; values stay in the host's Vercel project.

## 1. What to copy
```
replay-kit/            (whole folder; node_modules is git-ignored)
  server/core.mjs        API core, framework-free, zero deps
  src/recorder.js        recorder source (bundled with @rrweb/record)
  src/player.js, player.css   dashboard player (bundled with @rrweb/replay)
  build.mjs              esbuild → assets/rec.<hash>.js, assets/rpv.<hash>.js, dist-rec.txt, dist-rpv.txt
  tools/inject-tag.mjs, tools/rebuild.sh
  test/harness.mjs, test/e2e/*.py     (optional but handy)
api/_lib/replay.mjs, api/users/rp.mjs, api/users/replays.mjs   (3 thin wiring files)
```
`npm i` inside `replay-kit/` (dev deps: @rrweb/record, @rrweb/replay, esbuild, @electric-sql/pglite for the harness only).

## 2. Wire it
`api/_lib/replay.mjs` calls `createReplay({ sql, authed, brand, visitsTable, retentionDays })`.
* `sql(text, params)` → rows (the host's own Neon helper). `authed(req)` → true for a logged-in dashboard user (same cookie / header as the rest of the dashboard).
* **brand**: set a different value per site (`REPLAY_BRAND` env, e.g. `atclaim.com`). It is stored in the `host` column of `session_replays` / `session_replay_index`; the list API only returns rows for that brand, so all brands can share one Neon DB and the same tables.
* **visitsTable**: the existing visit/session table (needs `id` = tracker session id plus the columns used by the list query; adapt the SELECT in `core.mjs` if the pofofo schema differs). Ingest returns 404 if the visit row doesn't exist yet (the recorder starts only after the tracker has created it). If pofofo has no such table, point `visitsTable` at its equivalent or make the visit join optional.
* Optional env: `REPLAY_RETENTION_DAYS` (default 14), limits via createReplay options (maxChunkBytes, maxSessionBytes, maxChunksPerMinute, maxSessionsPerIpHour, maxTotalBytes, testRetentionHours, tz).
* Routes: `POST /api/users/rp/` public ingest · `GET /api/users/replays/` list (filters: range, source, device, clicked, converted, test) · `?ids=1` ids with replays · `?sid=<id>` binary frames `[u8 gz][u32be len][bytes]…` · `DELETE ?sid=<id>`.

## 3. Recorder contract
* Config (optional, set before the tag): `window.UBZ_REPLAY = { endpoint, sessionKey, maxMs, maxBytes, flushMs }`.
* Needs the tracker's session id in `sessionStorage[sessionKey]` (default `ubz1`, JSON `{id}`); no id → no recording. Skips `/users*`, `/api*`, bots/webdriver, `localStorage.ubz_test=1`, `localStorage.ubz_norec=1` (also `?norec=1` / `?norec=0`).
* Emits custom events `cta` and `nav` (used for timeline markers); if the new site's CTA clicks use other selectors, adjust the small hook in `recorder.js`.
* Privacy: every input/textarea/select value masked; password inputs never captured.
* Delivery: gzip via CompressionStream (plain JSON fallback), sendBeacon/keepalive every ~6 s and on pagehide, per-session cap 10 min / 1.5 MB.

## 4. Build and tag
```
cd replay-kit && tools/rebuild.sh ..          # or: node build.mjs all
node tools/inject-tag.mjs .. rec.<hash>.js [--anchor '<regex of the tracker script tag>'] [--skip apply/index.html] [--dry]
```
`inject-tag` is idempotent: inserts `<script src="/assets/rec.<hash>.js" defer></script>` after the tracker tag in every `.html`, re-points an existing rec tag on a rebuild, and reports pages without the anchor. Old hashed files are kept (never deleted). Each rebuild produces a new hash.

## 5. Dashboard integration
In the dashboard HTML: a container (`<div id="vR" hidden>`), a lazy `<script src="/assets/rpv.<hash>.js">` loaded only when the Replays tab opens, then
`UbzReplays.mount(el, { api: '/api/users/replays/', headers: () => ({'X-Users-Token': …}), onAuthFail, tz, tzLabel })`. Also `UbzReplays.open(sid)`, `.refresh()`, `.close()`. Deep links: `#replays`, `#replay=<sid>`. Set `localStorage.ubz_norec=1` on the dashboard so the owner's browser is never recorded. The player CSS is scoped under `.rpx` / `.rp-*` and adopts the dashboard's CSS variables.

## 6. Storage, retention, safety
* New tables only: `session_replays(sid, pg, idx, host, payload bytea, gz, bytes, ev, t0, t1, is_test, created_at)` PK (sid, pg, idx); `session_replay_index(sid, host, is_test, ih, chunks, bytes, events, t0, t1, …)`. Created on demand with `create table if not exists`; nothing existing is modified.
* Retention 14 d (test sessions 24 h), deleted on a session's first chunk and on dashboard list loads (throttled to once per 10 min) — no cron needed.
* Abuse: POST only, bot UA → 204, validated ids, 400 KB body / 8 MB inflated limits, per-session chunk/byte caps, per-session 24 chunks/min, per-IP-hash 40 new sessions/hour (IP stored only as a truncated SHA-256 hash), global 250 MB cap.

## 7. Verify on the new site
`node test/harness.mjs 8099` (pglite stand-in for Neon running the real handlers) then the Playwright scripts in `test/e2e/` (use a non-headless Chrome UA; pass `ubz_rec_test=1` in localStorage to override the bot/webdriver skip). Don't test against production analytics without tagging sessions as test (`ubz_test=1`) and deleting them afterwards.
