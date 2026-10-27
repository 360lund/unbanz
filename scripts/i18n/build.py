# -*- coding: utf-8 -*-
"""Build /nl/, /es/ and /pt-br/ and cross-link them with the English and French pages.
Usage: python3 scripts/i18n/build.py [nl es pt-br]   (default: every language that has a lang_*.py)"""
import os, re, sys, glob, hashlib, importlib
sys.path.insert(0, os.path.dirname(__file__))
import lib
from lib import *

LANGS = {'nl': 'lang_nl', 'es': 'lang_es', 'pt-br': 'lang_pt'}
BASE_JS = 'assets/site.d4eb65f0bc51.js'

SENT_OLD_START = "    const base = s === 'unban' ?"
SENT_OLD_END = "(window.unbanzViaTag ? ` ${window.unbanzViaTag}` : '');"

def build_js(S):
    s = open(os.path.join(ROOT, BASE_JS), encoding='utf-8').read()
    reps = [
     ("['unban', 'Unban my account'], ['ban', 'Ban an account'], ['username', 'Username claim'], ['ad', 'Ad account'], ['other', 'Other']", S['js_services']),
     ("LET'S GET IT DONE", S['js_eyebrow']), ("What do you need?", S['js_title']),
     ("<legend>Service</legend>", "<legend>%s</legend>" % S['js_legend_service']), ("<legend>Platform</legend>", "<legend>%s</legend>" % S['js_legend_platform']),
     ("Short reason <span>(optional)</span>", S['js_reason_label']),
     ("e.g. disabled after a login from a new phone", S['js_placeholder']),
     ("Continue on WhatsApp", S['js_continue']), ("Email us instead", S['js_email']),
     ("Never send passwords or login codes.", S['js_note']),
     ('aria-label="Close">', 'aria-label="%s">' % S['js_close']),
     ("'Close menu' : 'Open menu'", "'%s' : '%s'" % (S['menu_close'], S['menu_open'])),
     ("encodeURIComponent('Account help')", "encodeURIComponent('%s')" % S['js_mail_subject']),
    ]
    for a_, b_ in reps:
        assert a_ in s, a_
        s = s.replace(a_, b_)
    i = s.index(SENT_OLD_START); j = s.index(SENT_OLD_END) + len(SENT_OLD_END)
    s = s[:i] + S['js_sentence'].replace('%TAG%', S['tag']) + s[j:]
    h = hashlib.sha256(s.encode()).hexdigest()[:10]
    for f in glob.glob(os.path.join(ROOT, 'assets/site-%s.*.js' % S['js_code'])):
        os.remove(f)
    open(os.path.join(ROOT, 'assets/site-%s.%s.js' % (S['js_code'], h)), 'w', encoding='utf-8').write(s)
    return h

def rel(f):
    return os.path.relpath(f, ROOT)

def scan_fr():
    """FR pages: map english twin path -> fr url, and fr file -> twin."""
    twin_to_fr, file_twin = {}, {}
    for f in glob.glob(os.path.join(ROOT, 'fr', '**', 'index.html'), recursive=True):
        h = open(f, encoding='utf-8').read()
        m = re.search(r'<link rel="alternate" hreflang="en" href="https://unbanz\.com([^"]*)">', h)
        p = os.path.relpath(os.path.dirname(f), ROOT)
        fr_url = BASE + '/' + p.strip('.') .strip('/') + '/'
        fr_url = BASE + ('/fr/' if p == 'fr' else '/' + p + '/')
        if m:
            twin = m.group(1).strip('/')
            twin_to_fr[twin] = fr_url
            file_twin[f] = twin
        else:
            file_twin[f] = None
    return twin_to_fr, file_twin

def page_files_en():
    out = {}
    for f in glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True):
        r = rel(f)
        top = r.split(os.sep)[0]
        if top in ('fr', 'nl', 'es', 'pt-br', 'scripts', 'node_modules') or r.startswith('assets'):
            continue
        twin = os.path.dirname(r)
        out[twin.strip('/')] = f
    return out

RUN = re.compile(r'(?:<link rel="alternate" hreflang="[^"]*" href="[^"]*">)+')
FOOT_OLD_LANGS = re.compile(r'<a href="[^"]*" hreflang="(?:nl|es|pt-BR)" lang="(?:nl|es|pt-BR)">[^<]*</a>')

def main(only=None):
    sites = {}
    for code, modname in LANGS.items():
        if only and code not in only:
            continue
        mod = importlib.import_module(modname)
        sites[code] = mod.make()
    en_files = page_files_en()
    twin_to_fr, fr_file_twin = scan_fr()
    CLUSTER['en'] = {t: BASE + en_path(t) for t in en_files}
    CLUSTER['fr'] = dict(twin_to_fr)
    for code, site in sites.items():
        CLUSTER[code] = {}
        for k in site.order:
            tw = TWINS[k]
            if tw is not None:
                assert tw in en_files, (code, k, tw)
                CLUSTER[code][tw] = site.url(k)
    # include languages that were not built this run but already exist on disk is out of scope: build all three together
    for code, site in sites.items():
        js = build_js(site.S)
        missing = [k for k in TWINS if k not in site.pages]
        print(code, 'pages:', len(site.order), 'js', js, 'no page for:', [k for k in missing if k not in ('support', 'rights')] )
    changed = []
    # 1. write pages
    for code, site in sites.items():
        base = os.path.join(ROOT, site.dir)
        for k in site.order:
            html_ = site.build[k]()
            p = base if site.slugs[k] == '' else os.path.join(base, site.slugs[k])
            os.makedirs(p, exist_ok=True)
            open(os.path.join(p, 'index.html'), 'w', encoding='utf-8').write(html_)
    # 2. hreflang + footer links on EN pages
    for twin, f in en_files.items():
        h = open(f, encoding='utf-8').read()
        h2 = h
        has_new = any(twin in CLUSTER.get(c, {}) for c in ('nl', 'es', 'pt-br'))
        if has_new and 'hreflang="x-default"' in h2:
            runs = list(RUN.finditer(h2))
            assert len(runs) == 1, (f, len(runs))
            m = runs[0]
            h2 = h2[:m.start()] + hreflang_block('en', twin, BASE + en_path(twin)) + h2[m.end():]
        if 'hreflang="fr" lang="fr">Français</a>' in h2:
            h2 = FOOT_OLD_LANGS.sub('', h2)
            h2 = re.sub(r'<a href="[^"]*" hreflang="fr" lang="fr">Français</a>', lambda m: lang_links_for('en', twin if twin in CLUSTER['en'] else None), h2, count=1)
        if h2 != h:
            open(f, 'w', encoding='utf-8').write(h2)
            changed.append(BASE + en_path(twin))
    # 3. hreflang + footer links on FR pages
    for f, twin in fr_file_twin.items():
        h = open(f, encoding='utf-8').read()
        h2 = h
        if twin is not None:
            runs = list(RUN.finditer(h2))
            assert len(runs) == 1, (f, len(runs))
            m = runs[0]
            own = CLUSTER['fr'][twin]
            h2 = h2[:m.start()] + hreflang_block('fr', twin, own) + h2[m.end():]
        h2 = FOOT_OLD_LANGS.sub('', h2)
        h2 = re.sub(r'<a href="[^"]*" hreflang="en" lang="en">English</a>', lambda m: lang_links_for('fr', twin), h2, count=1)
        if h2 != h:
            open(f, 'w', encoding='utf-8').write(h2)
            p = os.path.relpath(os.path.dirname(f), ROOT)
            changed.append(BASE + ('/fr/' if p == 'fr' else '/' + p + '/'))
    # 4. sitemap
    sm = os.path.join(ROOT, 'sitemap.xml')
    s = open(sm, encoding='utf-8').read()
    for code, site in sites.items():
        s = re.sub(r'<url><loc>https://unbanz\.com/%s/[^<]*</loc>.*?</url>\n' % re.escape(site.dir), '', s, flags=re.S)
        s = s.replace('</urlset>', ''.join('<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (site.url(k), LASTMOD) for k in site.order) + '</urlset>')
    open(sm, 'w', encoding='utf-8').write(s)
    # 5. llms
    for code, site in sites.items():
        L = site.S['llms']
        lines = ''.join('- [%s](%s): %s\n' % (plain(site.pages[k]['title']).replace(' | Unbanz', ''), site.url(k), plain(site.pages[k]['desc'])) for k in site.order)
        qa = ''.join('- %s %s Guide: %s\n' % (q, ans, site.url(k)) for q, ans, k in L['qa'])
        block = '\n' + L['header'] + '\n\n' + L['intro'] + '\n\n' + L['facts_label'] + '\n\n' + L['facts'] + '\n\n' + L['pages_label'] + '\n\n' + lines + '\n' + L['qa_label'] + '\n\n' + qa
        for fn in ('llms.txt', 'llms-full.txt'):
            p = os.path.join(ROOT, fn)
            t = open(p, encoding='utf-8').read()
            i = t.find('\n' + L['header'])
            if i != -1:
                j = t.find('\n## ', i + 5)
                t = t[:i].rstrip('\n') + ('\n' + t[j:].lstrip('\n') if j != -1 else '')
            t = t.rstrip('\n') + '\n' + block
            open(p, 'w', encoding='utf-8').write(t)
    # 6. url lists
    allnew = []
    names = {'nl': 'nl_urls.txt', 'es': 'es_urls.txt', 'pt-br': 'ptbr_urls.txt'}
    for code, site in sites.items():
        urls = [site.url(k) for k in site.order]
        open('/workspace/' + names[code], 'w').write('\n'.join(urls) + '\n')
        allnew += urls
    open('/workspace/i18n_changed_other.txt', 'w').write('\n'.join(changed) + '\n')
    print('english/french pages edited:', len(changed))

if __name__ == '__main__':
    main(sys.argv[1:] or None)
