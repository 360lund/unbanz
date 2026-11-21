# Nov 20 2026: link agency Q&A pages from /white-label-agency/, homepage pricing-card agency CTA (en/fr/nl/es/pt-br),
# sitemaps and llms files. Idempotent.
import os, re, sys, urllib.parse, html
sys.path.insert(0, os.path.dirname(__file__))
from qa_agency import P
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); os.chdir(ROOT)
B = 'https://unbanz.com/'; TODAY = '2026-11-20'
rd = lambda f: open(f, encoding='utf8').read()
def wr(f, s): open(f, 'w', encoding='utf8').write(s)
esc = lambda t: html.escape(t, quote=True)
# 1. hub
f = 'white-label-agency/guides/index.html'; s = rd(f)
if 'id="agency-questions"' not in s:
    s = s.replace('<a href="#agency-guides">', '<a href="#agency-questions">Agency questions answered</a><a href="#agency-guides">', 1)
    blk = ('<h2 id="agency-questions">Agency questions answered</h2><p>Direct answers to what agencies ask before handing a client account to a white-label partner: how it works, what it costs, which platforms and how to vet a partner.</p><ul>'
           + ''.join(f'<li><a href="/{p["slug"]}/">{esc(p["q"])}</a></li>' for p in P) + '</ul>')
    s = s.replace('<h2 id="agency-guides">', blk + '<h2 id="agency-guides">', 1)
    s = re.sub(r'("dateModified":")[0-9-]+(")', r'\g<1>' + TODAY + r'\2', s)
    s = re.sub(r'(<meta content=")[0-9-]+(" property="article:modified_time"/>)', r'\g<1>' + TODAY + r'\2', s)
    wr(f, s)
# 2. homepage pricing card CTA
CH = {'': ('$1,200 per case','Usually 7–14 days','Refund if not reinstated'), 'fr': ('1 200 $ par dossier','7 à 14 jours en général','Remboursé si non rétabli'), 'nl': ('$1.200 per zaak','Meestal 7–14 dagen','Terugbetaald als niet hersteld'), 'es': ('1.200 $ por caso','Normalmente 7–14 días','Reembolso si no se recupera'), 'pt-br': ('US$ 1.200 por caso','Em geral 7–14 dias','Reembolso se não restaurar')}
H = {
 '': ('AGENCIES &amp; WHITE-LABEL', 'Need white-label recovery for clients?', 'For PR firms, talent managers, SMMAs and recovery agencies. You keep the client; we handle the platform work quietly, under your brand.', 'Agency program', 'Email us', '/white-label-agency/', 'White-label agency enquiry', 'Hi Unbanz, I run an agency and want white-label account recovery for our clients.\n\nAgency name: \nWebsite: \nCases per month (approx.): \n\nThanks'),
 'fr': ('AGENCES &amp; MARQUE BLANCHE', 'Besoin de récupération en marque blanche pour vos clients ?', 'Pour les agences RP, managers de talents, agences marketing et de récupération : nous gérons les plateformes en coulisses, vous gardez le client.', 'Programme agences', 'Écrivez-nous', '/fr/white-label-agences/', 'Agence marque blanche - demande', 'Bonjour Unbanz, je gère une agence et je veux proposer la récupération de comptes en marque blanche.\n\nAgence : \nSite web : \nDossiers par mois (env.) : \n\nMerci'),
 'nl': ('BUREAUS &amp; WHITE-LABEL', 'White-label herstel nodig voor je klanten?', 'Voor PR-bureaus, talentmanagers, marketing- en herstelbureaus: wij doen het platformwerk achter de schermen, jij houdt de klant.', 'Bureauprogramma', 'Mail ons', '/nl/white-label-bureau/', 'White-label bureau - aanvraag', 'Hoi Unbanz, ik heb een bureau en wil white-label accountherstel voor onze klanten.\n\nBureau: \nWebsite: \nZaken per maand (ong.): \n\nBedankt'),
 'es': ('AGENCIAS Y MARCA BLANCA', '¿Necesitas recuperación en marca blanca para tus clientes?', 'Para agencias de RR. PP., representantes de talento, agencias de marketing y de recuperación: hacemos el trabajo con la plataforma, tú te quedas con el cliente.', 'Programa para agencias', 'Escríbenos', '/es/white-label-agencias/', 'Agencia marca blanca - consulta', 'Hola Unbanz, tengo una agencia y quiero recuperación de cuentas en marca blanca para nuestros clientes.\n\nAgencia: \nWeb: \nCasos al mes (aprox.): \n\nGracias'),
 'pt-br': ('AGÊNCIAS E WHITE-LABEL', 'Precisa de recuperação white-label para seus clientes?', 'Para agências de RP, gestores de talentos, agências de marketing e de recuperação: fazemos o trabalho com a plataforma, você fica com o cliente.', 'Programa para agências', 'Envie um e-mail', '/pt-br/white-label-agencias/', 'Agência white-label - contato', 'Olá Unbanz, tenho uma agência e quero recuperação de contas white-label para nossos clientes.\n\nAgência: \nSite: \nCasos por mês (aprox.): \n\nObrigado'),
}
CSS = ('<style id="pn-ag-css">.price-notes .pn-agency{position:relative;overflow:hidden;margin-top:4px;padding:28px;border-radius:24px;color:#fff;background:radial-gradient(90% 140% at 100% 0%,#2a6489 0%,rgba(42,100,137,0) 62%),linear-gradient(135deg,#10344c 0%,#153d55 100%);box-shadow:0 24px 48px -30px rgba(16,52,76,.6)}'
       '.pn-agency .pn-eye{margin:0 0 10px;font-size:12px;font-weight:600;letter-spacing:.12em;color:#9fc9e6}.price-notes .pn-agency h3{margin:0;font-size:clamp(22px,2.2vw,28px);font-weight:400;line-height:1.18;letter-spacing:-.035em;color:#fff}'
       '.price-notes .pn-agency p.pn-d{margin:10px 0 0;color:#c9dfee;font-size:15px;line-height:1.55}.pn-agency .pn-chips{list-style:none;padding:0;margin:16px 0 0;display:flex;flex-wrap:wrap;gap:6px}'
       '.pn-agency .pn-chips li{font-size:13px;padding:6px 12px;border-radius:999px;background:rgba(255,255,255,.1);color:#e3eef6;box-shadow:inset 0 0 0 1px rgba(255,255,255,.14)}'
       '.pn-agency .pn-act{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}.pn-agency .pn-act a{display:inline-flex;align-items:center;justify-content:center;gap:6px;min-height:46px;padding:10px 20px;border-radius:999px;font-size:15px;font-weight:600;text-decoration:none;white-space:nowrap}'
       '.pn-agency .pn-more{background:#fff;color:#10344c}.pn-agency .pn-mail{background:transparent;color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.38)}'
       '@media(max-width:650px){.price-notes .pn-agency{padding:22px 20px}.pn-agency .pn-act a{flex:1 1 100%}}</style>')
OLD = re.compile(r'<div class="pn-agency" data-ag="nov20">.*?</div></div><style id="pn-ag-css">.*?</style>', re.S)
for pre, (e, h, d, more, mail, href, subj, body) in H.items():
    f = (pre + '/' if pre else '') + 'index.html'; s = rd(f)
    m = 'mailto:team@unbanz.com?subject=' + urllib.parse.quote(subj) + '&amp;body=' + urllib.parse.quote(body)
    blk = (f'<div class="pn-agency" data-ag="nov20"><p class="pn-eye">{e}</p><h3>{h}</h3><p class="pn-d">{d}</p><ul class="pn-chips">' + ''.join(f'<li>{c}</li>' for c in CH[pre]) + '</ul><div class="pn-act">'
           f'<a class="pn-more" href="{href}">{more} <span aria-hidden="true">→</span></a><a class="pn-mail" data-service="white-label" href="{m}">{mail} <span aria-hidden="true">↗︎</span></a></div></div>' + CSS)
    if OLD.search(s): s2 = OLD.sub(lambda _: blk, s, count=1)
    else:
        i = s.find('<div class="price-notes">'); assert i > 0, f
        j = s.find('</div></section>', i); assert j > 0
        s2 = s[:j] + blk + s[j:]
    if s2 != s: wr(f, s2); print('home', f)
# 3. sitemaps
for sm in ('sitemap.xml', 'sitemap-en.xml'):
    s = rd(sm); add = ''
    for p in P:
        u = B + p['slug'] + '/'
        if f'<loc>{u}</loc>' not in s: add += f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n'
    for hu in ('white-label-agency/', ''):
        s = re.sub(r'(<loc>' + re.escape(B + hu) + r'</loc><lastmod>)[^<]+', r'\g<1>' + TODAY, s)
    s = s.replace('</urlset>', add + '</urlset>', 1); wr(sm, s)
s = rd('sitemap-index.xml'); wr('sitemap-index.xml', re.sub(r'<lastmod>[^<]+</lastmod>', f'<lastmod>{TODAY}</lastmod>', s))
# 4. llms
blk = '\n## Agency and white-label questions answered (Nov 20 2026)\n' + ''.join(f'- [{p["q"]}]({B}{p["slug"]}/): {p["desc"]}\n' for p in P)
for f in ('llms.txt', 'llms-full.txt'):
    s = rd(f)
    if 'Agency and white-label questions answered (Nov 20 2026)' not in s: wr(f, s.rstrip('\n') + '\n' + blk)
print('ok')
