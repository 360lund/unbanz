import sys,re,os,html,glob; sys.path.insert(0,'/workspace/site/scripts/nov11')
import gen,gen2,b5
SITE='/workspace/site'
exec(open('run3.py').read().split('# ---------- hreflang merge')[1].split('for slug,en in built:')[0])
built=[]
for p in b5.P:
    p=dict(p); en=p.pop('_en'); gen2.build(p); built.append((p['slug'],en))
for slug,en in built:
    base=read_alts(path_of(U(en)))
    if not base: base=[('en',U(en)),('x-default',U(en))]
    lang=slug.split('/')[0]; hl=gen.HL[lang]
    base=[(l,u) for l,u in base if l!=hl]
    xd=[x for x in base if x[0]=='x-default']; rest=[x for x in base if x[0]!='x-default']
    write_group(rest+[(hl,U(slug))]+xd)
REV={v:k for k,v in gen.HL.items()}
# relocalize every member of touched groups in de/ar/it/tr
touched=set()
for slug,en in built:
    for l,u in read_alts(path_of(U(slug))): touched.add(u.replace('https://unbanz.com/','').strip('/'))
for s in touched:
    lang=s.split('/')[0]
    if lang not in ('de','ar','it','tr'): continue
    f=f'{SITE}/{s}/index.html'; t=open(f).read(); alts={}
    for l,u in read_alts(f):
        if l in REV: alts[REV[l]]=u.replace('https://unbanz.com/','').strip('/')
    open(f,'w').write(gen2.localize(t,lang,alts))
# hub links
HT={'fr':'Nouveaux guides','es':'Guías nuevas','pt-br':'Guias novos','de':'Neue Ratgeber','it':'Nuove guide','tr':'Yeni rehberler'}
def t_of(s): return html.unescape(re.search(r'<title>(.*?)</title>',open(f'{SITE}/{s}/index.html').read()).group(1))
for l,h in HT.items():
    f=f'{SITE}/{l}/index.html'; t=open(f).read()
    t=re.sub(r'<section class="container" data-nov11="r4".*?</section>','',t,flags=re.S)
    items=''.join(f'<li>{gen.a("/"+s+"/",html.escape(t_of(s)))}</li>' for s,_ in built if s.startswith(l+'/'))
    sec=f'<section class="container" data-nov11="r4" style="padding:32px 0"><h2>{h}</h2><ul>{items}</ul></section>'
    i=t.find('<section class="faq-section"'); 
    if i<0: i=t.find('</main>')
    t=t[:i]+sec+t[i:]; open(f,'w').write(t)
open('/workspace/aeo_nov11/built5.txt','w').write('\n'.join(s for s,_ in built)+'\n')
print('built',len(built),'touched',len(touched))
