import re,html
IG=[('/guides/instagram-account-suspended-appeal/','Instagram suspended: how to appeal'),('/guides/instagram-disabled-no-appeal-button/','No appeal button'),('/guides/instagram-id-verification-request/','ID or selfie check'),('/guides/instagram-account-disabled/','Instagram disabled'),('/guides/instagram-appeal-sent-no-response/','Appeal sent, no reply'),('/guides/hacked-instagram-account-recovery/','Hacked Instagram')]
FB=[('/guides/facebook-account-disabled-appeal/','Facebook disabled: how to appeal'),('/guides/facebook-disabled-appeal-rejected/','Appeal rejected'),('/guides/facebook-lost-access-to-email-or-phone/','Lost email or phone'),('/best-service-to-recover-disabled-facebook-account/','Choosing a Facebook recovery service')]
AD=[('/guides/meta-ad-account-restricted/','Meta ad account restricted'),('/best-facebook-ad-account-recovery-service/','Choosing ad account help')]
T={'instagram-account-help':IG,'instagram-account-recovery':IG,'instagram-unban-service':IG,'unban':IG+FB,'services':IG+FB+AD,'guides':IG+FB+AD,
 'facebook-account-help':FB,'facebook-account-recovery':FB,'facebook-unban-service':FB,'facebook-hacked-account-recovery-service':FB,
 'meta-ad-account-help':AD,'ad-account-recovery':AD,'how-it-works':IG[:3]+FB[:2]+AD[:1],'faq':IG[:3]+FB[:2]+AD[:1]}
out=[]
for p,L in T.items():
    f=p+'/index.html'; h=open(f).read()
    h=re.sub(r'<nav class="related-services container" aria-label="Most read guides" data-nov04g="links">.*?</nav>','',h,flags=re.S)
    L=[x for x in L if x[0]!='/'+p+'/']
    n='<nav class="related-services container" aria-label="Most read guides" data-nov04g="links">'+''.join('<a href="%s">%s</a>'%(u,html.escape(t)) for u,t in L)+'</nav>'
    assert h.count('</main>')==1,p
    h=h.replace('</main>',n+'</main>'); open(f,'w').write(h); out.append('https://unbanz.com/%s/'%p)
open('/tmp/g_links.txt','w').write('\n'.join(out)); print(len(out))
