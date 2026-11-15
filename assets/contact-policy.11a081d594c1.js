/* Nov 15 2026: our WhatsApp is no longer offered; every visitor gets the email route.
   Automatic contact channel from the existing Vercel country header.
   Same script for people and crawlers. No country picker and no saved override.
   /api/geo/ is private and no-store. This script does not keep the IP. */
(function () {
  try {
    var BOTH = {}; // Nov 15 2026: WhatsApp contact removed for every country; email only.
    try { sessionStorage.removeItem("ubz_cc"); } catch (e) {}
    var root = document.documentElement;
    function apply(code) {
      root.setAttribute("data-contact", code && BOTH[code] ? "both" : "email");
    }
    apply("");
    fetch("/api/geo/", { credentials: "omit", cache: "no-store" }).then(function (r) { return r.json(); }).then(function (j) {
      var code = String((j && j.c) || "").toUpperCase();
      apply(/^[A-Z]{2}$/.test(code) ? code : "");
    }).catch(function () { apply(""); });
  } catch (e) {}
})();
