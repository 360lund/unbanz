import os,re,glob
os.chdir('/workspace/site');n=0
for f in glob.glob('**/index.html',recursive=True):
    s=open(f).read();ch=False
    for aid in ['compared-2026','quick-answers-2026','updated-2026']:
        i=s.find(f'<h2 id="{aid}">')
        if i<0: continue
        sec=s.rfind('<section',0,i)
        if 'service-editorial' not in s[sec:sec+80]: continue
        e1=s.find('</article>',i);e2=s.find('<h2 id="about-unbanz">',i);e=min(x for x in [e1,e2] if x>0)
        blk=s[i:e];s=s[:i]+s[e:]
        se=s.find('</section>',i)+10
        s=s[:se]+'<article class="guide-body container">'+blk+'</article>'+s[se:];ch=True
    if ch: open(f,'w').write(s);n+=1;print(f)
print(n)
