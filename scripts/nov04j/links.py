import os,re
os.chdir('/workspace/site')
L='<a href="/meta-appeal-links-and-forms-directory/">Meta appeal links and forms</a>'
pages=['guides/index.html','instagram-account-help/index.html','facebook-account-help/index.html','meta-ad-account-help/index.html','instagram-appeal-form-not-working/index.html','ad-account-appeal-form-keeps-erroring/index.html','instagram-notice-types/index.html','facebook-notice-types/index.html','meta-ad-account-notice-types/index.html','instagram-account-disabled-vs-suspended-vs-restricted/index.html','guides/instagram-account-suspended-appeal/index.html','guides/facebook-account-disabled-appeal/index.html','guides/meta-ad-account-restricted/index.html','guides/instagram-account-disabled/index.html','guides/instagram-disabled-no-appeal-button/index.html','site-map/index.html']
for p in pages:
    if not os.path.exists(p): print('missing',p); continue
    h=open(p).read()
    if 'meta-appeal-links-and-forms-directory' in h: continue
    k=h.find('<nav class="related-services container"')
    if k<0: print('no nav',p); continue
    e=h.find('</nav>',k)
    h=h[:e]+L+h[e:]
    open(p,'w').write(h); print('linked',p)
