import pathlib,re,sys
H=sys.argv[1]; TAG=f'<script src="/assets/mail-pick.{H}.js" defer></script>'
n=0
for p in pathlib.Path('.').rglob('*.html'):
    if 'node_modules' in p.parts or p.parts[0] in ('users',): continue
    s=p.read_text(encoding='utf-8')
    if 'mailto:team@unbanz.com' not in s: continue
    s2=re.sub(r'<script src="/assets/mail-pick\.[0-9a-f]+\.js" defer></script>','',s)
    s2=s2.replace('</head>',TAG+'</head>',1)
    if s2!=s: p.write_text(s2,encoding='utf-8'); n+=1
print(n)
