/* Visitor-country contact channels. Same script for people and crawlers.
   Country comes from /api/geo/ (Vercel x-vercel-ip-country). No IP is stored.
   A sessionStorage choice overrides detection and is not a cookie. */
(function () {
  try {
    var BOTH = { US: 1, CA: 1, GB: 1, FR: 1, NL: 1, AE: 1, IT: 1 };
    var KEY = "ubz_cc";
    var root = document.documentElement;

    function segments(path) {
      return path.toLowerCase().split(/[^a-z0-9]+/);
    }
    function pathBoth() {
      var segs = segments(location.pathname || "/");
      var priority = { usa: 1, uk: 1, canada: 1, france: 1, netherlands: 1, uae: 1, dubai: 1, italy: 1, gulf: 1 };
      for (var i = 0; i < segs.length; i++) if (priority[segs[i]]) return true;
      return false;
    }
    function readOverride() {
      try { return sessionStorage.getItem(KEY) || ""; } catch (e) { return ""; }
    }
    function modeFor(code, override) {
      if (override === "BOTH") return "both";
      if (override === "EMAIL") return "email";
      if (override && BOTH[override]) return "both";
      if (override === "OTHER") return "email";
      if (code && BOTH[code]) return "both";
      if (code) return "email";
      return pathBoth() ? "both" : "email";
    }
    function apply(code, override) {
      root.setAttribute("data-contact", modeFor(code, override));
      root.setAttribute("data-cc", override || code || "");
      var sel = document.getElementById("ubz-cc");
      if (sel && document.activeElement !== sel) sel.value = override || "";
    }
    function mount(code) {
      var footer = document.querySelector(".footer-bottom") || document.querySelector("footer");
      if (!footer || document.getElementById("ubz-cc")) return;
      var lang = (root.lang || "en").toLowerCase().slice(0, 2);
      var label = { en: "Contact country", fr: "Pays du contact", nl: "Land voor contact", es: "País de contacto", pt: "País do contato" }[lang] || "Contact country";
      var auto = { en: "Detected automatically", fr: "Détecté automatiquement", nl: "Automatisch", es: "Detectado", pt: "Detectado automaticamente" }[lang] || "Detected automatically";
      var other = { en: "Other country", fr: "Autre pays", nl: "Ander land", es: "Otro país", pt: "Outro país" }[lang] || "Other country";
      var wrap = document.createElement("label");
      wrap.className = "ubz-loc";
      var text = document.createElement("span");
      text.textContent = label;
      var sel = document.createElement("select");
      sel.id = "ubz-cc";
      var options = [["", auto], ["US", "United States"], ["CA", "Canada"], ["GB", "United Kingdom"], ["FR", "France"], ["NL", "Netherlands"], ["AE", "United Arab Emirates"], ["IT", "Italy"], ["OTHER", other]];
      options.forEach(function (pair) {
        var opt = document.createElement("option");
        opt.value = pair[0];
        opt.textContent = pair[1];
        sel.appendChild(opt);
      });
      sel.value = readOverride();
      wrap.appendChild(text);
      wrap.appendChild(sel);
      footer.appendChild(wrap);
    }
    var detected = "";
    function refresh() { apply(detected, readOverride()); }
    refresh();
    mount("");
    var sel0 = document.getElementById("ubz-cc");
    if (sel0) sel0.addEventListener("change", function () {
      try { if (sel0.value) sessionStorage.setItem(KEY, sel0.value); else sessionStorage.removeItem(KEY); } catch (e) {}
      refresh();
    });
    if (readOverride()) return;
    fetch("/api/geo/", { credentials: "omit", cache: "no-store" }).then(function (r) { return r.json(); }).then(function (j) {
      var code = String((j && j.c) || "").toUpperCase();
      detected = /^[A-Z]{2}$/.test(code) ? code : "";
      refresh();
      if (sel0 && detected) sel0.setAttribute("data-detected", detected);
    }).catch(function () { refresh(); });
  } catch (e) {}
})();
