// Ads-tab Recordings panel for /users (loaded lazily by the dashboard when the Ads tab opens).
//   UbzAdRec.mount(el, { headers, onAuthFail })  -> renders list + player; returns Promise<sessions>
//   UbzAdRec.open(sid)  plays a recording      UbzAdRec.byVisit -> Map(visitId -> sid) for linking Ads rows
import { Replayer } from "@rrweb/replay";
import rrCss from "@rrweb/replay/dist/style.css";
(() => {
  const API = "/api/users/rec/", TZ = "Asia/Karachi";
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const CSS = `.arx table{border-collapse:collapse;width:100%}.arx th,.arx td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--b,#e3ebf2);vertical-align:top;font-size:13px}.arx th{font-size:12px;opacity:.7;font-weight:600}.arx .lp{max-width:300px;word-break:break-all}.arx .m{opacity:.65;font-size:12px}.arx .tg{display:inline-block;font-size:11px;padding:2px 8px;border-radius:99px;background:rgba(127,127,127,.14)}.arx .tg.ok{background:#e3f7ea;color:#157a3c}.arx button{font:inherit;font-size:12.5px;border:1px solid var(--b,#dfe7ee);background:transparent;color:inherit;border-radius:8px;padding:4px 10px;cursor:pointer}.arx button.pl{background:#2f7de1;color:#fff;border-color:#2f7de1}.arx button.dl{color:#c0392b}.arx .tb{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:8px}.arx .tb label{font-size:12.5px}.arx .pv{margin-top:14px}.arx .cols{display:grid;grid-template-columns:1fr 260px;gap:14px}.arx .stage{position:relative;overflow:hidden;background:#e9eef3;border-radius:10px}.arx .stage .replayer-wrapper{position:absolute;top:0;left:0}.arx .ctl{display:flex;gap:10px;align-items:center;margin-top:8px}.arx .ctl input{flex:1}.arx .side ol,.arx .side ul{padding-left:18px;margin:0}.arx .side li{margin:4px 0;word-break:break-all;font-size:12.5px}.arx .side h4{margin:10px 0 4px;font-size:12px;text-transform:uppercase;letter-spacing:.06em;opacity:.7}.arx .ph{display:flex;gap:12px;align-items:center;flex-wrap:wrap}.arx .ph button{margin-left:auto}@media(max-width:900px){.arx .cols{grid-template-columns:1fr}}`;
  let cfg = { headers: () => ({}), onAuthFail: () => {} }, root, sessions = [], showTest = false, rp = null, raf = 0;
  const byVisit = new Map();
  const when = (t) => new Date(t).toLocaleString("en-GB", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit", timeZone: TZ });
  const dur = (ms) => { const s = Math.max(0, Math.round(ms / 1000)); return Math.floor(s / 60) + "m " + String(s % 60).padStart(2, "0") + "s"; };
  let rn; try { rn = new Intl.DisplayNames(["en"], { type: "region" }); } catch {}
  const ctry = (c) => (c && /^[A-Z]{2}$/.test(c) ? String.fromCodePoint(...[...c].map((x) => 127397 + x.charCodeAt(0))) + " " + ((rn && rn.of(c)) || c) : "Unknown");
  async function api(q, opt = {}) {
    const r = await fetch(API + q, { credentials: "same-origin", cache: "no-store", ...opt, headers: { ...(cfg.headers() || {}), ...(opt.headers || {}) } });
    if (r.status === 401) { cfg.onAuthFail(); throw new Error("auth"); }
    if (!r.ok) throw new Error("HTTP " + r.status);
    return r;
  }
  async function refresh() {
    if (!root) return [];
    try { sessions = (await (await api("?list=1" + (showTest ? "&test=1" : ""))).json()).sessions; } catch (e) { root.querySelector(".ls").innerHTML = `<p class="m">Could not load recordings (${esc(e.message)})</p>`; return []; }
    byVisit.clear(); sessions.forEach((s) => { if (s.visit) byVisit.set(s.visit, s.sid); });
    const rows = sessions.map((s) => `<tr data-sid="${esc(s.sid)}"><td>${esc(when(s.t0))}${s.test ? ' <span class="tg">test</span>' : ""}</td><td>${esc(ctry(s.country))}${s.city ? `<div class="m">${esc(s.city)}</div>` : ""}</td><td>${esc(s.device)}<div class="m">${esc([s.browser, s.os].filter(Boolean).join(" · "))}</div></td><td class="lp">${esc(s.landing)}<div class="m">${esc(s.src)}</div></td><td class="num">${esc(dur(s.t1 - s.t0))}</td><td>${s.cta ? '<span class="tg ok">Contact opened</span>' : '<span class="m">—</span>'}</td><td style="white-space:nowrap"><button class="pl">Watch</button> <button class="dl" title="Delete recording">✕</button></td></tr>`).join("");
    root.querySelector(".ls").innerHTML = `<div class="scroll"><table><tr><th>Start (PKT)</th><th>Country</th><th>Device</th><th>Landing / ad params</th><th>Length</th><th>Contact</th><th></th></tr>${rows || '<tr><td colspan="7" class="m">No recordings yet. Every Google Ads visit (gclid / gad_source / utm google cpc) is recorded from now on.</td></tr>'}</table></div>`;
    root.querySelectorAll("tr[data-sid]").forEach((tr) => {
      tr.querySelector(".pl").onclick = () => open(tr.dataset.sid);
      tr.querySelector(".dl").onclick = async () => { if (!confirm("Delete this recording?")) return; try { await api("?sid=" + tr.dataset.sid, { method: "DELETE" }); } catch {} refresh(); };
    });
    return sessions;
  }
  function mount(el, o) {
    cfg = { ...cfg, ...(o || {}) }; root = el;
    if (!document.getElementById("arx-css")) { const st = document.createElement("style"); st.id = "arx-css"; st.textContent = rrCss + CSS; document.head.appendChild(st); }
    el.classList.add("arx");
    el.innerHTML = `<div class="tb"><label><input type="checkbox" class="tt"> show test sessions</label><span class="m">Inputs masked · kept 30 days</span><button class="rf" style="margin-left:auto">Refresh</button></div><div class="ls"><p class="m">Loading…</p></div><div class="pv"></div>`;
    el.querySelector(".rf").onclick = refresh; el.querySelector(".tt").onchange = (e) => { showTest = e.target.checked; refresh(); };
    return refresh();
  }
  async function open(sid) {
    const meta = sessions.find((x) => x.sid === sid), pl = root.querySelector(".pv");
    pl.innerHTML = `<p class="m">Loading recording…</p>`; pl.scrollIntoView({ behavior: "smooth", block: "start" });
    let evs; try { evs = await (await api("?sid=" + encodeURIComponent(sid))).json(); } catch (e) { pl.innerHTML = `<p class="m">Could not load (${esc(e.message)})</p>`; return; }
    if (!evs.length || !evs.some((e) => e.type === 2)) { pl.innerHTML = `<p class="m">No full snapshot in this session (visitor left within a second).</p>`; return; }
    evs.sort((a, b) => a.timestamp - b.timestamp);
    const t0 = evs[0].timestamp;
    const pages = evs.filter((e) => e.type === 4 && e.data && e.data.href).map((e) => ({ t: e.timestamp - t0, h: (() => { try { const u = new URL(e.data.href); return u.pathname + u.search; } catch { return e.data.href; } })() }));
    const L = { lead_email: "Opened email app (lead_email)", lead_whatsapp: "Opened WhatsApp (lead_whatsapp)", tap_email: "Tapped email button (picker opened)", tap_whatsapp: "Tapped WhatsApp button (picker opened)" };
    const marks = evs.filter((e) => e.type === 5 && L[e.data.tag]).map((e) => ({ t: e.timestamp - t0, k: e.data.tag }));
    pl.innerHTML = `<div class="ph"><b>${esc(meta ? when(meta.t0) + " PKT" : sid)}</b><span class="m">${esc(meta ? ctry(meta.country) + " · " + meta.device + " " + meta.browser : "")}</span><button class="cl">Close</button></div>
      <div class="cols"><div><div class="stage"></div><div class="ctl"><button class="pp">Pause</button><input class="sk" type="range" min="0" value="0" step="100"><span class="tm m"></span><select class="sp"><option value="1">1×</option><option value="2">2×</option><option value="4">4×</option><option value="8">8×</option></select></div></div>
      <div class="side"><h4>Pages</h4><ol>${pages.map((p) => `<li><a href="#" data-t="${p.t}">${esc(dur(p.t))}</a> ${esc(p.h)}</li>`).join("")}</ol><h4>Contact</h4>${marks.length ? "<ul>" + marks.map((m) => `<li><a href="#" data-t="${m.t}">${esc(dur(m.t))}</a> ${esc(L[m.k])}</li>`).join("") + "</ul>" : '<p class="m">No contact taps</p>'}</div></div>`;
    if (rp) { try { rp.pause(); rp.destroy && rp.destroy(); } catch {} } cancelAnimationFrame(raf);
    const stage = pl.querySelector(".stage");
    rp = new Replayer(evs, { root: stage, skipInactive: true, showWarning: false, mouseTail: { strokeStyle: "#e5484d" } });
    const total = rp.getMetaData().totalTime, sk = pl.querySelector(".sk"); sk.max = total;
    const fit = () => { const ifr = stage.querySelector("iframe"); if (!ifr) return; const fw = +ifr.width || 1280, fh = +ifr.height || 800, s = Math.min(1, stage.clientWidth / fw); const wr = stage.querySelector(".replayer-wrapper"); if (wr) { wr.style.transform = `scale(${s})`; wr.style.transformOrigin = "0 0"; } stage.style.height = Math.min(fh * s, innerHeight * 0.8) + "px"; };
    rp.on("resize", fit); setTimeout(fit, 50); addEventListener("resize", fit);
    let playing = true; rp.play(0);
    const tick = () => { if (!sk.isConnected) return; const t = rp.getCurrentTime(); sk.value = t; pl.querySelector(".tm").textContent = dur(t) + " / " + dur(total); raf = requestAnimationFrame(tick); }; tick();
    pl.querySelector(".pp").onclick = (e) => { if (playing) { rp.pause(); e.target.textContent = "Play"; } else { rp.play(rp.getCurrentTime()); e.target.textContent = "Pause"; } playing = !playing; };
    sk.oninput = () => { const t = +sk.value; playing ? rp.play(t) : rp.pause(t); };
    pl.querySelector(".sp").onchange = (e) => rp.setConfig({ speed: +e.target.value });
    pl.querySelectorAll("a[data-t]").forEach((a) => (a.onclick = (e) => { e.preventDefault(); playing = true; pl.querySelector(".pp").textContent = "Pause"; rp.play(Math.max(0, +a.dataset.t - 500)); }));
    pl.querySelector(".cl").onclick = () => { try { rp.pause(); } catch {} cancelAnimationFrame(raf); pl.innerHTML = ""; };
  }
  window.UbzAdRec = { mount, refresh, open, byVisit };
})();
