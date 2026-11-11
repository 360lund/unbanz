from gen import *
SV={'ig':('Instagram account recovery','800','/instagram-account-recovery/','ig_disabled','Instagram'),
'fb':('Facebook account recovery','900','/facebook-account-recovery/','fb','Facebook'),
'page':('Facebook Page recovery','600','/facebook-page-recovery/','fb_page','Meta'),
'ad':('Meta ad account recovery','1200','/ad-account-recovery/','ad','Meta'),
'bm':('Business Portfolio recovery','1500','/meta-business-portfolio-restricted-help/','bm','Meta'),
'user':('Instagram username claim','1200','/username/','username','Instagram'),
'snap':('Snapchat account recovery','800','/snapchat-unban-service/','snap','Snap'),
'tt':('TikTok ban recovery','900','/tiktok-account-help/','tiktok','TikTok'),
'yt':('YouTube channel recovery','1200','/youtube-account-help/','youtube','YouTube'),
'wa':('WhatsApp number unban','','/whatsapp-banned-number/','whatsapp','WhatsApp')}
PER={'page':' per Page','user':' per handle'}
def helpsec(k,extra=''):
    n,p,u,_,pl=SV[k]
    fee=f'a fixed ${int(p):,}{PER.get(k,"")}, paid upfront by card, with a 100% refund if the case fails' if p else 'a price confirmed before you pay, with a 100% refund if the case fails'
    return ('want-it-handled','Want it handled for you?',f'<p>Unbanz handles <a href="{u}">{n.lower() if not n.startswith(("Instagram","Facebook","Meta","TikTok","YouTube","Snapchat","Business","WhatsApp")) else n}</a> for {fee}. Work usually takes 3–7 days from the day we start, but timing is not guaranteed and {pl} makes the final decision. {extra}We are independent, not {pl}, and we never ask for your password or login codes.</p><p>To start, send a screenshot of the full notice, the username or link, and your country to <a href="mailto:team@unbanz.com">team@unbanz.com</a>. See every fee on the <a href="/pricing/">pricing page</a>.</p>')
def svc(k): n,p,u,sv,pl=SV[k]; return (n,p,'') if p else None
def P(**k):
    s=k.pop('svc',None)
    if s:
        k.setdefault('sv',SV[s][3])
        if SV[s][1] and k.pop('offer',True): k['service']=(SV[s][0],SV[s][1],'')
        if SV[s][1] and not any(x[0]=='want-it-handled' for x in k['sections']): k['sections'].append(helpsec(s))
    return k
