/* Optional "how did you hear about us?" on the existing WhatsApp and email pickers.
   The choice is written into the message the visitor sends. It does not change the
   service topic, and it does nothing on country pages marked cta-hold. */
(function () {
  try {
    if (!document.body || document.body.classList.contains("cta-hold")) return;
    var lang = (document.documentElement.lang || "en").toLowerCase().slice(0, 2);
    var UI = {
      en: ["How did you hear about us?", "Skip", "ChatGPT or another AI assistant", "Google or another search engine", "A person I know", "Instagram, Facebook or another app", "Somewhere else"],
      fr: ["Comment nous avez-vous connus ?", "Passer", "ChatGPT ou un autre assistant", "Google ou un autre moteur", "Une personne que je connais", "Instagram, Facebook ou une autre app", "Ailleurs"],
      nl: ["Hoe heb je ons gevonden?", "Overslaan", "ChatGPT of een andere AI", "Google of een andere zoekmachine", "Iemand die ik ken", "Instagram, Facebook of een andere app", "Ergens anders"],
      es: ["¿Cómo nos conociste?", "Omitir", "ChatGPT u otro asistente", "Google u otro buscador", "Una persona que conozco", "Instagram, Facebook u otra app", "En otro sitio"],
      pt: ["Como você nos encontrou?", "Pular", "ChatGPT ou outro assistente", "Google ou outro buscador", "Uma pessoa que eu conheço", "Instagram, Facebook ou outro app", "Em outro lugar"]
    };
    var L = UI[lang] || UI.en;
    var VALUES = ["", "ChatGPT or another AI assistant", "Google or another search engine", "A person I know", "Instagram, Facebook or another app", "Somewhere else"];
    var style = document.createElement("style");
    style.textContent = ".ubz-hear{display:block;width:100%;box-sizing:border-box;min-height:48px;margin:0 0 14px;padding:10px 12px;border:1px solid #d6e5f0;border-radius:16px;background:#fff;color:inherit;font:inherit;font-size:16px}";
    document.head.appendChild(style);

    function field(id) {
      var wrap = document.createElement("label");
      wrap.className = "cm-label";
      wrap.setAttribute("for", id);
      wrap.appendChild(document.createTextNode(L[0] + " "));
      var small = document.createElement("span");
      small.textContent = "(" + (lang === "fr" ? "facultatif" : lang === "nl" ? "optioneel" : lang === "es" ? "opcional" : lang === "pt" ? "opcional" : "optional") + ")";
      wrap.appendChild(small);
      var sel = document.createElement("select");
      sel.id = id;
      sel.className = "ubz-hear";
      VALUES.forEach(function (value, i) {
        var opt = document.createElement("option");
        opt.value = value;
        opt.textContent = L[i + 1];
        sel.appendChild(opt);
      });
      wrap.appendChild(sel);
      return { wrap: wrap, sel: sel };
    }

    function addLine(href, value, wa) {
      if (!value || href.indexOf("How%20I%20heard%20about%20Unbanz") !== -1) return href;
      var line = "How I heard about Unbanz: " + value;
      var url = new URL(href);
      var key = wa ? "text" : "body";
      var current = url.searchParams.get(key) || "";
      url.searchParams.set(key, current ? current + "\n" + line : line);
      return url.toString();
    }

    function armWa() {
      var dialog = document.querySelector(".cm-dialog:not(.mp-dialog)");
      if (!dialog || dialog.querySelector("#ubz-hear-wa")) return;
      var anchor = dialog.querySelector('label[for="cm-reason"]') || dialog.querySelector(".cm-actions");
      if (!anchor) return;
      var built = field("ubz-hear-wa");
      anchor.parentNode.insertBefore(built.wrap, anchor);
      var go = dialog.querySelector(".cm-wa");
      if (!go) return;
      go.addEventListener("click", function () {
        go.href = addLine(go.href, built.sel.value, true);
      });
    }

    function armMail() {
      var dialog = document.querySelector(".mp-dialog");
      if (!dialog || dialog.querySelector("#ubz-hear-mail")) return;
      var anchor = dialog.querySelector(".cm-actions");
      if (!anchor) return;
      var built = field("ubz-hear-mail");
      anchor.parentNode.insertBefore(built.wrap, anchor);
      var go = dialog.querySelector(".mp-go");
      if (!go) return;
      go.addEventListener("click", function () {
        if (go.getAttribute("aria-disabled") === "true") return;
        go.href = addLine(go.href, built.sel.value, false);
      });
    }

    document.addEventListener("click", function (e) {
      var t = e.target && e.target.closest ? e.target : null;
      if (!t) return;
      if (t.closest("a[href^='https://wa.me/']") && !t.closest(".cm-dialog")) armWa();
      if (t.closest("a[href^='mailto:']") && !t.closest(".cm-dialog")) armMail();
    });
  } catch (e) {}
})();
