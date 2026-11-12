import sys,re,json,html,os,glob
sys.path.insert(0,'/workspace/site/scripts/nov11'); sys.path.insert(0,'/workspace/site/scripts/nov12')
import gen,gen2
from gen import a,ul
D='2026-11-12'; gen.D=D
gen.DH.update({k:v.replace('11','12',1) for k,v in gen.DH.items()})
for l,d in [('ar','12 نوفمبر 2026'),('it','12 novembre 2026'),('tr','12 Kasım 2026')]: gen.DH[l]=d
gen.DH['en']='12 November 2026'
for L_,hl,loc in [('zh-tw','zh-Hant-TW','zh_TW'),('zh-hk','zh-Hant-HK','zh_HK')]:
    gen.DH[L_]='2026 年 11 月 12 日'; gen.UPD[L_]='更新於'; gen.TPL[L_]='tiktok-appeal-links-and-forms-directory'
    gen.LOC[L_]=loc; gen.HL[L_]=hl; gen.CTA[L_]=('用 WhatsApp 聯絡我們','想用 Email？ ↗︎')
    gen.ABOUT[L_]=('關於 Unbanz','Unbanz（unbanz.com）是一家獨立服務商，協助恢復被停用、停權或被盜的 Instagram、Facebook、TikTok、YouTube、Snapchat 與 Meta 廣告'+('帳號' if L_=='zh-tw' else '帳戶')+'，恢復 Facebook '+('粉絲專頁' if L_=='zh-tw' else '專頁')+'，以及申請用戶名稱。費用固定、預付，案件失敗 100% 退款。聯絡：team@unbanz.com。與 Meta、TikTok、Snap 或 Google 沒有關聯。')
    gen2.HUB[L_]=f'/{L_}/white-label-agency/'; gen2.REL[L_]='相關頁面'
    gen2.LBL[L_]=['Facebook 廣告'+('帳號' if L_=='zh-tw' else '帳戶'),'用戶名稱申請','代理商負責人','廣告'+('帳號' if L_=='zh-tw' else '帳戶'),'Instagram 用戶名稱']
    gen2.L[L_]=dict(skip='跳到主要內容',menu='開啟選單',mainnav='主要導覽',mobnav='行動版導覽',
      nav=[(f'/{L_}/white-label-agency/','首頁'),('/white-label-recovery-services-by-platform/','服務項目 (EN)'),('/white-label-bulk-recovery-cases-for-agencies/','大量送件 (EN)'),('/pricing/','價格 (EN)'),('/contact/','聯絡我們')],
      tag='帳號與用戶名稱恢復。<br>直接和我們聯絡。',
      foot=[(f'/{L_}/white-label-agency/','代理商白牌合作'),('/zh-tw/white-label-agency/' if L_=='zh-hk' else '/zh-hk/white-label-agency/','香港版' if L_=='zh-tw' else '台灣版'),('/white-label-agency/','White label (EN)'),('/white-label-recovery-services-by-platform/','各平台服務 (EN)'),('/white-label-private-label-case-reports/','白牌進度報告 (EN)'),('/pricing/','價格 (EN)'),('/reviews/','客戶評價 (EN)')],
      indep='獨立服務，與 Meta 無關。',mob=('WhatsApp 聯絡','Email'),
      clients='客戶',said='客戶怎麼說',transcript='逐字稿（英文）',qa='快速解答',good='你需要知道的。',tell='告訴我們發生了什麼。',email='寄 Email 給我們',privacy=('隱私權 (EN)','條款 (EN)'))
import wl_en,wl_markets
SITE='/workspace/site'
ALL=wl_en.PAGES+wl_markets.PAGES
AREA_DEF=["US","GB","CA","AU","IE","NZ","AE","SA","QA","KW","SG","HK","TW","DE","FR","NL","BE","CH","ES","IT","SE","NO","DK"]
for p in ALL:
    p=dict(p); area=p.pop('area',None)
    if p.get('lang','en').startswith('zh'):
        rel=p.pop('related',[]); p['sections']=p['sections']+[('related','相關頁面','<p>'+'、'.join(a(h,x) for h,x in rel)+'。</p>')]
    gen2.build(p)
    slug=p['slug']; f=f'{SITE}/{slug}/index.html'; t=open(f).read()
    m=re.search(r'<script type="application/ld\+json">(.*?)</script>',t,re.S); g=json.loads(m.group(1))
    URL=f'https://unbanz.com/{slug}/'
    for n in g['@graph']:
        if n.get('@type')=='BreadcrumbList': n['itemListElement'][0]['item']='https://unbanz.com/'
    svc=[n for n in g['@graph'] if n.get('@type')=='Service']
    aud={"@type":"BusinessAudience","audienceType":"Marketing agencies, social media agencies, account recovery resellers and B2B partners"}
    if svc:
        s=svc[0]; s['serviceType']='White label account recovery'; s['audience']=aud; s['areaServed']=area or AREA_DEF
    else:
        g['@graph'].append({"@type":"Service","@id":URL+"#service","name":gen.strip(p['h1']).rstrip('.。'),"serviceType":"White label account recovery","provider":{"@id":"https://unbanz.com/#organization"},"url":URL,"audience":aud,"areaServed":area or AREA_DEF,"description":gen.strip(p['answer'])[:300]})
    t=t[:m.start(1)]+json.dumps(g,ensure_ascii=False)+t[m.end(1):]
    t=re.sub(r'<meta name="robots" content="[^"]*">','<meta name="robots" content="index,follow,max-image-preview:large">',t)
    open(f,'w').write(t)
S=[p['slug'] for p in ALL]
open('/workspace/aeo_nov11/built_nov12_wl.txt','w').write('\n'.join(S)+'\n')
print('built',len(S))
