import sys; sys.path.insert(0,'.')
import importlib, re
from lib import REG, resolve
from check import scan
for m in sys.argv[1:]: importlib.import_module(m)
n=0
for s in REG.values():
    blob=' '.join([s['title'],s['desc'],s['h1'],s['hero'],s['answer'],s['blurb']]+[a+b for a,b in s['cards']]+[h+c for _,h,c in s['sections']]+[q+a for q,a in s['faq']])
    for p,c in scan(blob,s['slug']): print(s['slug'],p,'|',c); n+=1
    w=len(re.sub(r'<[^>]+>',' ',' '.join(c for _,_,c in s['sections'])).split())
    print(s['slug'],'words',w, 'answer',len(s['answer'].split()))
print('bad',n)
