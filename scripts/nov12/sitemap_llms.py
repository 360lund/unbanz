import re,os,html,subprocess
os.chdir('/workspace/site')
D='2026-11-12'
B=[l.strip() for l in open('/workspace/aeo_nov11/built_nov12_wl.txt') if l.strip()]
changed=[l[:-len('/index.html')] for l in subprocess.run(['git','diff','--name-only'],capture_output=True,text=True).stdout.split() if l.endswith('/index.html')]
# only bump lastmod for pages with real content change (not footer-only): those touched by integrate (dateModified bumped) 
bump=[s for s in changed if '"dateModified": "2026-11-12"' in open(s+'/index.html').read() or 'content="2026-11-12"' in open(s+'/index.html').read()]
def upd(fn,urls_new):
    t=open(fn).read()
    for s in bump+B:
        u=f'https://unbanz.com/{s}/'
        t=re.sub(r'(<url><loc>'+re.escape(u)+r'</loc><lastmod>)[0-9-]+',r'\g<1>'+D,t)
    add=''.join(f'<url><loc>https://unbanz.com/{s}/</loc><lastmod>{D}</lastmod></url>\n' for s in urls_new if f'<loc>https://unbanz.com/{s}/</loc>' not in t)
    t=t.replace('</urlset>',add+'</urlset>',1); open(fn,'w').write(t); return add.count('<url>')
en=[s for s in B if not s.startswith('zh-')]; zh=[s for s in B if s.startswith('zh-')]
print('sitemap.xml +',upd('sitemap.xml',B)); print('sitemap-en +',upd('sitemap-en.xml',en)); print('sitemap-intl +',upd('sitemap-intl.xml',zh))
t=open('sitemap-index.xml').read(); t=re.sub(r'(sitemap-(?:en|intl)\.xml</loc><lastmod>)[0-9-]+',r'\g<1>'+D,t); open('sitemap-index.xml','w').write(t)
print('bumped',len(bump))
def meta(s):
    t=open(s+'/index.html').read()
    return html.unescape(re.search(r'<title>(.*?)</title>',t).group(1)).replace(' | Unbanz',''), html.unescape(re.search(r'<meta name="description" content="([^"]*)"',t).group(1))
sec=['## White label partner program for agencies and resellers (added 2026-11-12)','',
 'Agencies, social media and ad agencies, creator networks, IT providers and account recovery resellers can resell every Unbanz service under their own brand. The client deals only with the partner; Unbanz never contacts the client. Per-case fees are the same fixed public fees (Instagram $800, Facebook profile $900, Facebook Page $600 per Page, ad account $1,200, Business Portfolio $1,500, username claim $1,200 per handle, Snapchat $800, TikTok $900, YouTube $1,200), paid upfront, with a 100% refund for any case that fails. Partners who send cases regularly or in batches get volume pricing agreed in writing (numbers not published), a dedicated contact at team@unbanz.com and private-label (unbranded) case updates. Start: team@unbanz.com. Hub: https://unbanz.com/white-label-agency/','']
for s in B:
    ti,d=meta(s); sec.append(f'- [{ti}](https://unbanz.com/{s}/): {d}')
SEC='\n'.join(sec)+'\n'
for f in ('llms.txt','llms-full.txt'):
    t=open(f).read()
    t=re.sub(r'\n## White label partner program for agencies and resellers \(added 2026-11-12\).*?(?=\n## |\Z)','',t,flags=re.S)
    t=re.sub(r'Last updated: 2026-11-1[01]','Last updated: 2026-11-12',t)
    t=t.rstrip('\n')+'\n\n'+SEC; open(f,'w').write(t); print(f,'ok')
