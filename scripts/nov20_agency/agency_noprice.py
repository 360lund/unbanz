"""Nov 20 2026 user rule: "For agency don't mention prices."
Post-process (idempotent; re-run after ANY agency build script): removes every agency / white-label price.
1) every page: agency band, contextual one-liner and pricing-card chip lose their price (all locales);
2) agency pages (path matches white-label/agency words): onboarding pricing step removed, any sentence with a money
   amount removed from visible text, meta/og/twitter text and JSON-LD strings; JSON-LD offers/price keys dropped;
   emptied answers get a neutral 'rate shared privately' line. Direct-customer $1,000 on non-agency pages is untouched."""
import re, json, pathlib, sys
R = pathlib.Path(__file__).resolve().parents[2]
SKIP = (".git", "node_modules", "scripts", "users", "qa-render")
AGP = re.compile(r"white-label|agenc|agences|bureau|agentur|agenzi|ajans|recovery-partner", re.I)
# consumer pages whose URL merely mentions an agency: keep their direct-customer prices
CONSUMER = ("ad-account-restricted-after-agency-shared-access", "facebook-page-owned-by-former-agency")
MONEY = re.compile(r"(US\$|\$|€|£)\s?\d|\d[\d,.\u00a0\u202f ]*\s?(\$|€|£|USD\b|dollars?\b)|\bUSD\s?\d|\bprice\":\s*\d", re.I)
NEUTRAL = {"en": "Rates are per case and shared privately once we’ve reviewed your volume and the cases.",
           "fr": "Le tarif par dossier est communiqué en privé après examen de votre volume.",
           "nl": "Het tarief per zaak delen we privé nadat we je volume hebben bekeken.",
           "es": "La tarifa por caso se comparte en privado tras revisar tu volumen.",
           "pt": "O valor por caso é enviado em particular depois que analisamos seu volume."}
GLOBAL = [  # (old, new) exact, every page
    (" You keep the client, we do the platform work quietly. $1,200 per case, usually 7–14 days.", " You keep the client, we do the platform work quietly. Usually 7–14 days."),
    (" runs under your brand at $1,200 per case.", " runs under your brand."),
    (" se fait sous votre marque, à 1 200 $ par dossier.", " se fait sous votre marque."),
    (" loopt onder jouw merk, voor $1.200 per zaak.", " loopt onder jouw merk."),
    (" funciona com a sua marca, por US$ 1.200 por caso.", " funciona com a sua marca."),
    (" funciona con tu marca, a 1.200 $ por caso.", " funciona con tu marca."),
    (" läuft unter deiner Marke, für 1.200 $ pro Fall (", " läuft unter deiner Marke ("),
    (" lavora con il tuo marchio, a 1.200 $ per caso (", " lavora con il tuo marchio ("),
    (" sizin markanızla çalışır, vaka başına 1.200 $ (", " sizin markanızla çalışır ("),
    ("<li>$1,200 per case</li>", "<li>Private partner rate</li>"),
    (" under your brand at $1,200 per case (one account or handle, any platform).", " under your brand (one account or handle, any platform)."),
    ("<li>US$ 1.200 por caso</li>", "<li>Valor de parceiro privado</li>"),
    ("<li>$1.200 per zaak</li>", "<li>Privé partnertarief</li>"),
    ("<li>1 200 $ par dossier</li>", "<li>Tarif partenaire privé</li>"),
    ("<li>1.200 $ por caso</li>", "<li>Tarifa de socio privada</li>"),
]
SENT = re.compile(r"(?<=[.!?。])\s+(?=[A-ZÀ-ÝÇ<\"“(¿¡0-9$])")
LEAF = re.compile(r"<(p|li|dd|dt|td|th|summary|h[1-6]|figcaption|span|b|strong|em|small|a)(\s[^>]*)?>((?:(?!</?(?:p|li|dd|dt|td|th|div|ul|ol|dl|section|table|tr|details|h[1-6])\b)[\s\S])*?)</\1>")
def txt(h): return re.sub(r"<[^>]+>", "", h)
def scrub(t):
    if not MONEY.search(txt(t)): return t
    parts = SENT.split(t)
    return " ".join(p for p in parts if not MONEY.search(txt(p))).strip()
def lang_of(s):
    m = re.search(r'<html[^>]*lang="([a-z]{2})', s); return m.group(1) if m else "en"
def fix_json(o, lg):
    if isinstance(o, dict):
        for k in ("price", "priceCurrency", "priceSpecification", "priceRange", "lowPrice", "highPrice"): o.pop(k, None)
        if isinstance(o.get("offers"), dict) and o["offers"].get("@type") == "Offer" and "itemOffered" not in o["offers"]: o.pop("offers")
        for k, v in list(o.items()):
            if isinstance(v, str):
                n = scrub(v)
                if n != v: o[k] = n or (NEUTRAL.get(lg, NEUTRAL["en"]) if k == "text" else "")
                if o[k] == "": o.pop(k)
            else: fix_json(v, lg)
    elif isinstance(o, list):
        for x in o: fix_json(x, lg)
def agency(s):
    lg = lang_of(s); neu = NEUTRAL.get(lg, NEUTRAL["en"])
    s = re.sub(r'<div class="ob-step" data-k="pricing">[\s\S]*?(?=<div class="ob-step" data-k="done">)', "", s)
    s = re.sub(r"<li><b>[^<]*\d[^<]*</b><span>[^<]*</span></li>", lambda m: "" if MONEY.search(txt(m.group(0))) else m.group(0), s)
    s = re.sub(r"<div><dt>([^<]*)</dt><dd>([^<]*)</dd></div>", lambda m: (f"<div><dt>{m.group(1)}</dt><dd>Per-case wholesale rate, shared privately after we review your volume</dd></div>" if lg == "en" else "") if MONEY.search(m.group(2)) else m.group(0), s)
    s = re.sub(r"(<title>)([^<]*)(</title>)", lambda m: m.group(1) + re.sub(r":?\s*(US\$|\$)\s?1[,.]200 per [Cc]ase", "", m.group(2)) + m.group(3), s)
    s = re.sub(r'(<meta content=")([^"]*)("[^>]*(?:name|property)="(?:description|og:title|og:description|twitter:title|twitter:description|og:image:alt)")',
               lambda m: m.group(1) + (scrub(re.sub(r":?\s*\$1,200 per Case", "", m.group(2))) or re.sub(r"(US\$ ?|\$)\s?\d[\d,.]*( per case)?", "a per-case rate shared privately", m.group(2))) + m.group(3), s)
    def ld(m):
        try: o = json.loads(m.group(2))
        except Exception: return m.group(0)
        # titles: drop ': $1,200 per Case'
        raw = json.dumps(o, ensure_ascii=False); raw = re.sub(r":?\s*\$1,200 per Case", "", raw); o = json.loads(raw)
        fix_json(o, lg); return m.group(1) + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + m.group(3)
    s = re.sub(r'(<script type="application/ld\+json">)([\s\S]*?)(</script>)', ld, s)
    head, body = (s.split("<body", 1) + [""])[:2]
    if body:
        for _ in range(3):
            body = LEAF.sub(lambda m: m.group(0) if not MONEY.search(txt(m.group(3))) else ("<%s%s>%s</%s>" % (m.group(1), m.group(2) or "", scrub(m.group(3)), m.group(1))), body)
        # emptied FAQ answers -> neutral line; other emptied leaves removed
        body = re.sub(r"(</summary>\s*)<p[^>]*>\s*</p>", lambda m: m.group(1) + "<p>" + neu + "</p>", body)
        body = re.sub(r"<(p|li|dd|td|span|b|strong|em|small|h[1-6])(\s[^>]*)?>\s*</\1>", "", body)
        s = head + "<body" + body
    return s
def main():
    tot = ag = 0
    for p in R.rglob("*.html"):
        if any(x in p.parts for x in SKIP): continue
        s0 = s = p.read_text(errors="ignore")
        for a, b in GLOBAL: s = s.replace(a, b)
        rel = str(p.relative_to(R))
        if AGP.search(rel) and not rel.startswith(CONSUMER): s = agency(s)
        if s != s0: p.write_text(s); tot += 1; ag += bool(AGP.search(rel))
    print("pages changed", tot, "agency pages changed", ag)
if __name__ == "__main__": main()
