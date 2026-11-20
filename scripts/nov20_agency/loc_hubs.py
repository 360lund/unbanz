"""Nov 20 2026 (d): localized agency hubs (fr/nl/es/pt-br) open with the same onboarding hero + 5-step card as
/white-label-agency/ (localized, $1,200 per case, 3-tier contact handoff via /api/geo/). Their existing hero is replaced
(the H1 and crumb are kept); the rest of the page is unchanged. Idempotent."""
import os, re, sys, glob
sys.path.insert(0, os.path.dirname(__file__))
from onboard_ui import hero
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); os.chdir(ROOT)
HUBS = {'fr/white-label-agences': 'fr', 'nl/white-label-bureau': 'nl', 'es/white-label-agencias': 'es', 'pt-br/white-label-agencias': 'pt'}
CSS = open('scripts/nov20_agency/hub.css', encoding='utf8').read().strip()
JS = re.search(r'/assets/agency-onboard\.[0-9a-f]+\.js', open('white-label-agency/index.html', encoding='utf8').read()).group(0)
HEADBLK = re.compile(r'<style id="wl-css">.*?</style><script defer src="/assets/agency-onboard\.[0-9a-f]+\.js"></script>', re.S)
for d, lang in HUBS.items():
    f = d + '/index.html'; s = open(f, encoding='utf8').read()
    m = re.search(r'<section class="(?:service-hero|wl-hero)">.*?</section>', s, re.S)
    crumb = re.search(r'<a class="crumb"[^>]*>.*?</a>', m.group(0), re.S).group(0)
    h1 = re.search(r'<h1>(.*?)</h1>', m.group(0), re.S).group(1)
    s = s[:m.start()] + hero(lang, crumb, h1) + s[m.end():]
    blk = f'<style id="wl-css">{CSS}</style><script defer src="{JS}"></script>'
    s = HEADBLK.sub(lambda _: blk, s) if HEADBLK.search(s) else s.replace('</head>', blk + '</head>', 1)
    open(f, 'w', encoding='utf8').write(s); print('hub', f)
