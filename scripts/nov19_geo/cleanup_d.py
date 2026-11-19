"""Nov 19 2026 pass D: localized suffix-form prices (800 $, 1.200 $ ...) -> from 1,000; collapse lists."""
import os,re
NB='\u00a0'
AMT=r'(?:600|800|900|1[.,  \u00a0\u202f]200|1[.,  \u00a0\u202f]500)'
FMT={'fr':'1'+NB+'000','en':'1,000','zh':'1,000','ar':'1,000'}
FROM={'de':'ab','es':'desde','fr':'à partir de','it':'da','pt':'a partir de','nl':'vanaf','tr':'','en':'from','ar':'','zh':''}
PREP={'de':r'(?:für |pauschal |für pauschal )','es':r'(?:por |de )','fr':r'(?:pour |de )','it':r'(?:a |per |di )','pt':r'(?:por |de )','nl':r'(?:voor |van )','tr':r'(?!)','en':r'(?:for )','ar':r'(?!)','zh':r'(?!)'}
LIST={'de':'ab 1.000 $ pro Konto oder Handle, auf jeder Plattform','es':'desde 1.000 $ por cuenta o usuario, en todas las plataformas','fr':'à partir de 1'+NB+'000 $ par compte ou pseudo, sur toutes les plateformes','it':'da 1.000 $ per account o nome utente, su ogni piattaforma','pt':'a partir de 1.000 $ por conta ou nome de usuário, em todas as plataformas','nl':'vanaf 1.000 $ per account of gebruikersnaam, op elk platform','tr':'hesap veya kullanıcı adı başına 1.000 $’dan başlayan ücretler, tüm platformlarda'}
def lang_of(s,p):
  m=re.search(r'<html[^>]*lang="([a-zA-Z]+)',s); l=(m.group(1).lower() if m else 'en')
  return 'pt' if l.startswith('pt') else l
tot=0;fl=0
for root,ds,fs in os.walk('.'):
  ds[:]=[d for d in ds if d not in ('.git','assets','scripts','node_modules','api')]
  for f in fs:
    if not f.endswith('.html'): continue
    p=os.path.join(root,f); s=open(p,encoding='utf-8').read(); o=s
    L=lang_of(s,p); num=FMT.get(L,'1.000'); fw=FROM.get(L,'')
    one=num+' $'
    frm=(fw+' '+one) if fw else one
    # prep + amount -> from-form
    s,a=re.subn(PREP.get(L,r'(?!)')+AMT+r' ?(?:\$|USD)',lambda m: frm,s)
    # bare amount
    s,b=re.subn(r'(?<![\d.,])'+AMT+r' ?(?:\$|USD)(?![\w])',one,s)
    # amount-first lists: "1.000 $ por X, 1.000 $ por Y y 1.000 $ por Z"
    if L in LIST:
      it1=re.escape(one)+r' (?:por|pour|für|per|voor|a|pro|par)? ?[^,<.;]{1,45}?'
      s,c=re.subn(it1+r'(?:, '+it1+r')*(?:,? (?:y|et|und|e|en|ve) '+it1+r')(?=[,.<;])',LIST[L],s)
      it2=r'[^\W\d_][^,<.;:]{0,35}? (?:'+re.escape(fw)+r' )?'+re.escape(one)+r'(?: [^\W\d_]{1,12})?'
      s,d=re.subn(r'(?<=[:(>] )'+it2+r'(?:, '+it2+r'){2,}|(?<=[:(>])'+it2+r'(?:, '+it2+r'){2,}',LIST[L],s)
    else: c=d=0
    tot+=a+b+c+d
    if s!=o: fl+=1; open(p,'w',encoding='utf-8').write(s)
print('repl',tot,'files',fl)
