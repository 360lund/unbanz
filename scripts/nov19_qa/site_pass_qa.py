"""Nov 19 2026: link Q&A pages from hubs / NL FAQ, add sitemap + llms entries."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_qa import PAGES, ROOT, TODAY
B = 'https://unbanz.com/'
def rd(f): return open(os.path.join(ROOT, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(ROOT, f), 'w', encoding='utf-8').write(s)
by = {}
for p in PAGES: by.setdefault(p['locale'], []).append(p)
MARK = 'id="questions"'
for loc, hub, label in (('en-US', 'us', 'Questions people ask in the US'), ('en-GB', 'uk', 'Questions people ask in the UK'), ('en-CA', 'ca', 'Questions people ask in Canada')):
    f = f'{hub}/index.html'; s = rd(f)
    if MARK in s: continue
    block = f'<h2 id="questions">{label}</h2><p>Short, direct answers to the questions we see most, with official links for each.</p><ul>' + ''.join(f'<li><a href="/{p["slug"]}/">{p["q"]}</a></li>' for p in by[loc]) + '</ul>'
    s = s.replace('<h2 id="instagram">', block + '<h2 id="instagram">', 1)
    s = s.replace('<p>On this page</p><a href="#instagram">', '<p>On this page</p><a href="#questions">Questions people ask</a><a href="#instagram">', 1)
    s = re.sub(r'<meta content="[^"]*" property="article:modified_time"/>', f'<meta content="{TODAY}" property="article:modified_time"/>', s)
    wr(f, s)
# NL FAQ page
f = 'nl/veelgestelde-vragen/index.html'; s = rd(f)
if 'id="vragen-nl"' not in s:
    block = ('<section class="answer-first container" id="vragen-nl" style="padding-top:48px"><p class="eyebrow">VRAGEN UIT NEDERLAND</p><h2>Losse vragen, met een direct antwoord</h2><ul>'
             + ''.join(f'<li><a href="/{p["slug"]}/">{p["q"]}</a></li>' for p in by['nl-NL']) + '</ul></section>')
    s = s.replace('<section class="faq-section" id="faq">', block + '<section class="faq-section" id="faq">', 1)
    wr(f, s)
f = 'nl/whatsapp-account-geblokkeerd/index.html'; s = rd(f)
if 'waarom-wordt-mijn-whatsapp-geblokkeerd' not in s:
    s = s.replace('<a href="/nl/contact/">Contact</a></nav>', '<a href="/nl/waarom-wordt-mijn-whatsapp-geblokkeerd/">Waarom geblokkeerd?</a><a href="/nl/hoe-lang-blijft-whatsapp-geblokkeerd/">Hoe lang geblokkeerd?</a><a href="/nl/contact/">Contact</a></nav>', 1)
    wr(f, s)
# sitemaps
for sm in ('sitemap.xml', 'sitemap-en.xml', 'sitemap-intl.xml'):
    s = rd(sm); add = ''
    for p in PAGES:
        nl = p['slug'].startswith('nl/')
        if sm == 'sitemap-en.xml' and nl: continue
        if sm == 'sitemap-intl.xml' and not nl: continue
        u = B + p['slug'] + '/'
        if f'<loc>{u}</loc>' not in s: add += f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n'
    for hubu in ('us/', 'uk/', 'ca/', 'nl/veelgestelde-vragen/'):
        s = re.sub(r'(<loc>' + re.escape(B + hubu) + r'</loc><lastmod>)[^<]+', r'\g<1>' + TODAY, s)
    s = s.replace('</urlset>', add + '</urlset>', 1); wr(sm, s)
s = rd('sitemap-index.xml'); wr('sitemap-index.xml', re.sub(r'<lastmod>[^<]+</lastmod>', f'<lastmod>{TODAY}</lastmod>', s))
# llms
blk = '\n## Country questions and answers (Nov 19 2026)\n'
for loc, name in (('en-US', 'USA'), ('en-GB', 'UK'), ('en-CA', 'Canada'), ('nl-NL', 'Netherlands (Dutch)')):
    blk += f'### {name}\n' + ''.join(f'- [{p["q"]}]({B}{p["slug"]}/): {p["desc"]}\n' for p in by[loc])
for f in ('llms.txt', 'llms-full.txt'):
    s = rd(f)
    if 'Country questions and answers (Nov 19 2026)' not in s:
        wr(f, s.rstrip('\n') + '\n' + blk)
print('ok')
