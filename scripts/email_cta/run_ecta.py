"""Apply ecta to Unbanz (/workspace/site) and Pofofo sites. Usage: run_ecta.py [unbanz|pofofo|all] [--check]"""
import os, re, sys, json, hashlib, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ecta

HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, 'ecta.css')).read()
_PARENT = os.path.basename(os.path.dirname(HERE))
_REPO = os.path.dirname(os.path.dirname(HERE))
SITE_ROOT = _REPO if _PARENT == 'scripts' else '/workspace/site'          # copy in site/scripts/email_cta
POFOFO_ROOT = _REPO if _PARENT == '_src' else '/workspace/pofofo'        # copy in pofofo/_src/email_cta
SKIP_DIRS = ('users/', 'node_modules/', '.git/', 'scripts/', 'docs/', 'api/', '_src/', 'assets/')

UNBANZ = dict(root=SITE_ROOT, brand='Unbanz', host='unbanz.com',
  home=('', 'fr', 'es', 'nl', 'pt-br', 'de', 'it', 'tr', 'ar'),
  contact=('contact', 'fr/contact', 'nl/contact', 'es/contacto', 'pt-br/contato'),
  faq=('faq', 'fr/faq', 'es/preguntas-frecuentes', 'pt-br/perguntas-frequentes'))

POFOFO = ['atclaim', 'ogclaim', 'usernm', 'adaccountunban', 'restoreadaccount', 'adsaccountrecovery', 'banhelp', 'acctback', 'acctfix', 'bansfix', 'unbanhelp']

def pofofo_cfg(s):
    root = POFOFO_ROOT + '/sites/' + s
    h = open(root + '/index.html').read()
    m = re.search(r'<meta property="og:site_name" content="([^"]+)"', h)
    c = re.search(r'<link rel="canonical" href="https://(?:www\.)?([^/"]+)', h)
    return dict(root=root, brand=m.group(1), host=c.group(1), home=('',), contact=('contact',), faq=('faq',))

VARS = {'acctfix': ':root{--ecta-bg:#2e804c}\n', 'bansfix': ':root{--ecta-bg:#237c7c}\n',
        'ogclaim': ':root{--ecta-card-bg:#121212;--ecta-card-ink:#f2f2f2}\n', 'restoreadaccount': ':root{--ecta-card-bg:#121212;--ecta-card-ink:#f2f2f2}\n'}

def css_asset(root, write=True):
    css = VARS.get(os.path.basename(root), '') + CSS
    hx = hashlib.sha256(css.encode()).hexdigest()[:12]
    p = '%s/assets/ecta.%s.css' % (root, hx)
    if write and not os.path.exists(p):
        open(p, 'w').write(css)
    return '/assets/ecta.%s.css' % hx

def run(cfg, check=False):
    root = cfg['root']; href = css_asset(root, write=not check)
    tot = dict(pages=0, changed=0, blocks=0, ldchanged=0, bad=0, faq=0, band=0, hdr=0)
    for p in glob.glob(root + '/**/*.html', recursive=True):
        rel = os.path.relpath(p, root)
        if rel.startswith(SKIP_DIRS) or rel.startswith('google') or '</head>' not in (h := open(p, encoding='utf-8').read()):
            continue
        tot['pages'] += 1
        new, st = ecta.apply_page(h, rel, cfg['brand'], href, cfg['host'], cfg['home'], cfg['contact'], cfg['faq'])
        tot['blocks'] += st['blocks']; tot['ldchanged'] += st['changed']; tot['bad'] += st['bad']; tot['faq'] += st['faq_added']
        tot['band'] += 'ecta-band' in new; tot['hdr'] += 'ecta-hdr' in new
        if new != h:
            tot['changed'] += 1
            if not check: open(p, 'w', encoding='utf-8').write(new)
    for n in ('llms.txt', 'llms-full.txt'):
        p = root + '/' + n
        if os.path.exists(p):
            t = open(p, encoding='utf-8').read(); nt = ecta.apply_llms(t, cfg['brand'])
            if nt != t and not check: open(p, 'w', encoding='utf-8').write(nt)
    print(os.path.basename(root), cfg['brand'], tot)

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'; check = '--check' in sys.argv
    if which in ('unbanz', 'all'): run(UNBANZ, check)
    if which in ('pofofo', 'all'):
        for s in POFOFO: run(pofofo_cfg(s), check)

def _strip(t, is_html=True):
    """Run the WhatsApp-contact strip (../strip_whatsapp_contact/strip_one.py) when it sits next to this folder."""
    d = os.path.join(os.path.dirname(HERE), 'strip_whatsapp_contact')
    import timeframe  # Nov 15 2026: recovery time is guaranteed 7–14 days, refund if not reinstated within 14 days
    if not os.path.isfile(os.path.join(d, 'strip_one.py')):
        return timeframe.fix(t)
    if d not in sys.path: sys.path.insert(0, d)
    import strip_one
    return timeframe.fix(strip_one.strip_one(t, is_html))

def apply_unbanz_page(html, rel):
    """Generator hook for one Unbanz page (rel like 'about/index.html')."""
    c = UNBANZ
    if rel.replace('\\', '/').lstrip('/').startswith(SKIP_DIRS) or '</head>' not in html:
        return html
    html = _strip(html)
    return ecta.apply_page(html, rel, c['brand'], css_asset(c['root']), c['host'], c['home'], c['contact'], c['faq'])[0]

def apply_pofofo_page(html, site, rel):
    """Generator hook for one Pofofo page (site like 'atclaim', rel like 'faq/index.html')."""
    if site not in POFOFO or '</head>' not in html or rel.replace('\\', '/').lstrip('/').startswith(SKIP_DIRS):
        return html
    c = pofofo_cfg(site) if os.path.exists(POFOFO_ROOT + '/sites/' + site + '/index.html') else None
    if not c:
        return html
    html = _strip(html)
    return ecta.apply_page(html, rel, c['brand'], css_asset(c['root']), c['host'], c['home'], c['contact'], c['faq'])[0]

def apply_pofofo_llms(text, site):
    if site not in POFOFO:
        return text
    return ecta.apply_llms(_strip(text, False), pofofo_cfg(site)['brand'])

def run_nf404(check=False):
    p = POFOFO_ROOT + '/api/_lib/nf404.mjs'; s = open(p).read()
    d = json.loads(s[s.index('{'): s.rindex('}') + 1]); n = 0
    for k in POFOFO:
        if k not in d: continue
        cfg = pofofo_cfg(k); href = css_asset(cfg['root'], write=not check)
        new, st = ecta.apply_page(_strip(d[k]), '404.html', cfg['brand'], href, cfg['host'], (), (), ())
        if new != d[k]: d[k] = new; n += 1
    if n and not check:
        open(p, 'w').write('export const PAGES = ' + json.dumps(d, ensure_ascii=False) + ';\n')
    print('nf404 changed', n)

if __name__ == '__main__' and ('pofofo' in sys.argv or 'all' in sys.argv or len(sys.argv) == 1):
    run_nf404('--check' in sys.argv)
