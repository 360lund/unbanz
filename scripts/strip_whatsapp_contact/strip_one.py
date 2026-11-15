"""Per-page version of run_all.py for generator hooks: strip_one(text, is_html) runs the same rules in the same order
on one page string (no file walking). Added Nov 15 2026."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path: sys.path.insert(0, HERE)
import strip_anchors, strip_text, strip_copy, strip_copy2

def _rules(name):
    src = open(os.path.join(HERE, name), encoding='utf-8').read()
    cut = re.search(r'\nn ?= ?0\n', src)
    ns = {}
    exec(compile(src[:cut.start()], name, 'exec'), ns)
    return ns['R']

_JSONLD, _C3, _C4 = _rules('strip_jsonld.py'), _rules('strip_copy3.py'), _rules('strip_copy4.py')

def strip_one(t, is_html=True):
    if is_html and ('wa.me' in t or 'whatsapp.com/send' in t):
        t = strip_anchors.process(t)[0]
    if is_html:
        for r, s in _JSONLD: t = r.sub(s, t)
    t = strip_text.fix(t); t = strip_copy.fix(t); t = strip_copy2.fix(t)
    for r, s in _C3: t = r.sub(s, t)
    for r, s in _C4: t = r.sub(s, t)
    return t
