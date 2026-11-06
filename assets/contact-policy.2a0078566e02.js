/* Automatic contact channel from the existing Vercel country header.
   Same script for people and crawlers. No country picker and no saved override.
   /api/geo/ is private and no-store. This script does not keep the IP. */
(function () {
  try {
    var BOTH = { US: 1, CA: 1, GB: 1, FR: 1, NL: 1, AE: 1, IT: 1 };
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
