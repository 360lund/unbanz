import sys,os,re,zlib;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod
ns={};exec(open('scripts/nov04m/fanout2.py').read().split('P={')[0],ns);g=ns;A=g['A'];qa=g['qa']
u={};[exec(x,u) for x in open('scripts/nov04m/fanout4.py').read().split('\n') if x[:3] in ('UI=','UT=','UTM','US=')]
l={};[exec(x,l) for x in open('scripts/nov04m/fanout6.py').read().split('\n') if x[:3] in ('L1=','L2=','L3=')]
UN=[u[k] for k in ('UI','UT','UTM','US')];LO=[l[k] for k in ('L1','L2','L3')]
SKIP=re.compile(r'^(about|contact|faq|pricing|privacy|terms|reviews|services|site-map|trustpilot|refund-policy|how-it-works|is-unbanz-legit|guides|unban-pricing|username-claim-pricing|meta-appeal-links-and-forms-directory)$|unbanz-vs|tiktok|whatsapp|threads|sextortion|harassment|copyright|scam-dm|memorial|white-label|agency|client-|partner|recovery-job|police|ftc-|ico-|gdpr|fake-ban|deactivate-or-delete|download-your-data|reach-drop|account-recovery-by-country|dubai|abu-dhabi|is-an-unban|ways-to-get|how-much|best-username|glossary|notice-types|removed-post|-cost')
def pick(p):
    if re.search(r'^ad-|meta-ad|meta-business|pixel|guides/meta-|guides/ad-|advertise|business-manager|ad-account|ads-charged|meta-support-chat',p): return 'ad',[g['ADR'],g['ADAC'],g['ADT'],g['ADV']]
    if 'username' in p or 'og-' in p: return 'un',UN
    if 'hack' in p: return 'ac',[g['HACK'],LO[2],LO[1]]
    if re.search(r'lost-access|email|phone|two-factor|code|password|log-in|login|reset',p): return 'ac',LO+[g['NOID']]
    if re.search(r'selfie|id-|verification|human',p): return 'ac',[g['VER'],g['NOID'],g['TIME']]
    if re.search(r'instagram|facebook|disabled|suspended|appeal|account',p): return 'ac',[g['AC'],g['TIME'],g['ACE'],g['NOID']]
    return None,None
lim=int(sys.argv[1]);out=sys.argv[2]
todo=[]
for f in sorted(__import__('glob').glob('**/index.html',recursive=True)):
    p=f[:-11]
    if not p or p.split('/')[0] in ('fr','nl','es','pt-br','users','api','node_modules') or SKIP.search(p): continue
    s=open(f).read()
    if 'noindex' in s[:3000] or re.search(r'id="[a-z-]*-2026"',s): continue
    k,it=pick(p)
    if k: todo.append((p,k,it,s))
urls=[]
for p,k,it,s in todo[:lim]:
    it=[x for x in it if x[0] not in s];r=zlib.crc32(p.encode())%len(it) if it else 0
    it=(it[r:]+it[:r])[:3]
    if not it: continue
    t={'ad':'Ad account questions people also ask (2026)','un':'Username questions people also ask (2026)','ac':'Questions people also ask (2026)'}[k]
    if add_section(p,qa(t,it,''),anchor=A): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls),'remaining',len(todo)-lim);open(out,'w').write('\n'.join(urls))
