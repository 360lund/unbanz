import sys, re
from nlib import *
import importlib
for m in sys.argv[1:]: importlib.import_module('p_'+m)
def wc(s): return len(re.sub(r'<[^>]+>',' ',s).split())
BANN = r'\b(snel\w*|rápid\w*|rapide\w*|vite|vaste? (prijs|tarief)|prix fixe|precio fijo|preço fixo|garanti\w*|garantí\w*|garantiz\w*|garantid\w*|cases?|casos?|cas|caso|zaken?|dagen|días|dias|jours|semana|week|semaine|beoordel\w*|revis\w*|examin\w*)\b|—|[\U0001F300-\U0001FAFF]'
for lg,pgs in PAGES.items():
    for k,p in pgs.items():
        a=wc(' '.join(p['answer'])); 
        flag='' if 40<=a<=60 else ' ANSWER=%d'%a
        txtall=' '.join([p['title'],p['desc'],p['h1'],p['hero'],' '.join(p['answer']),' '.join(c for x in p['cards'] for c in x),' '.join(b for _,h,b in p['secs']),' '.join(q+' '+an for q,an in p['faq'])])
        hits=[m.group(0) for m in re.finditer(BANN,txtall,re.I)]
        body=sum(wc(b) for _,_,b in p['secs'])
        print(lg,k,'ans',a,'body',body,'faq',len(p['faq']),'title',len(p['title']),'desc',len(p['desc']),flag,hits)
