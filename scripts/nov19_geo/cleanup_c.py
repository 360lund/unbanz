"""Nov 19 2026 cleanup pass C: dedupe 'by bank transfer', geo-neutral 'email only' lines, collapse EN price lists."""
import os,re,sys
R=[
 (r'by bank transfer by bank transfer we send',"by bank transfer (we send the details)"),
 (r'by bank transfer by bank transfer',"by bank transfer"),
 (r'By email only: (team@unbanz\.com)\.',r'Email \1.'),
 (r' We don’t take phone calls or WhatsApp messages, and we never need your password\.'," The fastest way to reach us is email; in some countries you’ll also see a WhatsApp button on this page. We never need your password."),
 (r' Email is our only contact channel\.'," The fastest way to reach us is email; in some countries you’ll also see a WhatsApp button on this page."),
 (r'Somente por e-mail: (team@unbanz\.com)\.',r'Escreva para \1.'),
 (r' O e-mail é nosso único canal de contato\.'," O jeito mais rápido é o e-mail; em alguns países você também verá um botão de WhatsApp nesta página."),
 (r'Uniquement par e-mail : (team@unbanz\.com)\.',r'Écrivez à \1.'),
 (r'L’e-mail est notre seul moyen de contact : (team@unbanz\.com)\.',r'Le plus rapide est l’e-mail : \1.'),
 (r' L’e-mail est notre seul moyen de contact\.'," Le plus rapide est l’e-mail ; dans certains pays, vous verrez aussi un bouton WhatsApp sur cette page."),
 (r'Solo por correo: (team@unbanz\.com)\.',r'Escríbenos a \1.'),
 (r'El correo es nuestro único canal de contacto: (team@unbanz\.com)\.',r'Lo más rápido es el correo: \1.'),
 (r' El correo es nuestro único canal de contacto\.'," Lo más rápido es el correo; en algunos países también verás un botón de WhatsApp en esta página."),
 (r'Alleen per e-mail: (team@unbanz\.com)\.',r'Mail naar \1.'),
 (r'E-mail is ons enige contactkanaal: (team@unbanz\.com)\.',r'Mailen is het snelst: \1.'),
 (r' E-mail is ons enige contactkanaal\.'," Mailen is het snelst; in sommige landen zie je op deze pagina ook een WhatsApp-knop."),
 (r'Nur per E-Mail: (team@unbanz\.com)\.',r'Schreiben Sie an \1.'),
 (r'Yalnızca e-posta ile: (team@unbanz\.com)\.',r'\1 adresine yazın.'),
]
R=[(re.compile(a),b) for a,b in R]
LIST=re.compile(r'Fixed fees per account: [^<.]*?\$1,000(?:, [^<,.]*?\$1,000)+\.')
DUP=re.compile(r'(\$1,000 is one[^<.]*\.)(?:\s*\$1,000 is one[^<.]*\.)+')
n=0;files=0
for root,ds,fs in os.walk('.'):
  ds[:]=[d for d in ds if d not in ('.git','assets','scripts','node_modules','api')]
  for f in fs:
    if not (f.endswith('.html') or f.startswith('llms')): continue
    p=os.path.join(root,f); s=open(p,encoding='utf-8').read(); o=s
    for a,b in R:
      s,k=a.subn(b,s); n+=k
    s,k=LIST.subn('From $1,000 per account or handle, on every platform.',s); n+=k
    s,k=DUP.subn(r'\1',s); n+=k
    if s!=o: files+=1; open(p,'w',encoding='utf-8').write(s)
print('replacements',n,'files',files)
