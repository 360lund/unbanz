import re,json,sys
n=0
for p in open('/workspace/refreshed.txt').read().split():
    f=p+'/index.html';h=open(f).read()
    m=re.search(r'id="updated-nov-2026">Updated November 2026</h2><p>.*?</p><h3>(.*?)</h3><p>(.*?)</p>',h,re.S)
    if not m: print('nosec',p);continue
    q=re.sub('<[^>]+>','',m.group(1));a=re.sub('<[^>]+>','',m.group(2))
    i=h.find('"FAQPage"')
    if i<0: print('nofaq',p);continue
    j=h.find('"mainEntity"',i);k=h.find('[',j)+1
    if json.dumps(q,ensure_ascii=False) in h[k:k+20000] or j<0: continue
    qj=json.dumps({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}},ensure_ascii=False,separators=(',',':'))
    h=h[:k]+qj+','+h[k:];open(f,'w').write(h);n+=1
print(n)
