# -*- coding: utf-8 -*-
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page
import os, sys, re, subprocess, html as H
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'dd29'))
import lib
lib.DATE = '2026-11-01'; lib.DATE_LONG = '1 November 2026'
from c_nov01 import *
from lib import ROOT, FAM, esc
D = '2026-11-01'
C = {'US': 'United States', 'GB': 'United Kingdom', 'CA': 'Canada', 'AU': 'Australia', 'AE': 'United Arab Emirates', 'SA': 'Saudi Arabia', 'QA': 'Qatar', 'KW': 'Kuwait',
     'FR': 'France', 'DE': 'Germany', 'CH': 'Switzerland'}
TERMS = 'Terms are agreed with you before any work starts.'
def area(a): return [{'@type': 'Country', 'name': C[x]} for x in (a if isinstance(a, list) else [a])]
_hb = lib.how_block
def how_block(p):
    s = _hb(p); old = 'We tell you honestly whether this is something we can help with.'
    assert old in s
    return s.replace(old, old + ' ' + TERMS)
lib.how_block = how_block
TR = set(l.split('/')[0] for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n') if l)
def exists(u): return os.path.exists(os.path.join(ROOT, u.strip('/'), 'index.html')) or u.strip('/') in [p['slug'] for p in PAGES]
def L(p): return ('/%s/' % p['slug'], p['crumb'])
WIN = [('/guides/instagram-account-suspended-appeal/', 'Instagram suspended: how to appeal'), ('/guides/facebook-account-disabled-appeal/', 'Facebook disabled appeal'),
       ('/guides/meta-ad-account-restricted/', 'Meta ad account restricted'), ('/guides/instagram-disabled-no-appeal-button/', 'No appeal button')]
EXTRA = {'meta-ad-account-disabled-saudi-arabia': ['/meta-ad-account-disabled-uae/', '/facebook-account-disabled-saudi-arabia-what-to-do/'],
         'meta-ad-account-disabled-france': ['/meta-ad-account-disabled-germany/', '/instagram-account-recovery-france/'],
         'meta-ad-account-disabled-switzerland': ['/meta-ad-account-disabled-germany/', '/instagram-disabled-switzerland-what-to-do/'],
         'instagram-disabled-france-what-to-do': ['/instagram-disabled-eu-what-to-do/', '/instagram-account-recovery-france/'],
         'instagram-disabled-germany-what-to-do': ['/instagram-disabled-eu-what-to-do/', '/instagram-account-recovery-germany/'],
         'facebook-account-disabled-qatar-what-to-do': ['/facebook-account-recovery-qatar/', '/facebook-lost-access-to-email-or-phone-gulf/'],
         'snapchat-account-locked-france': ['/snapchat-account-locked-uk/', '/snapchat-account-ban-service/'],
         'snapchat-account-locked-usa': ['/snapchat-account-locked-uk/', '/snapchat-account-ban-service/']}
def title_of(u):
    f = os.path.join(ROOT, u.strip('/'), 'index.html')
    m = re.search(r'<title>([^<|]*)', open(f, encoding='utf-8').read()); return H.unescape(m.group(1).strip().split(':')[0])
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
    for u, _ in WIN:
        if not exists(u): bad.add(('WIN', u))
    if bad: raise SystemExit('BROKEN %s' % sorted(bad))
    for p in PAGES:
        F = FAM[p['fam']]
        sib = [L(q) for q in PAGES if q is not p and FAM[q['fam']]['platform'] == F['platform'] and q['fam'] == p['fam']] or [L(q) for q in PAGES if q is not p]
        rel = [F['parent']] + [(u, title_of(u)) for u in EXTRA[p['slug']]] + sib[:4]
        relq = WIN + [('/how-it-works/', 'How Unbanz works'), ('/white-label-agency/', 'For agencies')]
        p['related_final'] = (rel, relq)
        h = lib.build(p, None)
        assert TERMS in h and 'Not affiliated with Meta' in h and 'wa.me/19342012490' in h and '447723' not in h.replace(' ', '')
        d = os.path.join(ROOT, p['slug']); os.makedirs(d, exist_ok=True); write_page(os.path.join(d, 'index.html'), h)
    def nav(label, links): return '<nav class="related-services container" aria-label="%s" data-dd29="nov01">%s</nav>' % (label, ''.join('<a href="%s">%s</a>' % (u, esc(t)) for u, t in links))
    changed = []
    def patch(u, label, links):
        f = os.path.join(ROOT, u.strip('/'), 'index.html')
        if not os.path.exists(f): print('skip', u); return
        s = open(f, encoding='utf-8').read()
        if 'data-dd29="nov01"' in s or s.count('</main>') != 1: print('nopatch', u); return
        s = s.replace('</main>', nav(label, links) + '</main>', 1); s = re.sub(r'("dateModified"\s*:\s*")[^"]*', r'\g<1>' + D, s); open(f, 'w', encoding='utf-8').write(s); changed.append(u)
    P = {p['slug']: L(p) for p in PAGES}
    adsa, adfr, adch = P['meta-ad-account-disabled-saudi-arabia'], P['meta-ad-account-disabled-france'], P['meta-ad-account-disabled-switzerland']
    igfr, igde, fbqa = P['instagram-disabled-france-what-to-do'], P['instagram-disabled-germany-what-to-do'], P['facebook-account-disabled-qatar-what-to-do']
    scfr, scus = P['snapchat-account-locked-france'], P['snapchat-account-locked-usa']
    patch('/meta-ad-account-help/', 'Meta ad accounts: more countries', [adsa, adfr, adch])
    patch('/ad-account-recovery/', 'Ad account help by country', [adsa, adfr, adch])
    patch('/guides/meta-ad-account-restricted/', 'Ad account restricted: by country', [adsa, adfr, adch])
    patch('/meta-ad-account-disabled-uae/', 'Elsewhere in the Gulf', [adsa])
    patch('/meta-ad-account-disabled-germany/', 'Neighbouring countries', [adfr, adch])
    patch('/instagram-disabled-eu-what-to-do/', 'By country', [igfr, igde])
    patch('/guides/instagram-account-suspended-appeal/', 'Instagram disabled: France and Germany', [igfr, igde])
    patch('/instagram-account-help/', 'Instagram disabled: more countries', [igfr, igde])
    patch('/instagram-account-recovery-france/', 'More for France', [igfr, adfr, scfr])
    patch('/instagram-account-recovery-germany/', 'More for Germany', [igde])
    patch('/instagram-account-recovery-switzerland/', 'More for Switzerland', [adch])
    patch('/instagram-account-recovery-usa/', 'More for the US', [scus])
    patch('/instagram-disabled-qatar-what-to-do/', 'Facebook in Qatar', [fbqa])
    patch('/facebook-account-recovery-qatar/', 'More for Qatar', [fbqa])
    patch('/facebook-account-help/', 'Facebook disabled: Qatar', [fbqa])
    patch('/facebook-account-disabled-uae-what-to-do/', 'Elsewhere in the Gulf', [fbqa])
    patch('/facebook-account-disabled-saudi-arabia-what-to-do/', 'Ads in Saudi Arabia', [adsa, fbqa])
    patch('/snapchat-account-help/', 'Snapchat locked: more countries', [scfr, scus])
    patch('/snapchat-account-ban-service/', 'Snapchat locked by country', [scfr, scus])
    patch('/snapchat-account-locked-uk/', 'Other countries', [scfr, scus])
    items = [(p['slug'], p['title'], p['desc']) for p in PAGES]
    open('/tmp/nov01_urls.txt', 'w').write('\n'.join('https://unbanz.com/%s/' % s for s, _, _ in items) + '\n')
    open('/tmp/nov01_changed.txt', 'w').write('\n'.join('https://unbanz.com' + u for u in changed) + '\n')
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    for u in changed + ['/site-map/']:
        sm = re.sub(r'(<loc>https://unbanz.com%s</loc>\s*<lastmod>)[^<]*' % re.escape(u), r'\g<1>' + D, sm)
    add = ''.join('<url><loc>https://unbanz.com/%s/</loc><lastmod>%s</lastmod></url>\n' % (s, D) for s, _, _ in items if 'https://unbanz.com/%s/</loc>' % s not in sm)
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
    # HTML site map: insert into the English list, alphabetically
    f = os.path.join(ROOT, 'site-map', 'index.html'); s = open(f, encoding='utf-8').read()
    i = s.index('<h2>English</h2>'); j = s.index('</ul>', i); seg = s[i:j]
    lis = re.findall(r'<li><a href="([^"]+)">(.*?)</a></li>', seg)
    have = {h for h, _ in lis}
    for sl, t, _ in items:
        if '/%s/' % sl not in have: lis.append(('/%s/' % sl, esc(t)))
    lis.sort(key=lambda x: x[0])
    k = seg.index('<li>'); seg2 = seg[:k] + ''.join('<li><a href="%s">%s</a></li>' % x for x in lis)
    s = s[:i] + seg2 + s[j:]; open(f, 'w', encoding='utf-8').write(s)
    for fn, fmt in (('llms.txt', '- [%s](%s): %s'), ('llms-full.txt', '- %s: %s — %s')):
        f = os.path.join(ROOT, fn); s = open(f, encoding='utf-8').read(); Hh = '## Meta ad accounts, Instagram, Facebook and Snapchat by country (2026-11-01)'
        if Hh not in s: open(f, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + Hh + '\n\n' + '\n'.join(fmt % (t, 'https://unbanz.com/%s/' % sl, d) for sl, t, d in items) + '\n')
    print(len(PAGES), 'pages;', len(changed), 'patched')
if __name__ == '__main__': main()
