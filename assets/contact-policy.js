/* Nov 21 2026: WhatsApp contact removed (account suspended). Email is the only contact path.
   /api/geo/ still sets contactAllowed:false for IN/PK/IR (IP or time zone); those visitors get no contact.
   This file never requests or displays a WhatsApp number. */
(function () {
  try {
    try { sessionStorage.removeItem("ubz_cc"); } catch (e) {}
    var root = document.documentElement;
    var lang = (root.getAttribute("lang") || "en").toLowerCase().slice(0, 2);
    root.setAttribute("data-contact", "email");
    if (root.hasAttribute("data-noc")) return;
    var REPLY = {
      en: "Usually replies within 30 minutes",
      nl: "Meestal binnen 30 minuten antwoord",
      fr: "Réponse généralement en 30 minutes",
      es: "Suele responder en 30 minutos",
      pt: "Normalmente responde em 30 minutos",
      de: "Antwortet in der Regel innerhalb von 30 Minuten",
      it: "Di solito risponde entro 30 minuti",
      ar: "عادةً يتم الرد خلال 30 دقيقة",
      zh: "通常在 30 分钟内回复",
      tr: "Genellikle 30 dakika içinde yanıt verir"
    };
    var note = REPLY[lang] || REPLY.en;
    function addReply(el, tag, cls) {
      if (!el || el.querySelector("." + cls) || el.getAttribute("data-noc-skip")) return;
      var n = document.createElement(tag);
      n.className = cls;
      n.textContent = note;
      el.appendChild(n);
    }
    function notes() {
      if (root.hasAttribute("data-noc")) return;
      var heroes = document.querySelectorAll(".hero-cta");
      for (var i = 0; i < heroes.length; i++) addReply(heroes[i], "p", "cta-reply");
      var bars = document.querySelectorAll(".mobile-contact a[href^='mailto:']");
      for (var j = 0; j < bars.length; j++) {
        if (!bars[j].querySelector(".mc-sub")) {
          var s = document.createElement("span");
          s.className = "mc-sub";
          s.textContent = note;
          bars[j].appendChild(s);
        }
      }
      var acts = document.querySelectorAll(".ag-act, .pn-agency .pn-act, .cta-pair");
      for (var k = 0; k < acts.length; k++) {
        if (acts[k].querySelector("a[href^='mailto:']")) addReply(acts[k], "p", "cta-reply");
      }
    }
    var tz = "";
    try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch (e) {}
    fetch("/api/geo/?tz=" + encodeURIComponent(tz), { credentials: "omit", cache: "no-store" }).then(function (r) { return r.json(); }).then(function (j) {
      if (j && j.contactAllowed === false) { if (window.__ubzNoc) window.__ubzNoc(); return; }
      if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", notes);
      else notes();
    }).catch(function () {
      if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", notes);
      else notes();
    });
  } catch (e) {}
})();
