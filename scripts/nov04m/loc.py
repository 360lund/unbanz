import re,sys
sys.path.insert(0,'/workspace/site/scripts/nov04l')
from lib import bump_lastmod
BAN=re.compile(r'\b(cases?|garanti\w*|guarantee\w*|garantie\w*|prix fixe|vaste prijs|snapchat|rapide|snel geregeld)\b',re.I)
LBL={'fr':('Mis à jour le','4 novembre 2026','a-propos'),'nl':('Bijgewerkt op','4 november 2026','over-unbanz')}
def qa(title,items,anchor):
    return f'<h2 id="{anchor}">{title}</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in items)
def add(lang,slug,block,anchor,date='2026-11-04'):
    p=f'{lang}/{slug}/index.html';s=open(p).read()
    if f'id="{anchor}"' in s: return None
    t=re.sub(r'<[^>]+>|https?://\S+','',block);b=BAN.findall(t);assert not b,(slug,b)
    lab,dh,ab=LBL[lang];i=s.find(f'<h2 id="{ab}">');assert i>0,slug
    s=s[:i]+block+s[i:]
    if '"dateModified"' in s: s=re.sub(r'"dateModified":"[^"]*"',f'"dateModified":"{date}"',s)
    else: s=s.replace('"@type":"WebPage",',f'"@type":"WebPage","dateModified":"{date}",',1)
    if 'class="guide-meta"' not in s:
        h=s.find('</h1>');s=s[:h+5]+f'<p class="guide-meta">{lab} <time datetime="{date}">{dh}</time></p>'+s[h+5:]
    open(p,'w').write(s);return f'https://unbanz.com/{lang}/{slug}/'
