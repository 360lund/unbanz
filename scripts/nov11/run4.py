import sys,os,re,json,glob,shutil; sys.path.insert(0,'/workspace/site/scripts/nov11')
import gen,b4
os.chdir('/workspace/site')
out=[]
for p in b4.PAGES:
    p=dict(p); gen.build(p); out.append(p['slug'])
# redirects
vj=json.load(open('vercel.json')); rd=vj.setdefault('redirects',[])
have={r['source'] for r in rd}
for old,new in b4.REDIRECT.items():
    for s in (f'/{old}',f'/{old}/'):
        if s not in have: rd.append({'source':s,'destination':new,'permanent':True})
json.dump(vj,open('vercel.json','w'),indent=2,ensure_ascii=False)
for old in b4.REDIRECT:
    if os.path.isdir(old): shutil.rmtree(old)
# internal links site-wide
anch={}
for old,new in b4.REDIRECT.items():
    m=old.replace('meta-appeal-links-','')
    anch[old]=new+('#'+m if new!='/meta-appeal-links-and-forms-directory/' else '')
pat=re.compile(r'(href="(?:https://unbanz\.com)?/)(meta-appeal-links-(?:'+'|'.join(re.escape(o.replace('meta-appeal-links-','')) for o in b4.REDIRECT)+r'))/"')
n=0
for f in glob.glob('**/*.html',recursive=True)+['llms.txt','llms-full.txt']:
    t=open(f).read()
    t2=pat.sub(lambda m:m.group(1)+anch[m.group(2)].lstrip('/')+'"',t)
    t2=re.sub(r'https://unbanz\.com/(meta-appeal-links-(?:'+'|'.join(re.escape(o.replace('meta-appeal-links-','')) for o in b4.REDIRECT)+r'))/',lambda m:'https://unbanz.com'+anch[m.group(1)],t2) if f.endswith('.txt') else t2
    if t2!=t: open(f,'w').write(t2); n+=1
open('/workspace/aeo_nov11/built4.txt','w').write('\n'.join(out)+'\n')
print('built',len(out),'linkfiles',n)
