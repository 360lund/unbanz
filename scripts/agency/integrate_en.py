#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire the English agency pages into the site. Idempotent. Run from anywhere."""
import os, re, sys, json, html, glob, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import lib
for m in ['c1_core', 'c2_audience', 'c3_services', 'c4_ops', 'c5_hubs', 'c6_extra']: importlib.import_module(m)
ROOT = lib.ROOT; DATE = '2026-10-28'; REG = lib.REG
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
E_ = lambda s: html.escape(s, quote=False)

GROUPS = [('start', 'Start here'), ('compare', 'Compare your options'), ('audience', 'By type of agency'),
          ('service', 'By service'), ('ops', 'Templates, checklists and pricing')]
ORDER = []
for g, _ in GROUPS: ORDER += [k for k, s in REG.items() if s['group'] == g]
assert len(ORDER) == len(REG)
open('/tmp/agency_en_slugs.txt', 'w').write('\n'.join(ORDER) + '\n')

def meta(slug):
    h = rd(slug + '/index.html')
    ti = html.unescape(re.search(r'<title>(.*?)</title>', h, re.S).group(1))
    de = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
    return ti, de

def set_dates(h):
    h = re.sub(r'(<meta property="article:modified_time" content=")[^"]*', r'\g<1>' + DATE, h)
    return re.sub(r'("dateModified":")[^"]*', r'\g<1>' + DATE, h)

# ---------------- 1. hub section + ItemList
def hub():
    p = 'white-label-agency/index.html'; h = rd(p)
    if 'id="agency-guides"' in h: return
    sec = ['<h2 id="agency-guides">White label guides for agencies</h2>',
           '<p class="updated">Last updated: October 2026</p>',
           '<p>Your clients do not know Unbanz. We work for your agency, behind the scenes and under your brand, and you keep the client relationship. These guides cover how it works, what your client sees, how to price it and the templates to use.</p>']
    items = []
    for g, name in GROUPS:
        sec.append('<h3>%s</h3><ul>' % name)
        for k in [k for k in ORDER if REG[k]['group'] == g]:
            s = REG[k]; sec.append('<li><a href="/%s/">%s</a>: %s</li>' % (k, E_(s['label']), E_(s['blurb'])))
            items.append(k)
        sec.append('</ul>')
    block = ''.join(sec)
    h = h.replace('<h2 id="countries">', block + '<h2 id="countries">', 1)
    # ItemList in JSON-LD
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    d = json.loads(m.group(1))
    d['@graph'].append({'@type': 'ItemList', '@id': 'https://unbanz.com/white-label-agency/#guides', 'name': 'White label guides for agencies',
        'numberOfItems': len(items), 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': 'https://unbanz.com/%s/' % k, 'name': REG[k]['label']} for i, k in enumerate(items)]})
    h = h[:m.start(1)] + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + h[m.end(1):]
    wr(p, set_dates(h))

# ---------------- 2. JSON-LD patches on existing agency pages
AUD = '"audience":{"@type":"Audience","audienceType":"Marketing agencies"},'
KA = ['White label account recovery for agencies', 'Agency account recovery partner', 'White label Instagram username claims']
MO = ('"makesOffer":[{"@type":"Offer","itemOffered":{"@type":"Service","name":"White label account recovery for agencies","serviceType":"White label account recovery",'
      '"url":"https://unbanz.com/white-label-agency/","audience":{"@type":"Audience","audienceType":"Marketing agencies"}}}],')
def patch_ld(h):
    i = h.find('"@type":"Service"')
    if i > 0 and 'audienceType' not in h[i:i + 1500]:
        j = h.find('"provider":{"@id":"https://unbanz.com/#organization"},', i)
        if 0 < j < i + 900: h = h[:j] + AUD + h[j:]
    if '"makesOffer"' not in h and '"Snapchat Community Guidelines"]' in h:
        add = ''.join(',"%s"' % k for k in KA)
        h = h.replace('"Snapchat Community Guidelines"]', '"Snapchat Community Guidelines"' + add + '],' + MO.rstrip(','), 1)
    return h

# ---------------- 3. client-knowledge FAQ (EN)
OLD_Q = 'Does my client need to know Unbanz is involved?'
NEW_Q = 'Will my client know Unbanz is involved?'
OLD_A = 'That is up to you. We work with you, not with your client, and you stay the point of contact.'
NEW_A = 'No. Your clients do not know Unbanz. We work for your agency, behind the scenes and under your brand, and we do not contact your client. You stay the point of contact.'

def countries():
    paths = sorted(glob.glob(os.path.join(ROOT, 'white-label-agency-*/index.html')))
    extra = [('/white-label-account-recovery/', 'White label account recovery guide'), ('/what-your-client-sees-white-label-recovery/', 'What your client sees'),
             ('/how-white-label-account-recovery-works/', 'How white label recovery works')]
    n = 0
    for p in paths:
        s = open(p, encoding='utf-8').read(); o = s
        s = s.replace(OLD_Q, NEW_Q).replace(OLD_A, NEW_A)
        s = patch_ld(s)
        if '/white-label-account-recovery/' not in s:
            navs = list(re.finditer(r'<nav class="related-services[^"]*"[^>]*>.*?</nav>', s, re.S))
            if navs:
                m = navs[0]; blk = m.group(0)
                s = s[:m.start()] + blk[:-6] + ''.join('<a href="%s">%s</a>' % x for x in extra) + '</nav>' + s[m.end():]
        if s != o: s = set_dates(s); open(p, 'w', encoding='utf-8').write(s); n += 1
    return n

def other_ld():
    for p in ['index.html', 'about/index.html', 'services/index.html', 'agency-ad-account-recovery/index.html', 'white-label-agency/index.html']:
        s = rd(p); o = patch_ld(s)
        if o != s: wr(p, o)


# ---------------- 3b. extra inbound links between new pages (post-build, idempotent)
X = {
 'account-recovery-incident-report-template-for-agencies': ['client-status-update-templates-account-recovery', 'agency-intake-form-checklist-account-recovery', 'account-recovery-sop-template-for-agencies', 'white-label-agency-glossary', 'how-white-label-account-recovery-works'],
 'client-account-security-audit-agency-service': ['prevent-client-account-lockouts-agency-checklist', 'white-label-recovery-for-web-design-seo-agencies', 'white-label-recovery-for-local-marketing-agencies', 'agency-pricing-models-reselling-recovery'],
 'white-label-recovery-for-app-growth-agencies': ['white-label-recovery-for-ad-agencies', 'white-label-meta-ad-account-recovery-media-buyers', 'white-label-facebook-ad-account-recovery', 'white-label-account-recovery'],
 'white-label-recovery-for-ecommerce-agencies': ['white-label-facebook-page-recovery', 'white-label-recovery-for-ugc-agencies', 'white-label-recovery-for-ad-agencies', 'white-label-business-portfolio-recovery'],
 'white-label-threads-account-recovery': ['white-label-instagram-account-recovery', 'white-label-recovery-for-social-media-agencies', 'white-label-recovery-for-influencer-talent-agencies', 'white-label-agency-faq'],
 'when-to-turn-down-recovery-job': ['agency-account-recovery-red-flags', 'agency-intake-form-checklist-account-recovery', 'white-label-hacked-account-recovery', 'account-recovery-sop-template-for-agencies'],
 'white-label-recovery-for-branding-creative-studios': ['white-label-username-claim', 'white-label-recovery-for-ugc-agencies', 'white-label-recovery-for-social-media-agencies', 'white-label-recovery-for-web-design-seo-agencies'],
 'white-label-recovery-for-pr-firms': ['white-label-recovery-for-reputation-management-firms', 'white-label-impersonation-fake-account-removal', 'how-to-tell-client-account-disabled-template', 'client-status-update-templates-account-recovery'],
 'white-label-snapchat-account-recovery': ['white-label-username-claim', 'white-label-recovery-for-influencer-talent-agencies', 'white-label-recovery-for-ugc-agencies', 'white-label-instagram-account-recovery'],
 'white-label-recovery-for-reputation-management-firms': ['white-label-recovery-for-pr-firms', 'white-label-hacked-account-recovery', 'agency-client-confidentiality-account-recovery'],
}
def extras():
    n = 0
    inv = {}
    for tgt, srcs in X.items():
        for s_ in srcs: inv.setdefault(s_, []).append(tgt)
    for src, tgts in inv.items():
        p = src + '/index.html'; s = rd(p); o = s
        navs = list(re.finditer(r'<nav class="related-services[^"]*"[^>]*>.*?</nav>', s, re.S))
        m = navs[0]; blk = m.group(0)
        add = ''.join('<a href="/%s/">%s</a>' % (t, E_(REG[t]['label'])) for t in tgts if 'href="/%s/"' % t not in s.replace(blk, '', 0) or 'href="/%s/"' % t not in blk)
        add = ''.join('<a href="/%s/">%s</a>' % (t, E_(REG[t]['label'])) for t in tgts if 'href="/%s/"' % t not in blk)
        if add: wr(p, s[:m.start()] + blk[:-6] + add + '</nav>' + s[m.end():]); n += 1
    return n

# ---------------- 4. nav / footer / services
FOOT_OLD = '<a href="/ad-account-recovery/">Ad account recovery</a>'
FOOT_NEW = FOOT_OLD + '<a href="/white-label-agency/">For agencies</a>'
MOB_OLD = '<a href="/pricing/">Pricing</a><a href="/contact/">Contact</a></nav>'
MOB_NEW = '<a href="/pricing/">Pricing</a><a href="/white-label-agency/">For agencies</a><a href="/contact/">Contact</a></nav>'
def chrome():
    n = 0
    for p in glob.glob(os.path.join(ROOT, '**/index.html'), recursive=True) + [os.path.join(ROOT, 'index.html')]:
        rel = os.path.relpath(p, ROOT)
        if rel.split('/')[0] in ('nl', 'es', 'fr', 'pt-br', 'node_modules'): continue
        s = open(p, encoding='utf-8').read(); o = s
        s = re.sub(r'(<a href="/white-label-agency/">For agencies</a>){2,}', '<a href="/white-label-agency/">For agencies</a>', s)
        if FOOT_NEW not in s: s = s.replace(FOOT_OLD, FOOT_NEW, 1)
        if '<a href="/white-label-agency/">For agencies</a><a href="/contact/">' not in s: s = s.replace(MOB_OLD, MOB_NEW, 1)
        if s != o: open(p, 'w', encoding='utf-8').write(s); n += 1
    return n

def services():
    p = 'services/index.html'; s = rd(p)
    if '/white-label-agency/' in s.split('class="container hub-services"')[1][:4000]: return
    card = ('<article><div><h2>White label for agencies</h2><p>Account recovery and username claims for your clients, under your brand. Your clients do not know Unbanz.</p></div>'
            '<div class="service-row-actions"><a class="service-chat" href="https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20run%20an%20agency%20and%20want%20to%20talk%20about%20white%20label" data-service="white-label">Message us on WhatsApp <span aria-hidden="true">↗︎</span></a>'
            '<a href="/white-label-agency/">See details ↗︎</a></div></article>')
    i = s.find('class="container hub-services"'); j = s.find('</div></section>', i)
    wr(p, set_dates(s[:j] + card + s[j:]))

# ---------------- 5. sitemap + llms
def registry():
    pages = [('/%s/' % k,) + meta(k) for k in ORDER]
    s = rd('sitemap.xml'); add = ''
    for u, _, _ in pages:
        if 'https://unbanz.com' + u not in s: add += '<url><loc>https://unbanz.com%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE)
    if add: s = s.replace('</urlset>', add + '</urlset>')
    for u in ['/', '/about/', '/services/', '/white-label-agency/', '/agency-ad-account-recovery/'] + sorted('/' + os.path.basename(os.path.dirname(p)) + '/' for p in glob.glob(os.path.join(ROOT, 'white-label-agency-*/index.html'))):
        s = re.sub(r'(<loc>https://unbanz\.com%s</loc><lastmod>)[^<]*' % re.escape(u), r'\g<1>' + DATE, s)
    wr('sitemap.xml', s)
    t = rd('llms.txt')
    if '/white-label-account-recovery/' not in t:
        lines = '### White label account recovery for agencies (2026-10-28)\n\nUnbanz works for marketing agencies behind the scenes, under the agency brand. The agency keeps the client relationship and the agency client does not deal with Unbanz. The platform makes the final decision and no outcome is promised.\n\n' + \
            ''.join('- [%s](https://unbanz.com%s): %s\n' % (ti.replace(' | Unbanz', ''), u, de) for u, ti, de in pages) + '\n'
        t = t.replace('### New pages (2026-10-28)', lines + '### New pages (2026-10-28)', 1); wr('llms.txt', t)
    f = rd('llms-full.txt')
    if '/white-label-account-recovery/' not in f:
        f = f.rstrip('\n') + '\n\n## White label account recovery for agencies (2026-10-28)\n\nUnbanz works for marketing agencies behind the scenes, under the agency brand. The agency keeps the client relationship, and the agency\'s clients do not deal with Unbanz. Intake is by WhatsApp +1 934 201 2490 or team@unbanz.com. The platform makes the final decision and no outcome is promised.\n\n' + \
            '\n'.join('- %s: https://unbanz.com%s — %s' % (ti.replace(' | Unbanz', ''), u, de) for u, ti, de in pages) + '\n'
        wr('llms-full.txt', f)

if __name__ == '__main__':
    print('extras', extras()); hub(); print('countries', countries()); other_ld(); services(); print('chrome', chrome()); registry(); print('ok')
