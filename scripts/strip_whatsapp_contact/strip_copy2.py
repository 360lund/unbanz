import re, os, sys
R = [
 (r'Contacter Unbanz\s?:\s?WhatsApp ou e-mail', 'Contacter Unbanz par e-mail'),
 (r'Can I reach Unbanz other than WhatsApp\?', 'Can I reach Unbanz by email?'),
 (r'Send it on WhatsApp\.', 'Email it to team@unbanz.com.'),
 (r'(?<=[>"])WhatsApp or team@unbanz\.com', 'Email team@unbanz.com'),
 (r'(?<=[>"])WhatsApp or email\.', 'By email.'),
 (r'<p>WhatsApp or email\. You hear', '<p>By email. You hear'),
 (r'WhatsApp: <br>', ''),
 (r'<p>Message us on WhatsApp\. We never', '<p>Email us. We never'),
 (r'joignable par WhatsApp et par e-mail', 'joignable par e-mail'),
 (r'(?i)por whatsapp o (?:por )?correo', 'por correo'),
 (r'Pelo WhatsApp ou (?:por )?e-mail', 'Por e-mail'),
 (r'pelo WhatsApp ou (?:por )?e-mail', 'por e-mail'),
 (r'(?i)par whatsapp ou (?:par )?e-mail', 'par e-mail'),
 (r'(?i)via whatsapp of (?:per )?e-mail', 'per e-mail'),
 # llms text dumps
 (r'(?m)^[ \t-]*(?:Contact: )?WhatsApp:? \+1 934 201 2490(?: \(https://wa\.me/\d+\))?\s*\n', ''),
 (r'(?:Contact: )?WhatsApp:? \+1 934 201 2490 \(https://wa\.me/\d+\)[,;]?\s?', ''),
 (r'(?m)^[ \t-]*Contact: WhatsApp https://wa\.me/\S*\s*\n', ''),
 (r'Message us on WhatsApp\s{1,3}(?=(?:Email|Prefer email\?|See details|Read the guide|Home|Leave))', ''),
 (r'Send us the notice on WhatsApp\s{1,3}(?=(?:Email|Prefer email\?))', ''),
 (r'Message us on WhatsApp\s{1,3}Prefer email\?', 'Email us'),
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
                t = open(p, encoding='utf-8').read(); o = t; t = fix(t)
                if t != o: open(p, 'w', encoding='utf-8').write(t); n += 1
    print(n)
