#!/usr/bin/env python3
"""Patch the 74 older 'Short answer' layout pages in place: same hero / answer-first / 3-card block as the original service
pages (oct28d_top.top_v2) with hand-written per-page cards (oct28f_cards.CARDS). Idempotent."""
import html, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import oct28d_top as T2
from oct28f_cards import CARDS
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RX = re.compile(r'<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="/">Home / (?P<crumb>.*?)</a><h1>(?P<h1>.*?)</h1><p>(?P<hero>.*?)</p>'
  r'<div class="hero-cta"><a class="button button-light" href="(?P<wa>[^"]*)"[^>]*>[^<]*<span aria-hidden="true">↗︎</span></a><a class="hero-email" href="(?P<mail>[^"]*)">Prefer email\? ↗︎</a></div></div></section>'
  r'<article class="guide-body container"><h2 id="answer">Short answer</h2><p>(?P<ans>.*?)</p>', re.S)
def service(slug, wa):
    if 'claim%20this%20username' in wa: return 'username'
    if any(k in slug for k in ('ad-account', 'ads-account', 'business-manager', 'meta-business', 'agency')): return 'ad'
    return 'unban'
if __name__ == '__main__':
    n = 0
    for slug in CARDS:
        f = os.path.join(ROOT, slug, 'index.html')
        t = open(f, encoding='utf-8').read()
        if 'class="answer-first container"' in t.split('<article class="guide-body')[0]: continue
        m = RX.search(t); assert m, slug
        assert '<' not in m['h1'], slug
        ans = re.sub(r'<[^>]+>', '', m['ans'])
        top = T2.top_v2(h1=html.unescape(m['h1']), hero_html=m['hero'], wa=m['wa'], ws=service(slug, m['wa']), mail=m['mail'],
                        answer=html.unescape(ans), cards=CARDS[slug])
        t = t[:m.start()] + top + '<article class="guide-body container">' + t[m.end():]
        open(f, 'w', encoding='utf-8').write(t); n += 1
    print('patched', n, 'of', len(CARDS))
