# -*- coding: utf-8 -*-
"""Build the white label agency pages: 43 English (hub + 42 countries) and the native twins. Run from anywhere."""
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_oct25_pages as b
import oct28e_content as c
import oct28e_native as nat

b.DATE = '2026-10-28'
ROOT = b.ROOT if hasattr(b, 'ROOT') else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def english():
    out = []
    pgs = c.pages()
    for p in pgs:
        h = b.build(p)
        key = p['slug'][len('white-label-agency'):].lstrip('-')
        url = 'https://unbanz.com/%s/' % p['slug']
        if c.TWINS.get(key):
            # replace the self-only hreflang run with the cluster
            pat = r'<link rel="alternate" hreflang="[^"]*" href="%s">' % re.escape(url)
            assert len(re.findall(pat, h)) >= 2, p['slug']
            first = re.search(pat, h).start()
            h = re.sub(pat, '', h)
            h = h[:first] + nat.alt_links(key) + h[first:]
            h = nat.foot_links(h, key)
        d = os.path.join(ROOT, p['slug'])
        os.makedirs(d, exist_ok=True)
        write_page(os.path.join(d, 'index.html'), h)
        out.append('/%s/' % p['slug'])
    return out

if __name__ == '__main__':
    en = english(); nv = nat.write_all()
    print(len(en), len(nv))
    open('/tmp/wl_urls.txt', 'w').write('\n'.join('https://unbanz.com' + u for u in en + nv) + '\n')
