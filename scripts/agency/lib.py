# -*- coding: utf-8 -*-
"""Agency / white label page kit (2026-10-28 evening). Helpers, registry, link resolver, English builder."""
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import html, os, re, sys, json, copy
from urllib.parse import quote
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import build_oct25_pages as b

ROOT = b.ROOT
DATE = '2026-10-28'
UPDATED = 'October 2026'
CSS_NAME = None

def esc(s): return html.escape(s, quote=True)
def txt(s): return html.escape(s, quote=False)

# ---------- block helpers (all return html; text is written already typographically clean)
def P(*t): return ''.join('<p>%s</p>' % x for x in t)
def UL(items): return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
def OL(items): return '<ol>' + ''.join('<li>%s</li>' % i for i in items) + '</ol>'
def H3(t, *blocks): return '<h3>%s</h3>' % t + ''.join(blocks)
def TABLE(head, rows):
    return ('<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' %
            (''.join('<th>%s</th>' % h for h in head), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)))
def DEFN(term, text): return '<div class="dfn"><p class="dfn-term">%s</p><p>%s</p></div>' % (term, text)
def TMPL(title, *lines): return '<div class="tmpl"><p class="tmpl-title">%s</p>%s</div>' % (title, ''.join('<p>%s</p>' % l for l in lines))
def GLOSS(items): return '<dl class="glossary">' + ''.join('<dt id="%s">%s</dt><dd>%s</dd>' % (re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-'), t, d) for t, d in items) + '</dl>'

# ---------- registry
REG = {}      # slug -> spec
def reg(spec):
    assert spec['slug'] not in REG, spec['slug']
    REG[spec['slug']] = spec
    return spec

LINK = re.compile(r'\[\[([^|\]]+)\|([^\]]+)\]\]')
def resolve(s, where=''):
    def f(m):
        t, label = m.group(1), m.group(2)
        if t.startswith('/'):
            return '<a href="%s">%s</a>' % (t, label)
        if os.environ.get('LENIENT') and t not in REG: return label
        assert t in REG, (where, 'unknown link target', t)
        return '<a href="/%s/">%s</a>' % (t, label)
    return LINK.sub(f, s)

HUB = '/white-label-agency/'
BASE_REL = [('/instagram-account-recovery/', 'Instagram account recovery'), ('/facebook-account-recovery/', 'Facebook account recovery'),
            ('/agency-ad-account-recovery/', 'Agency ad account recovery'), ('/instagram-username-claim/', 'Instagram username claim')]
RELQ = [('/how-it-works/', 'How Unbanz works'), ('/faq/', 'Unbanz FAQ'), ('/refund-policy/', 'Payment and refund policy'), ('/is-unbanz-legit/', 'Is Unbanz legit?')]

def agency_org():
    org = copy.deepcopy(b.ORG)
    ka = org.get('knowsAbout', [])
    for k in ('White label account recovery for agencies', 'Agency account recovery partner', 'White label Instagram username claims'):
        if k not in ka: ka.append(k)
    org['knowsAbout'] = ka
    org['makesOffer'] = [{'@type': 'Offer', 'itemOffered': {
        '@type': 'Service', 'name': 'White label account recovery for agencies', 'serviceType': 'White label account recovery',
        'url': 'https://unbanz.com/white-label-agency/', 'audience': {'@type': 'Audience', 'audienceType': 'Marketing agencies'}}}]
    return org
AGENCY_ORG = agency_org()

def body_html(spec):
    secs = spec['sections']
    out = ['<p class="updated">Last updated: %s</p>' % UPDATED]
    if len(secs) >= 5:
        out.append('<nav class="toc" aria-label="On this page"><p>On this page</p><ul>%s</ul></nav>' % ''.join('<li><a href="#%s">%s</a></li>' % (i, txt(h)) for i, h, _ in secs))
    for i, h, body in secs:
        out.append('<h2 id="%s">%s</h2>%s' % (i, txt(h), body))
    return resolve(''.join(out), spec['slug'])

def to_build(spec):
    slug = spec['slug']
    rel_slugs = spec.get('rel', [])
    related = [(HUB, 'White label agency hub')] + [('/%s/' % s, REG[s]['label']) for s in rel_slugs if not (os.environ.get('LENIENT') and s not in REG)] + spec.get('rel_extra', BASE_REL[:2])
    wa = quote(spec.get('wa') or ('Hey Unbanz, I run an agency and want to talk about %s' % spec['label'].lower()), safe='')
    title = spec['title'] + ' | Unbanz'
    p = dict(date=DATE, slug=slug, title=title, desc=spec['desc'], lang='en-US', crumb=spec['label'], h1=spec['h1'], hero=spec['hero'],
             answer=spec['answer'], wa=wa, subj='White%20label%20agency', ws='unban', svc=spec['svc'] if 'svc' in spec else spec['label'],
             body=[body_html(spec)], faq=[(resolve(q), re.sub(r'<[^>]+>', '', resolve(a))) for q, a in spec['faq']], related=related, relq=RELQ, v2=True,
             area=None, cards=spec['cards'], crumb_parent=('White label agency', HUB),
             stype='White label account recovery for agencies', audience='Marketing agencies', org=AGENCY_ORG)
    return p

CSS_LINK = None
def css_hash():
    import hashlib
    c = open(os.path.join(HERE, 'agency.css')).read()
    h = hashlib.md5(c.encode()).hexdigest()[:10]
    dst = os.path.join(ROOT, 'assets', 'agency.%s.css' % h)
    if not os.path.exists(dst): open(dst, 'w').write(c)
    return h
def css_tag(): return '<link rel="stylesheet" href="/assets/agency.%s.css">' % css_hash()

def build_en(spec):
    h = b.build(to_build(spec))
    assert '</head>' in h
    if '/assets/agency.' not in h: h = h.replace('</head>', css_tag() + '</head>', 1)
    d = os.path.join(ROOT, spec['slug']); os.makedirs(d, exist_ok=True)
    write_page(os.path.join(d, 'index.html'), h)
    return h

def mk(slug, label, group, title, desc, h1, hero, answer, cards, sections, faq, rel, blurb, **kw):
    spec = dict(slug=slug, label=label, group=group, title=title, desc=desc, h1=h1, hero=hero, answer=answer, cards=cards,
                sections=sections, faq=faq, rel=rel, blurb=blurb)
    spec.update(kw)
    return reg(spec)
