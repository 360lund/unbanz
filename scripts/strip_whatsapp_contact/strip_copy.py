import re, os, sys
R = [
 # English specifics
 (r'(?:Message|Contact) us on WhatsApp or email team@', 'Email us at team@'),
 (r'WhatsApp us or email team@', 'Email us at team@'),
 (r'Message us on WhatsApp or (?:by )?email', 'Email us'),
 (r'(Message|Contact) (Unbanz|Usernm|Unbanhelp|Ogclaim|Bansfix|Ban Help|Acctfix|Acctback|Atclaim|Restore Ad Account|Ads Account Recovery|Ad Account Unban) (?:on|by) WhatsApp or (?:by )?email', r'Email \2'),
 (r'Contact (Unbanz|Usernm|Ogclaim|Atclaim|Restore Ad Account|Ads Account Recovery|Ad Account Unban) on WhatsApp or (?:at )?team@', r'Email \1 at team@'),
 (r'Contact (Unbanz|Usernm|Ogclaim|Atclaim|Restore Ad Account|Ads Account Recovery|Ad Account Unban|Ban Help|Bansfix|Acctfix|Acctback|Unbanhelp): WhatsApp (?:&amp;|&|and) [Ee]mail', r'Contact \1 by Email'),
 (r'when you message us on WhatsApp or email', 'when you email us'),
 (r'(?:on|by|over|via) WhatsApp or (?:by |via )?email', 'by email'),
 (r'(?:on|by) WhatsApp or (?:to|at) team@', 'to team@'),
 (r'(?:Send it|Send it to us) on WhatsApp or to team@', 'Send it to team@'),
 (r'on WhatsApp and email the whole way', 'by email the whole way'),
 (r'(an?|the) WhatsApp or email (click|enquiry|link)', lambda m: ('an' if m.group(1).lower().startswith('a') else m.group(1)) + ' email ' + m.group(2)),
 (r'Contact links open WhatsApp or your email app', 'Contact links open your email app'),
 (r'(?<![\w>])WhatsApp or email only', 'Email only'),
 (r'whether you tapped WhatsApp or email', 'whether you tapped email'),
 (r'in your WhatsApp chat or email', 'by email'),
 (r'with your WhatsApp number or email thread', 'with your email thread'),
 (r'A saved WhatsApp chat or email address for your partner', 'A saved email address for your partner'),
 (r'one website, one WhatsApp number, one email', 'one website, one email'),
 (r'one website, one WhatsApp number and one email', 'one website and one email'),
 (r'A website, an email and one WhatsApp number you can check', 'A website and an email you can check'),
 (r'Ask on WhatsApp and we tell you', 'Email us and we tell you'),
 (r'Send the handle to Atclaim on WhatsApp for a route check', 'Email the handle to Atclaim for a route check'),
 # French
 (r'Contacter Unbanz : WhatsApp ou e-mail', 'Contacter Unbanz par e-mail'),
 (r'(?:sur|par) WhatsApp ou (?:par )?e-mail', 'par e-mail'),
 (r'avec un site, une adresse e-mail et un numéro WhatsApp officiels', 'avec un site et une adresse e-mail officiels'),
 (r'avec un site, un e-mail et un numéro WhatsApp officiels', 'avec un site et un e-mail officiels'),
 (r'par WhatsApp via les boutons du site, par e-mail à', 'par e-mail à'),
 # Spanish
 (r'por WhatsApp o (?:por )?correo', 'por correo'),
 # Portuguese
 (r'(?:pelo|por) WhatsApp ou (?:por )?e-mail', 'por e-mail'),
 (r'sem um botão de WhatsApp ou e-mail nesta página', 'por e-mail'),
 # Dutch
 (r'(?:via|op) WhatsApp of (?:per )?e-mail', 'per e-mail'),
 (r'Via WhatsApp of per e-mail naar team@', 'Per e-mail naar team@'),
 # old fee-block sentence
 (r'\s?WhatsApp is offered in the United States, Canada, the United Kingdom, France, the Netherlands, the United Arab Emirates and Italy\. Elsewhere, use email\.', ''),
]
R = [(re.compile(a), b) for a, b in R]
def fix(t):
    for r, s in R: t = r.sub(s, t)
    return t
if __name__ == '__main__':
    n = 0
    for root in sys.argv[1:]:
        for dp, dn, fn in os.walk(root):
            dn[:] = [d for d in dn if d not in ('.git', 'node_modules', 'users', 'scripts', 'docs')]
            for f in fn:
                if not f.endswith(('.html', '.txt', '.xml')): continue
                p = os.path.join(dp, f)
                try: t = open(p, encoding='utf-8').read()
                except Exception: continue
                o = t; t = fix(t)
                if t != o: open(p, 'w', encoding='utf-8').write(t); n += 1
    print(n)
