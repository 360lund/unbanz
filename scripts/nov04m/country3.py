import sys,os;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod
ns={};exec(open('scripts/nov04m/country.py').read().split('T={}')[0],ns)
A=ns['A'];ads=ns['ads'];C=ns['C']
T={f'white-label-agency-{c}':ads(c)[:3] for c in C}
T['meta-business-verification-documents-uk-eu-us']=[(f'Which documents work in {C[c]["n"]}?',f'Usually {C[c]["doc"]}, with the legal name and address matching the business portfolio exactly.') for c in C]
urls=[]
for p,it in T.items():
    if not os.path.exists(p+'/index.html'): print('skip',p);continue
    s=open(p+'/index.html').read();it=[x for x in it if x[0] not in s]
    b=f'<h2 id="{A}">Local questions, answered (2026)</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in it)
    if it and add_section(p,b,anchor=A): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b14.txt','w').write('\n'.join(urls))
