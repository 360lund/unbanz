import re, os, sys
R = [
 (re.compile(r'"telephone": ?"\+?1?[-\s]?934[-\s]?201[-\s]?2490",\s?'), ''),
 (re.compile(r',\s?"telephone": ?"\+?1?[-\s]?934[-\s]?201[-\s]?2490"'), ''),
 (re.compile(r'"(url|serviceUrl)": ?"https://wa\.me/19342012490"'), r'"\1":"mailto:team@unbanz.com"'),
]
n=0
for root in sys.argv[1:]:
  for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d not in ('.git','node_modules')]
    for f in fn:
      if not f.endswith('.html'): continue
      p=os.path.join(dp,f); t=open(p,encoding='utf-8').read(); o=t
      for r,s in R: t=r.sub(s,t)
      if t!=o: open(p,'w',encoding='utf-8').write(t); n+=1
print(n)
