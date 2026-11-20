"""Nov 20 2026 (c): /white-label-agency/ becomes a short closing/onboarding page (hero + 5-step onboarding picker +
How it works + partner terms). The long guide hub it used to be moves, unchanged in substance, to
/white-label-agency/guides/ ("Agency resources"), which also lists the agency Q&A pages. Source = git HEAD hub,
so the script is re-runnable."""
import os, re, json, subprocess, sys, html, hashlib, shutil
sys.path.insert(0, os.path.dirname(__file__))
from qa_agency import P
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); os.chdir(ROOT)
B = 'https://unbanz.com/'; HUB = B + 'white-label-agency/'; GU = HUB + 'guides/'; TODAY = '2026-11-20'
esc = lambda t: html.escape(t, quote=True)
src = subprocess.check_output(['git', 'show', 'HEAD:white-label-agency/index.html']).decode('utf8')
# onboarding script asset (hashed)
js = open('scripts/nov20_agency/onboard.js', 'rb').read(); hsh = hashlib.sha256(js).hexdigest()[:12]
JS = f'/assets/agency-onboard.{hsh}.js'; shutil.copy('scripts/nov20_agency/onboard.js', 'assets/agency-onboard.' + hsh + '.js')
ART = re.compile(r'<div aria-hidden="true" class="ub-hero-art">.*?</div>', re.S)
LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
def set_meta(head, title, desc, url):
    head = re.sub(r'<title>.*?</title>', f'<title>{esc(title)}</title>', head, flags=re.S)
    for a in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'<meta content="[^"]*" ' + re.escape(a) + '/>', f'<meta content="{esc(desc)}" {a}/>', head)
    for a in ('property="og:title"', 'name="twitter:title"'):
        head = re.sub(r'<meta content="[^"]*" ' + re.escape(a) + '/>', f'<meta content="{esc(title)}" {a}/>', head)
    head = re.sub(r'<meta content="[^"]*" property="og:url"/>', f'<meta content="{url}" property="og:url"/>', head)
    head = re.sub(r'<link href="[^"]*" rel="canonical"/>', f'<link href="{url}" rel="canonical"/>', head)
    head = re.sub(r'(<meta content=")[0-9-]+(" property="article:modified_time"/>)', r'\g<1>' + TODAY + r'\2', head)
    return head
hi = src.index('</head>'); mi = src.index('<main id="content">') + len('<main id="content">'); ti = src.index('</main>')
head0, bodystart, main0, tail = src[:hi], src[hi:mi], src[mi:ti], src[ti:]
g0 = json.loads(LD.search(head0).group(1))['@graph']
base_nodes = [n for n in g0 if n.get('@type') in ('Organization', 'WebSite')]
for n in base_nodes: n.pop('paymentAccepted', None)

# ---------- 1. /white-label-agency/guides/ (old hub content) ----------
gh = set_meta(head0, 'Agency Resources: White-Label Account Recovery Guides | Unbanz',
              'Guides and direct answers for agencies offering white-label Instagram, Facebook, TikTok and WhatsApp account recovery: pricing, client communication, vetting partners, bulk cases and country pages.', GU)
gh = re.sub(r'<link href="[^"]*" hreflang="[^"]*" rel="alternate"/>', '', gh)
gh = gh.replace(f'<link href="{GU}" rel="canonical"/>', f'<link href="{GU}" rel="canonical"/><link href="{GU}" hreflang="en" rel="alternate"/>')
nodes = []
for n in g0:
    t = n.get('@type')
    if t in ('Organization', 'WebSite'): continue
    if t in ('Service', 'Product', 'Offer'): continue
    s = json.dumps(n, ensure_ascii=False).replace(HUB + '#', GU + '#')
    n = json.loads(s)
    if t == 'WebPage': n.update({'url': GU, 'name': 'Agency resources: white-label account recovery guides', 'dateModified': TODAY}); n.pop('mainEntity', None)
    if t == 'BreadcrumbList':
        n['itemListElement'] = [{"@type": "ListItem", "position": 1, "name": "Home", "item": B}, {"@type": "ListItem", "position": 2, "name": "White label for agencies", "item": HUB}, {"@type": "ListItem", "position": 3, "name": "Agency resources", "item": GU}]
    if t == 'FAQPage': n['url'] = GU
    if t == 'ItemList':
        n['itemListElement'] = [{"@type": "ListItem", "position": i + 1, "url": B + p['slug'] + '/', "name": p['q']} for i, p in enumerate(P)] + [dict(x, position=x['position'] + len(P)) for x in n['itemListElement']]
        n['numberOfItems'] = len(n['itemListElement'])
    nodes.append(n)
ld = json.dumps({"@context": "https://schema.org", "@graph": base_nodes + nodes}, ensure_ascii=False, separators=(',', ':'))
m = LD.search(gh); gh = gh[:m.start()] + '<script type="application/ld+json">' + ld + '</script>' + gh[m.end():]
gm = ART.sub('', main0, count=1)
gm = gm.replace('<a class="crumb" href="/">Home / Services</a>', '<a class="crumb" href="/white-label-agency/">Home / White label for agencies</a>', 1)
gm = re.sub(r'<h1>.*?</h1>', '<h1>Agency resources: white-label recovery guides.</h1>', gm, count=1, flags=re.S)
gm = re.sub(r'(<h1>.*?</h1>)<p>.*?</p><div class="hero-cta">.*?</div>', lambda mm: mm.group(1) + '<p>Everything agencies ask before offering account recovery under their own brand: how it works, pricing, client communication, vetting a partner and country pages. Ready to start? <a href="/white-label-agency/">Onboard as an agency partner</a>.</p><div class="hero-cta"><a class="button button-light" href="/white-label-agency/">Start agency onboarding <span aria-hidden="true">→</span></a></div>', gm, count=1, flags=re.S)
gm = gm.replace('<a href="#agency-guides">', '<a href="#agency-questions">Agency questions answered</a><a href="#agency-guides">', 1)
gm = gm.replace('<h2 id="agency-guides">', '<h2 id="agency-questions">Agency questions answered</h2><p>Direct answers to what agencies ask before handing a client account to a white-label partner.</p><ul>' + ''.join(f'<li><a href="/{p["slug"]}/">{esc(p["q"])}</a></li>' for p in P) + '</ul><h2 id="agency-guides">', 1)
gm = re.sub(r'<section class="service-fees container" id="service-fees">.*?</section>', '<section class="service-fees container" id="service-fees"><p class="eyebrow">AGENCY RATE</p><h2>$1,200 per case.</h2><p>The white-label rate is $1,200 per case (one account or one handle), paid upfront by bank transfer, no cards. Most cases take 7 to 14 days. If the account is not reinstated within 14 calendar days, you get a 100% refund, paid the same business day. Volume pricing for 5+ cases a month after a first test case. The platform decides the outcome. <a href="/white-label-agency/">Start onboarding</a>.</p></section>', gm, count=1, flags=re.S)
os.makedirs('white-label-agency/guides', exist_ok=True)
open('white-label-agency/guides/index.html', 'w', encoding='utf8').write(gh + bodystart + gm + tail)

# ---------- 2. /white-label-agency/ (closing / onboarding page) ----------
TITLE = 'White-Label Account Recovery for Agencies: $1,200 per Case | Unbanz'
DESC = 'White-label Instagram, Facebook, TikTok and X account recovery and username claims for PR, talent, SMMA and reputation agencies. $1,200 per case, usually 7–14 days, full refund the same business day if not reinstated in 14 days.'
hh = set_meta(head0, TITLE, DESC, HUB)
hh = hh.replace('</head>', '')
nodes = base_nodes + [
 {"@type": "WebPage", "@id": HUB + "#webpage", "url": HUB, "name": TITLE, "description": DESC, "isPartOf": {"@id": B + "#website"}, "inLanguage": "en", "dateModified": TODAY, "breadcrumb": {"@id": HUB + "#breadcrumb"}, "mainEntity": {"@id": HUB + "#service"}},
 {"@type": "Service", "@id": HUB + "#service", "name": "White-label account recovery for agencies", "serviceType": "White-label social media account recovery and username claims", "description": "Agencies keep the client; Unbanz files the appeal or username claim through the platform's official process in the background. The platform makes the final decision.", "provider": {"@id": B + "#organization"}, "areaServed": "Worldwide", "url": HUB,
  "audience": {"@type": "BusinessAudience", "audienceType": "PR firms, talent management, SMMA, reputation management and legal agencies"},
  "hasOfferCatalog": {"@type": "OfferCatalog", "name": "White-label services", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in ("Instagram and Facebook account recovery", "Facebook ad account and Business Manager recovery", "TikTok and X account recovery", "Instagram username claims")]},
  "offers": {"@type": "Offer", "price": 1200, "priceCurrency": "USD", "description": "Per case (one account or one handle), paid upfront by bank transfer. Usually 7–14 days. 100% refund paid the same business day if not reinstated within 14 calendar days.", "url": HUB}},
 {"@type": "BreadcrumbList", "@id": HUB + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": B}, {"@type": "ListItem", "position": 2, "name": "White label for agencies", "item": HUB}]},
]
ld = json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, separators=(',', ':'))
m = LD.search(hh); hh = hh[:m.start()] + '<script type="application/ld+json">' + ld + '</script>' + hh[m.end():]
CSS = open('scripts/nov20_agency/hub.css', encoding='utf8').read().strip()
hh += f'<style id="wl-css">{CSS}</style><script defer src="{JS}"></script>'
def opts(vals): return ''.join(f'<button type="button" class="ob-opt" aria-pressed="false" data-v="{esc(v)}">{esc(l)}</button>' for v, l in vals)
back = '<button type="button" class="ob-back">← Back</button>'
card = ('<div class="ob" id="ob" aria-label="Agency onboarding"><div class="ob-top"><p class="ob-t">Agency onboarding</p><p class="ob-count">5 quick questions</p></div><div class="ob-bar" aria-hidden="true"><i></i></div>'
 '<div class="ob-step" data-k="type"><p class="ob-q">What kind of agency are you?</p><div class="ob-opts">' + opts([(x, x) for x in ('PR', 'Talent management', 'SMMA', 'Reputation', 'Legal', 'Other')]) + '</div>'
 '<label class="ob-lab" for="ob-name">Agency name <span>(optional)</span></label><input class="ob-in" id="ob-name" type="text" autocomplete="organization" placeholder="e.g. Northside Talent" maxlength="80"/>'
 '<div class="ob-nav"><span></span><button type="button" class="ob-next" disabled>Continue →</button></div></div>'
 '<div class="ob-step" data-k="volume"><p class="ob-q">How many client cases do you handle per month?</p><div class="ob-opts ob-col">' + opts([(x, x) for x in ('1–3 / month', '4–10 / month', '10+ / month')]) + '</div><div class="ob-nav">' + back + '</div></div>'
 '<div class="ob-step" data-k="service"><p class="ob-q">What do you need most?</p><div class="ob-opts ob-col">' + opts([(x, x) for x in ('Instagram & Facebook bans', 'TikTok / X bans', 'Username claims', 'Mix of all')]) + '</div><div class="ob-nav">' + back + '</div></div>'
 '<div class="ob-step" data-k="pricing"><p class="ob-q">Our white-label rate is $1,200 per case via upfront bank transfer. Are you okay with that?</p><div class="ob-opts ob-col">' + opts([('Yes, $1,200/case works', 'Yes, $1,200/case works'), ('Yes, need 5+/mo volume pricing', 'Yes, I need 5+/mo volume pricing')]) + '</div><div class="ob-nav">' + back + '</div></div>'
 '<div class="ob-step" data-k="done"><p class="ob-q">You’re all set. Send us your answers.</p><ul class="ob-sum"></ul><div class="ob-out"></div><div class="ob-nav">' + back + '</div></div>'
 '</div>')
hero = ('<section class="wl-hero"><div class="container wl-grid"><div class="wl-copy"><a class="crumb" href="/">Home / For agencies</a><p class="wl-eye">WHITE-LABEL PARTNER PROGRAM</p>'
 '<h1>White-label account recovery for agencies.</h1><p class="wl-lead">You keep the client. We file the appeal or username claim quietly in the background, with no Unbanz name in front of your client.</p>'
 '<ul class="wl-terms"><li><b>$1,200</b><span>per case</span></li><li><b>7–14</b><span>days, usually</span></li><li><b>100%</b><span>refund if not reinstated in 14 days</span></li></ul>'
 '<p class="wl-fine">Upfront bank transfer · no cards · no passwords needed · official platform processes only.</p></div>' + card + '</div></section>')
how = ('<section class="wl-how container" aria-labelledby="wl-how-t"><h2 id="wl-how-t">How it works</h2><ol>'
 '<li><b>Send the case</b><p>Handle or profile link, a screenshot of the notice and the date it happened. No passwords or login codes.</p></li>'
 '<li><b>We file it, white-label</b><p>We use the platform’s official route. You get plain updates you can forward under your own brand. Usually 7–14 days.</p></li>'
 '<li><b>Reinstated, or refunded</b><p>If the account is not reinstated within 14 calendar days, you get a 100% refund, paid the same business day.</p></li></ol></section>')
terms = ('<section class="wl-pt container" aria-labelledby="wl-pt-t"><h2 id="wl-pt-t">Partner terms</h2><dl>'
 '<div><dt>Rate</dt><dd>$1,200 per case (one account or one handle)</dd></div>'
 '<div><dt>Volume</dt><dd>Volume pricing for 5+ cases a month, after a first test case</dd></div>'
 '<div><dt>Payment</dt><dd>Upfront bank transfer to our US or UK business account. No cards.</dd></div>'
 '<div><dt>Timeline</dt><dd>Usually 7–14 days</dd></div>'
 '<div><dt>Refund</dt><dd>100%, paid the same business day, if not reinstated within 14 calendar days</dd></div>'
 '<div><dt>Platforms</dt><dd>Instagram, Facebook and ad accounts, TikTok, X, username claims</dd></div>'
 '<div><dt>Confidentiality</dt><dd>We never contact your client. Signed agreement available.</dd></div></dl>'
 '<p class="wl-disc">Unbanz is independent and not affiliated with Meta, Instagram, Facebook, TikTok or X. The platform makes the final decision on every case. <a href="/white-label-agency/guides/">Agency resources</a></p></section>')
open('white-label-agency/index.html', 'w', encoding='utf8').write(hh + bodystart + hero + how + terms + tail)
print('ok', JS)
