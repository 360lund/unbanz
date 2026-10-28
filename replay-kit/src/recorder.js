// Session recorder (public pages only). Built into assets/rec.<hash>.js together with a slimmed rrweb record.
// Loaded with `defer`; it does nothing until the page `load` event + an idle moment, so it never competes with
// first paint, the tracker, the sticky bar or the popup.
import { record } from "@rrweb/record";

(() => {
  "use strict";
  const CFG = window.UBZ_REPLAY || {};
  const EP = CFG.endpoint || "/api/users/rp/";          // ingest route
  const SESSION_KEY = CFG.sessionKey || "ubz1";           // sessionStorage key where the tracker keeps {id, ...}
  const MAX_MS = CFG.maxMs || 10 * 60 * 1000;             // per-session recording cap
  const MAX_BYTES = CFG.maxBytes || 1_500_000;            // per-session cap on bytes sent (compressed)
  const FLUSH_MS = CFG.flushMs || 6000;
  const FIRST_FLUSH_MS = 1500;                            // send the first snapshot quickly (bounces still get something)
  const BEACON_MAX = 60_000;                              // sendBeacon / keepalive hard limit is 64KB
  const BOT = /bot|crawl|spider|slurp|preview|headless|lighthouse/i;

  const ls = (k, v) => { try { return v === undefined ? localStorage.getItem(k) : (v === null ? localStorage.removeItem(k) : localStorage.setItem(k, v)); } catch { return null; } };
  const ss = (k, v) => { try { return v === undefined ? sessionStorage.getItem(k) : sessionStorage.setItem(k, v); } catch { return null; } };

  // ---- who is never recorded ----
  if (/^\/(users|api)(\/|$)/.test(location.pathname)) return;                        // the dashboard itself
  try { const q = new URLSearchParams(location.search).get("norec"); if (q === "1") ls("ubz_norec", "1"); else if (q === "0") ls("ubz_norec", null); } catch {}
  if (ls("ubz_norec") === "1") return;                                                // owner browser (set by /users or ?norec=1)
  const dev = ls("ubz_rec_test") === "1";                                             // developer override for tests only
  const test = ls("ubz_test") === "1";                                                // same flag the tracker uses (x:1)
  if (test && !dev) return;
  if (!dev && (BOT.test(navigator.userAgent || "") || navigator.webdriver)) return;   // bots / automation

  let st = null;
  try { st = JSON.parse(ss(SESSION_KEY) || "null"); } catch {}
  const sid = st && st.id;
  if (!sid || !/^[a-z0-9]{8,40}$/i.test(sid)) return;                                // no tracker session -> nothing to link to

  let rs = {};
  try { rs = JSON.parse(ss("ubzr") || "{}") || {}; } catch {}
  if (rs.done) return;
  const now0 = Date.now();
  if (!rs.t0) rs.t0 = now0;
  if (!rs.b) rs.b = 0;
  const save = () => ss("ubzr", JSON.stringify(rs));
  if (now0 - rs.t0 > MAX_MS || rs.b > MAX_BYTES) { rs.done = 1; save(); return; }

  const pg = Math.random().toString(36).slice(2, 8).padEnd(4, "0");   // one id per page load (chunk key = sid + pg + idx)
  let idx = 0, buf = [], timer = 0, stopFn = null, dead = false, chain = Promise.resolve();

  const stop = (finish) => {
    if (dead) return;
    dead = true; clearTimeout(timer);
    try { stopFn && stopFn(); } catch {}
    if (finish) { rs.done = 1; save(); }
  };

  const gzip = async (str) => {
    const s = new Blob([str]).stream().pipeThrough(new CompressionStream("gzip"));
    return new Uint8Array(await new Response(s).arrayBuffer());
  };

  // POST one chunk. Resolves true when stored (or harmlessly dropped), false when the page should stop recording.
  async function post(events) {
    const json = JSON.stringify(events);
    let body = json, z = 0;
    if (window.CompressionStream) { try { body = await gzip(json); z = 1; } catch { body = json; z = 0; } }
    const size = z ? body.length : json.length;
    if (size > 390_000) return true;                                   // absurdly large chunk: drop it, keep going
    const url = `${EP}?s=${sid}&g=${pg}&i=${idx++}&z=${z}&x=${test ? 1 : 0}&a=${events[0].timestamp}&b=${events[events.length - 1].timestamp}&n=${events.length}`;
    for (let attempt = 0; attempt < 3; attempt++) {
      try {
        const r = await fetch(url, { method: "POST", body, keepalive: size < BEACON_MAX, headers: { "Content-Type": "application/octet-stream" }, credentials: "same-origin" });
        if (r.ok) { rs.b += size; save(); if (rs.b > MAX_BYTES) { stop(true); } return true; }
        if (r.status === 404 || r.status >= 500) { await new Promise((ok) => setTimeout(ok, 2500)); continue; }   // visit row not there yet / transient
        return false;                                                   // 4xx: limits or refusal -> stop quietly
      } catch { await new Promise((ok) => setTimeout(ok, 2500)); }
    }
    return true;
  }

  function flush() {
    clearTimeout(timer); timer = 0;
    if (!buf.length) { if (!dead) timer = setTimeout(flush, FLUSH_MS); return; }
    const evs = buf; buf = [];
    chain = chain.then(() => post(evs)).then((ok) => { if (!ok) stop(true); }).catch(() => {});
    if (!dead) timer = setTimeout(flush, FLUSH_MS);
  }

  // Last chance when the page is hidden / unloaded: plain JSON through sendBeacon (can't await compression there).
  function flushFinal() {
    if (!buf.length) return;
    const evs = buf; buf = [];
    try {
      const json = JSON.stringify(evs);
      if (json.length > BEACON_MAX) return;
      const url = `${EP}?s=${sid}&g=${pg}&i=${idx++}&z=0&x=${test ? 1 : 0}&a=${evs[0].timestamp}&b=${evs[evs.length - 1].timestamp}&n=${evs.length}`;
      navigator.sendBeacon(url, new Blob([json], { type: "application/octet-stream" }));
    } catch {}
  }

  function begin() {
    if (dead) return;
    try {
      stopFn = record({
        emit(e) {
          if (dead) return;
          if (Date.now() - rs.t0 > MAX_MS) { flush(); stop(true); return; }
          buf.push(e);
          if (buf.length > 4000) flush();                               // runaway DOM churn guard
        },
        // privacy: every form control value is masked ("*"), passwords can never be captured, password fields are blocked entirely
        maskAllInputs: true,
        maskInputOptions: { password: true },
        blockSelector: "input[type=password], [data-rr-block], .rr-block",
        maskTextClass: "rr-mask",
        ignoreClass: "rr-ignore",
        slimDOMOptions: "all",
        inlineStylesheet: true,                                          // replay is exact even if CSS files change later
        inlineImages: false,
        collectFonts: false,
        recordCanvas: false,
        recordCrossOriginIframes: false,
        sampling: { mousemove: 60, mouseInteraction: true, scroll: 120, media: 800, input: "last" },
      });
    } catch { dead = true; return; }
    timer = setTimeout(flush, FIRST_FLUSH_MS);

    // Markers for the player: the same click classification the tracker uses (WhatsApp / popup / email).
    document.addEventListener("click", (e) => {
      try {
        const a = e.target && e.target.closest && e.target.closest('a[href^="https://wa.me/"], a[href^="mailto:"]');
        if (!a || dead) return;
        const dlg = a.closest(".cm-dialog");
        const wa = a.href.startsWith("https://wa.me/");
        const k = wa ? (dlg || a.hasAttribute("data-direct") || e.metaKey || e.ctrlKey || e.shiftKey ? "whatsapp" : "popup") : "email";
        record.addCustomEvent("cta", { k });
      } catch {}
    }, true);
    const nav = () => { try { if (!dead) record.addCustomEvent("nav", { h: location.pathname + location.search + location.hash }); } catch {} };
    addEventListener("hashchange", nav); addEventListener("popstate", nav);
    document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flushFinal(); });
    addEventListener("pagehide", flushFinal);
  }

  const go = () => { if ("requestIdleCallback" in window) requestIdleCallback(begin, { timeout: 2500 }); else setTimeout(begin, 300); };
  if (document.readyState === "complete") setTimeout(go, 200); else addEventListener("load", () => setTimeout(go, 200), { once: true });
})();
