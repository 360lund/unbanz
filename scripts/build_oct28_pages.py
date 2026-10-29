#!/usr/bin/env python3
"""Build the reference pages added on 2026-10-28."""
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page  # adds the human-only CTA note tag (homepages excluded)
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_oct25_pages as b
import oct28_content as c
b.DATE = c.DATE
for _p in c.PAGES: _p['v2'] = True
def with_ld(out, extra):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', out, re.S)
    d = json.loads(m.group(1).replace('<\\/', '</'))
    d['@graph'].append(extra)
    ld = json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return out[:m.start(1)] + ld + out[m.end(1):]
TBL_CSS = ('<style>.guide-body .table-wrap{overflow-x:auto;margin:20px 0;border:1px solid #d9e6ef;border-radius:16px;background:#fff;-webkit-overflow-scrolling:touch}'
  '.guide-body table{width:100%;border-collapse:collapse;font-size:15.5px;min-width:460px}'
  '.guide-body th{text-align:left;background:#e8f2f9;color:#25415d;font-weight:700;padding:12px 16px}'
  '.guide-body td{padding:12px 16px;border-top:1px solid #e3edf4;color:#3a566e;vertical-align:top;line-height:1.55;font-size:15.5px}</style>')
for p in c.PAGES:
    d = os.path.join(b.ROOT, p['slug']); os.makedirs(d, exist_ok=True)
    out = b.build(p)
    if p['slug'] == 'instagram-recovery-glossary':
        url = 'https://unbanz.com/%s/' % p['slug']
        out = with_ld(out, {'@type': 'DefinedTermSet', '@id': url + '#terms', 'name': 'Instagram and Meta account recovery glossary', 'url': url,
            'hasDefinedTerm': [{'@type': 'DefinedTerm', 'name': t, 'description': dsc, 'url': 'https://unbanz.com' + u, 'inDefinedTermSet': url + '#terms'} for t, dsc, u in c.GLOSS]})
    out = out.replace('</head>', TBL_CSS + '</head>', 1)
    write_page(os.path.join(d, 'index.html'), out)
    print('wrote', p['slug'], len(out))
