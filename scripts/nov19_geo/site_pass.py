"""Nov 19 2026 site pass (idempotent):
1. Copy compliance: no 'guaranteed' timing, no 'contacts at Meta' (EN + NL).
2. hreflang clusters en-US / en-GB / en-CA / en-NL (+ existing language alternates).
3. og:locale on country pages; footer country links; NL title tweaks; hub links.
4. sitemap + llms entries for new pages."""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
B = 'https://unbanz.com/'
TODAY = '2026-11-19'
changed = set()

def rd(rel): return open(os.path.join(ROOT, rel), encoding='utf-8').read()
def wr(rel, s, old):
    if s != old:
        open(os.path.join(ROOT, rel), 'w', encoding='utf-8').write(s); changed.add(rel)

def all_files():
    for root, ds, fs in os.walk(ROOT):
        ds[:] = [d for d in ds if d not in ('.git', 'assets', 'scripts', 'node_modules', 'marketing', 'research', '.vercel', '.agents', 'api')]
        for f in fs:
            if f.endswith('.html') or f in ('llms.txt', 'llms-full.txt'):
                yield os.path.relpath(os.path.join(root, f), ROOT)

R = r'7[–-]14'
COMPLIANCE = [
 (r'Every case is guaranteed within (' + R + ') days', r'Most cases are done within \1 days'),
 (r'with a Guaranteed (' + R + ') days', r'usually done in \1 days'),
 (r'Guaranteed within (' + R + ') days', r'Usually within \1 days'),
 (r'guaranteed within (' + R + ') days', r'usually within \1 days'),
 (r'Guaranteed (' + R + ') days', r'Usually \1 days'),
 (r'guaranteed (' + R + ') days', r'usually \1 days'),
 (r'Gegarandeerd binnen (' + R + ') dagen', r'Meestal binnen \1 dagen'),
 (r'gegarandeerd binnen (' + R + ') dagen', r'meestal binnen \1 dagen'),
 # Meta-contacts lines (user decision Nov 18: never claim Meta contacts or partnership)
 (r' For Facebook and Instagram cases we work through our contacts at Meta, and Meta makes the final decision\.', ' Meta makes the final decision.'),
 (r' For Facebook and Instagram cases we work through our contacts at Meta, with payment upfront and a 100% refund if it fails\.', ' Payment is upfront, with a 100% refund if it fails.'),
 (r' For Facebook and Instagram cases we work through our contacts at Meta, alongside the official routes\.', ' We work through the official routes.'),
 (r' For Facebook and Instagram cases we (?:also )?work through our contacts at Meta\.', ''),
 (r' For Instagram and Facebook cases it works through contacts at Meta alongside the standard reports and processes\.', ' It works through the standard reports and processes.'),
 (r' Works through contacts at Meta for Facebook and Instagram cases\.', ''),
 (r' and, for (?:Instagram and Facebook|Facebook and Instagram) cases, (?:our|its) contacts at Meta', ''),
 (r"(through Meta[’'\\u2019]+s official channels) and our contacts at Meta", r'\1'),
 (r'through the official process and our contacts at Meta', 'through the official process'),
 (r'; for Facebook and Instagram cases (?:we work|it works) through (?:our )?contacts at Meta', ''),
 (r', but for Instagram and Facebook cases we work through our contacts at Meta, and we know', ', but we know'),
 (r'take on the case through our contacts at Meta', 'take on the case through the official routes'),
 (r', en bij Facebook- en Instagram-zaken werken we via onze contacten bij Meta\.', '.'),
 (r' Bij Facebook- en Instagram-zaken werken we via onze contacten bij Meta; je betaalt', ' Je betaalt'),
 (r' Bij Facebook- en Instagram-zaken werken we via onze contacten bij Meta\.', ''),
 (r'; bij Facebook- en Instagram-zaken werkt Unbanz via eigen contacten bij Meta\.', '.'),
 (r'Unbanz werkt bij Facebook- en Instagram-zaken via eigen contacten bij Meta, zonder officiële band en zonder garantie op resultaat\.', 'Unbanz werkt via de officiële routes van Meta, zonder officiële band met Meta en zonder garantie op resultaat.'),
]
COMP = [(re.compile(a), b) for a, b in COMPLIANCE]

CLUSTERS = [
 ('instagram-account-recovery', {'en-US': 'instagram-account-recovery-usa', 'en-GB': 'instagram-account-recovery-uk', 'en-CA': 'instagram-account-recovery-canada', 'en-NL': 'instagram-account-recovery-netherlands'}),
 ('facebook-account-recovery', {'en-US': 'facebook-account-recovery-usa', 'en-GB': 'facebook-account-recovery-uk', 'en-CA': 'facebook-account-recovery-canada', 'en-NL': 'facebook-account-recovery-netherlands'}),
 ('instagram-hacked-account-recovery-service', {'en-US': 'instagram-hacked-usa-what-to-do', 'en-GB': 'instagram-hacked-uk-what-to-do', 'en-CA': 'instagram-hacked-canada-what-to-do', 'en-NL': 'instagram-hacked-netherlands-what-to-do'}),
 ('guides/hacked-facebook-account-recovery', {'en-US': 'facebook-hacked-usa-what-to-do', 'en-GB': 'facebook-hacked-uk-what-to-do', 'en-CA': 'facebook-hacked-canada-what-to-do', 'en-NL': 'facebook-hacked-netherlands-what-to-do'}),
 ('instagram-account-disabled-appeal', {'en-US': 'instagram-disabled-usa-what-to-do', 'en-GB': 'instagram-disabled-uk-what-to-do', 'en-CA': 'instagram-disabled-canada-what-to-do', 'en-NL': 'instagram-account-suspended-netherlands-what-to-do'}),
 ('guides/facebook-account-disabled-appeal', {'en-US': 'facebook-account-disabled-usa-what-to-do', 'en-GB': 'facebook-account-disabled-uk-what-to-do', 'en-CA': 'facebook-account-disabled-canada-what-to-do', 'en-NL': 'facebook-account-disabled-netherlands-what-to-do'}),
 ('meta-appeal-links-and-forms-directory', {'en-US': 'meta-appeal-links-usa', 'en-GB': 'meta-appeal-links-uk', 'en-CA': 'meta-appeal-links-canada', 'en-NL': 'meta-appeal-links-netherlands'}),
 ('instagram-username-claim', {'en-US': 'instagram-username-claim-usa', 'en-GB': 'instagram-username-claim-uk', 'en-CA': 'instagram-username-claim-canada', 'en-NL': 'instagram-username-claim-netherlands'}),
 ('tiktok-account-banned-how-to-get-it-back', {'en-US': 'tiktok-account-banned-usa', 'en-GB': 'tiktok-account-banned-uk', 'en-CA': 'tiktok-account-banned-canada'}),
 ('whatsapp-banned-number', {'en-US': 'whatsapp-banned-usa', 'en-GB': 'whatsapp-banned-uk', 'en-CA': 'whatsapp-banned-canada', 'nl': 'nl/whatsapp-account-geblokkeerd', 'nl-NL': 'nl/whatsapp-account-geblokkeerd'}),
]
LINK = re.compile(r'<link href="([^"]+)" hreflang="([^"]+)" rel="alternate"/>')
def head_links(s):
    h = s[:s.index('</head>')]
    return LINK.findall(h)
def set_links(s, pairs):
    h_end = s.index('</head>'); h = s[:h_end]
    h = LINK.sub('', h)
    canon = re.search(r'<link href="[^"]+" rel="canonical"/>', h)
    tags = ''.join(f'<link href="{u}" hreflang="{l}" rel="alternate"/>' for u, l in pairs)
    h = h[:canon.end()] + tags + h[canon.end():]
    return h + s[h_end:]

def do_clusters():
    seen = {}
    for gen, cmap in CLUSTERS:
        gs = rd(gen + '/index.html')
        base = [(u, l) for u, l in head_links(gs) if l not in ('en-US', 'en-GB', 'en-CA', 'en-NL', 'x-default') and not (l == 'en' and u != B + gen + '/')]
        if not any(l == 'en' for _, l in base): base.insert(0, (B + gen + '/', 'en'))
        for l, slug in cmap.items():
            base = [(u, ll) for u, ll in base if ll != l]
            base.append((B + slug + '/', l))
        # order: en, country variants, other languages, x-default
        order = {'en': 0, 'en-US': 1, 'en-GB': 2, 'en-CA': 3, 'en-NL': 4}
        base.sort(key=lambda x: order.get(x[1], 10))
        base.append((B + gen + '/', 'x-default'))
        members = []
        for u, _ in base:
            if u not in members: members.append(u)
        for u in members:
            rel = u[len(B):] + 'index.html'
            if u in seen and seen[u] != gen: print('WARN member in two clusters', u, seen[u], gen)
            seen[u] = gen
            if not os.path.exists(os.path.join(ROOT, rel)): print('WARN missing', rel); continue
            s = rd(rel); wr(rel, set_links(s, base), s)
        print('cluster', gen, len(base), 'links', len(members), 'pages')

OGL = [('-uk', 'en_GB'), ('-uk-what-to-do', 'en_GB'), ('-canada', 'en_CA'), ('-canada-what-to-do', 'en_CA')]
def og_locale(rel, s):
    slug = rel[:-len('/index.html')] if rel.endswith('/index.html') else ''
    loc = None
    if re.search(r'-(uk)(-|$)', slug) and not re.search(r'(usa|eu|australia)', slug): loc = 'en_GB'
    elif re.search(r'-canada(-|$)', slug) and 'australia' not in slug and 'usa' not in slug: loc = 'en_CA'
    elif slug.startswith('nl/') or slug == 'nl': loc = 'nl_NL'
    if loc:
        s = re.sub(r'<meta content="[^"]*" property="og:locale"/>', f'<meta content="{loc}" property="og:locale"/>', s, count=1)
    return s

FOOT_OLD = '<a href="/meta-appeal-links-and-forms-directory/">Appeal links</a>'
FOOT_NEW = FOOT_OLD + '<a href="/us/">USA help</a><a href="/uk/">UK help</a><a href="/ca/">Canada help</a>'

NL_TITLES = {
 'nl/instagram-account-terugkrijgen/index.html': ('Instagram account terugkrijgen na uitschakeling of hack', 'Instagram account herstellen of terugkrijgen na blokkade of hack'),
 'nl/facebook-account-terugkrijgen/index.html': ('Facebook account terugkrijgen: uitgeschakeld of gehackt', 'Facebook account herstellen: uitgeschakeld of gehackt'),
 'nl/instagram-account-gehackt/index.html': ('Instagram-account gehackt: zo krijg je het terug | Unbanz', 'Instagram gehackt? Wat nu en zo herstel je je account | Unbanz'),
 'nl/facebook-account-gehackt/index.html': ('Facebook-account gehackt: wat moet je doen? | Unbanz', 'Facebook gehackt? Wat nu en zo herstel je je account | Unbanz'),
}

def main():
    leftovers = {'guarantee_timing': 0, 'meta_contacts': 0}
    for rel in all_files():
        s = rd(rel); old = s
        for rx, rep in COMP: s = rx.sub(rep, s)
        if rel.endswith('.html'):
            s = og_locale(rel, s)
            if '<html lang="en"' in s and FOOT_OLD in s and '/us/">USA help' not in s:
                s = s.replace(FOOT_OLD, FOOT_NEW, 1)
        if rel in NL_TITLES:
            a, b = NL_TITLES[rel]; s = s.replace(a, b)
        wr(rel, s, old)
        if re.search(r'[Gg]uaranteed? (?:within )?' + R + ' days|[Gg]egarandeerd binnen', s): leftovers['guarantee_timing'] += 1
        if re.search(r'contacts? at Meta|contacten bij Meta', s): leftovers['meta_contacts'] += 1
    print('leftovers', leftovers)
    do_clusters()
    # hub links on country index + NL home
    rel = 'account-recovery-by-country/index.html'; s = rd(rel); old = s
    if 'href="/us/"' not in s:
        s = s.replace('</h1>', '</h1><p class="guide-meta">Country hubs: <a href="/us/">USA</a> · <a href="/uk/">UK</a> · <a href="/ca/">Canada</a> · <a href="/nl/">Nederland</a></p>', 1)
    wr(rel, s, old)
    rel = 'nl/index.html'; s = rd(rel); old = s
    if 'whatsapp-account-geblokkeerd' not in s:
        s = s.replace('<a href="/nl/officiele-links-whatsapp-nummer-geblokkeerd/">WhatsApp-nummer geblokkeerd</a>', '<a href="/nl/officiele-links-whatsapp-nummer-geblokkeerd/">WhatsApp-nummer geblokkeerd</a><a href="/nl/whatsapp-account-geblokkeerd/">WhatsApp-account geblokkeerd of beperkt</a>', 1)
    wr(rel, s, old)
    print('nl home linked', 'whatsapp-account-geblokkeerd' in rd('nl/index.html'))
    # cross links from existing generic pages to new country pages
    for gen, pairs in [('tiktok-account-banned-how-to-get-it-back', [('tiktok-account-banned-usa', 'Banned in the USA'), ('tiktok-account-banned-uk', 'Banned in the UK'), ('tiktok-account-banned-canada', 'Banned in Canada')]),
                       ('whatsapp-banned-number', [('whatsapp-banned-usa', 'Banned in the USA'), ('whatsapp-banned-uk', 'Banned in the UK'), ('whatsapp-banned-canada', 'Banned in Canada'), ('nl/whatsapp-account-geblokkeerd', 'Nederlands')])]:
        rel = gen + '/index.html'; s = rd(rel); old = s
        if f'href="/{pairs[0][0]}/"' not in s:
            nav = '<nav aria-label="By country" class="related-services container">' + ''.join(f'<a href="/{a}/">{b}</a>' for a, b in pairs) + '</nav>'
            s = s.replace('</main>', nav + '</main>', 1)
        wr(rel, s, old)
    # country pages -> hubs
    for suffix, hub, label in [('-usa', 'us', 'All USA guides'), ('-uk', 'uk', 'All UK guides'), ('-canada', 'ca', 'All Canada guides')]:
        for rel in [f for f in os.listdir(ROOT) if f.endswith(suffix) or f.endswith(suffix + '-what-to-do')]:
            p = rel + '/index.html'
            if not os.path.exists(os.path.join(ROOT, p)): continue
            s = rd(p); old = s
            if f'href="/{hub}/"' not in s and '</main>' in s:
                s = s.replace('</main>', f'<nav aria-label="Country hub" class="related-services container"><a href="/{hub}/">{label}</a><a href="/account-recovery-by-country/">Recovery by country</a></nav></main>', 1)
            wr(p, s, old)
    # sitemaps
    sys.path.insert(0, os.path.dirname(__file__)); from content import PAGES
    new = [p['slug'] for p in PAGES]
    for sm in ('sitemap.xml', 'sitemap-en.xml', 'sitemap-intl.xml'):
        s = rd(sm); old = s
        for slug in new:
            if sm == 'sitemap-en.xml' and slug.startswith('nl/'): continue
            if sm == 'sitemap-intl.xml' and not slug.startswith('nl/'): continue
            loc = f'<loc>{B}{slug}/</loc>'
            if loc not in s:
                s = s.replace('</urlset>', f'<url>{loc}<lastmod>{TODAY}</lastmod></url>\n</urlset>')
        # bump lastmod for changed pages
        def bump(m):
            u = m.group(1); rel = u[len(B):] + 'index.html' if u != B else 'index.html'
            return f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>' if rel in changed else m.group(0)
        s = re.sub(r'<url><loc>([^<]+)</loc><lastmod>[^<]+</lastmod></url>', bump, s)
        wr(sm, s, old)
    s = rd('sitemap-index.xml'); wr('sitemap-index.xml', re.sub(r'<lastmod>[^<]+</lastmod>', f'<lastmod>{TODAY}</lastmod>', s), s)
    # llms
    block = ('\n## Country hubs (Nov 19 2026)\n'
             f'- USA: {B}us/ (TikTok: {B}tiktok-account-banned-usa/, WhatsApp: {B}whatsapp-banned-usa/)\n'
             f'- UK: {B}uk/ (TikTok: {B}tiktok-account-banned-uk/, WhatsApp: {B}whatsapp-banned-uk/)\n'
             f'- Canada: {B}ca/ (TikTok: {B}tiktok-account-banned-canada/, WhatsApp: {B}whatsapp-banned-canada/)\n'
             f'- Netherlands (Dutch): {B}nl/ (WhatsApp geblokkeerd: {B}nl/whatsapp-account-geblokkeerd/)\n'
             '- Timing: usually 7–14 days once work starts, full refund if not reinstated within 14 days. The platform makes the final decision. Unbanz is independent and not affiliated with Meta, TikTok or WhatsApp.\n')
    for f in ('llms.txt', 'llms-full.txt'):
        s = rd(f); old = s
        if '## Country hubs (Nov 19 2026)' not in s: s = s.rstrip('\n') + '\n' + block
        wr(f, s, old)
    open(os.path.join(ROOT, 'scripts/nov19_geo/changed.txt'), 'w').write('\n'.join(sorted(changed)) + '\n')
    print('changed files', len(changed))

if __name__ == '__main__':
    main()
