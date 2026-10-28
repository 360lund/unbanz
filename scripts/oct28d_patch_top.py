#!/usr/bin/env python3
"""Patch the already-built extra pages in place: swap the plain guide-style top (hero + 'Short answer') for the same
hero / answer-first / 3-card block used by the original service pages. Idempotent. Mirrors build_oct25_pages.build(v2)."""
import html, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import oct28d_top as T2
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SLUGS = [l.strip() for l in open(os.path.join(os.path.dirname(__file__), 'oct28d_targets.txt')) if l.strip()]
RX = re.compile(r'<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="/">Home / (?P<crumb>.*?)</a><h1>(?P<h1>.*?)</h1><p>(?P<hero>.*?)</p>'
  r'<div class="hero-cta"><a class="button button-light" href="(?P<wa>[^"]*)"[^>]*>[^<]*<span aria-hidden="true">↗︎</span></a><a class="hero-email" href="(?P<mail>[^"]*)">Prefer email\? ↗︎</a></div></div></section>'
  r'<article class="guide-body container"><h2 id="answer">Short answer</h2><p>(?P<ans>.*?)</p>', re.S)
n = 0
for slug in SLUGS:
    f = os.path.join(ROOT, slug, 'index.html')
    t = open(f, encoding='utf-8').read()
    if 'class="answer-first container"' in t.split('<article class="guide-body')[0]:
        continue
    m = RX.search(t)
    assert m, slug
    h1 = T2.H1.get(slug, html.unescape(m['h1']))
    ws = 'username' if 'claim%20this%20username' in m['wa'] else 'unban'
    top = T2.top_v2(h1=h1, hero_html=m['hero'], wa=m['wa'], ws=ws, mail=m['mail'], answer=html.unescape(m['ans']),
                    cards=T2.cards_for(slug, h1))
    t = t[:m.start()] + top + '<article class="guide-body container">' + t[m.end():]
    open(f, 'w', encoding='utf-8').write(t); n += 1
print('patched', n, 'of', len(SLUGS))
