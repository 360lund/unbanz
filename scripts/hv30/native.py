# -*- coding: utf-8 -*-
import os as _o, sys as _s
_d = _o.path.dirname(_o.path.abspath(__file__))
while not _o.path.exists(_o.path.join(_d, 'cta_note.py')): _d = _o.path.dirname(_d)
_s.path.append(_d); from cta_note import write_page
import os, re, json, html, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
E = lambda s: html.escape(s, quote=True)
A = lambda h, t: '<a href="%s">%s</a>' % (h, t)
ol = lambda xs: '<ol>%s</ol>' % ''.join('<li>%s</li>' % x for x in xs)
ul = lambda xs: '<ul>%s</ul>' % ''.join('<li>%s</li>' % x for x in xs)
CFG = {
 'nl': dict(tpl='nl/dsa-recht-op-beroep-meta', home='Home', crumb2=('Gidsen', '/nl/veelgestelde-vragen/'), alts=['nl'], rel="Gerelateerde pagina's",
   how=('Zo gaat het met Unbanz', ['Stuur ons je gebruikersnaam, een screenshot van de melding en de datum via WhatsApp of e-mail.', 'We zeggen eerlijk of we kunnen helpen.', 'Voorwaarden worden met je afgesproken voordat het werk begint.', 'We gebruiken de officiële routes van het platform. Het platform beslist, en niemand kan de uitkomst beloven.']), safe='voorzichtig'),
 'fr': dict(tpl='fr/droit-de-recours-dsa-meta', home='Accueil', crumb2=('Guides', '/fr/faq/'), alts=['fr', 'fr-FR'], rel='Pages liées',
   how=('Comment ça se passe avec Unbanz', ['Envoyez-nous votre nom d’utilisateur, une capture de la notification et la date, par WhatsApp ou e-mail.', 'Nous vous disons honnêtement si nous pouvons aider.', 'Les conditions sont convenues avec vous avant le début du travail.', 'Nous passons par les procédures officielles de la plateforme. C’est elle qui décide, et personne ne peut promettre le résultat.']), safe=None),
}
FR_TAIL = ('<h2 id="prudence">Restez prudent</h2><p>Personne n’a besoin de votre mot de passe ni de vos codes de connexion pour vous aider. Si quelqu’un vous propose en message privé de tout régler, vous demande de vous connecter via un lien ou dit avoir un contact chez Meta, ne donnez pas suite. Unbanz ne demande jamais vos identifiants et n’a aucun accès particulier : nous utilisons les mêmes procédures officielles que vous.</p>'
  '<h2 id="a-propos">À propos d’Unbanz</h2><p>Unbanz (unbanz.com) est un service indépendant qui aide particuliers, entreprises et agences pour les comptes Instagram, Facebook et Snapchat désactivés, les demandes de pseudo et la récupération de comptes publicitaires Meta. Contact : WhatsApp +1 934 201 2490 ou team@unbanz.com. Non affilié à Meta. Ce n’est pas un conseil juridique.</p>')
P = []
def page(lang, slug, title, desc, h1, crumb, answer, sections, faq, related): P.append(dict(lang=lang, slug=slug, title=title, desc=desc, h1=h1, crumb=crumb, answer=answer, sections=sections, faq=faq, related=related))
def build(p):
    C = CFG[p['lang']]; t = open(os.path.join(ROOT, C['tpl'], 'index.html'), encoding='utf-8').read()
    url = 'https://unbanz.com/%s/%s/' % (p['lang'], p['slug']); turl = 'https://unbanz.com/%s/' % C['tpl']
    head, rest = t.split('<main id="content">', 1); main, foot = rest.split('</main>', 1)
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % E(p['title']), head, 1, re.S)
    for k in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'<meta %s content="[^"]*">' % k, '<meta %s content="%s">' % (k, E(p['desc'])), head, 1)
    for k in ('property="og:title"', 'name="twitter:title"'):
        head = re.sub(r'<meta %s content="[^"]*">' % k, '<meta %s content="%s">' % (k, E(p['title'])), head, 1)
    head = head.replace(turl, url)
    m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', head, re.S)
    g = json.loads(m.group(2).replace('<\\/', '</'))['@graph']
    base = [x for x in g if x['@type'] in ('Organization', 'WebSite')]
    wp = [x for x in g if x['@type'] == 'WebPage'][0]; wp.update(name=p['title'], description=p['desc'], dateModified='2026-10-29', datePublished='2026-10-29')
    bc = {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': C['home'], 'item': 'https://unbanz.com/%s/' % p['lang']},
        {'@type': 'ListItem', 'position': 2, 'name': C['crumb2'][0], 'item': 'https://unbanz.com' + C['crumb2'][1]},
        {'@type': 'ListItem', 'position': 3, 'name': p['crumb'], 'item': url}]}
    fq = {'@type': 'FAQPage', '@id': url + '#faq', 'url': url, 'inLanguage': p['lang'], 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in p['faq']]}
    ld = json.dumps({'@context': 'https://schema.org', '@graph': base + [wp, bc, fq]}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    head = head[:m.start(2)] + ld + head[m.end(2):]
    hero = re.search(r'<section class="service-hero">.*?</section>', main, re.S).group(0)
    hero = re.sub(r'<h1>.*?</h1><p>.*?</p>', '<h1>%s</h1><p>%s</p>' % (E(p['h1']), E(p['answer'])), hero, 1, re.S)
    art = re.search(r'<article class="guide-body container">(.*?)</article>', main, re.S).group(1)
    tail = art[art.find('<h2 id="voorzichtig">'):] if C['safe'] else FR_TAIL
    secs = ''.join('<h2 id="s%d">%s</h2>%s' % (i, E(h), b if b.startswith('<') else '<p>%s</p>' % b) for i, (h, b) in enumerate(p['sections']))
    how = '<h2 id="met-unbanz">%s</h2>%s' % (C['how'][0], ol(C['how'][1]))
    faqs = re.search(r'<section class="faq-section".*?</section>', main, re.S).group(0)
    faqs = re.sub(r'<div class="simple-faq">.*</div></div></section>$', '<div class="simple-faq">%s</div></div></section>' % ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (E(q), E(a)) for q, a in p['faq']), faqs, flags=re.S)
    proof = re.search(r'<section class="service-proof container">.*?</section>', main, re.S).group(0)
    nav = '<nav class="related-services container" aria-label="%s">%s</nav>' % (E(C['rel']), ''.join(A(u, E(x)) for u, x in p['related']))
    out = head + '<main id="content">' + hero + '<article class="guide-body container">' + secs + how + tail + '</article>' + faqs + proof + nav + '</main>' + foot
    assert out.count(url) >= 4 and turl not in out and '7723' not in out, p['slug']
    return out
def run():
    TR = set(l for l in subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n'))
    for p in P:
        f = '%s/%s/index.html' % (p['lang'], p['slug'])
        if f in TR and not os.environ.get('REBUILD'): raise SystemExit('COLLISION ' + f)
        for u, _ in p['related']:
            assert os.path.exists(os.path.join(ROOT, u.strip('/'), 'index.html')) or u.strip('/').split('/')[-1] in [q['slug'] for q in P], (p['slug'], u)
        assert len(p['title']) <= 65 and len(p['desc']) <= 160, (p['slug'], len(p['title']), len(p['desc']))
    for p in P:
        os.makedirs(os.path.join(ROOT, p['lang'], p['slug']), exist_ok=True); write_page(os.path.join(ROOT, p['lang'], p['slug'], 'index.html'), build(p))
    return ['https://unbanz.com/%s/%s/' % (p['lang'], p['slug']) for p in P]
