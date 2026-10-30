# -*- coding: utf-8 -*-
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page
import os, sys, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'dd29'))
import lib
lib.DATE = '2026-10-30'; lib.DATE_LONG = '30 October 2026'
from c_oct30 import *
from lib import ROOT, FAM, esc
C = {'US': 'United States', 'GB': 'United Kingdom', 'CA': 'Canada', 'AU': 'Australia', 'AE': 'United Arab Emirates', 'SA': 'Saudi Arabia', 'QA': 'Qatar'}
EU = ['France', 'Germany', 'Netherlands', 'Ireland', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Austria', 'Italy', 'Spain', 'Poland']
TERMS = 'Terms are agreed with you before any work starts.'
def area(a):
    out = []
    for x in (a if isinstance(a, list) else [a]):
        out += [{'@type': 'Country', 'name': n} for n in (EU if x == 'EU' else [C[x]])]
    return out
_hb = lib.how_block
def how_block(p):
    s = _hb(p); old = 'We tell you honestly whether this is something we can help with.'
    assert old in s
    return s.replace(old, old + ' ' + TERMS)
lib.how_block = how_block
TR = set(l.split('/')[0] for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n') if l)
def exists(u): return os.path.exists(os.path.join(ROOT, u.strip('/'), 'index.html')) or u.strip('/') in [p['slug'] for p in PAGES]
def L(p): return ('/%s/' % p['slug'], p['crumb'])
WIN = [('/guides/instagram-account-suspended-appeal/', 'Instagram suspended: how to appeal'), ('/guides/instagram-disabled-no-appeal-button/', 'No appeal button'),
       ('/guides/instagram-id-verification-request/', 'ID verification request'), ('/guides/facebook-account-disabled-appeal/', 'Facebook disabled appeal'),
       ('/guides/facebook-lost-access-to-email-or-phone/', 'Lost access to email or phone'), ('/inactive-instagram-username/', 'Inactive usernames')]
EXTRA = {'instagram-disabled-canada-what-to-do': ['/instagram-account-recovery-canada/', '/instagram-disabled-usa-what-to-do/'],
         'instagram-disabled-australia-what-to-do': ['/instagram-account-recovery-australia/', '/instagram-disabled-uk-what-to-do/'],
         'instagram-disabled-uae-what-to-do': ['/instagram-account-recovery-uae/', '/meta-ad-account-disabled-uae/'],
         'instagram-no-appeal-button-eu-uk-routes': ['/instagram-disabled-eu-what-to-do/', '/dsa-appeal-right-instagram-facebook/'],
         'facebook-account-disabled-uk-what-to-do': ['/facebook-ad-account-disabled-uk/', '/your-rights-when-meta-disables-your-account/'],
         'facebook-account-disabled-usa-what-to-do': ['/report-hacked-account-police-action-fraud-ic3/', '/facebook-ad-account-restricted-us-business/'],
         'instagram-username-claim-saudi-arabia': ['/instagram-username-claim-uae/', '/instagram-account-recovery-saudi-arabia/'],
         'instagram-username-claim-qatar': ['/instagram-username-claim-uae/', '/instagram-account-recovery-qatar/']}
def title_of(u):
    f = os.path.join(ROOT, u.strip('/'), 'index.html')
    m = re.search(r'<title>([^<|]*)', open(f, encoding='utf-8').read()); return m.group(1).strip().split(':')[0]
def main():
    for p in PAGES:
        if p['slug'] in TR: raise SystemExit('COLLISION ' + p['slug'])
        p['area'] = area(p['area'])
    bad = set()
    for p in PAGES:
        for s in p['sections']:
            for u in re.findall(r'href="(/[^"]*)"', s):
                if not exists(u): bad.add((p['slug'], u))
        for u in EXTRA[p['slug']]:
            if not exists(u): bad.add((p['slug'], u))
    if bad: raise SystemExit('BROKEN %s' % sorted(bad))
    for p in PAGES:
        F = FAM[p['fam']]
        sib = [L(q) for q in PAGES if q is not p and FAM[q['fam']]['ws'] == F['ws']] or [L(q) for q in PAGES if q is not p]
        rel = [F['parent']] + [(u, title_of(u)) for u in EXTRA[p['slug']]] + sib[:4]
        relq = WIN[:4] + [('/how-it-works/', 'How Unbanz works'), ('/white-label-agency/', 'For agencies')]
        p['related_final'] = (rel, relq)
        h = lib.build(p, None)
        assert TERMS in h and 'Not affiliated with Meta' in h and 'wa.me/19342012490' in h and '447723' not in h.replace(' ', '')
        d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
    def nav(label, links): return '<nav class="related-services container" aria-label="%s" data-dd29="oct30">%s</nav>' % (label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
    changed = []
    def patch(u, label, links):
        f = os.path.join(ROOT, u.strip('/'), 'index.html')
        if not os.path.exists(f): print('skip', u); return
        s = open(f, encoding='utf-8').read()
        if 'data-dd29="oct30"' in s or s.count('</main>') != 1: print('nopatch', u); return
        open(f, 'w', encoding='utf-8').write(s.replace('</main>', nav(label, links) + '</main>', 1)); changed.append(u)
    P = {p['slug']: L(p) for p in PAGES}
    ig = [P[k] for k in ('instagram-disabled-canada-what-to-do', 'instagram-disabled-australia-what-to-do', 'instagram-disabled-uae-what-to-do', 'instagram-no-appeal-button-eu-uk-routes')]
    fb = [P['facebook-account-disabled-uk-what-to-do'], P['facebook-account-disabled-usa-what-to-do']]
    us = [P['instagram-username-claim-saudi-arabia'], P['instagram-username-claim-qatar']]
    patch('/instagram-account-help/', 'Instagram disabled: by country', ig)
    patch('/facebook-account-help/', 'Facebook disabled: by country', fb)
    patch('/username/', 'Username claims in the Gulf', us)
    patch('/guides/instagram-disabled-no-appeal-button/', 'If you live in the EU or UK', [P['instagram-no-appeal-button-eu-uk-routes'], ig[0], ig[1], ig[2]])
    patch('/guides/instagram-account-suspended-appeal/', 'Instagram disabled: by country', ig)
    patch('/guides/facebook-account-disabled-appeal/', 'Facebook disabled: by country', fb)
    patch('/instagram-disabled-usa-what-to-do/', 'Other countries', ig + fb[1:])
    patch('/instagram-disabled-uk-what-to-do/', 'Other countries', ig + fb[:1])
    patch('/instagram-disabled-eu-what-to-do/', 'If there is no appeal button', [ig[3]])
    patch('/instagram-account-recovery-canada/', 'More for Canada', [ig[0]])
    patch('/instagram-account-recovery-australia/', 'More for Australia', [ig[1]])
    patch('/instagram-account-recovery-uae/', 'More for the UAE', [ig[2]])
    patch('/instagram-username-claim-uae/', 'Other Gulf countries', us)
    patch('/instagram-account-recovery-saudi-arabia/', 'More for Saudi Arabia', [us[0]])
    patch('/instagram-account-recovery-qatar/', 'More for Qatar', [us[1]])
    items = [(p['slug'], p['title'], p['desc']) for p in PAGES]
    open('/tmp/oct30_urls.txt', 'w').write('\n'.join('https://unbanz.com/%s/' % s for s, _, _ in items) + '\n')
    open('/tmp/oct30_changed.txt', 'w').write('\n'.join('https://unbanz.com' + u for u in changed) + '\n')
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    for u in changed:
        sm = re.sub(r'(<loc>https://unbanz.com%s</loc>\s*<lastmod>)[^<]*' % re.escape(u), r'\g<1>2026-10-30', sm)
    add = ''.join('<url><loc>https://unbanz.com/%s/</loc><lastmod>2026-10-30</lastmod></url>\n' % s for s, _, _ in items if 'https://unbanz.com/%s/</loc>' % s not in sm)
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
    for fn, fmt in (('llms.txt', '- [%s](%s): %s'), ('llms-full.txt', '- %s: %s — %s')):
        f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read(); H = '## Country and Gulf username guides (2026-10-30)'
        if H not in s: open(f, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + H + '\n\n' + '\n'.join(fmt % (t, 'https://unbanz.com/%s/' % sl, d) for sl, t, d in items) + '\n')
    print(len(PAGES), 'pages;', len(changed), 'patched')
if __name__ == '__main__': main()
