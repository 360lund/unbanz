#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire the 32 native agency pages into the site. Idempotent. Run nat/nlib.write_all() first."""
import os, re, sys, json, html, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'nat'))
import nlib as L
L.load()
ROOT = L.ROOT; DATE = '2026-10-28'
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)
H = lambda s: html.escape(s, quote=True)

HUBS = {'nl': ['white-label-bureau', 'white-label-bureau-nederland', 'white-label-bureau-belgie'],
        'es': ['white-label-agencias', 'white-label-agencias-espana'],
        'pt-br': ['white-label-agencias', 'white-label-agencias-brasil'],
        'fr': ['white-label-agences', 'white-label-agences-belgique', 'white-label-agences-france', 'white-label-agences-luxembourg', 'white-label-agences-suisse']}
OLDQ = {'nl': 'Moet mijn klant weten', 'es': '¿Mi cliente tiene que saber', 'pt-br': 'Meu cliente precisa saber', 'fr': 'Mon client doit-il savoir'}
NEWQA = {'nl': ('Weten mijn klanten dat Unbanz erbij betrokken is?', 'Nee. Je klanten kennen Unbanz niet. We werken voor jouw bureau, op de achtergrond en onder jouw merk, en we nemen nooit contact op met je klant. Jij blijft het aanspreekpunt.'),
         'es': ('¿Mis clientes saben que Unbanz participa?', 'No. Tus clientes no conocen a Unbanz. Trabajamos para tu agencia, en segundo plano y con tu marca, y nunca contactamos con tu cliente. Tú sigues siendo el contacto.'),
         'pt-br': ('Meus clientes sabem que a Unbanz está envolvida?', 'Não. Seus clientes não conhecem a Unbanz. Trabalhamos para a sua agência, nos bastidores e com a sua marca, e nunca contatamos o seu cliente. Você continua sendo o contato.'),
         'fr': ('Mes clients savent-ils qu’Unbanz intervient ?', 'Non. Vos clients ne connaissent pas Unbanz. Nous travaillons pour votre agence, en coulisses et sous votre marque, et nous ne contactons jamais votre client. Vous restez l’interlocuteur.')}
SEC = {'nl': ('White label gidsen voor bureaus', 'Je klanten kennen Unbanz niet. We werken voor jouw bureau, op de achtergrond en onder jouw merk. Deze pagina’s leggen elk onderdeel uit.'),
       'es': ('Guías white label para agencias', 'Tus clientes no conocen a Unbanz. Trabajamos para tu agencia, en segundo plano y con tu marca. Estas páginas explican cada parte.'),
       'pt-br': ('Guias white label para agências', 'Seus clientes não conhecem a Unbanz. Trabalhamos para a sua agência, nos bastidores e com a sua marca. Estas páginas explicam cada parte.'),
       'fr': ('Guides white label pour agences', 'Vos clients ne connaissent pas Unbanz. Nous travaillons pour votre agence, en coulisses et sous votre marque. Ces pages expliquent chaque point.')}

def twins():
    n = 0
    for k in L.KEYS:
        p = L.EN[k] + '/index.html'; h = rd(p)
        if '<link rel="alternate" hreflang="nl"' in h: continue
        add = ''.join('<link rel="alternate" hreflang="%s" href="https://unbanz.com%s">' % (c, L.url(lg, k)) for lg in L.LANGS for c in L.N.LANG_CODES[lg])
        m = re.search(r'<link rel="alternate" hreflang="x-default" href="[^"]*">', h); assert m, p
        h = h[:m.start()] + add + h[m.start():]
        wr(p, h); n += 1
    return n

def hubs():
    n = 0
    for lg, slugs in HUBS.items():
        for sl in slugs:
            p = '%s/%s/index.html' % (lg, sl); h = rd(p); o = h
            # faq html
            q, a = NEWQA[lg]
            def rep(m): return '<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (H(q), H(a))
            h, c = re.subn(r'<details><summary>' + re.escape(html.escape(OLDQ[lg], quote=False)) + r'[^<]*<span[^>]*>\+</span></summary><p>.*?</p></details>', rep, h, flags=re.S)
            if c == 0 and q not in h and H(q) not in h: print('NO FAQ MATCH', p)
            # json-ld
            m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', h, re.S)
            j = json.loads(m.group(2))
            for nd in j['@graph']:
                if nd['@type'] == 'FAQPage':
                    for it in nd['mainEntity']:
                        if it['name'].startswith(OLDQ[lg]):
                            it['name'] = q; it['acceptedAnswer']['text'] = a
                if nd['@type'] == 'Service':
                    nd['audience'] = {'@type': 'Audience', 'audienceType': 'Marketing agencies'}
                    nd['serviceType'] = 'White label account recovery for agencies'
                if nd['@type'] == 'WebPage': nd['dateModified'] = DATE
            h = h[:m.start(2)] + json.dumps(j, ensure_ascii=False, separators=(',', ':')) + h[m.end(2):]
            # guides section
            if 'id="agency-guides"' not in h:
                ttl, intro = SEC[lg]
                sec = '<section class="container agency-guides" id="agency-guides"><h2>%s</h2><p>%s</p><ul>%s</ul></section>' % (
                    H(ttl), H(intro), ''.join('<li><a href="%s">%s</a></li>' % (L.url(lg, k), H(L.PAGES[lg][k]['h1'].rstrip('.'))) for k in L.KEYS))
                i = h.find('<section class="faq-section"'); assert i > 0, p
                h = h[:i] + sec + h[i:]
            # related nav link
            pil = L.url(lg, 'pillar')
            if 'href="%s"' % pil not in h.split('<nav class="related-services')[1] if '<nav class="related-services' in h else True:
                h = re.sub(r'(<nav class="related-services container"[^>]*>)', r'\g<1><a href="%s">%s</a>' % (pil, H(L.PAGES[lg]['pillar']['label'])), h, count=1)
            if h != o: wr(p, h); n += 1
    return n

def registry():
    new = [L.url(lg, k) for k in L.KEYS for lg in L.LANGS]
    s = rd('sitemap.xml'); add = ''.join('<url><loc>https://unbanz.com%s</loc><lastmod>%s</lastmod></url>\n' % (u, DATE) for u in new if 'https://unbanz.com' + u not in s)
    if add: wr('sitemap.xml', s.replace('</urlset>', add + '</urlset>'))
    def meta(u):
        h = rd(u.strip('/') + '/index.html')
        return html.unescape(re.search(r'<title>(.*?)</title>', h, re.S).group(1)).replace(' | Unbanz', ''), html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
    t = rd('llms.txt')
    if '/nl/white-label-accountherstel-voor-bureaus/' not in t:
        blk = '### White label for agencies, native versions (2026-10-28)\n\nDutch, Spanish, Brazilian Portuguese and French versions of the main white label agency pages. Your clients do not know Unbanz. Unbanz works for the agency, behind the scenes and under the agency brand.\n\n'
        for lg in L.LANGS:
            for k in L.KEYS:
                u = L.url(lg, k); ti, de = meta(u); blk += '- [%s](https://unbanz.com%s): %s\n' % (ti, u, de)
        blk += '\n'
        assert '### New pages (2026-10-28)' in t
        wr('llms.txt', t.replace('### New pages (2026-10-28)', blk + '### New pages (2026-10-28)', 1))
    f = rd('llms-full.txt')
    if '/nl/white-label-accountherstel-voor-bureaus/' not in f:
        blk = '\n## White label for agencies, native versions (2026-10-28)\n\nDutch, Spanish, Brazilian Portuguese and French versions of the main white label agency pages.\n\n'
        for lg in L.LANGS:
            for k in L.KEYS:
                u = L.url(lg, k); ti, de = meta(u); blk += '- %s: https://unbanz.com%s — %s\n' % (ti, u, de)
        wr('llms-full.txt', f.rstrip('\n') + '\n' + blk)
    pri = [L.EN[k] for k in L.KEYS]
    return new

if __name__ == '__main__':
    print('twins', twins()); print('hubs', hubs()); new = registry()
    open('/tmp/agency_nat_urls.txt', 'w').write('\n'.join(new) + '\n'); print('ok', len(new))
