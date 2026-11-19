/* Nov 19 2026: WhatsApp contact for visitors whose IP country is US, CA, GB, NL or AE.
   The number is NOT in any HTML or in this file. /api/geo/ (private, no-store) returns it
   only for those countries, from Vercel's IP country header. Everyone else: email only. */
(function () {
  try {
    try { sessionStorage.removeItem("ubz_cc"); } catch (e) {}
    var root = document.documentElement;
    var nl = (root.getAttribute("lang") || "").toLowerCase().indexOf("nl") === 0;
    root.setAttribute("data-contact", "email");
    function mk(num, cls, label) {
      var a = document.createElement("a");
      a.href = "https://wa.me/" + num + "?text=" + encodeURIComponent(nl ? "Hoi Unbanz, ik heb hulp nodig met mijn account." : "Hi Unbanz, I need help with my account.");
      a.className = "wa-direct " + (cls || "");
      a.setAttribute("rel", "nofollow noopener");
      a.setAttribute("target", "_blank");
      a.setAttribute("data-service", "whatsapp");
      a.textContent = label;
      return a;
    }
    function show(num, disp) {
      if (!/^[0-9]{8,15}$/.test(num)) return;
      root.setAttribute("data-contact", "both");
      var L = nl ? "WhatsApp ons" : "WhatsApp us";
      var bar = document.querySelector(".mobile-contact");
      if (bar && !bar.querySelector(".wa-direct")) bar.insertBefore(mk(num, "", "WhatsApp"), bar.firstChild);
      var hdr = document.querySelector(".ecta-hdr");
      if (hdr && hdr.parentNode && !document.querySelector(".wa-hdr")) hdr.parentNode.insertBefore(mk(num, "ecta-hdr wa-hdr", "WhatsApp"), hdr.nextSibling);
      var heroes = document.querySelectorAll(".hero-cta");
      for (var i = 0; i < heroes.length; i++) if (!heroes[i].querySelector(".wa-direct")) heroes[i].appendChild(mk(num, "hero-email", L + " ↗︎"));
      var fb = document.querySelector(".footer-bottom");
      if (fb && !fb.querySelector(".wa-direct")) fb.appendChild(mk(num, "", "WhatsApp " + (disp || "")));
      var only = document.querySelectorAll(".ecta-only");
      for (var j = 0; j < only.length; j++) {
        only[j].textContent = nl
          ? "Mail team@unbanz.com of stuur een WhatsApp naar " + disp + ". Vermeld het platform, je gebruikersnaam of profiellink en wat er gebeurde."
          : "Email team@unbanz.com or WhatsApp us on " + disp + ". Include the platform, your username or profile link, and what happened.";
      }
    }
    fetch("/api/geo/", { credentials: "omit", cache: "no-store" }).then(function (r) { return r.json(); }).then(function (j) {
      if (j && j.wa) {
        if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { show(String(j.wa), String(j.wd || "")); });
        else show(String(j.wa), String(j.wd || ""));
      }
    }).catch(function () {});
  } catch (e) {}
})();
