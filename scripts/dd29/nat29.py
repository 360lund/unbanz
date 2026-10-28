# -*- coding: utf-8 -*-
"""Native-language siblings (fr, pt-br, es) of selected dd29 EN pages. Reuses adacct native.build."""
import os, re, sys, types
HERE = os.path.dirname(os.path.abspath(__file__)); AD = os.path.join(HERE, '..', 'adacct')
sys.path.insert(0, AD); sys.path.insert(0, HERE)
src = open(os.path.join(AD, 'native.py'), encoding='utf-8').read()
src = src.replace('sib = [TOPICS[(k + i) % 6] for i in (1, 2, 3)]', 'sib = [TOPICS[(k + i) % len(TOPICS)] for i in range(1, min(4, len(TOPICS)))]')
src = src.replace("k = TOPICS.index(topic);", "k = TOPICS.index(topic);")
assert 'len(TOPICS)' in src
N = types.ModuleType('native29'); N.__file__ = os.path.join(AD, 'native.py'); exec(compile(src, N.__file__, 'exec'), N.__dict__)
import nat_fr, nat_pt, nat_es
from nat import fr as ofr, pt as opt, es as oes
EN = {'spam': 'instagram-suspended-for-spam-appeal', 'thirdparty': 'instagram-suspended-after-third-party-app',
      'fakename': 'facebook-disabled-for-fake-name-appeal', 'twofa': 'instagram-hacked-two-factor-turned-on-by-hacker',
      'billing': 'ad-account-disabled-after-billing-country-change', 'spike': 'ad-account-disabled-after-sudden-spend-spike'}
PARENT = {  # lang -> parent key -> (path, label)
 'fr': {'ig': ('fr/compte-instagram-desactive-comment-recuperer', 'Compte Instagram'), 'fb': ('fr/compte-facebook-desactive-faire-appel', 'Compte Facebook'), 'ad': (None, None)},
 'pt-br': {'ig': ('pt-br/conta-do-instagram-desativada', 'Conta do Instagram'), 'fb': ('pt-br/conta-do-facebook-desativada-contestar', 'Conta do Facebook'), 'ad': (None, None)},
 'es': {'ig': ('es/cuenta-de-instagram-desactivada', 'Cuenta de Instagram'), 'fb': ('es/cuenta-de-facebook-desactivada-apelar', 'Cuenta de Facebook'), 'ad': (None, None)}}
SRC = {'fr': (nat_fr, ofr), 'pt-br': (nat_pt, opt), 'es': (nat_es, oes)}
ORDER = ['billing', 'spike', 'spam', 'thirdparty', 'twofa', 'fakename']   # priority
HLNAME = N.HL
def langs_of(topic): return [lk for lk in ('fr', 'pt-br', 'es') if topic in SRC[lk][0].T]
def pth(lk, topic): return '%s/%s' % (lk, SRC[lk][0].T[topic]['slug'])
def paths(): return [pth(lk, t) for t in ORDER for lk in ('fr', 'pt-br', 'es') if t in SRC[lk][0].T]
def en_alts():
    out = {}
    for t, en in EN.items():
        u = lambda p: 'https://unbanz.com/%s/' % p
        a = [('en', u(en)), ('en-US', u(en))]
        for lk in langs_of(t):
            h1, h2, _ = HLNAME[lk]
            a += [(h1, u(pth(lk, t))), (h2, u(pth(lk, t)))] if h1 != h2 else [(h1, u(pth(lk, t)))]
        a.append(('x-default', u(en))); out[en] = a
    return out
def build_all(root):
    N.EN = EN
    done = []
    for lk in ('fr', 'pt-br', 'es'):
        new, old = SRC[lk]
        tps = [t for t in ORDER if t in new.T]
        N.TOPICS = tps
        for t in tps:
            N.LANGS = {k: (types.SimpleNamespace(L=dict(SRC[k][1].L), T=SRC[k][0].T), N.LANGS_ORIG[k][1], N.LANGS_ORIG[k][2]) for k in langs_of(t)}
            par = new.T[t]['parent']; pp, label = PARENT[lk][par]
            L = N.LANGS[lk][0].L
            if pp:
                L['crumb_mid'] = label; N.CORE[lk] = pp
            else:
                N.CORE[lk] = N.CORE_ORIG[lk]
            s = N.build(lk, t)
            if par != 'ad': s = s.replace('data-service="ad"', 'data-service="unban"')
            p = pth(lk, t); os.makedirs(os.path.join(root, p), exist_ok=True)
            open(os.path.join(root, p, 'index.html'), 'w', encoding='utf-8').write(s); done.append(p)
    return done
N.LANGS_ORIG = dict(N.LANGS); N.CORE_ORIG = dict(N.CORE)
if __name__ == '__main__':
    print(len(build_all(N.ROOT)))
