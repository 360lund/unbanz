/* Nov 20 2026: agency onboarding picker on /white-label-agency/. 5 steps; the last step hands off by the 3-tier rule:
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
    if (cnt) cnt.textContent = "Step " + (cur + 1) + " of " + steps.length;
    if (cur === steps.length - 1) finish();
    var h = steps[cur].querySelector(".ob-q"); if (h && go.moved) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
    go.moved = true;
  }
  function msg() {
    var name = (card.querySelector("#ob-name") || {}).value || "";
    return "Hi Unbanz, I'd like to onboard as a white-label agency partner.\n\n" +
      "Agency type: " + (ans.type || "") + "\n" + "Agency name: " + name.trim() + "\n" +
      "Client cases per month: " + (ans.volume || "") + "\n" + "Services needed: " + (ans.service || "") + "\n" +
      "Pricing: " + (ans.pricing || "") + "\n\nWebsite: \nBest way to reach me: ";
  }
  function finish() {
    var out = card.querySelector(".ob-out"); if (!out) return;
    var sum = card.querySelector(".ob-sum");
    if (sum) sum.innerHTML = ["type", "volume", "service", "pricing"].map(function (k) { return ans[k] ? "<li>" + ans[k].replace(/[<>&]/g, "") + "</li>" : ""; }).join("");
    out.innerHTML = '<p class="ob-wait">One moment…</p>';
    getGeo().then(function (g) {
      out.innerHTML = "";
      if (!g || g.contactAllowed === false || root.hasAttribute("data-noc")) {
        var q = steps[cur].querySelector(".ob-q"); if (q) q.textContent = "Thanks for your answers.";
        out.innerHTML = '<p class="ob-na">Direct agency onboarding is currently unavailable in your region.</p>'; return;
      }
      var m = msg(), subj = "Agency onboarding: " + (ans.type || "agency") + ", " + (ans.volume || "");
      var wa = g.whatsapp && !navigator.webdriver ? String(g.whatsapp).replace(/\D/g, "") : "";
      var em = g.email && /^[^@\s]+@[^@\s]+$/.test(g.email) ? g.email : "";
      if (wa) out.appendChild(btn("ob-wa", "https://wa.me/" + wa + "?text=" + encodeURIComponent(m), "Send on WhatsApp", true));
      if (em) out.appendChild(btn(wa ? "ob-em ob-alt" : "ob-em", "mailto:" + em + "?subject=" + encodeURIComponent(subj) + "&body=" + encodeURIComponent(m), "Send by email", false));
      var n = document.createElement("p"); n.className = "ob-fine";
      n.textContent = wa ? "Your answers are pre-filled. We reply within one business day." : "Your answers are pre-filled in the email. We reply within one business day.";
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
