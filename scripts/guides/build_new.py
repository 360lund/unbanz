import re, json, html, glob, os, sys, importlib.util
sys.path.insert(0, '/workspace/site/scripts/guides')
from common import *

TEMPLATE_SLUG = 'instagram-account-locked'
DATE_ISO, DATE_TXT = '2026-10-24', '24 October 2026'
GROUP_SVC = {'instagram': ('/instagram-account-recovery/', 'Instagram account recovery', 'Instagram'),
             'facebook': ('/facebook-account-recovery/', 'Facebook account recovery', 'Facebook'),
             'ads': ('/ad-account-recovery/', 'Ad account recovery', None),
             'snapchat': ('/snapchat-unban-service/', 'Snapchat unban service', 'Snapchat')}

def smart(s):
    """curly apostrophes in text nodes only"""
    parts = re.split(r'(<[^>]*>)', s)
    for i, p in enumerate(parts):
        if not p.startswith('<'):
            p = re.sub(r"(?<=\w)'(?=\w)", '’', p)
            p = re.sub(r"(?<=s)'(?=\s)", '’', p)
            parts[i] = p
    return ''.join(parts)

def plain(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()

def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', plain(s).lower()).strip('-')[:40]

def load_guides():
    gs = []
    for f in sorted(glob.glob(ROOT + '/scripts/guides/content/g_*.py')):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        gs += m.GUIDES
    ex = {}
    for f in sorted(glob.glob(ROOT + '/scripts/guides/content/x_*.py')):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k, v in m.EXPAND.items():
            d = ex.setdefault(k, dict(secs=[], faq=[]))
            d['secs'] = d.get('secs', []) + v.get('secs', [])
            d['faq'] = d.get('faq', []) + v.get('faq', [])
            if 'intro' in v: d['intro'] = d.get('intro', '') + v['intro']
    for g in gs:
        e = ex.get(g['slug'])
        if not e: continue
        secs = list(g['secs'])
        i = [k for k, (sid, _, _) in enumerate(secs) if sid == 'dont'][0]
        secs[i:i] = e.get('secs', [])
        g['secs'] = secs
        g['faq'] = list(g['faq']) + e.get('faq', [])
        if 'intro' in e: g['intro'] = g['intro'] + ' ' + e['intro']
    return gs

def shell_parts():
    h = open(f'{ROOT}/guides/{TEMPLATE_SLUG}/index.html', encoding='utf-8').read()
    first_ld = h.find('<script type="application/ld+json">')
    org = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1)
    orgd = json.loads(org)
    nodes = [n for n in orgd['@graph'] if n['@type'] in ('Organization', 'WebSite')]
    for n in nodes:
        if n['@type'] == 'Organization':
            n['sameAs'] = [u for u in n['sameAs'] if 'trustpilot' not in u.lower()]
    # strip the Review-ish subjectOf link to reviews page? keep as is (video reviews page, no ratings)
    pre_head = h[:first_ld]
    after_ld = h.find('<link rel="preload"')
    mid = h[after_ld:h.find('<main id="content">') + len('<main id="content">')]
    post = h[h.find('</main>'):]
    return pre_head, nodes, mid, post

OLD_TITLE = 'Instagram Account Locked? Unlocking It Safely Explained'
OLD_DESC = 'Instagram says your account is locked for your safety or due to a possible hack? What the lock means and how to unlock it with official steps.'

def build_page(g, parts, css_name):
    pre_head, nodes, mid, post = parts
    slug = g['slug']; url = f'https://unbanz.com/guides/{slug}/'
    title = html.escape(g['mt'], quote=True); desc = html.escape(g['desc'], quote=True)
    ph = pre_head.replace(OLD_TITLE, g['mt'] if False else title).replace(OLD_DESC, desc)
    ph = ph.replace(f'https://unbanz.com/guides/{TEMPLATE_SLUG}/', url)
    # JSON-LD
    plat = g.get('plat')
    about = [{"@type": "Thing", "name": g['aboutname']}] if g.get('aboutname') else []
    art = {"@type": "Article", "@id": url + '#article', "headline": g['h1'], "description": g['desc'], "datePublished": DATE_ISO, "dateModified": DATE_ISO,
           "author": {"@type": "Organization", "name": "Unbanz team", "url": "https://unbanz.com/"}, "publisher": {"@id": "https://unbanz.com/#organization"},
           "image": "https://unbanz.com/assets/unbanz-share-v5.jpg",
           "mainEntityOfPage": {"@type": "WebPage", "@id": url, "url": url, "name": g['mt'], "breadcrumb": {"@id": url + '#breadcrumb'}},
           "inLanguage": "en", "isPartOf": {"@id": "https://unbanz.com/#website"}, "about": about}
    bc = {"@type": "BreadcrumbList", "@id": url + '#breadcrumb', "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://unbanz.com/"},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://unbanz.com/guides/"},
        {"@type": "ListItem", "position": 3, "name": g['h1'], "item": url}]}
    graph = {"@context": "https://schema.org", "@graph": nodes + [art, bc]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "@id": url + '#faq', "url": url,
           "mainEntity": [{"@type": "Question", "name": smart(q), "acceptedAnswer": {"@type": "Answer", "text": plain(smart(a))}} for q, a in g['faq']]}
    ld = ('<script type="application/ld+json">' + json.dumps(graph, ensure_ascii=False, separators=(',', ':')) + '</script>'
          '<script type="application/ld+json">' + json.dumps(faq, ensure_ascii=False, separators=(',', ':')) + '</script>')
    mid2 = re.sub(r'/assets/site\.[0-9a-f]{12}\.css', '/assets/' + css_name, mid)
    # CTA
    svc = g.get('svc', 'unban')
    cta = g['cta']  # dict kicker,title,text,wa,subject,top_wa
    top = top_cta(cta['top_wa'], cta['subject'], svc, plat)
    # sections
    body = ''.join(f'<h2 id="{sid}">{smart(h)}</h2>{smart(b)}' for sid, h, b in g['secs'])
    secs = convert_body(body)
    midcard = cta_card('mid', cta['kicker'], cta['title'], cta['text'], cta['wa'], cta['subject'], svc, plat)
    closecard = cta_card('close', cta['kicker2'], cta['title2'], cta['text2'], cta['wa2'], cta['subject'], svc, plat)
    secs.insert(min(3, len(secs)), midcard)
    toc_items = ''.join(f'<li><a href="#{sid}">{smart(re.sub(r"^(?:Step )?\d+[.:]\s*", "", h) if False else h)}</a></li>' for sid, h, _ in g['secs'])
    toc_items += '<li><a href="#faq">Frequently asked questions</a></li><li><a href="#sources">Official sources</a></li>'
    toc = toc_html('<ol>' + toc_items + '</ol>')
    src = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{html.escape(l)}</a></li>' for l, u in g['src'])
    sources = (f'<div class="guide-sources" id="sources"><h2>Official sources</h2><ul>{src}</ul><p>Meta and Snap update their help pages and flows often. '
               'Always follow the wording on your own screen and the current official Help Center. Unbanz is an independent service and is not affiliated with Meta, Instagram, Facebook or Snapchat.</p></div>')
    article = ('<article class="guide-body guide-v2 container">' + toc + '<div class="guide-main">' + ''.join(secs) + closecard + sources + '</div></article>')
    hero = ('<section class="service-hero"><div class="container"><a class="crumb" href="/guides/">Home / Guides</a>'
            f'<h1>{smart(html.escape(g["h1"], quote=False))}</h1><p class="quick-answer"><strong>Short answer:</strong> {smart(g["short"])}</p><p>{smart(g["intro"])}</p>'
            f'<p class="guide-meta">By the Unbanz team · Published <time datetime="{DATE_ISO}">{DATE_TXT}</time> · Updated <time datetime="{DATE_ISO}">{DATE_TXT}</time></p>{top}</div></section>')
    faqh = ''.join(f'<details><summary>{smart(q)}<span aria-hidden="true">+</span></summary><p>{smart(a)}</p></details>' for q, a in g['faq'])
    faqs = ('<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro"><p class="eyebrow">YOUR QUESTIONS</p><h2>Frequently asked questions</h2></div>'
            f'<div class="simple-faq">{faqh}</div></div></section>')
    gsvc = GROUP_SVC[g['group']]
    proof = ('<section class="service-proof container"><h2>Want it done for you?</h2><p>Want us to handle it? Get a quote and send us the details. Your password stays with you.</p>'
             f'<div class="cta-pair"><a class="button button-blue" href="{wa_link(cta["wa"])}"{attrs(svc, plat)}>Get a quote on WhatsApp <span aria-hidden="true">↗︎</span></a>'
             f'<a class="button button-light" href="{mail_link(cta["subject"])}">Email us</a></div></section>')
    pills = ''.join(f'<a href="{h}">{html.escape(l)}</a>' for h, l in g['rel'])
    pills += f'<a href="{gsvc[0]}">{gsvc[1]}</a><a href="/guides/">All guides</a><a href="/contact/">Contact</a>'
    rel = f'<nav class="related-services container" aria-label="Related pages"><p class="rel-label">Related guides</p>{pills}</nav>'
    return ph + ld + mid2 + hero + article + faqs + proof + rel + post

def wordcount(g):
    t = ' '.join([g['short'], g['intro']] + [h + ' ' + b for _, h, b in g['secs']] + [q + ' ' + a for q, a in g['faq']])
    return len(plain(t).split())

BAN = re.compile(r'\bcases?\b|we review|fixed.price|fast turnaround|guarantee|trustpilot|\bstars?\b|rating|bypass|evade|evasion', re.I)

def main():
    css_name = sorted(glob.glob(ROOT + '/assets/site.*.css'), key=os.path.getmtime)[-1].split('/')[-1]
    guides = load_guides()
    slugs = [g['slug'] for g in guides]
    assert len(set(slugs)) == len(slugs), 'dup slugs'
    sitemap = open(ROOT + '/sitemap.xml').read()
    known = set(re.findall(r'<loc>https://unbanz.com([^<]*)</loc>', sitemap)) | {f'/guides/{s}/' for s in slugs}
    parts = shell_parts()
    idx = []
    for g in guides:
        for h, _ in g['rel']:
            if not os.environ.get('SOFT'): assert h in known, (g['slug'], h)
        for h in g.get('inbound', []):
            assert h in known, (g['slug'], 'inbound', h)
        page = build_page(g, parts, css_name)
        t = re.sub(r'<script.*?</script>', '', page, flags=re.S)
        t = re.sub(r'<[^>]+>', ' ', t)
        t = t.replace('Independent service. Not affiliated with Meta.', '')
        bad = BAN.findall(t)
        if bad: print('BANNED', g['slug'], bad)
        d = f'{ROOT}/guides/{g["slug"]}'
        os.makedirs(d, exist_ok=True)
        open(d + '/index.html', 'w', encoding='utf-8').write(page)
        idx.append(dict(slug=g['slug'], h1=g['h1'], desc=g['desc'], group=g['group'], tag=g['tag'], inbound=g.get('inbound', []), sdesc=g['desc']))
        print(f'{wordcount(g):5d} {g["slug"]}')
    json.dump(idx, open(ROOT + '/scripts/guides/new_index.json', 'w'), ensure_ascii=False, indent=1)
    # sitemap
    add = ''
    for g in guides:
        loc = f'https://unbanz.com/guides/{g["slug"]}/'
        if loc not in sitemap:
            add += f'<url><loc>{loc}</loc><lastmod>2026-10-24</lastmod></url>\n'
    if add:
        sitemap = sitemap.replace('</urlset>', add + '</urlset>')
        open(ROOT + '/sitemap.xml', 'w').write(sitemap)
    # llms
    for fn, fmt in (('llms.txt', lambda g: f'- [{g["h1"]}](https://unbanz.com/guides/{g["slug"]}/): {g["desc"]}\n'),
                    ('llms-full.txt', lambda g: f'- {g["h1"]}: https://unbanz.com/guides/{g["slug"]}/\n')):
        s = open(f'{ROOT}/{fn}', encoding='utf-8').read()
        lines = ''.join(fmt(g) for g in guides if f'/guides/{g["slug"]}/' not in s)
        if not lines: continue
        marker = '\n## Optional\n' if fn == 'llms.txt' else '\n## Contact\n'
        i = s.index(marker)
        s = s[:i].rstrip('\n') + '\n' + lines + s[i:]
        open(f'{ROOT}/{fn}', 'w', encoding='utf-8').write(s)
    # inbound pills
    for g in guides:
        for href in g.get('inbound', []):
            p = ROOT + href + 'index.html'
            h = open(p, encoding='utf-8').read()
            new = f'/guides/{g["slug"]}/'
            if f'href="{new}"' in h: continue
            m = re.search(r'(<nav class="related-services[^>]*>.*?)(<a href="/guides/">All guides</a>|</nav>)', h, re.S)
            assert m, p
            label = g.get('pill') or g['h1']
            h = h[:m.end(1)] + f'<a href="{new}">{html.escape(label)}</a>' + h[m.end(1):]
            open(p, 'w', encoding='utf-8').write(h)
    print('guides', len(guides))

if __name__ == '__main__':
    main()
