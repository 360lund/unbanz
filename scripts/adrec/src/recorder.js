// Nov 20 2026: session recorder for GOOGLE ADS visitors only. Loaded by the inline #ubz-adrec loader, which
// injects this file only when the visit came from an ad (gclid/gbraid/wbraid/gad_source or utm_source=google +
// paid utm_medium) and remembers that in sessionStorage "ubzad" for the rest of the visit. Everyone else never
// downloads it. Recordings go to /api/rec/ (private Vercel Blob store), viewed at /users/rec/.
import { record } from "@rrweb/record";
(() => {
  "use strict";
  const EP = "/api/rec/", MAX_MS = 15 * 60 * 1000, MAX_BYTES = 2_000_000, FLUSH_MS = 5000, BEACON_MAX = 60_000;
  const BOT = /bot|crawl|spider|slurp|preview|headless|lighthouse|mediapartners|adsbot/i;
  const ss = (k, v) => { try { return v === undefined ? sessionStorage.getItem(k) : sessionStorage.setItem(k, v); } catch { return null; } };
  if (/^\/(users|api)(\/|$)/.test(location.pathname)) return;
  let ls = null; try { ls = localStorage; } catch {}
  const dev = ls && ls.getItem("ubz_rec_test") === "1";
  if (!dev && (BOT.test(navigator.userAgent || "") || navigator.webdriver)) return;
  let st; try { st = JSON.parse(ss("ubzad") || "null"); } catch {}
  if (!st) return;
  if (!st.sid) { st.sid = Array.from(crypto.getRandomValues(new Uint8Array(12)), (b) => b.toString(36).padStart(2, "0")).join("").slice(0, 20); st.b = 0; st.t0 = Date.now(); }
  const save = () => ss("ubzad", JSON.stringify(st));
  save();
  if (st.done || Date.now() - st.t0 > MAX_MS || st.b > MAX_BYTES) return;
  const first = !st.m; // first page of the visit -> server writes meta.json
  const test = /(^|[?&])gclid=test(&|$)/.test(st.l || "") || (ls && ls.getItem("ubz_test") === "1") ? 1 : 0;
  const pg = Math.random().toString(36).slice(2, 8).padEnd(6, "0");
  let idx = 0, buf = [], timer = 0, stopFn = null, dead = false, chain = Promise.resolve(), cta = 0;
  const stop = (fin) => { if (dead) return; dead = true; clearTimeout(timer); try { stopFn && stopFn(); } catch {} if (fin) { st.done = 1; save(); } };
  const gzip = async (s) => new Uint8Array(await new Response(new Blob([s]).stream().pipeThrough(new CompressionStream("gzip"))).arrayBuffer());
  const qs = (evs, z) => {
    let u = `${EP}?s=${st.sid}&g=${pg}&i=${idx++}&z=${z}&x=${test}&a=${evs[0].timestamp}&b=${evs[evs.length - 1].timestamp}&c=${cta}`;
    if (first && idx === 1) { u += "&f=1&l=" + encodeURIComponent((st.l || location.pathname).slice(0, 400)) + "&r=" + encodeURIComponent((st.r || "").slice(0, 200)); st.m = 1; save(); }
    return u;
  };
  // privacy: pre-filled mailto / WhatsApp links carry what the visitor typed (username, note) -> strip their query
  const scrub = (j) => j.replace(/(mailto:[^"\\?]*)\?[^"\\]*/gi, "$1").replace(/(https:\/\/(?:wa\.me|api\.whatsapp\.com)\/)[^"\\]*/gi, "$1");
  async function post(evs) {
    const json = scrub(JSON.stringify(evs)); let body = json, z = 0;
    if (window.CompressionStream) { try { body = await gzip(json); z = 1; } catch { body = json; z = 0; } }
    const size = z ? body.length : json.length;
    if (size > 390_000) return true;
    const url = qs(evs, z);
    for (let t = 0; t < 3; t++) {
      try {
        const r = await fetch(url, { method: "POST", body, keepalive: size < BEACON_MAX, headers: { "Content-Type": "application/octet-stream" } });
        if (r.ok) { st.b += size; save(); if (st.b > MAX_BYTES) stop(true); return true; }
        if (r.status >= 500) { await new Promise((ok) => setTimeout(ok, 2500)); continue; }
        return false;
      } catch { await new Promise((ok) => setTimeout(ok, 2500)); }
    }
    return true;
  }
  function flush() {
    clearTimeout(timer); timer = 0;
    if (buf.length) { const evs = buf; buf = []; chain = chain.then(() => post(evs)).then((ok) => { if (!ok) stop(true); }).catch(() => {}); }
    if (!dead) timer = setTimeout(flush, FLUSH_MS);
  }
  function flushFinal() {
    if (!buf.length) return; const evs = buf; buf = [];
    try { const json = scrub(JSON.stringify(evs)); if (json.length > BEACON_MAX) return; navigator.sendBeacon(qs(evs, 0), new Blob([json], { type: "application/octet-stream" })); } catch {}
  }
  function begin() {
    if (dead) return;
    try {
      stopFn = record({
        emit(e) { if (dead) return; if (Date.now() - st.t0 > MAX_MS) { flush(); stop(true); return; } buf.push(e); if (buf.length > 4000) flush(); },
        maskAllInputs: true, maskInputOptions: { password: true }, blockSelector: "input[type=password], [data-rr-block], .rr-block",
        maskTextClass: "rr-mask", ignoreClass: "rr-ignore", slimDOMOptions: "all", inlineStylesheet: true, inlineImages: false,
        collectFonts: false, recordCanvas: false, recordCrossOriginIframes: false,
        sampling: { mousemove: 60, mouseInteraction: true, scroll: 120, media: 800, input: "last" },
      });
    } catch { dead = true; return; }
    timer = setTimeout(flush, 1200);
    const mark = (k, d) => { try { if (!dead) record.addCustomEvent(k, d || {}); } catch {} };
    // contact markers: picker opened, email app opened, WhatsApp opened (same moments as GTM lead_email / lead_whatsapp)
    document.addEventListener("click", (e) => {
      const t = e.target && e.target.closest && e.target.closest("a,button"); if (!t) return;
      const h = t.getAttribute("href") || "";
      if (t.matches("a.mp-go, a.ob-go")) { cta = 1; mark(t.classList.contains("ob-wa") || h.startsWith("https://wa.me/") ? "lead_whatsapp" : "lead_email"); }
      else if (t.matches('a[data-wa="1"], .wa-direct')) mark("tap_whatsapp");
      else if (/^mailto:/i.test(h)) mark("tap_email");
    }, true);
    const nav = () => mark("nav", { h: location.pathname + location.search + location.hash });
    addEventListener("hashchange", nav); addEventListener("popstate", nav);
    document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flushFinal(); });
    addEventListener("pagehide", flushFinal);
  }
  const go = () => ("requestIdleCallback" in window ? requestIdleCallback(begin, { timeout: 2000 }) : setTimeout(begin, 300));
  if (document.readyState === "complete") setTimeout(go, 100); else addEventListener("load", () => setTimeout(go, 100), { once: true });
})();
