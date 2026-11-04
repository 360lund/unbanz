# Strip leftover ban/takedown/account-removal/Snapchat service offers (visible + JSON-LD). Idempotent.
import re,glob,json
KILL=["Snapchat account unbans","Locked Snapchat accounts","Fake account takedowns","Impersonation account removal","Snapchat username claims","Snapchat Community Guidelines","Account removal and reporting help","Account bans and takedowns","Account unban, appeal and account removal services","Account removal and reporting services"]
R=[("Social media account unbans, account removals and username claims","Instagram, Facebook and Meta ad account recovery, and username claims"),
("Social media account unbans, appeals and account removal help","Instagram and Facebook account recovery and appeals"),
("Instagram, Facebook and Snapchat account service","Instagram, Facebook and Meta ad account recovery service"),
("Instagram, Facebook and Snapchat account unbans, username claims, and Meta ad account recovery","Instagram and Facebook account unbans, username claims, and Meta ad account recovery"),
("Unbans & account removals.","Account recovery and username claims."),
("Instagram and Facebook unbans and account removals, plus username claims","Instagram and Facebook unbans, Meta ad account recovery and username claims"),
("Instagram & Facebook Unbans and Account Removals","Instagram & Facebook Unbans and Username Claims"),
("Instagram and Facebook unbans and account removals","Instagram and Facebook unbans and username claims"),
("unbans, account removals and username claims","unbans and username claims"),
("ad account recovery, account removal help and Instagram usern","ad account recovery and Instagram usern"),
("not affiliated with Meta or Snapchat","not affiliated with Meta"),
("Instagram · Facebook · Snapchat · Pseudos","Instagram · Facebook · Pseudos"),
("Instagram, Facebook ou Snapchat","Instagram ou Facebook"),("Instagram, Facebook of Snapchat","Instagram of Facebook"),
("Meta, Threads et Snapchat","Meta et Threads"),("Meta, Threads en Snapchat","Meta en Threads"),("Meta, Threads y Snapchat","Meta y Threads"),
("niet verbonden aan Meta of Snapchat","niet verbonden aan Meta"),("Meta en Snapchat publiceren","Meta publiceert"),("Meta et Snapchat ne publient","Meta ne publie"),
("non affilié à Meta, Instagram, Facebook ou Snapchat","non affilié à Meta, Instagram ou Facebook"),
("pseudo Instagram, Facebook ou Snapchat","pseudo Instagram ou Facebook"),(" and Snapchat unbans."," unbans."),("Facebook and Snapchat too","Facebook too"),
("See impersonation removal.",""),("Usernames, Snapchat and TikTok","Usernames and TikTok")]
R+=[("Unbanz — unbans and account removals for Instagram and Facebook","Unbanz — unbans and username claims for Instagram and Facebook"),
("Unbanz: unbans and account removals for Instagram and Facebook","Unbanz: unbans and username claims for Instagram and Facebook"),
("unbans, ad accounts, account removals and username claims","unbans, ad accounts and username claims"),
("Unbans, Account Removals &amp; Username Claims","Unbans &amp; Username Claims"),("Unbans, Account Removals & Username Claims","Unbans & Username Claims"),
("Instagram &amp; Facebook Unbans, Account Removals &amp; Username Claims","Instagram &amp; Facebook Unbans &amp; Username Claims"),
("Instagram, Facebook and Snapchat. Send","Instagram and Facebook. Send"),("Instagram, Facebook &amp; Snapchat |","Instagram &amp; Facebook |"),
("Unbanz — Unbans and account removals.","Unbanz — Unbans and username claims."),
(" For an account removal, send the link to the account and say what it did: scam, impersonation or harassment.",""),
(" For an account removal, send the profile link and what it’s doing.",""),
("Unbans &amp; Account Removals: Instagram, Facebook","Unbans &amp; Username Claims: Instagram, Facebook"),("Unbans & Account Removals: Instagram, Facebook","Unbans & Username Claims: Instagram, Facebook"),
("Instagram &amp; Facebook<br>unbans and account removals.","Instagram &amp; Facebook<br>unbans and username claims."),
("Need an account taken down or a username claimed? We handle that too.","Need a username claimed? We handle that too."),
("Unbans, account removals and<br>username claims.","Unbans, ad account recovery and<br>username claims."),
("<tr><td>Account removals and username claims</td>","<tr><td>Username claims</td>"),
(" · account removals · "," · "),("no tiene afiliación con Meta ni con Snapchat","no tiene afiliación con Meta"),
("Instagram, Facebook o Snapchat","Instagram o Facebook"),("Meta y Snapchat no publican","Meta no publica"),
("hacked Instagram, Facebook and Snapchat accounts back","hacked Instagram and Facebook accounts back"),
("Instagram, Facebook, ad account, Snapchat, other","Instagram, Facebook, ad account, other"),
("<a href=\"/facebook-username-claim/\">Facebook usernames</a> and Snapchat usernames.","<a href=\"/facebook-username-claim/\">Facebook usernames</a>."),
("Threads and Snapchat. The client","and Threads. The client"),(" See white label impersonation and fake account removal.",""),
('"Snapchat username claim",',''),
("Are unbans and account removals safe?","Are unbans safe?"),("Yes. Unbans work from your username and the notice, and account removals go through the platforms’ own reporting systems.","Yes. Unbans work from your username and the notice."),
(" and account removal safety."," safety.")]
CONTACT=re.compile(r'<a class="contact-option" href="[^"]*(?:Snapchat|taken%20down)[^"]*"[^>]*>.*?</a>|<a href="[^"]*account%20removed" data-service="ban">[^<]*</a>',re.S)
ch=[]
for f in glob.glob('**/index.html',recursive=True)+['llms.txt','llms-full.txt']:
    if f.startswith(('users/','scripts/')): continue
    s=open(f).read(); o=s
    if 'noindex' in s[:4000]: continue
    for a,b in R: s=s.replace(a,b)
    for k in KILL: s=s.replace('"%s",'%k,'').replace(',"%s"'%k,'').replace(', "%s"'%k,'')
    s=CONTACT.sub('',s)
    if s!=o: open(f,'w').write(s); ch.append(f)
print(len(ch)); open('/tmp/nr.txt','a').write('\n'.join(ch)+'\n')
