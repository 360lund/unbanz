# -*- coding: utf-8 -*-
"""Human-only paid-service note (assets/cta-note.<hash>.js). Every generator calls with_cta_note(html, url_path) on the
page HTML before writing, so new pages include the script tag automatically.
Excluded: the homepage (/) and locale homes (/fr/ /es/ /nl/ /pt-br/), and utility pages (404, /users/, /apply/, /leads).
The script itself is client-side only (country from /api/geo/, skipped for bots/automation), so indexable content never changes."""
import re
CTA_ASSET = '/assets/cta-note.261dbe9ac445.js'
CTA_TAG = '<script src="%s" defer></script>' % CTA_ASSET
_OLD = re.compile(r'<script src="/assets/cta-note\.[0-9a-f]+\.js" defer></script>')
_HOME = re.compile(r'^(?:fr|es|nl|pt-br)?$', re.I)
_SKIP = re.compile(r'^/?(?:404\.html|users(?:/.*)?|apply(?:/.*)?|leads(?:/.*)?)$', re.I)

def wants_cta_note(path):
    """path: site-relative, e.g. 'about/index.html', '/about/', '/', '/fr/'. True when the page should carry the tag."""
    p = (path or '').strip().replace('\\', '/')
    p = re.sub(r'^/+', '', p)
    p = re.sub(r'(^|/)index\.html$', r'\1', p)
    p = p.rstrip('/')
    if _HOME.match(p) or _SKIP.match(p): return False
    return True

def with_cta_note(html, path):
    """Return html with the current CTA tag (idempotent). Homepage / utility pages get any tag removed."""
    if not wants_cta_note(path) or 'name="robots" content="noindex' in html:
        return _OLD.sub('', html)
    if _OLD.search(html):  # replace in place, drop any duplicates
        first = [True]
        def sub(m):
            if first[0]: first[0] = False; return CTA_TAG
            return ''
        return _OLD.sub(sub, html)
    if '</head>' not in html: return html
    return html.replace('</head>', CTA_TAG + '</head>', 1)

def write_page(path, html):
    """Drop-in for open(path, 'w', encoding='utf-8').write(html) when writing a site page: adds the CTA tag (homepages excluded)."""
    import os
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rel = os.path.relpath(os.path.abspath(path), root)
    with open(path, 'w', encoding='utf-8') as fh: fh.write(with_cta_note(html, rel))
