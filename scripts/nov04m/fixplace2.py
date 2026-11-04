import re,glob
AN=['related-2026','sub-questions-2026','local-questions-2026','quick-answers-2026','updated-2026','compared-2026']
n=0;out=[]
for f in glob.glob('**/index.html',recursive=True):
    s=open(f).read();o=s
    for a in AN:
        pat=f'<article class="guide-body container"><h2 id="{a}">'
        i=s.find(pat)
        if i<0: continue
        vt=s.find('<section class="vt')
        if vt<0 or i<vt: continue
        j=s.find('</article>',i)+10;blk=s[i+len('<article class="guide-body container">'):j-10]
        s=s[:i]+s[j:]
        ab=s.find('<h2 id="about-unbanz">')
        if ab<0 or ab>s.find('<section class="vt'): s=s[:i]+pat[:-len(f'<h2 id="{a}">')]+blk+'</article>'+s[i:];continue
        s=s[:ab]+blk+s[ab:]
    if s!=o: open(f,'w').write(s);n+=1;out.append(f)
print(n);print(out[:5])
