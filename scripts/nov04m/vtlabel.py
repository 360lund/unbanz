import re,glob,html
R=re.compile(r'(<button class="vt-play" type="button" aria-label=")([^"]*)(">)<b>([^<]*)</b>')
n=0;files=[]
for f in glob.glob('**/index.html',recursive=True):
    s=open(f).read()
    def fx(m):
        lab,b=m.group(2),m.group(4);bt=html.unescape(b)
        if html.unescape(lab).lower().startswith(bt.lower()): return m.group(0)
        l=lab[0].lower()+lab[1:]
        return f'{m.group(1)}{b}: {l}{m.group(3)}<b>{b}</b>'
    t=R.sub(fx,s)
    if t!=s: open(f,'w').write(t);files.append(f);n+=1
print(n)
