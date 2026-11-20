/* Nov 20 2026 (b): /api/geo/ is asked by every visitor; contactAllowed:false (IN/PK/IR IP or time zone) removes ALL contact via window.__ubzNoc.
   Nov 20 2026: strict WhatsApp contact. Shown only when /api/geo/ returns a number, which it does only for
   IP country US, CA, GB, NL or AE AND a browser time zone of one of those countries (VPN users elsewhere fail).
   The browser checks the time zone first too, so blocked visitors never even request it. Automation never asks.
   The number is NOT in any HTML or in this file, and it is never printed on the page: the WhatsApp button opens
   the same "What do you need help with?" picker as email, then WhatsApp with the answers pre-filled. */
(function () {
  try {
    try { sessionStorage.removeItem("ubz_cc"); } catch (e) {}
    var root = document.documentElement;
    var lang = (root.getAttribute("lang") || "").toLowerCase();
    var nl = lang.indexOf("nl") === 0;
    root.setAttribute("data-contact", "email");
    if (root.hasAttribute("data-noc")) return; // IN/PK/IR: no contact at all (inline #ubz-noc guard)
    var TZ = "|America/Adak|America/Anchorage|America/Atikokan|America/Atka|America/Blanc-Sablon|America/Boise|America/Cambridge_Bay|America/Chicago|America/Coral_Harbour|America/Creston|America/Dawson|America/Dawson_Creek|America/Denver|America/Detroit|America/Edmonton|America/Fort_Nelson|America/Fort_Wayne|America/Glace_Bay|America/Goose_Bay|America/Halifax|America/Indiana/Indianapolis|America/Indiana/Knox|America/Indiana/Marengo|America/Indiana/Petersburg|America/Indiana/Tell_City|America/Indiana/Vevay|America/Indiana/Vincennes|America/Indiana/Winamac|America/Indianapolis|America/Inuvik|America/Iqaluit|America/Juneau|America/Kentucky/Louisville|America/Kentucky/Monticello|America/Knox_IN|America/Los_Angeles|America/Louisville|America/Menominee|America/Metlakatla|America/Moncton|America/Montreal|America/New_York|America/Nipigon|America/Nome|America/North_Dakota/Beulah|America/North_Dakota/Center|America/North_Dakota/New_Salem|America/Pangnirtung|America/Phoenix|America/Rainy_River|America/Rankin_Inlet|America/Regina|America/Resolute|America/Shiprock|America/Sitka|America/St_Johns|America/Swift_Current|America/Thunder_Bay|America/Toronto|America/Vancouver|America/Whitehorse|America/Winnipeg|America/Yakutat|America/Yellowknife|Asia/Dubai|Canada/Atlantic|Canada/Central|Canada/Eastern|Canada/Mountain|Canada/Newfoundland|Canada/Pacific|Canada/Saskatchewan|Canada/Yukon|Europe/Amsterdam|Europe/Belfast|Europe/London|GB|GB-Eire|Navajo|Pacific/Honolulu|US/Alaska|US/Aleutian|US/Arizona|US/Central|US/East-Indiana|US/Eastern|US/Hawaii|US/Indiana-Starke|US/Michigan|US/Mountain|US/Pacific|";
    var tz = "";
    try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch (e) {}
    var waOk = !!tz && TZ.indexOf("|" + tz + "|") >= 0 && !navigator.webdriver;
    var num = "";
    function openWa(a) {
      var t = a && a.getAttribute("data-topic");
      if (window.unbanzMailPick && window.unbanzMailPick.wa) { window.unbanzMailPick.open(t, { wa: num }); return; }
      var msg = nl ? "Hoi Unbanz, ik heb hulp nodig met mijn account.\nPlatform en gebruikersnaam: \nWat er gebeurde: " : "Hi Unbanz, I need help with my account.\nPlatform and username: \nWhat happened: ";
      window.open("https://wa.me/" + num + "?text=" + encodeURIComponent(msg), "_blank", "noopener");
    }
    function mk(cls, label) {
      var a = document.createElement("a");
      a.href = "#whatsapp";
      a.className = "wa-direct " + (cls || "");
      a.setAttribute("role", "button");
      a.setAttribute("data-wa", "1");
      a.textContent = label;
      return a;
    }
    function show() {
      root.setAttribute("data-contact", "both");
      var L = nl ? "WhatsApp ons" : "WhatsApp us";
      var bar = document.querySelector(".mobile-contact");
      if (bar && !bar.querySelector(".wa-direct")) bar.insertBefore(mk("", "WhatsApp"), bar.firstChild);
      var hdr = document.querySelector(".ecta-hdr");
      if (hdr && hdr.parentNode && !document.querySelector(".wa-hdr")) hdr.parentNode.insertBefore(mk("ecta-hdr wa-hdr", "WhatsApp"), hdr.nextSibling);
      var heroes = document.querySelectorAll(".hero-cta");
      for (var i = 0; i < heroes.length; i++) if (!heroes[i].querySelector(".wa-direct")) heroes[i].appendChild(mk("hero-email", L + " ↗︎"));
      var ag = document.querySelectorAll(".ag-band .ag-act");
      for (var g = 0; g < ag.length; g++) if (!ag[g].querySelector(".wa-direct")) { var w = mk("", "WhatsApp"); w.setAttribute("data-topic", "other"); ag[g].appendChild(w); }
      var fb = document.querySelector(".footer-bottom");
      if (fb && !fb.querySelector(".wa-direct")) fb.appendChild(mk("", "WhatsApp"));
      var only = document.querySelectorAll(".ecta-only");
      for (var j = 0; j < only.length; j++) {
        only[j].textContent = nl
          ? "Mail team@unbanz.com of tik op WhatsApp. Kies je probleem en vermeld je gebruikersnaam of profiellink."
          : "Email team@unbanz.com or tap WhatsApp. Pick your issue and add your username or profile link.";
      }
      document.addEventListener("click", function (e) {
        if (e.defaultPrevented || e.button !== 0) return;
        var a = e.target.closest && e.target.closest('a[data-wa="1"]');
        if (!a) return;
        e.preventDefault();
        openWa(a);
      });
    }
    fetch("/api/geo/?tz=" + encodeURIComponent(tz), { credentials: "omit", cache: "no-store" }).then(function (r) { return r.json(); }).then(function (j) {
      if (j && j.contactAllowed === false) { if (window.__ubzNoc) window.__ubzNoc(); return; }
      if (!waOk) return;
      var n = j && j.wa ? String(j.wa) : "";
      if (!/^[0-9]{8,15}$/.test(n)) return;
      num = n;
      if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", show);
      else show();
    }).catch(function () {});
  } catch (e) {}
})();
