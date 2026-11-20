"""Nov 20 2026: inline Google Ads replay loader before </body> on every public page (idempotent; re-points the hash).
Non-ad visitors run ~0.4 KB of inline JS and download nothing. Skips /users, scripts, node_modules."""
import json, re, pathlib
R = pathlib.Path(__file__).resolve().parents[2]
REC = json.load(open(R / "scripts/adrec/dist.json"))["adrec"]
JS = ('(function(){try{var s=sessionStorage,k="ubzad",a=s.getItem(k),q=location.search;'
      'if(!a&&(/[?&](gclid|gbraid|wbraid|gad_source)=/.test(q)||/[?&]utm_source=google(&|$)/i.test(q)&&/[?&]utm_medium=(cpc|ppc|paid[a-z_]*)(&|$)/i.test(q))){'
      'a=JSON.stringify({l:location.pathname+q,r:(document.referrer||"").slice(0,200),t:Date.now()});s.setItem(k,a)}'
      'if(a){var e=document.createElement("script");e.src="/assets/' + REC + '";e.async=true;document.body.appendChild(e)}}catch(e){}})();')
TAG = '<script id="ubz-adrec">' + JS + '</script>'
OLD = re.compile(r'<script id="ubz-adrec">.*?</script>', re.S)
n = 0
for p in R.rglob("*.html"):
    if any(x in p.parts for x in (".git", "node_modules", "scripts", "users", "qa-render")): continue
    s = p.read_text(errors="ignore")
    if "</body>" not in s: continue
    s2 = OLD.sub("", s)
    i = s2.rfind("</body>"); s2 = s2[:i] + TAG + s2[i:]
    if s2 != s: p.write_text(s2); n += 1
print("pages", n, REC)
