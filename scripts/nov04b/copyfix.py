import re,glob,os
R=set(l.strip() for l in open('/tmp/rem.txt') if l.strip())
P=[('account unbans and appeals, account removal and reporting help, and username claims','account recovery, unbans and appeals, and username claims'),
('Unbanz: Instagram &amp; Facebook Unbans, Removals &amp; Usernames','Unbanz: Instagram &amp; Facebook Account Recovery and Usernames'),
('Unbans &amp; Account Removals: Instagram, Facebook','Services: Instagram, Facebook and Meta Ad Account Recovery'),
('Instagram &amp; Facebook unbans and account removals.','Instagram and Facebook account recovery.'),
('Unbans, account removals and username claims.','Account recovery, Meta ad accounts and username claims.'),
('Unban and account removal questions.','Account recovery questions.'),
('Unbanz FAQ: Legit, Pricing, Unbans, Removals &amp; Usernames','Unbanz FAQ: Legit, Pricing, Account Recovery and Usernames'),
('Pricing: Unbans, Account Removals &amp; Username Claims | Unbanz','Pricing: Account Recovery and Username Claims | Unbanz'),
('Instagram and Facebook unbans, account removals, impersonation reporting, Meta ad accounts and usernames','Instagram and Facebook account recovery, Meta ad accounts and username claims'),
('Instagram and Facebook unbans, account removals and username claims','Instagram and Facebook account recovery and username claims'),
('Instagram and Facebook unbans, removals, username claims and Meta ad accounts','Instagram and Facebook account recovery, Meta ad accounts and username claims'),
(', and real results are on <a href="/work/">unbanz.com/work/</a>.','.'),(', and real results are on unbanz.com/work/.','.'),
(' Fake, impersonator and scam accounts are reported through',' Username claims go through'),
]
n=0
for f in glob.glob('**/index.html',recursive=True):
    p=os.path.dirname(f) or '.'
    if p in R or f.startswith(('scripts','users')): continue
    h=open(f).read();o=h
    for a,b in P: h=h.replace(a,b)
    h=re.sub(r'<h3>[^<]*(?:Snapchat|account removal|take down)[^<]*</h3><p>.*?</p>','',h,flags=re.I|re.S)
    if h!=o: open(f,'w').write(h); n+=1
print(n)
