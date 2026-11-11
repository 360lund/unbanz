import sys,re,os,html; sys.path.insert(0,'/workspace/site/scripts/nov11')
import gen
from common import *
import b_country,b_misc,b_i18n
SITE='/workspace/site'
built=[]
for mod in (b_country,b_misc,b_i18n):
    for p in mod.PAGES:
        p=dict(p); dg=p.pop('_degroup',None)
        gen.build(p); built.append((p['slug'],dg))
# DE hub
de_pages=[p['slug'] for p in b_i18n.PAGES if p.get('lang')=='de']
def t_of(s):
    t=open(f'{SITE}/{s}/index.html').read(); return html.unescape(re.search(r'<title>(.*?)</title>',t).group(1))
hub=dict(slug='de',lang='de',sv='unban',crumb=('Start','/de/'),crumbtxt='Start',title='Unbanz auf Deutsch: Konto gesperrt, gehackt oder deaktiviert?',short='Unbanz auf Deutsch',
 desc='Hilfe auf Deutsch für gesperrte, deaktivierte und gehackte Instagram-, Facebook-, TikTok- und YouTube-Konten, Facebook-Seiten und Werbekonten. Festpreise, 100 % Rückerstattung.',
 h1='Konto gesperrt, gehackt oder deaktiviert?',lede='Ratgeber auf Deutsch und Wiederherstellung zum Festpreis, im Voraus bezahlt, mit 100 % Rückerstattung bei Misserfolg.',
 answer='<strong>Unbanz ist ein unabhängiger Dienst, der gesperrte, deaktivierte und gehackte Konten über die offiziellen Verfahren der Plattformen zurückholt.</strong> Festpreise: Instagram 800 $, Facebook 900 $, Facebook-Seite 600 $, Werbekonto 1.200 $, Business-Portfolio 1.500 $, Nutzername 1.200 $, TikTok 900 $, YouTube 1.200 $. Zahlung im Voraus, 100 % Rückerstattung, wenn der Fall scheitert. Wir fragen nie nach Passwörtern.',
 cards=[('Festpreise','Vorher bekannt.'),('100 % zurück','Bei Misserfolg.'),('Keine Passwörter','Niemals.')],
 sections=[('ratgeber','Ratgeber auf Deutsch',ul([a('/'+s+'/',html.escape(t_of(s))) for s in de_pages])),
  ('kontakt','Kontakt','<p>Schick einen Screenshot der Meldung, den Nutzernamen oder Link und dein Land an <a href="mailto:team@unbanz.com">team@unbanz.com</a>. Wir antworten ehrlich, ob wir den Fall übernehmen können.</p>')],
 faqs=[('Ist Unbanz Meta oder TikTok?','Nein. Unbanz ist unabhängig.'),('Wie lange dauert es?','Meist 3–7 Tage ab Start, ohne Garantie.')])
gen.build(hub); built.append(('de','home'))
# ---------- hreflang groups
ALT=re.compile(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\s*')
def path_of(url): 
    p=url.replace('https://unbanz.com/','').strip('/'); return f'{SITE}/{p}/index.html' if p else f'{SITE}/index.html'
def read_alts(f): return re.findall(r'<link rel="alternate" hreflang="([^"]*)" href="([^"]*)">',open(f).read())
def write_group(pairs):
    tags=''.join(f'<link rel="alternate" hreflang="{l}" href="{u}">' for l,u in pairs)
    members={u for l,u in pairs if l!='x-default'}
    n=0
    for u in members:
        f=path_of(u)
        if not os.path.exists(f): print('MISSING',u); continue
        t=open(f).read(); t2=ALT.sub('',t)
        t2=t2.replace('<link rel="canonical"',tags+'<link rel="canonical"',1)
        if t2!=t: open(f,'w').write(t2); n+=1
    return n
U=lambda s:'https://unbanz.com/'+s.strip('/')+'/' if s else 'https://unbanz.com/'
for key,g in b_i18n.G.items():
    pairs=[(gen.HL[l],U(s)) for l,s in g.items()]+[('x-default',U(g['en']))]
    print('group',key,write_group(pairs))
for slug,dg in built:
    if dg is None: continue
    en_slug = '' if dg=='home' else dg
    base=read_alts(path_of(U(en_slug)))
    if not base: base=[('en',U(en_slug)),('x-default',U(en_slug))]
    base=[(l,u) for l,u in base if l!='de']
    xd=[x for x in base if x[0]=='x-default']; rest=[x for x in base if x[0]!='x-default']
    pairs=rest+[('de',U(slug))]+xd
    print('degroup',slug,write_group(pairs))
open('/workspace/aeo_nov11/built2.txt','w').write('\n'.join(s for s,_ in built))
print(len(built))
