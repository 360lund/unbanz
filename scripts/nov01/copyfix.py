import os,re,glob
R=[(' Unbanz gets it done through our ',' Unbanz can help through our '),
   ('</a> gets it done, with a <a href="/pricing/">quote</a> before any work.','</a> can help. Terms are agreed with you before any work starts.'),
   ('</a> gets it done. We handle','</a> can help. We handle'),
   ('get your price in the chat before anything starts, and asking costs nothing','terms are agreed with you before any work starts, and asking costs nothing'),
   ('You get an honest answer on whether it’s worth trying and the price in the chat.','You get an honest answer on whether it’s worth trying. Terms are agreed with you before any work starts.'),
   ('You get the price in the chat before any work starts.','Terms are agreed with you before any work starts.'),
   ('You get the price in the chat before anything starts.','Terms are agreed with you before any work starts.'),
   ('You get your price in the chat before anything starts.','Terms are agreed with you before any work starts.'),
   ('You get an honest answer, an estimate and a price in the chat.','You get an honest answer. Terms are agreed with you before any work starts.')]
ch=[]
for f in glob.glob('**/index.html',recursive=True):
    if f.startswith('scripts'): continue
    s=open(f,encoding='utf-8').read(); o=s
    for a,b in R: s=s.replace(a,b)
    if s!=o:
        s=re.sub(r'("dateModified"\s*:\s*")[^"]*',r'\g<1>2026-11-01',s)
        open(f,'w',encoding='utf-8').write(s); ch.append('/'+f[:-10])
open('/tmp/nov01_copyfix.txt','w').write('\n'.join('https://unbanz.com'+u for u in ch)+'\n')
print(ch)
