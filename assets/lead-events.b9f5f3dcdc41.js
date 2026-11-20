/* Nov 20 2026 CRO: GTM conversion events (container GTM-PGDPS7SK fires Google Ads conversions on these).
   lead_email    = the visitor opens their email app from the picker ("Write the email") or agency onboarding.
   lead_whatsapp = the visitor opens WhatsApp from the picker or agency onboarding (top-tier countries only).
   Capture phase on window, so it runs before the picker/onboarding handlers. Never pushes the email address,
   the WhatsApp number or any typed text; only the event name, issue topic, source and page path. */
(function () {
  var last = 0;
  function push(ev, a, src) {
    var now = Date.now(); if (now - last < 800) return; last = now;
    try {
      window.dataLayer = window.dataLayer || [];
      var dlg = a.closest(".cm-dialog");
      var sel = dlg && dlg.querySelector(".mp-sel-tx"); var topic = (sel && sel.textContent) || a.getAttribute("data-topic") || "";
      window.dataLayer.push({ event: ev, lead_source: src, lead_topic: String(topic).slice(0, 40), page_path: location.pathname });
    } catch (e) {}
  }
  window.addEventListener("click", function (e) {
    var t = e.target; if (!t || !t.closest) return;
    var a = t.closest("a.mp-go, a.ob-go");
    if (!a) return;
    var href = a.getAttribute("href") || "";
    var src = a.classList.contains("ob-go") ? "agency_onboarding" : "picker";
    if (a.classList.contains("ob-wa") || /^https:\/\/wa\.me\//.test(href)) push("lead_whatsapp", a, src);
    else if (/^mailto:/i.test(href)) push("lead_email", a, src);
  }, true);
})();
