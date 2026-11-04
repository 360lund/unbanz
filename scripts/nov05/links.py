import os,re,glob
os.chdir('/workspace/site')
A=lambda s,t:f'<a href="/{s}/">{t}</a>'
IG=A('instagram-appeal-links-and-forms-directory','Instagram appeal links and forms');FB=A('facebook-appeal-links-and-forms-directory','Facebook appeal links and forms')
AD=A('meta-ad-account-appeal-links-directory','Meta ad account appeal links');SC=A('snapchat-support-links-and-forms-directory','Snapchat support links and forms')
CM=A('how-to-contact-meta-about-a-disabled-account','how to contact Meta about a disabled account')
def sec(links): return f'<h2 id="platform-links-2026">Official links by platform</h2><p>Need only the links for one platform? See {links}. Wondering whether Meta can be reached by phone or email? Read {CM}.</p>'
M={'guides/facebook-account-disabled-appeal':FB+' and '+IG,'guides/facebook-disabled-appeal-rejected':FB,'guides/facebook-lost-access-to-email-or-phone':FB,'facebook-lost-access-to-email-or-phone-usa':FB,
'guides/instagram-account-suspended-appeal':IG+' and '+FB,'guides/instagram-disabled-no-appeal-button':IG,'guides/instagram-account-disabled':IG,'guides/instagram-check-account-status':IG,'instagram-account-disabled-after-hack-appeal':IG,
'guides/meta-ad-account-restricted':AD,'guides/meta-ad-payment-declined-fix':AD,'guides/snapchat-device-banned-appeal':SC,'snapchat-unban-service':SC,'snapchat-unlock-form-error-or-no-reply':SC}
for p,l in M.items():
    f=p+'/index.html';h=open(f).read()
    if 'platform-links-2026' in h: continue
    s=sec(l)
    if '<h2 id="compare-2026">' in h: h=h.replace('<h2 id="compare-2026">',s+'<h2 id="compare-2026">',1)
    else:
        i=h.find('<article class="guide-body')
        j=h.find('</article>',i) if i>=0 else -1
        if j<0:
            # service page: add before footer-ish related nav
            k=h.find('<nav class="related-services')
            if k<0: print('skip',p);continue
            h=h[:k]+'<section class="container guide-body">'+s+'</section>'+h[k:]
        else: h=h[:j]+s+h[j:]
    open(f,'w').write(h);print('linked',p)
# directory page: new section before Related
f='meta-appeal-links-and-forms-directory/index.html';h=open(f).read()
if 'platform-directories' not in h:
    h=h.replace('<h2 id="related">',f'<h2 id="platform-directories">Directories by platform</h2><p>Each platform also has its own page with a short “which link do you need” table: {IG}, {FB}, {AD} and {SC}. For phone, email and other ways people try to reach Meta, see {CM}.</p><h2 id="related">',1)
    open(f,'w').write(h);print('linked dir')
for f in ['site-map/index.html','guides/index.html']:
    h=open(f).read()
    if 'instagram-appeal-links-and-forms-directory' in h: continue
    h=re.sub(r'(<a href="/meta-appeal-links-and-forms-directory/">Meta appeal links and forms[^<]*</a>)',lambda m:m.group(1)+IG+FB+AD+SC+A('how-to-contact-meta-about-a-disabled-account','How to contact Meta'),h,count=1)
    open(f,'w').write(h);print('linked',f)
