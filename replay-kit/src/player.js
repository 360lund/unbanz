// Replays dashboard section: filterable list + session player. Loaded only on the dashboard (never on public pages).
//   UbzReplays.mount(rootEl, { api, headers, onAuthFail, tz, tzLabel })
//   UbzReplays.refresh()   re-fetch the list        UbzReplays.open(sid) / .close()
// Deep link: #replay=<sid> (the module watches the hash).
import { Replayer } from "@rrweb/replay";
import rrCss from "@rrweb/replay/dist/style.css";
import css from "./player.css";

(() => {
  "use strict";
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const IC = {
    play: '<svg viewBox="0 0 16 16" fill="currentColor"><path d="M4 2.5v11l9.5-5.5z"/></svg>',
    pause: '<svg viewBox="0 0 16 16" fill="currentColor"><rect x="3.5" y="2.5" width="3" height="11" rx=".8"/><rect x="9.5" y="2.5" width="3" height="11" rx=".8"/></svg>',
    redo: '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13.5 8a5.5 5.5 0 1 1-1.8-4.1"/><path d="M13.5 2.5v3h-3"/></svg>',
    x: '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3.5 3.5l9 9M12.5 3.5l-9 9"/></svg>',
    prev: '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3L5 8l5 5"/></svg>',
    next: '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3l5 5-5 5"/></svg>',
    trash: '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 4.5h11M6 4.5V3h4v1.5M4 4.5l.7 8.5h6.6l.7-8.5"/></svg>',
    link: '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6.8 9.2a3 3 0 0 0 4.2 0l2-2a3 3 0 0 0-4.2-4.2l-.8.8"/><path d="M9.2 6.8a3 3 0 0 0-4.2 0l-2 2a3 3 0 0 0 4.2 4.2l.8-.8"/></svg>',
    list: '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><path d="M5.5 4h8M5.5 8h8M5.5 12h8M2.5 4h.01M2.5 8h.01M2.5 12h.01"/></svg>',
  };

  let styleEl;
  const injectCss = () => { if (styleEl) return; styleEl = document.createElement("style"); styleEl.textContent = rrCss + "\n" + css; document.head.appendChild(styleEl); };

  const CFG = { api: "/api/users/replays/", headers: () => ({}), onAuthFail: () => {}, tz: "Asia/Karachi", tzLabel: "PKT" };
  const hdr = () => ({ ...(CFG.headers() || {}) });
  const SEEN_KEY = "rp_seen";
  const seenSet = () => { try { return new Set(JSON.parse(localStorage.getItem(SEEN_KEY) || "[]")); } catch { return new Set(); } };
  const markSeen = (sid) => { try { const s = seenSet(); s.add(sid); localStorage.setItem(SEEN_KEY, JSON.stringify([...s].slice(-600))); } catch {} };

  const mmss = (ms) => { const s = Math.max(0, Math.round(ms / 1000)); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); };
  const mmss1 = (ms) => { const s = Math.max(0, Math.floor(ms / 1000)); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); };
  let regionName; try { regionName = new Intl.DisplayNames(["en"], { type: "region" }); } catch {}
  const country = (c) => (!c || c === "??" ? "Unknown" : (regionName && regionName.of(c)) || c);
  const flag = (c) => (c && /^[A-Z]{2}$/.test(c) ? String.fromCodePoint(...[...c].map((x) => 127397 + x.charCodeAt(0))) : "");
  const when = (t) => new Date(t).toLocaleString("en-GB", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit", timeZone: CFG.tz });
  const ago = (t) => { const s = Math.max(0, (Date.now() - new Date(t)) / 1e3); return s < 45 ? "Just now" : s < 3600 ? Math.round(s / 60) + "m ago" : s < 86400 ? Math.round(s / 3600) + "h ago" : Math.round(s / 86400) + "d ago"; };
  const pathOf = (h) => { try { const u = new URL(h, "https://x"); return (u.pathname || "/") + (u.hash || ""); } catch { return h || "/"; } };

  // ===================== list =====================
  const F = { range: "7d", source: "", device: "", clicked: false, converted: false };
  let root, rows = [], sources = new Set(), loading = false, listTimer = 0, fetchSeq = 0;

  async function api(qs, opt = {}) {
    const r = await fetch(CFG.api + qs, { credentials: "same-origin", headers: hdr(), ...opt });
    if (r.status === 401) { CFG.onAuthFail(); throw new Error("auth"); }
    return r;
  }

  function mountList() {
    root.classList.add("rpx");
    root.innerHTML = `
      <div class="rp-tool">
        <div class="rp-seg" id="rp-range" role="group" aria-label="Date range"><button data-r="today">Today</button><button data-r="7d" aria-pressed="true">7d</button><button data-r="14d">14d</button></div>
        <select class="rp-field" id="rp-src" aria-label="Source"><option value="">All sources</option></select>
        <select class="rp-field" id="rp-dev" aria-label="Device"><option value="">All devices</option><option>Mobile</option><option>Desktop</option><option>Tablet</option></select>
        <button class="rp-tg" id="rp-clk" aria-pressed="false"><i></i>Clicked WhatsApp / popup</button>
        <button class="rp-tg" id="rp-cv" aria-pressed="false"><i></i>Converted</button>
        <span class="rp-note num" id="rp-note"></span>
      </div>
      <section class="rp-card"><div class="rp-head"><span>Time (${esc(CFG.tzLabel)})</span><span>Source</span><span>Country</span><span>Device</span><span>Pages</span><span>Length</span><span>Outcome</span></div><div id="rp-list"></div></section>
      <p class="rp-foot" id="rp-foot"></p>`;
    const $ = (s) => root.querySelector(s);
    $("#rp-range").addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b) return; F.range = b.dataset.r; $("#rp-range").querySelectorAll("button").forEach((x) => x.setAttribute("aria-pressed", x === b)); refresh(true); });
    $("#rp-src").addEventListener("change", (e) => { F.source = e.target.value; refresh(true); });
    $("#rp-dev").addEventListener("change", (e) => { F.device = e.target.value; refresh(true); });
    for (const [id, k] of [["#rp-clk", "clicked"], ["#rp-cv", "converted"]]) $(id).addEventListener("click", (e) => { F[k] = !F[k]; e.currentTarget.setAttribute("aria-pressed", F[k]); refresh(true); });
    $("#rp-list").addEventListener("click", (e) => { const r = e.target.closest(".rp-row"); if (r) go(r.dataset.sid); });
    root.addEventListener("keydown", (e) => { if (e.key === "Enter" && e.target.classList.contains("rp-row")) go(e.target.dataset.sid); });
  }

  const chips = (r) => {
    const o = [];
    if (r.opened_popup) o.push('<span class="rp-chip pop">Popup</span>');
    if (r.clicked_whatsapp) o.push('<span class="rp-chip wa">WhatsApp</span>');
    if (r.clicked_email) o.push('<span class="rp-chip em">Email</span>');
    return o.length ? o.join("") : '<span class="rp-chip no">No click</span>';
  };

  function renderList() {
    const el = root.querySelector("#rp-list");
    const seen = seenSet();
    if (loading && !rows.length) { el.innerHTML = Array(6).fill('<div style="padding:12px 16px"><div class="rp-sk" style="height:34px"></div></div>').join(""); return; }
    if (!rows.length) { el.innerHTML = '<div class="rp-empty"><b>No replays match</b><span>Sessions appear here a few seconds after a visitor opens a page.</span></div>'; return; }
    el.innerHTML = rows.map((r) => {
      const pages = Array.isArray(r.pages) ? r.pages : [];
      const n = r.page_count || pages.length || 1;
      const first = pathOf(r.landing || pages[0] || "/");
      const dur = r.t1 && r.t0 ? mmss(r.t1 - r.t0) : "–";
      const when1 = r.started_at || r.created_at;
      return `<button class="rp-row" data-sid="${esc(r.sid)}" aria-label="Watch replay">
        <div class="rp-c rp-time c-t"><span class="rp-seen ${seen.has(r.sid) ? "s" : ""}" title="${seen.has(r.sid) ? "Watched" : "New"}"></span><div><b class="num">${esc(when(when1))}</b><span>${esc(ago(when1))}${r.is_test ? " · test" : ""}</span></div></div>
        <div class="rp-c c-s"><b>${esc(r.source || "Direct")}</b><span>${esc(r.g || "")}</span></div>
        <div class="rp-c c-c"><b>${flag(r.country) ? flag(r.country) + " " : ""}${esc(country(r.country))}</b><span>${esc(r.city || "")}</span></div>
        <div class="rp-c c-v"><b>${esc(r.device || "–")}</b><span>${esc([r.browser, r.os].filter(Boolean).join(" · "))}</span></div>
        <div class="rp-c c-p"><b>${esc(first)}</b><span>${n} page${n === 1 ? "" : "s"}${n > 1 ? " · " + esc(pages.slice(1, 3).map(pathOf).join(", ")) + (n > 3 ? "…" : "") : ""}</span></div>
        <div class="rp-c c-d"><span class="rp-dur">${dur}</span></div>
        <div class="rp-out c-o">${chips(r)}</div></button>`;
    }).join("");
  }

  async function refresh(force) {
    if (!root || (loading && !force)) return;
    if (!force && player) return;                        // do not shuffle the list under an open player
    loading = true; const seq = ++fetchSeq;
    if (force) renderList();
    const p = new URLSearchParams({ range: F.range });
    if (F.source) p.set("source", F.source);
    if (F.device) p.set("device", F.device);
    if (F.clicked) p.set("clicked", "1");
    if (F.converted) p.set("converted", "1");
    try {
      const d = await (await api("?" + p)).json();
      if (seq !== fetchSeq) return;
      rows = d.replays || [];
      for (const r of rows) if (r.source) sources.add(r.source);
      const sel = root.querySelector("#rp-src");
      sel.innerHTML = '<option value="">All sources</option>' + [...sources].sort().map((s) => `<option${s === F.source ? " selected" : ""}>${esc(s)}</option>`).join("");
      const mb = (Number(d.stats?.bytes || 0) / 1e6).toFixed(1);
      root.querySelector("#rp-note").textContent = `${rows.length} replay${rows.length === 1 ? "" : "s"} · ${d.stats?.sessions ?? 0} stored (${mb} MB) · ${d.retentionDays}-day retention`;
      root.querySelector("#rp-foot").textContent = `Replays rebuild each visitor’s screen from recorded page changes, mouse, taps and scrolls. All form fields are masked and passwords are never recorded; the dashboard, your own browser and test traffic are not recorded. Sessions are capped at about 10 minutes and deleted after ${d.retentionDays} days.`;
    } catch (e) { if (e.message !== "auth") root.querySelector("#rp-list").innerHTML = '<div class="rp-empty"><b>Could not load replays</b><span>Try again in a moment.</span></div>'; rows = rows || []; }
    loading = false; renderList();
  }

  // ===================== player =====================
  let player = null, cameFromList = false;

  const go = (sid) => { cameFromList = true; location.hash = "replay=" + sid; };

  function sync() {
    const m = /^#replay=([a-z0-9]{8,40})$/i.exec(location.hash);
    if (m) { if (!player || player.sid !== m[1]) openPlayer(m[1]); } else if (player) closePlayer();
  }

  async function loadEvents(sid, onProgress) {
    const r = await api("?sid=" + encodeURIComponent(sid));
    if (!r.ok) throw new Error(r.status === 404 ? "notfound" : "load");
    const buf = new Uint8Array(await r.arrayBuffer());
    onProgress && onProgress(buf.length);
    const dv = new DataView(buf.buffer);
    const all = [];
    for (let o = 0; o + 5 <= buf.length;) {
      const gz = buf[o], len = dv.getUint32(o + 1); o += 5;
      let bytes = buf.subarray(o, o + len); o += len;
      try {
        if (gz) bytes = new Uint8Array(await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"))).arrayBuffer());
        const arr = JSON.parse(new TextDecoder().decode(bytes));
        for (const e of arr) all.push(e);
      } catch { /* skip a damaged chunk */ }
    }
    all.sort((a, b) => a.timestamp - b.timestamp);
    // The stream must start at a Meta + FullSnapshot pair.
    const fi = all.findIndex((e) => e.type === 2);
    if (fi < 0) return [];
    let mi = -1; for (let i = fi - 1; i >= 0; i--) if (all[i].type === 4) { mi = i; break; }
    const meta = mi >= 0 ? all[mi] : { type: 4, timestamp: all[fi].timestamp, data: { href: "", width: 1280, height: 720 } };
    return [meta, ...all.slice(fi)];
  }

  function analyse(events) {
    const t0 = events[0].timestamp, total = Math.max(1, events[events.length - 1].timestamp - t0);
    const touchy = (events[0].data.width || 1280) <= 820;
    const marks = [], act = [];
    let lastHref = null;
    for (const e of events) {
      const t = e.timestamp - t0;
      if (e.type === 4) {
        const h = e.data && e.data.href;
        if (h !== lastHref || !marks.some((m) => m.k === "page")) marks.push({ t, k: "page", label: pathOf(h || "") });
        lastHref = h; act.push(t);
      } else if (e.type === 5 && e.data && e.data.tag === "cta") {
        const k = e.data.payload && e.data.payload.k;
        const label = { whatsapp: "Clicked WhatsApp", popup: "Opened WhatsApp popup", email: "Clicked email" }[k];
        if (label) {
          for (let i = marks.length - 1; i >= 0 && marks[i].t >= t - 600; i--) if (marks[i].k === "click") marks.splice(i, 1);   // the generic click that opened it
          marks.push({ t, k: k === "whatsapp" ? "wa" : k, label });
        }
      } else if (e.type === 5 && e.data && e.data.tag === "nav") {
        marks.push({ t, k: "page", label: pathOf(e.data.payload && e.data.payload.h) });
      } else if (e.type === 3) {
        const s = e.data.source;
        if (s === 2 && e.data.type === 2) marks.push({ t, k: "click", label: touchy ? "Tap" : "Click" });
        if (s === 1 || s === 2 || s === 3 || s === 5 || s === 6 || s === 12) act.push(t);
      }
    }
    marks.sort((a, b) => a.t - b.t);
    const gaps = [];
    for (let i = 1; i < act.length; i++) if (act[i] - act[i - 1] >= 3000) gaps.push([act[i - 1], act[i]]);
    return { t0, total, marks, gaps, touchy, w: events[0].data.width || 1280, h: events[0].data.height || 720 };
  }

  async function openPlayer(sid) {
    closePlayer(true);
    injectCss();
    const idx = rows.findIndex((r) => r.sid === sid);
    const info = idx >= 0 ? rows[idx] : null;
    const P = (player = { sid, idx, info, raf: 0, dead: false, rep: null, playing: false, speed: 1, skip: true, cur: -1 });
    const ov = document.createElement("div");
    ov.className = "rpx rp-ov";
    ov.setAttribute("role", "dialog"); ov.setAttribute("aria-modal", "true"); ov.setAttribute("aria-label", "Session replay");
    const title = info ? `${flag(info.country) ? flag(info.country) + " " : ""}${esc(country(info.country))}${info.city ? ", " + esc(info.city) : ""} · ${esc(info.source || "Direct")}` : "Session replay";
    const sub = info ? esc([info.device, info.browser, info.os].filter(Boolean).join(" · ") + " · " + when(info.started_at || info.created_at) + " " + CFG.tzLabel) : "";
    ov.innerHTML = `
      <div class="rp-top">
        <button class="rp-btn" data-a="close" aria-label="Back to replays">${IC.prev}<span class="t">Replays</span></button>
        <div class="rp-ttl"><b>${title}</b><span>${sub}</span></div>
        <button class="rp-btn" data-a="newer" aria-label="Newer session" title="Newer session">${IC.prev}</button>
        <button class="rp-btn" data-a="older" aria-label="Older session" title="Older session">${IC.next}</button>
        <button class="rp-btn" data-a="link" aria-label="Copy link" title="Copy link">${IC.link}</button>
        <button class="rp-btn del" data-a="del" aria-label="Delete replay" title="Delete replay">${IC.trash}</button>
        <button class="rp-btn sidetg" data-a="side" aria-label="Session details">${IC.list}</button>
      </div>
      <div class="rp-main">
        <div class="rp-stagewrap">
          <div class="rp-addr"><span class="pill"><em class="n">–</em><b class="u">Loading…</b></span></div>
          <div class="rp-stage"><div class="rp-frame" style="opacity:0"><div class="rp-scaler"><div class="rp-root"></div></div></div>
            <button class="rp-big" data-a="play" aria-label="Play"><span></span></button>
            <div class="rp-load"><div class="rp-spin"></div><span class="lt">Loading replay…</span></div>
            <div class="rp-toast"></div><div class="rp-skip">Skipping inactivity…</div></div>
          <div class="rp-ctl">
            <div class="rp-bar" tabindex="0" role="slider" aria-label="Timeline" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><div class="rp-track"><div class="rp-fill"></div></div><div class="rp-thumb"></div><div class="rp-tip"></div></div>
            <div class="rp-row2">
              <button class="rp-play" data-a="play" aria-label="Play">${IC.play}</button>
              <span class="rp-time2"><b class="tc">0:00</b> / <span class="tt">0:00</span></span>
              <div class="rp-seg rp-sp" role="group" aria-label="Speed"><button data-s="1" aria-pressed="true">1x</button><button data-s="2">2x</button><button data-s="4">4x</button></div>
              <button class="rp-tg" data-a="skip" aria-pressed="true"><i></i>Skip inactivity</button>
            </div>
            <div class="rp-legend"><span><i></i>Page</span><span><i class="c"></i>Click</span><span><i class="p"></i>Popup</span><span><i class="w"></i>WhatsApp</span><span><i class="e"></i>Email</span><span>Space play · ←/→ 5s · 1/2/4 speed · S skip · Esc close</span></div>
          </div>
        </div>
        <aside class="rp-side"><div class="rp-sec"><h3>Session</h3><dl class="rp-kv" id="rp-kv"></dl></div><div class="rp-sec" style="padding-bottom:4px;border:0"><h3>Events</h3></div><div class="rp-evs"></div></aside>
      </div>`;
    document.body.appendChild(ov);
    document.documentElement.style.overflow = "hidden";
    P.ov = ov;
    const q = (s) => ov.querySelector(s);
    P.el = { stage: q(".rp-stage"), frame: q(".rp-frame"), scaler: q(".rp-scaler"), root: q(".rp-root"), load: q(".rp-load"), lt: q(".lt"), toast: q(".rp-toast"), skip: q(".rp-skip"), big: q(".rp-big"), bar: q(".rp-bar"), track: q(".rp-track"), fill: q(".rp-fill"), thumb: q(".rp-thumb"), tip: q(".rp-tip"), tc: q(".tc"), tt: q(".tt"), play: q(".rp-play"), url: q(".u"), n: q(".n"), evs: q(".rp-evs"), kv: q("#rp-kv") };
    ov.querySelector('[data-a="newer"]').disabled = idx <= 0;
    ov.querySelector('[data-a="older"]').disabled = idx < 0 || idx >= rows.length - 1;
    ov.querySelector('[data-a="del"]').disabled = false;
    fillInfo(P);
    bindPlayer(P);
    markSeen(sid);
    if (root) renderList();
    q('[data-a="play"]').focus({ preventScroll: true });

    let events;
    try { events = await loadEvents(sid, (n) => { P.el.lt.textContent = `Preparing replay… ${(n / 1024).toFixed(0)} KB`; }); }
    catch (e) { if (!P.dead) showErr(P, e.message === "notfound" ? "This replay was deleted or has expired." : "Could not load this replay."); return; }
    if (P.dead) return;
    if (events.length < 2) return showErr(P, "Nothing usable was recorded for this visit.");
    P.events = events; P.a = analyse(events);
    P.el.tt.textContent = mmss(P.a.total);
    buildBar(P); buildEvents(P);
    try {
      P.rep = new Replayer(events, { root: P.el.root, speed: 1, skipInactive: true, inactivePeriodThreshold: 3000, maxSpeed: 360, mouseTail: false, showWarning: false, showDebug: false, triggerFocus: false, pauseAnimation: true, liveMode: false, useVirtualDom: false });
    } catch (e) { return showErr(P, "This recording could not be rebuilt."); }
    const rep = P.rep;
    rep.on("resize", (d) => fit(P, d.width, d.height));
    rep.on("finish", () => { P.playing = false; P.ended = true; updPlay(P); });
    rep.on("skip-start", () => P.el.skip.classList.add("on"));
    rep.on("skip-end", () => P.el.skip.classList.remove("on"));
    rep.on("event-cast", (e) => { if (e.type === 3 && (e.data.source === 1 || e.data.source === 2 || e.data.source === 6)) P.el.stage.classList.add("m"); });
    P.el.load.hidden = true;
    fit(P, P.a.w, P.a.h);
    P.el.frame.style.opacity = 1;
    P.seekTo(0, true);
    P.raf = requestAnimationFrame(() => tick(P));
  }

  function showErr(P, msg) {
    P.el.load.hidden = false;
    P.el.load.innerHTML = `<div class="rp-err"><b>Replay unavailable</b><span>${esc(msg)}</span></div>`;
    P.el.url.textContent = "–";
  }

  function fillInfo(P) {
    const r = P.info; if (!r) { P.el.kv.innerHTML = ""; return; }
    const pages = Array.isArray(r.pages) ? r.pages : [];
    const kv = [
      ["Started", when(r.started_at || r.created_at) + " " + CFG.tzLabel],
      ["Source", r.source || "Direct"],
      ["Country", (flag(r.country) ? flag(r.country) + " " : "") + country(r.country)],
      ["Device", [r.device, r.browser].filter(Boolean).join(" · ")],
      ["Landing", pathOf(r.landing || pages[0] || "/")],
      ["Pages", String(r.page_count || pages.length || 1)],
      ["Scrolled", r.scroll_max != null ? r.scroll_max + "%" : "–"],
      ["Active", r.active_s != null ? r.active_s + "s" : "–"],
      ["Outcome", r.clicked_whatsapp ? "WhatsApp" : r.clicked_email ? "Email" : r.opened_popup ? "Popup only" : "No click"],
    ];
    P.el.kv.innerHTML = kv.map(([k, v]) => `<dt>${esc(k)}</dt><dd title="${esc(v)}">${esc(v)}</dd>`).join("");
  }

  function fit(P, w, h) {
    P.vw = w; P.vh = h;
    const phone = w <= 820;
    const st = P.el.stage, pad = 32, bez = phone ? 20 : 2;
    const aw = Math.max(80, st.clientWidth - pad - bez), ah = Math.max(80, st.clientHeight - pad - bez);
    const s = Math.min(aw / w, ah / h, 1);
    P.scale = s;
    P.el.frame.classList.toggle("phone", phone);
    P.el.scaler.style.width = Math.round(w * s) + "px";
    P.el.scaler.style.height = Math.round(h * s) + "px";
    P.el.root.style.transform = `scale(${s})`;
    P.el.root.style.width = w + "px"; P.el.root.style.height = h + "px";
    const wr = P.el.root.querySelector(".replayer-wrapper");
    if (wr) { wr.style.width = w + "px"; wr.style.height = h + "px"; }
  }

  function buildBar(P) {
    const { a, el } = P;
    const pc = (t) => (t / a.total * 100).toFixed(3) + "%";
    el.track.insertAdjacentHTML("beforeend", a.gaps.map(([s, e]) => `<div class="rp-gap" style="left:${pc(s)};width:${pc(e - s)}"></div>`).join(""));
    const mk = a.marks.map((m) => `<div class="rp-mk ${m.k}" style="left:${pc(m.t)}"></div>`).join("");
    el.bar.insertAdjacentHTML("beforeend", `<div style="position:absolute;inset:0;pointer-events:none">${mk}</div>`);
    // the page marker for t=0 is always visible
  }

  function buildEvents(P) {
    const ms = P.a.marks;
    P.el.evs.innerHTML = ms.map((m, i) => `<button class="rp-ev ${m.k}" data-i="${i}"><time>${mmss1(m.t)}</time><i></i><span>${m.k === "page" ? "Page · " : ""}${esc(m.label)}</span></button>`).join("");
    P.el.evs.addEventListener("click", (e) => { const b = e.target.closest(".rp-ev"); if (b) P.seekTo(Math.max(0, ms[+b.dataset.i].t - 800)); });
  }

  const toast = (P, msg) => { P.el.toast.textContent = msg; P.el.toast.classList.add("on"); clearTimeout(P.tt); P.tt = setTimeout(() => P.el.toast.classList.remove("on"), 2200); };

  function updPlay(P) {
    P.el.play.innerHTML = P.ended ? IC.redo : P.playing ? IC.pause : IC.play;
    P.el.play.setAttribute("aria-label", P.playing ? "Pause" : "Play");
    P.el.big.classList.toggle("on", !P.playing && !P.scrub && !!P.rep);
  }

  function bindPlayer(P) {
    const { ov, el } = P;
    const total = () => (P.a ? P.a.total : 0);
    P.seekTo = (t, autoplay) => {
      if (!P.rep) return;
      t = Math.max(0, Math.min(total(), t));
      P.ended = false;
      if (autoplay || P.playing) { P.rep.play(t); P.playing = true; } else { P.rep.pause(t); }
      updPlay(P); paint(P, t);
    };
    P.toggle = () => {
      if (!P.rep) return;
      if (P.playing) { P.rep.pause(); P.playing = false; }
      else { const t = P.rep.getCurrentTime(); if (P.ended || t >= total() - 50) { P.ended = false; P.rep.play(0); } else P.rep.play(t); P.playing = true; }
      updPlay(P);
    };
    ov.addEventListener("click", (e) => {
      const b = e.target.closest("[data-a],[data-s]"); if (!b) return;
      if (b.dataset.s) { P.speed = +b.dataset.s; if (P.rep) P.rep.setConfig({ speed: P.speed }); ov.querySelectorAll("[data-s]").forEach((x) => x.setAttribute("aria-pressed", x === b)); return; }
      const a = b.dataset.a;
      if (a === "close") close();
      else if (a === "play") P.toggle();
      else if (a === "skip") { P.skip = !P.skip; b.setAttribute("aria-pressed", P.skip); if (P.rep) { P.rep.setConfig({ skipInactive: P.skip }); if (!P.skip) el.skip.classList.remove("on"); } }
      else if (a === "newer") step(-1);
      else if (a === "older") step(1);
      else if (a === "side") ov.classList.toggle("side");
      else if (a === "link") { const u = location.href.split("#")[0] + "#replay=" + P.sid; (navigator.clipboard ? navigator.clipboard.writeText(u) : Promise.reject()).then(() => toast(P, "Link copied"), () => toast(P, u)); }
      else if (a === "del") del(P);
    });
    // scrubber
    const bar = el.bar;
    const tAt = (ev) => { const r = bar.getBoundingClientRect(); return Math.max(0, Math.min(1, (ev.clientX - r.left) / r.width)) * total(); };
    let wasPlaying = false, lastSeek = 0;
    bar.addEventListener("pointerdown", (ev) => {
      if (!P.rep) return;
      bar.setPointerCapture(ev.pointerId); P.scrub = true; bar.classList.add("drag"); wasPlaying = P.playing;
      const t = tAt(ev); P.rep.pause(t); P.playing = false; P.dragT = t; paint(P, t); bar.focus({ preventScroll: true });
    });
    bar.addEventListener("pointermove", (ev) => {
      if (!P.a) return;
      const t = tAt(ev), r = bar.getBoundingClientRect();
      el.tip.style.left = Math.max(40, Math.min(r.width - 40, ev.clientX - r.left)) + "px";
      const near = P.a.marks.find((m) => Math.abs(m.t - t) / total() * r.width < 7 && m.k !== "click");
      el.tip.textContent = mmss1(t) + (near ? " · " + near.label : "");
      if (P.scrub) { P.dragT = t; paint(P, t); const n = performance.now(); if (n - lastSeek > 90) { lastSeek = n; P.rep.pause(t); } }
    });
    const up = (ev) => {
      if (!P.scrub) return; P.scrub = false; bar.classList.remove("drag");
      const t = tAt(ev); P.dragT = null; P.ended = false;
      if (wasPlaying) { P.rep.play(t); P.playing = true; } else P.rep.pause(t);
      updPlay(P); paint(P, t);
    };
    bar.addEventListener("pointerup", up); bar.addEventListener("pointercancel", up);
    // keyboard
    P.key = (e) => {
      if (!P.ov || e.target.closest && e.target.closest("select,input,textarea")) return;
      const k = e.key;
      if (k === "Escape") { e.preventDefault(); close(); }
      else if (k === " " || k === "k") { if (e.target.closest && e.target.closest("button") && k === " " && !e.target.classList.contains("rp-play") && !e.target.classList.contains("rp-big")) return; e.preventDefault(); P.toggle(); }
      else if (k === "ArrowLeft" || k === "ArrowRight") { e.preventDefault(); if (P.rep) P.seekTo(P.rep.getCurrentTime() + (k === "ArrowRight" ? 1 : -1) * (e.shiftKey ? 15000 : 5000)); }
      else if (k === "1" || k === "2" || k === "4") ov.querySelector(`[data-s="${k}"]`).click();
      else if (k === "s" || k === "S") ov.querySelector('[data-a="skip"]').click();
    };
    document.addEventListener("keydown", P.key);
    P.resize = () => { if (P.vw) fit(P, P.vw, P.vh); };
    addEventListener("resize", P.resize);
    if ("ResizeObserver" in window) { P.ro = new ResizeObserver(P.resize); P.ro.observe(el.stage); }
    // focus trap (dialog)
    P.trap = (e) => { if (e.key !== "Tab") return; const f = [...ov.querySelectorAll("button:not([disabled]),[tabindex='0']")].filter((x) => x.offsetParent); if (!f.length) return; const i = f.indexOf(document.activeElement); if (e.shiftKey && i <= 0) { e.preventDefault(); f[f.length - 1].focus(); } else if (!e.shiftKey && i === f.length - 1) { e.preventDefault(); f[0].focus(); } };
    ov.addEventListener("keydown", P.trap);
  }

  function paint(P, t) {
    if (!P.a) return;
    const total = P.a.total, p = Math.max(0, Math.min(1, t / total));
    P.el.fill.style.transform = `scaleX(${p})`;
    P.el.thumb.style.left = p * 100 + "%";
    const s = mmss1(t);
    if (P._s !== s) { P._s = s; P.el.tc.textContent = s; P.el.bar.setAttribute("aria-valuenow", Math.round(p * 100)); P.el.bar.setAttribute("aria-valuetext", s + " of " + mmss1(total)); }
    // current page + event
    const ms = P.a.marks; let pi = -1, ei = -1, pn = 0, pages = 0;
    for (let i = 0; i < ms.length && ms[i].t <= t + 20; i++) { ei = i; if (ms[i].k === "page") { pi = i; pn++; } }
    for (const m of ms) if (m.k === "page") pages++;
    if (pi !== P.cur) {
      const first = P.cur === -1; P.cur = pi;
      if (pi >= 0) { P.el.url.textContent = ms[pi].label; P.el.n.textContent = `Page ${pn} of ${pages}`; if (!first && P.playing) toast(P, "Navigated to " + ms[pi].label); }
    }
    if (ei !== P.curE) { P.curE = ei; P.el.evs.querySelectorAll(".cur").forEach((x) => x.classList.remove("cur")); const b = P.el.evs.querySelector(`[data-i="${ei}"]`); if (b) { b.classList.add("cur"); const c = P.el.evs; if (b.offsetTop < c.scrollTop || b.offsetTop + b.offsetHeight > c.scrollTop + c.clientHeight) c.scrollTop = b.offsetTop - c.clientHeight / 2; } }
  }

  function tick(P) {
    if (P.dead) return;
    if (P.rep && !P.scrub) {
      let t = P.rep.getCurrentTime();
      if (P.playing && t >= P.a.total - 30) { P.playing = false; P.ended = true; t = P.a.total; updPlay(P); P.rep.pause(P.a.total); }
      paint(P, Math.min(t, P.a.total));
    }
    P.raf = requestAnimationFrame(() => tick(P));
  }

  function step(d) {
    if (!player) return;
    const i = player.idx + d; if (i < 0 || i >= rows.length) return;
    cameFromList = true; location.hash = "replay=" + rows[i].sid;
  }

  async function del(P) {
    if (!confirm("Delete this replay permanently? Analytics data for the visit stays.")) return;
    try {
      const r = await api("?sid=" + encodeURIComponent(P.sid), { method: "DELETE" });
      if (!r.ok) throw 0;
      rows = rows.filter((x) => x.sid !== P.sid);
      const next = rows[Math.min(P.idx, rows.length - 1)];
      if (next && P.idx >= 0) { cameFromList = true; location.hash = "replay=" + next.sid; } else close();
      renderList();
    } catch { toast(P, "Could not delete"); }
  }

  function close() {
    if (cameFromList) { cameFromList = false; history.back(); }
    else { history.replaceState(null, "", location.pathname + location.search + "#replays"); closePlayer(); }
  }

  function closePlayer(quiet) {
    const P = player; if (!P) return;
    player = null; P.dead = true;
    cancelAnimationFrame(P.raf); clearTimeout(P.tt);
    document.removeEventListener("keydown", P.key); removeEventListener("resize", P.resize);
    try { P.ro && P.ro.disconnect(); } catch {}
    try { P.rep && P.rep.destroy && P.rep.destroy(); } catch {}
    P.ov.remove();
    if (!quiet) { document.documentElement.style.overflow = ""; if (root) renderList(); }
  }

  // ===================== public API =====================
  function mount(el, opts = {}) {
    Object.assign(CFG, opts);
    root = el; injectCss(); mountList();
    addEventListener("hashchange", sync);
    clearInterval(listTimer);
    listTimer = setInterval(() => { if (!document.hidden && root.offsetParent !== null && !player) refresh(); }, 30000);
    refresh(true).then(sync);
  }
  window.UbzReplays = { mount, refresh: () => refresh(true), open: go, close: () => player && close() };
})();
