import re, os, sys
N = r'\+1 934 201 2490'
RULES = [
 # anchors labelled with the number (converted to mailto earlier) inside contact lists
 (r'<li>WhatsApp: <a [^>]*>' + N + r'</a>\.?</li>', ''),
 (r'<a href="mailto:[^"]*">' + N + r'</a> or team@unbanz\.com', 'team@unbanz.com'),
 (r'our WhatsApp is ' + N + r' \(wa\.me/19342012490\), our email is', 'our email is'),
 (r'our WhatsApp is ' + N + r', our email is', 'our email is'),
 (r'One WhatsApp: ' + N + r'\. One email:', 'One email:'),
 (r"What is Unbanz's official WhatsApp number\?", 'What is Unbanz&#x27;s official contact?__Q'),
 (r'(>|")' + N + r'\. Our email is team@unbanz\.com\.', r'\1Email only: team@unbanz.com. We do not use a WhatsApp number.'),
 (r'WhatsApp \(' + N + r'\) or email \(team@unbanz\.com\)', 'Email (team@unbanz.com)'),
 (r', or message us on WhatsApp at ' + N, ''),
 (r'unbanz\.com, team@unbanz\.com and WhatsApp ' + N, 'unbanz.com and team@unbanz.com'),
 (r'unbanz\.com, WhatsApp ' + N + r' and team@unbanz\.com', 'unbanz.com and team@unbanz.com'),
 (r'team@unbanz\.com, WhatsApp ' + N, 'team@unbanz.com'),
 (r'team@unbanz\.com or WhatsApp ' + N, 'team@unbanz.com'),
 (r'Website unbanz\.com\. WhatsApp ' + N + r'\. Email', 'Website unbanz.com. Email'),
 (r'WhatsApp ' + N + r', email team@', 'Email team@'),
 (r'you can reach us on WhatsApp ' + N + r' or team@', 'you can reach us at team@'),
 (r'(?:to Unbanz )?on WhatsApp ' + N + r' or by email to team@', 'by email to team@'),
 (r'By WhatsApp on ' + N + r' or by email to team@', 'By email to team@'),
 (r'(?:message|Message) Unbanz on WhatsApp ' + N + r' or email team@', 'email team@'),
 (r'Send a message on WhatsApp at ' + N + r' or email team@', 'Email team@'),
 (r'Message WhatsApp ' + N + r' or email team@', 'Email team@'),
 (r'WhatsApp on ' + N + r' or email team@', 'Email team@'),
 (r'Écrivez sur WhatsApp au ' + N + r' ou par e-mail à team@', 'Écrivez par e-mail à team@'),
 (r'Escribe por WhatsApp al ' + N + r' o por correo a team@', 'Escribe por correo a team@'),
 (r'Escreva pelo WhatsApp ' + N + r' ou por e-mail para team@', 'Escreva por e-mail para team@'),
 (r'Stuur een bericht via WhatsApp op ' + N + r' of mail team@', 'Mail team@'),
 (r'(Contact ?: )WhatsApp ' + N + r' (?:or|ou|of|o) (?:email )?team@', r'\1team@'),
 (r'WhatsApp ' + N + r' or email team@', 'Email team@'),
 (r'WhatsApp ' + N + r' (?:or|ou|of|o) team@', 'Email team@'),
 (r'WhatsApp ' + N + r'\. Email team@', 'Email team@'),
]
RULES = [(re.compile(a), b) for a, b in RULES]
def fix(t):
    for r, s in RULES: t = r.sub(s, t)
    return t
if __name__ == '__main__':
    n = 0
    for root in sys.argv[1:]:
        for dp, dn, fn in os.walk(root):
            dn[:] = [d for d in dn if d not in ('.git', 'node_modules', 'users')]
            for f in fn:
                if not f.endswith(('.html', '.txt', '.md', '.xml')): continue
                if '/scripts/' in dp or '/docs' in dp: continue
                p = os.path.join(dp, f)
                try: t = open(p, encoding='utf-8').read()
                except Exception: continue
                o = t; t = fix(t)
                if t != o: open(p, 'w', encoding='utf-8').write(t); n += 1
    print(n)
