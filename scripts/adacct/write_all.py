# -*- coding: utf-8 -*-
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import os, re, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hub
from lib import ROOT, DATE, build
import native
pages = hub.all_pages()
_twin = {v: k for k, v in native.EN.items()}
for p in pages:
    if p['slug'] in _twin: p['alts'] = native.alts_for(_twin[p['slug']])
out = []
for p in pages:
    d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True)
    write_page(os.path.join(d, 'index.html'), build(p))
    out.append(p['slug'])
print('wrote', len(out))
open('/tmp/adacct_new_slugs.txt', 'w').write('\n'.join(out))

# sitemap
sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
add = ''
for s in out:
    u = 'https://unbanz.com/%s/' % s
    if '<loc>%s</loc>' % u not in sm:
        add += '<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE)
sm = sm.replace('</urlset>', add + '</urlset>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)

# llms.txt / llms-full.txt
def first_sentence(t): return t
lt = open(os.path.join(ROOT, 'llms.txt'), encoding='utf-8').read()
if 'Meta ad account help' not in lt or 'meta-ad-account-help' not in lt:
    lines = ['## Meta ad account help', '',
             'Independent help with disabled, restricted and rejected Meta ad accounts and business portfolios. Hub: https://unbanz.com/meta-ad-account-help/ . Meta makes the final decision on every review.', '']
    for p in pages:
        lines.append('- [%s](https://unbanz.com/%s/): %s' % (p['title'], p['slug'], p['desc']))
    block = '\n'.join(lines) + '\n\n'
    lt = lt.replace('## Guides\n', block + '## Guides\n', 1)
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write(lt)
lf = open(os.path.join(ROOT, 'llms-full.txt'), encoding='utf-8').read()
if 'meta-ad-account-help/' not in lf:
    lines = ['## Meta ad account help', '']
    for p in pages:
        lines += ['### %s' % p['title'], '', 'Source: https://unbanz.com/%s/' % p['slug'], '', p['answer'], '']
        for q, a in p['faq'][:2]:
            lines.append('%s %s' % (q, a))
        lines.append('')
    block = '\n'.join(lines) + '\n'
    marker = '## Username claims: quick answers'
    assert marker in lf
    lf = lf.replace(marker, block + marker, 1)
    open(os.path.join(ROOT, 'llms-full.txt'), 'w', encoding='utf-8').write(lf)

# native pages
native_paths = native.pages()
for lk in native.LANGS:
    for t in native.TOPICS:
        p = native.path(lk, t); os.makedirs(os.path.join(ROOT, p), exist_ok=True)
        write_page(os.path.join(ROOT, p, 'index.html'), native.build(lk, t))
print('native', len(native_paths))
open('/tmp/adacct_native_paths.txt', 'w').write('\n'.join(native_paths))
sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read(); add = ''
for pth in native_paths:
    u = 'https://unbanz.com/%s/' % pth
    if '<loc>%s</loc>' % u not in sm: add += '<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE)
sm = sm.replace('</urlset>', add + '</urlset>'); open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
lt = open(os.path.join(ROOT, 'llms.txt'), encoding='utf-8').read()
heads = {'fr': '## Français (France)', 'nl': '## Nederlands (Nederland)', 'es': '## Español (España)', 'pt-br': '## Português (Brasil)'}
for lk, hd in heads.items():
    lines = ''
    for t in native.TOPICS:
        d = native.LANGS[lk][0].T[t]; u = 'https://unbanz.com/%s/' % native.path(lk, t)
        if u not in lt: lines += '- [%s](%s): %s\n' % (d['title'], u, d['desc'])
    if not lines: continue
    i = lt.index(hd); j = lt.find('\n## ', i + 5)
    if j == -1: lt = lt.rstrip('\n') + '\n' + lines
    else: lt = lt[:j].rstrip('\n') + '\n' + lines + lt[j:]
open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write(lt)
lf = open(os.path.join(ROOT, 'llms-full.txt'), encoding='utf-8').read()
if 'Meta ad account help (native' not in lf:
    out = ['## Meta ad account help (native languages)', '']
    for lk in native.LANGS:
        for t in native.TOPICS:
            d = native.LANGS[lk][0].T[t]
            out += ['### %s' % d['title'], '', 'Source: https://unbanz.com/%s/' % native.path(lk, t), '', d['answer'], '']
    marker = '## Username claims: quick answers'
    lf = lf.replace(marker, '\n'.join(out) + '\n' + marker, 1)
    open(os.path.join(ROOT, 'llms-full.txt'), 'w', encoding='utf-8').write(lf)
# link new natives from the existing native core ad pages
for lk, core in native.CORE.items():
    f = os.path.join(ROOT, core, 'index.html'); s = open(f, encoding='utf-8').read()
    if native.path(lk, 'payment') in s: continue
    items = ''.join('<a href="/%s/">%s</a>' % (native.path(lk, t), native.esc(native.LANGS[lk][0].T[t]['title'])) for t in native.TOPICS)
    s = s.replace('</nav></main>', items + '</nav></main>', 1) if False else re.sub(r'(<nav class="related-services container"[^>]*>)', lambda m: m.group(1) + items, s, 1)
    open(f, 'w', encoding='utf-8').write(s)
# keep in step with the agency integration: "For agencies" link in the desktop nav of the new EN pages
_nav = '<a href="/pricing/">Pricing</a><a href="/contact/">Contact</a></nav>'
for sl in open('/tmp/adacct_new_slugs.txt').read().split():
    fp = os.path.join(ROOT, sl, 'index.html'); t = open(fp, encoding='utf-8').read()
    if _nav in t and '/white-label-agency/">For agencies' not in t:
        t = t.replace(_nav, '<a href="/pricing/">Pricing</a><a href="/white-label-agency/">For agencies</a><a href="/contact/">Contact</a></nav>', 1)
        open(fp, 'w', encoding='utf-8').write(t)
