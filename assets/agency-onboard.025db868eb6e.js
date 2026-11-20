/* Nov 20 2026: agency onboarding picker on /white-label-agency/. 4 steps (no pricing step: agency prices are never shown, Nov 20 rule); the last step hands off by the 3-tier rule:
   /api/geo/ returns whatsapp only for US/CA/GB/NL/AE IP + time zone (both), email for everyone else (email only),
   and nothing for IN/PK/IR IP or time zone (no contact at all, html[data-noc]). No address or number is in the HTML. */
(function () {
  var card = document.getElementById("ob");
  if (!card) return;
  var root = document.documentElement;
  card.classList.add("ob-js");
  var steps = [].slice.call(card.querySelectorAll(".ob-step"));
  var bar = card.querySelector(".ob-bar i"), cnt = card.querySelector(".ob-count");
  var ans = {}, cur = 0, geo = null, geoP = null;
  // Localized pages pass their strings in data-i18n (JSON); English defaults.
  var S = { step: "Step {n} of {t}", wait: "One moment…", thanks: "Thanks for your answers.", na: "Direct agency onboarding is currently unavailable in your region.",
    wa: "Send on WhatsApp", em: "Send by email", fineWa: "Your answers are pre-filled. We reply within one business day.", fineEm: "Your answers are pre-filled in the email. We reply within one business day.",
    intro: "Hi Unbanz, I'd like to onboard as a white-label agency partner.", lType: "Agency type", lName: "Agency name", lVol: "Client cases per month", lSvc: "Services needed",
    lPrice: "Pricing", lWeb: "Website", lReach: "Best way to reach me", subj: "Agency onboarding" };
  try { var X = JSON.parse(card.getAttribute("data-i18n") || "{}"); for (var k in X) S[k] = X[k]; } catch (e) {}
  function tz() { try { return Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch (e) { return ""; } }
  function getGeo() {
    if (geoP) return geoP;
    if (root.hasAttribute("data-noc")) return (geoP = Promise.resolve({ contactAllowed: false }));
    geoP = fetch("/api/geo/?tz=" + encodeURIComponent(tz()), { credentials: "same-origin", cache: "no-store" })
      .then(function (r) { return r.json(); }).catch(function () { return { contactAllowed: true, email: null }; })
      .then(function (g) { geo = g; if (g && g.contactAllowed === false && window.__ubzNoc) window.__ubzNoc(); return g; });
    return geoP;
  }
  function go(i) {
    cur = Math.max(0, Math.min(steps.length - 1, i));
    steps.forEach(function (s, k) { s.classList.toggle("on", k === cur); s.setAttribute("aria-hidden", k === cur ? "false" : "true"); });
    if (bar) bar.style.width = ((cur + 1) / steps.length * 100) + "%";
    if (cnt) cnt.textContent = S.step.replace("{n}", cur + 1).replace("{t}", steps.length);
    if (cur === steps.length - 1) finish();
    var h = steps[cur].querySelector(".ob-q"); if (h && go.moved) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
    go.moved = true;
  }
  function msg() {
    var name = (card.querySelector("#ob-name") || {}).value || "";
    return S.intro + "\n\n" + S.lType + ": " + (ans.type || "") + "\n" + S.lName + ": " + name.trim() + "\n" +
      S.lVol + ": " + (ans.volume || "") + "\n" + S.lSvc + ": " + (ans.service || "") + "\n" +
      (ans.pricing ? S.lPrice + ": " + ans.pricing + "\n" : "") + "\n" + S.lWeb + ": \n" + S.lReach + ": ";
  }
  function finish() {
    var out = card.querySelector(".ob-out"); if (!out) return;
    var sum = card.querySelector(".ob-sum");
    if (sum) sum.innerHTML = ["type", "volume", "service", "pricing"].map(function (k) { return ans[k] ? "<li>" + ans[k].replace(/[<>&]/g, "") + "</li>" : ""; }).join("");
    out.innerHTML = ""; var w = document.createElement("p"); w.className = "ob-wait"; w.textContent = S.wait; out.appendChild(w);
    getGeo().then(function (g) {
      out.innerHTML = "";
      if (!g || g.contactAllowed === false || root.hasAttribute("data-noc")) {
        var q = steps[cur].querySelector(".ob-q"); if (q) q.textContent = S.thanks;
        var na = document.createElement("p"); na.className = "ob-na"; na.textContent = S.na; out.appendChild(na); return;
      }
      var m = msg(), subj = S.subj + ": " + (ans.type || "agency") + ", " + (ans.volume || "");
      var wa = g.whatsapp && !navigator.webdriver ? String(g.whatsapp).replace(/\D/g, "") : "";
      var em = g.email && /^[^@\s]+@[^@\s]+$/.test(g.email) ? g.email : "";
      if (wa) out.appendChild(btn("ob-wa", "https://wa.me/" + wa + "?text=" + encodeURIComponent(m), S.wa, true));
      if (em) out.appendChild(btn(wa ? "ob-em ob-alt" : "ob-em", "mailto:" + em + "?subject=" + encodeURIComponent(subj) + "&body=" + encodeURIComponent(m), S.em, false));
      var n = document.createElement("p"); n.className = "ob-fine";
      n.textContent = wa ? S.fineWa : S.fineEm;
      if (wa || em) out.appendChild(n);
    });
  }
  function btn(cls, href, label, isWa) {
    // Own click handling: the site-wide mail picker (team@ mailto) and cta-note (wa.me links) must not re-route these.
    var a = document.createElement("a"); a.className = "ob-go " + cls; a.href = isWa ? "#whatsapp" : href;
    a.setAttribute("data-ob", "1"); a.textContent = label;
    a.addEventListener("click", function (e) {
      e.stopPropagation();
      if (isWa) { e.preventDefault(); window.open(href, "_blank", "noopener"); }
    });
    return a;
  }
  card.addEventListener("click", function (e) {
    var o = e.target.closest(".ob-opt");
    if (o) {
      var s = o.closest(".ob-step"), key = s.getAttribute("data-k");
      [].forEach.call(s.querySelectorAll(".ob-opt"), function (x) { x.setAttribute("aria-pressed", x === o ? "true" : "false"); });
      ans[key] = o.getAttribute("data-v") || o.textContent.trim();
      var nx = s.querySelector(".ob-next"); if (nx) nx.disabled = false;
      if (!s.querySelector(".ob-next")) setTimeout(function () { go(cur + 1); }, 160);
      if (cur >= steps.length - 3) getGeo();
      return;
    }
    if (e.target.closest(".ob-next")) { go(cur + 1); return; }
    if (e.target.closest(".ob-back")) { go(cur - 1); return; }
  });
  go(0);
})();
