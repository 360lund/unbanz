/* Nov 20 2026 CRO: lead clicks from the picker or agency onboarding.
   lead_email    = the visitor opens their email app ("Write the email" or an onboarding mailto).
   lead_whatsapp = the visitor opens WhatsApp (top-tier countries only).
   Capture phase on window, so it runs before the picker/onboarding handlers. Keeps the dataLayer
   event and also fires Google Ads conversion AW-18585642552/B22SCPTisbwdELjMqZ5F via gtag
   (beacon, no event_callback, so the mailto / wa.me navigation is not delayed). One click is one
   conversion (800ms debounce). Never pushes the email address, the WhatsApp number or any typed text;
   only the event name, issue topic, source and page path. */
(function () {
  var last = 0;
  var ADS_SEND_TO = "AW-18585642552/B22SCPTisbwdELjMqZ5F";
  function push(ev, a, src) {
    var now = Date.now(); if (now - last < 800) return; last = now;
    try {
      window.dataLayer = window.dataLayer || [];
      var dlg = a.closest(".cm-dialog");
      var sel = dlg && dlg.querySelector(".mp-sel-tx"); var topic = (sel && sel.textContent) || a.getAttribute("data-topic") || "";
      topic = String(topic).slice(0, 40);
      window.dataLayer.push({ event: ev, lead_source: src, lead_topic: topic, page_path: location.pathname });
      if (typeof window.gtag !== "function") window.gtag = function gtag(){dataLayer.push(arguments);};
      window.gtag("event", "conversion", { send_to: ADS_SEND_TO, transport_type: "beacon", event_callback: undefined });
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
