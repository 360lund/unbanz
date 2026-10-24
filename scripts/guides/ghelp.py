def mk(slug, h1, mt, desc, group, tag, plat, short, intro, secs, faq, src, rel, inbound, wa, subj, mid, close, svc='unban', pill=None, aboutname=None):
    """mid/close = (kicker, title, text)"""
    return dict(slug=slug, h1=h1, mt=mt, desc=desc, group=group, tag=tag, plat=plat, svc=svc, short=short, intro=intro, secs=secs, faq=faq,
                src=[(l, u) for l, u in src], rel=rel, inbound=inbound, pill=pill, aboutname=aboutname or plat or 'Meta ads',
                cta=dict(top_wa=f'Hey Unbanz, {wa}', wa=f'Hey Unbanz, {wa}', wa2=f'Hey Unbanz, {wa}', subject=subj,
                         kicker=mid[0], title=mid[1], text=mid[2], kicker2=close[0], title2=close[1], text2=close[2]))

IG_HELP = ('Instagram Help Center', 'https://help.instagram.com/')
FB_HELP = ('Facebook Help Center', 'https://www.facebook.com/help/')
BIZ_HELP = ('Meta Business Help Center', 'https://www.facebook.com/business/help/')
IG_HACKED = ('Instagram: hacked or inaccessible accounts', 'https://www.instagram.com/hacked/')
FB_HACKED = ('Facebook: hacked accounts', 'https://www.facebook.com/hacked')
SNAP_ACC = ('Snapchat Accounts Portal', 'https://accounts.snapchat.com/')
SNAP_HELP = ('Snapchat Support', 'https://help.snapchat.com/')
CS = ('Meta Community Standards', 'https://transparency.meta.com/policies/community-standards/')
ADS = ('Meta Advertising Standards', 'https://transparency.meta.com/policies/ad-standards/')
ACCQ = ('Meta Account Quality', 'https://business.facebook.com/accountquality')
