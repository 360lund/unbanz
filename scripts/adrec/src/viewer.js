// Private viewer for ad-visitor recordings (/users/rec/). Token from #k=<token> or the prompt; kept in sessionStorage.
import { Replayer } from "@rrweb/replay";
import rrCss from "@rrweb/replay/dist/style.css";
(() => {
  const API = "/api/users/rec/", TZ = "Asia/Karachi";
  const $ = (s) => document.querySelector(s);
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const st = document.createElement("style"); st.textContent = rrCss; document.head.appendChild(st);
  let tok = ""; try { const m = location.hash.match(/k=([A-Za-z0-9_\-]+)/); if (m) { sessionStorage.setItem("adrec_k", m[1]); history.replaceState(null, "", location.pathname); } tok = sessionStorage.getItem("adrec_k") || ""; } catch {}
  try { localStorage.setItem("ubz_norec", "1"); } catch {}
  const when = (t) => new Date(t).toLocaleString("en-GB", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit", second: "2-digit", timeZone: TZ }) + " PKT";
  const dur = (ms) => { const s = Math.max(0, Math.round(ms / 1000)); return Math.floor(s / 60) + "m " + String(s % 60).padStart(2, "0") + "s"; };
  let regionName; try { regionName = new Intl.DisplayNames(["en"], { type: "region" }); } catch {}
  const ctry = (c) => (c && /^[A-Z]{2}$/.test(c) ? String.fromCodePoint(...[...c].map((x) => 127397 + x.charCodeAt(0))) + " " + ((regionName && regionName.of(c)) || c) : "Unknown");
  async function api(q, opt = {}) {
    const r = await fetch(API + q, { ...opt, headers: { "X-Rec-Token": tok, ...(opt.headers || {}) }, cache: "no-store" });
    if (r.status === 401 || r.status === 403) { gate("Wrong or missing key."); throw new Error("auth"); }
    if (!r.ok) throw new Error("HTTP " + r.status);
    return r;
  }
  function gate(msg) {
    $("#app").innerHTML = `<form id="g" class="card"><h2>Ad visitor replays</h2><p class="mut">${esc(msg || "Enter the viewer key.")}</p><input id="gk" type="password" autocomplete="off" placeholder="Viewer key"><button>Open</button></form>`;
    $("#g").onsubmit = (e) => { e.preventDefault(); tok = $("#gk").value.trim(); try { sessionStorage.setItem("adrec_k", tok); } catch {} list(); };
  }
  let showTest = false;
  async function list() {
    $("#app").innerHTML = `<p class="mut">Loading…</p>`;
    let d; try { d = await (await api("?list=1" + (showTest ? "&test=1" : ""))).json(); } catch (e) { if (e.message !== "auth") $("#app").innerHTML = `<p>Could not load: ${esc(e.message)}</p>`; return; }
    const rows = d.sessions.map((s) => `<tr data-sid="${esc(s.sid)}"><td>${esc(when(s.t0))}${s.test ? ' <span class="tag">test</span>' : ""}</td><td>${esc(ctry(s.country))}${s.city ? "<br><span class=mut>" + esc(s.city) + "</span>" : ""}</td><td>${esc(s.device || "")}<br><span class=mut>${esc([s.browser, s.os].filter(Boolean).join(" · "))}</span></td><td class="lp">${esc(s.landing || "")}<br><span class=mut>${esc(s.src || "")}</span></td><td>${esc(dur(s.t1 - s.t0))}</td><td>${s.cta ? '<span class="tag ok">Contact opened</span>' : '<span class="mut">—</span>'}</td><td><button class="play">Play</button> <button class="del" title="Delete">✕</button></td></tr>`).join("");
    $("#app").innerHTML = `<div class="bar"><h2>Ad visitor replays</h2><label><input type="checkbox" id="tt" ${showTest ? "checked" : ""}> show test sessions</label><button id="rf">Refresh</button></div>
      <p class="mut">${d.sessions.length} session(s) · Google Ads visitors only · inputs masked · kept 30 days</p>
      <div class="tw"><table><thead><tr><th>Start</th><th>Country</th><th>Device</th><th>Landing page / source</th><th>Length</th><th>Contact</th><th></th></tr></thead><tbody>${rows || '<tr><td colspan=7 class="mut">No recordings yet.</td></tr>'}</tbody></table></div><div id="pl"></div>`;
    $("#rf").onclick = list; $("#tt").onchange = (e) => { showTest = e.target.checked; list(); };
    document.querySelectorAll("tr[data-sid]").forEach((tr) => {
      tr.querySelector(".play").onclick = () => play(tr.dataset.sid, d.sessions.find((x) => x.sid === tr.dataset.sid));
      tr.querySelector(".del").onclick = async () => { if (!confirm("Delete this recording?")) return; await api("?sid=" + tr.dataset.sid, { method: "DELETE" }); list(); };
    });
  }
  let rp = null, raf = 0;
  async function play(sid, meta) {
    const pl = $("#pl"); pl.innerHTML = `<p class="mut">Loading recording…</p>`; pl.scrollIntoView({ behavior: "smooth" });
    let evs; try { evs = await (await api("?sid=" + encodeURIComponent(sid))).json(); } catch (e) { pl.innerHTML = `<p>Could not load: ${esc(e.message)}</p>`; return; }
    if (!evs.length || !evs.some((e) => e.type === 2)) { pl.innerHTML = `<p class="mut">This session has no full snapshot yet (visitor left within a second).</p>`; return; }
    evs.sort((a, b) => a.timestamp - b.timestamp);
    const t0 = evs[0].timestamp;
    const pages = evs.filter((e) => e.type === 4 && e.data && e.data.href).map((e) => ({ t: e.timestamp - t0, h: (() => { try { const u = new URL(e.data.href); return u.pathname + u.search; } catch { return e.data.href; } })() }));
    const marks = evs.filter((e) => e.type === 5 && /^(lead_|tap_)/.test(e.data.tag)).map((e) => ({ t: e.timestamp - t0, k: e.data.tag }));
    const L = { lead_email: "Opened email app (lead_email)", lead_whatsapp: "Opened WhatsApp (lead_whatsapp)", tap_email: "Tapped an email button (picker opened)", tap_whatsapp: "Tapped WhatsApp button (picker opened)" };
    pl.innerHTML = `<div class="card"><div class="bar"><b>${esc(meta ? when(meta.t0) : sid)}</b><span class="mut">${esc(meta ? ctry(meta.country) + " · " + (meta.device || "") + " " + (meta.browser || "") : "")}</span><button id="cl">Close</button></div>
      <div class="cols"><div><div id="stage"></div><div class="ctl"><button id="pp">Pause</button><input id="sk" type="range" min="0" value="0" step="100"><span id="tm" class="mut"></span><select id="sp"><option value="1">1×</option><option value="2">2×</option><option value="4">4×</option><option value="8">8×</option></select></div></div>
      <div class="side"><h3>Pages</h3><ol>${pages.map((p) => `<li><a href="#" data-t="${p.t}">${esc(dur(p.t))}</a> ${esc(p.h)}</li>`).join("")}</ol><h3>Contact events</h3>${marks.length ? "<ul>" + marks.map((m) => `<li><a href="#" data-t="${m.t}">${esc(dur(m.t))}</a> ${esc(L[m.k] || m.k)}</li>`).join("") + "</ul>" : '<p class="mut">None</p>'}</div></div></div>`;
    if (rp) { try { rp.pause(); rp.destroy && rp.destroy(); } catch {} } cancelAnimationFrame(raf);
    rp = new Replayer(evs, { root: $("#stage"), skipInactive: true, showWarning: false, mouseTail: { strokeStyle: "#e5484d" }, UNSAFE_replayCanvas: false });
    const total = rp.getMetaData().totalTime; const sk = $("#sk"); sk.max = total;
    const fit = () => { const w = $("#stage").clientWidth, ifr = $("#stage iframe"); if (!ifr) return; const fw = +ifr.width || 1280, fh = +ifr.height || 800, s = Math.min(1, w / fw); const wr = $("#stage .replayer-wrapper"); if (wr) { wr.style.transform = `scale(${s})`; wr.style.transformOrigin = "0 0"; } $("#stage").style.height = Math.min(fh * s, innerHeight * 0.8) + "px"; };
    rp.on("resize", fit); setTimeout(fit, 50); addEventListener("resize", fit);
    let playing = true; rp.play(0);
    const tick = () => { const t = rp.getCurrentTime(); sk.value = t; $("#tm").textContent = dur(t) + " / " + dur(total); raf = requestAnimationFrame(tick); }; tick();
    $("#pp").onclick = () => { if (playing) { rp.pause(); $("#pp").textContent = "Play"; } else { rp.play(rp.getCurrentTime()); $("#pp").textContent = "Pause"; } playing = !playing; };
    sk.oninput = () => { const t = +sk.value; playing ? rp.play(t) : rp.pause(t); };
    $("#sp").onchange = (e) => rp.setConfig({ speed: +e.target.value });
    pl.querySelectorAll("a[data-t]").forEach((a) => (a.onclick = (e) => { e.preventDefault(); const t = Math.max(0, +a.dataset.t - 500); playing = true; $("#pp").textContent = "Pause"; rp.play(t); }));
    $("#cl").onclick = () => { try { rp.pause(); } catch {} cancelAnimationFrame(raf); pl.innerHTML = ""; };
  }
  tok ? list() : gate();
})();
