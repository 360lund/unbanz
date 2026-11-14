# Nov 14 conversion pass for help/service/guide pages.
# Adds (1) a benefit-led email button in the hero for visitors who only get email, (2) a "How can we help?"
# block with issue options that open the email picker preset to that issue, plus a trust strip,
# (3) a mid-page "three steps" block with a CTA. Leaves the hero design, the bottom CTA (.service-proof),
# the mobile contact bar, the footer, head/SEO/schema and the visitor-country scripts untouched.
# Idempotent: re-running replaces its own blocks (marked data-hx="nov14").
import pathlib, re, sys, html, urllib.parse
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from i18n import T
CSS_TAG = sys.argv[1]  # e.g. <link rel="stylesheet" href="/assets/help-cta.HASH.css">
ROOT = pathlib.Path('.')
SKIP_PARTS = ('white-label', 'agency', 'agencies', 'agences', 'agencias', 'agencias', 'bureaus', 'partner', 'reseller',
              'pricing', 'preise', 'prix', 'precios', 'precos', 'prijzen', 'tarifs', 'fiyat', 'prezzi', 'smma')
SKIP_TOP = {'users', 'about', 'privacy', 'terms', 'refund-policy', 'work', 'contact', 'reviews', 'api', 'assets', 'scripts', 'node_modules'}
SKIP_PREFIX = ('client-',)
LANGS = {'en': 'en', 'fr': 'fr', 'nl': 'nl', 'es': 'es', 'pt': 'pt', 'de': 'de', 'it': 'it', 'tr': 'tr', 'ar': 'ar'}
SUBJ = dict(ig_disabled='Instagram disabled - help', ig_hacked='Instagram hacked - help', fb='Facebook account - help',
            username='Username claim - help', ad='Ad account restricted - help', bm='Business Portfolio - help',
            page='Facebook Page - help', tiktok='TikTok account - help', youtube='YouTube channel - help',
            whatsapp='WhatsApp number - help', snap='Snapchat account - help', other='Account help')
ORDER = ['ig_disabled', 'ig_hacked', 'fb', 'username', 'ad', 'bm', 'page', 'tiktok', 'youtube', 'whatsapp', 'snap', 'other']
CASE_RE = re.compile(r'ban-service|report-|scammer|impersonat|fake-|harass|hate-page|usurpation|intimidatie|denunciar|melden|sextor')

def infer(path):
    s = path.lower()
    if 'snapchat' in s: return 'snap'
    if 'tiktok' in s: return 'tiktok'
    if 'youtube' in s: return 'youtube'
    if 'whatsapp' in s: return 'whatsapp'
    if re.search(r'username|gebruikersnaam|pseudo|nutzername|nome-utente|nome-de-usuario|nombre-de-usuario|kullanici-adi|one-letter|/og-|handle', s): return 'username'
    if re.search(r'business-portfolio|business-manager|business-suite', s): return 'bm'
    if re.search(r'ad-account|ads-|meta-ad|advertentie|publicit|pixel|werbekonto|anuncios|reklam', s): return 'ad'
    if re.search(r'facebook-page|page-recovery|pagina-facebook|page-facebook|facebookpagina|facebook-seite|-page-', s): return 'page'
    if 'instagram' in s: return 'ig_hacked' if re.search(r'hack|pirat|gehackt|hacke', s) else 'ig_disabled'
    if 'facebook' in s: return 'fb'
    return 'other'

def hero_kind(path, topic):
    if CASE_RE.search(path): return 'case'
    return {'username': 'username', 'ad': 'ad', 'bm': 'bm', 'page': 'page', 'youtube': 'youtube', 'whatsapp': 'whatsapp'}.get(topic, 'account')

def mailto(L, topic):
    hi, f_issue, f_user, f_country, bye = L['body']
    body = f"{hi}\n\n{f_issue}: {L['topics'][topic]}\n{f_user}: \n{f_country}: \n\n{bye}"
    return 'mailto:team@unbanz.com?subject=' + urllib.parse.quote(SUBJ[topic]) + '&body=' + urllib.parse.quote(body)

e = lambda x: html.escape(x, quote=True)
ARROW_LTR = ' <span aria-hidden="true">→</span>'
ARROW_RTL = ' <span aria-hidden="true">←</span>'

def blocks(L, path, topic, wa_href, is_dir, rtl=False):
    ARROW = ARROW_RTL if rtl else ARROW_LTR
    kind = hero_kind(path, topic)
    hero_btn = f'<a class="button button-light hx-start" href="{e(mailto(L, topic))}" data-topic="{topic}" data-hx="nov14">{e(L["hero"][kind])}{ARROW}</a>'
    order = [topic] + [t for t in ORDER if t != topic and t != 'other'] + (['other'] if topic != 'other' else [])
    opts = ''.join(f'<a class="hx-opt{" is-match" if t == topic else ""}" href="{e(mailto(L, t))}" data-topic="{t}">{e(L["topics"][t])}</a>' for t in order)
    trust = list(L['trust'])
    if topic == 'username': trust[2] = L['trust_user6']
    tl = ''.join(f'<li>{e(x)}</li>' for x in trust) + f'<li class="hx-rev"><a href="/reviews/">{e(L["reviews"])}</a></li>'
    indep = '' if is_dir else f'<p class="hx-indep">{e(L["indep"])}</p>'
    help_html = (f'<section class="hx-help container" aria-labelledby="hx-help-t" data-hx="nov14"><div class="hx-card">'
                 f'<div class="hx-head"><p class="eyebrow">{e(L["eyebrow"])}</p><h2 id="hx-help-t">{e(L["h2_user"] if topic == "username" else L["h2"])}</h2><p class="hx-sub">{e(L["sub"])}</p></div>'
                 f'<div class="hx-opts" role="list">{opts}</div><ul class="hx-trust">{tl}</ul>{indep}</div></section>')
    go = L['go_user'] if topic == 'username' else (L['go_case'] if kind == 'case' else L['go'])
    steps = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in L['steps'])
    wa = f'<a class="hx-wa" href="{e(wa_href)}">{e(L["wa"])} <span aria-hidden="true">↗︎</span></a>' if wa_href else ''
    steps_html = (f'<section class="hx-steps container" aria-labelledby="hx-steps-t" data-hx="nov14"><p class="eyebrow">{e(L["s_eyebrow"])}</p>'
                  f'<h2 id="hx-steps-t">{e(L["s_h2"])}</h2><ol class="hx-list">{steps}</ol>'
                  f'<div class="hx-cta"><a class="button button-blue hx-go" href="{e(mailto(L, topic))}" data-topic="{topic}">{e(go)}{ARROW}</a>{wa}</div>'
                  f'<p class="hx-mini">{e(L["mini"])}</p></section>')
    return hero_btn, help_html, steps_html

def strip_old(s):
    s = re.sub(r'<section class="hx-(?:help|steps) container"[^>]*data-hx="nov14".*?</section>', '', s, flags=re.S)
    s = re.sub(r'<div class="hero-cta hx-hero"><a class="button button-light hx-start"[^>]*>.*?</a></div>', '', s, flags=re.S)
    s = re.sub(r'<a class="button button-light hx-start"[^>]*>.*?</a>', '', s, flags=re.S)
    s = re.sub(r'<link rel="stylesheet" href="/assets/help-cta\.[0-9a-f]+\.css">', '', s)
    return s

def section_end(s, start):
    # end index of the <section ...> that begins at start (handles nested sections)
    depth, i = 0, start
    for m in re.finditer(r'<(/?)section\b', s[start:]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return start + m.start() + len('</section>')
    return -1

changed, skipped = [], {}
for p in sorted(ROOT.rglob('index.html')):
    parts = p.parts
    rel = '/'.join(parts[:-1])
    if parts[0] in SKIP_TOP or any(x in rel for x in SKIP_PARTS) or (parts[-2] if len(parts) > 1 else '').startswith(SKIP_PREFIX):
        skipped['rule'] = skipped.get('rule', 0) + 1; continue
    s0 = p.read_text(encoding='utf-8')
    if '<section class="service-hero' not in s0 or '<main' not in s0:
        skipped['template'] = skipped.get('template', 0) + 1; continue
    m = re.search(r'<html[^>]*\slang="([a-zA-Z]+)', s0)
    lang = LANGS.get((m.group(1) if m else 'en').lower()[:2])
    if not lang:
        skipped['lang'] = skipped.get('lang', 0) + 1; continue
    L = T[lang]
    s = strip_old(s0)
    path = '/' + rel + '/'
    topic = infer(path)
    hs = s.find('<section class="service-hero'); he = section_end(s, hs)
    hero = s[hs:he]
    wam = re.search(r'href="(https://wa\.me/[^"]+)"', hero) or re.search(r'href="(https://wa\.me/[^"]+)"', s)
    wa_href = html.unescape(wam.group(1)) if wam else 'https://wa.me/19342012490'
    is_dir = bool(re.search(r'director|links|liens|enlaces|links-oficiais|einspruch-links|appeal-links', path))
    hero_btn, help_html, steps_html = blocks(L, path, topic, wa_href, is_dir, lang == 'ar')
    # 1) hero button
    if '<div class="hero-cta">' in hero:
        hero2 = hero.replace('<div class="hero-cta">', '<div class="hero-cta">' + hero_btn, 1)
    else:
        k = hero.rfind('</div></section>')
        if k < 0: skipped['hero'] = skipped.get('hero', 0) + 1; continue
        hero2 = hero[:k] + '<div class="hero-cta hx-hero">' + hero_btn + '</div>' + hero[k:]
    s = s[:hs] + hero2 + s[he:]
    he = hs + len(hero2)
    # 2) help block: after answer-first section if it directly follows, else right after the hero
    pos = he
    nxt = s.find('<section', he)
    if nxt >= 0 and s.startswith('<section class="answer-first', nxt) and s[he:nxt].strip() == '':
        pos = section_end(s, nxt)
    s = s[:pos] + help_html + s[pos:]
    after = pos + len(help_html)
    # 3) steps block: before testimonials, else after the first guide-body article, else before FAQ, else before service-proof
    cands = []
    v = s.find('<section class="vt ', after)
    if v >= 0: cands.append(v)
    else:
        g = s.find('<article class="guide-body', after)
        if g >= 0:
            ge = s.find('</article>', g)
            if ge >= 0: cands.append(ge + len('</article>'))
        if not cands:
            f = s.find('<section class="faq-section', after)
            if f > after + 50: cands.append(f)
        if not cands:
            sp = s.find('<section class="service-proof', after)
            if sp >= 0: cands.append(sp)
    if cands:
        q = cands[0]
        s = s[:q] + steps_html + s[q:]
    # CSS
    s = s.replace('</head>', CSS_TAG + '</head>', 1)
    if s != s0:
        p.write_text(s, encoding='utf-8'); changed.append(path)
print('changed', len(changed), 'skipped', skipped)
pathlib.Path('scripts/nov14/changed_urls.txt').write_text('\n'.join('https://unbanz.com' + c for c in changed) + '\n')
