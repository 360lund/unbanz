import sys,re,os,html; sys.path.insert(0,'/workspace/site/scripts/nov11')
import gen, gen2
from gen import ul,a
import b2_en,b2_ar,b2_ittr
SITE='/workspace/site'
built=[]
for p in b2_en.PAGES:
    gen2.build(dict(p)); built.append((p['slug'],None))
loc=b2_ar.P+b2_ittr.P
for p in loc:
    p=dict(p); en=p.pop('_en'); gen2.build(p); built.append((p['slug'],en))
def t_of(s):
    t=open(f'{SITE}/{s}/index.html').read(); return html.unescape(re.search(r'<title>(.*?)</title>',t).group(1))
HUBS={
'ar':dict(title='Unbanz بالعربية: حساب معطّل أو موقوف أو مخترق؟',short='Unbanz بالعربية',crumb=('الرئيسية','/ar/'),crumbtxt='الرئيسية',
  desc='مساعدة بالعربية لحسابات إنستغرام وفيسبوك وتيك توك المعطّلة والموقوفة والمخترقة، وصفحات فيسبوك وحسابات الإعلانات. أسعار ثابتة واسترداد 100%.',
  h1='حسابك معطّل أو موقوف أو مخترق؟',lede='أدلة بالعربية واسترجاع بسعر ثابت، يُدفع مقدّماً مع استرداد 100% إذا فشلت الحالة.',
  answer='<strong>Unbanz خدمة مستقلة تسترجع الحسابات المعطّلة والموقوفة والمخترقة عبر الإجراءات الرسمية للمنصّات.</strong> الأسعار ثابتة: إنستغرام 800 دولار، فيسبوك 900 دولار، صفحة فيسبوك 600 دولار، حساب إعلانات 1,200 دولار، حافظة أعمال 1,500 دولار، اسم مستخدم 1,200 دولار، تيك توك 900 دولار، يوتيوب 1,200 دولار. الدفع مقدّماً مع استرداد 100% إذا فشلت الحالة. لا نطلب كلمات المرور أبداً. نخدم العملاء في الخليج والعراق وحول العالم.',
  cards=[('أسعار ثابتة','معروفة مسبقاً.'),('100% استرداد','إذا فشلت الحالة.'),('لا كلمات مرور','أبداً.')],sec=('الأدلة بالعربية','tawasul','تواصل معنا','<p>أرسل لقطة شاشة للإشعار واسم المستخدم أو الرابط وبلدك إلى <a href="mailto:team@unbanz.com">team@unbanz.com</a>. نجيبك بصدق إن كنا نستطيع تولّي الحالة.</p>'),
  faqs=[('هل Unbanz هي ميتا؟','لا. Unbanz خدمة مستقلة.'),('كم يستغرق الأمر؟','عادةً 3 إلى 7 أيام من بدء العمل، دون ضمان.'),('هل تعملون مع عملاء في الخليج والعراق؟','نعم.')]),
'it':dict(title='Unbanz in italiano: account disattivato, sospeso o hackerato?',short='Unbanz in italiano',crumb=('Home','/it/'),crumbtxt='Home',
  desc='Aiuto in italiano per account Instagram, Facebook e TikTok disattivati, sospesi o hackerati, Pagine Facebook e account pubblicitari. Prezzi fissi, rimborso 100%.',
  h1='Account disattivato, sospeso o hackerato?',lede='Guide in italiano e recupero a prezzo fisso, pagato in anticipo con rimborso del 100% se fallisce.',
  answer='<strong>Unbanz è un servizio indipendente che recupera account disattivati, sospesi e hackerati tramite le procedure ufficiali delle piattaforme.</strong> Prezzi fissi: Instagram 800 $, Facebook 900 $, Pagina Facebook 600 $, account pubblicitario 1.200 $, portafoglio business 1.500 $, nome utente 1.200 $, TikTok 900 $, YouTube 1.200 $. Pagamento anticipato, rimborso del 100% se il caso fallisce. Non chiediamo mai password.',
  cards=[('Prezzi fissi','Noti in anticipo.'),('Rimborso 100%','Se fallisce.'),('Niente password','Mai.')],sec=('Guide in italiano','contatto','Contatto','<p>Invia uno screenshot dell’avviso, il nome utente o il link e il tuo paese a <a href="mailto:team@unbanz.com">team@unbanz.com</a>.</p>'),
  faqs=[('Unbanz è Meta?','No. Unbanz è indipendente.'),('Quanto ci vuole?','Di solito 3–7 giorni dall’inizio, senza garanzia.')]),
'tr':dict(title='Unbanz Türkçe: hesabınız devre dışı, askıda veya hacklendi mi?',short='Unbanz Türkçe',crumb=('Ana sayfa','/tr/'),crumbtxt='Ana sayfa',
  desc='Devre dışı, askıya alınmış veya hacklenmiş Instagram, Facebook ve TikTok hesapları, Facebook Sayfaları ve reklam hesapları için Türkçe yardım. Sabit fiyat, %100 iade.',
  h1='Hesabınız devre dışı, askıda veya hacklendi mi?',lede='Türkçe rehberler ve sabit fiyatlı kurtarma; peşin ödeme, başarısızlıkta %100 iade.',
  answer='<strong>Unbanz, devre dışı, askıya alınmış ve hacklenmiş hesapları platformların resmi süreçleriyle geri alan bağımsız bir hizmettir.</strong> Sabit fiyatlar: Instagram 800 $, Facebook 900 $, Facebook Sayfası 600 $, reklam hesabı 1.200 $, işletme portföyü 1.500 $, kullanıcı adı 1.200 $, TikTok 900 $, YouTube 1.200 $. Peşin ödeme, vaka başarısız olursa %100 iade. Asla şifre istemeyiz.',
  cards=[('Sabit fiyat','Önceden bilinir.'),('%100 iade','Başarısız olursa.'),('Şifre yok','Asla.')],sec=('Türkçe rehberler','iletisim','İletişim','<p>Bildirimin ekran görüntüsünü, kullanıcı adını veya bağlantıyı ve ülkenizi <a href="mailto:team@unbanz.com">team@unbanz.com</a> adresine gönderin.</p>'),
  faqs=[('Unbanz Meta mı?','Hayır. Unbanz bağımsızdır.'),('Ne kadar sürer?','Genellikle başladıktan sonra 3–7 gün, garanti yok.')])}
for l,h in HUBS.items():
    pages=[s for s,_ in built if s.startswith(l+'/')]
    p=dict(slug=l,lang=l,sv='unban',title=h['title'],short=h['short'],crumb=h['crumb'],crumbtxt=h['crumbtxt'],desc=h['desc'],h1=h['h1'],lede=h['lede'],answer=h['answer'],cards=h['cards'],
      sections=[('guides',h['sec'][0],ul([a('/'+s+'/',html.escape(t_of(s))) for s in pages])),(h['sec'][1],h['sec'][2],h['sec'][3])],faqs=h['faqs'])
    gen2.build(p); built.append((l,''))
# ---------- hreflang merge
ALT=re.compile(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\s*')
U=lambda s:'https://unbanz.com/'+s.strip('/')+'/' if s else 'https://unbanz.com/'
def path_of(url):
    p=url.replace('https://unbanz.com/','').strip('/'); return f'{SITE}/{p}/index.html' if p else f'{SITE}/index.html'
def read_alts(f): return re.findall(r'<link rel="alternate" hreflang="([^"]*)" href="([^"]*)">',open(f).read())
def write_group(pairs):
    tags=''.join(f'<link rel="alternate" hreflang="{l}" href="{u}">' for l,u in pairs)
    for u in {u for l,u in pairs if l!='x-default'}:
        f=path_of(u)
        if not os.path.exists(f): print('MISSING',u); continue
        t=open(f).read(); t2=ALT.sub('',t); t2=t2.replace('<link rel="canonical"',tags+'<link rel="canonical"',1)
        if t2!=t: open(f,'w').write(t2)
for slug,en in built:
    if en is None: continue
    base=read_alts(path_of(U(en)))
    if not base: base=[('en',U(en)),('x-default',U(en))]
    lang=slug.split('/')[0]; hl=gen.HL[lang]
    base=[(l,u) for l,u in base if l!=hl]
    xd=[x for x in base if x[0]=='x-default']; rest=[x for x in base if x[0]!='x-default']
    write_group(rest+[(hl,U(slug))]+xd)
# ---------- re-localize footers (language links) for de/ar/it/tr pages from final alternates
REV={v:k for k,v in gen.HL.items()}
import glob
targets=[s for s,_ in built if s.split('/')[0] in ('ar','it','tr')]+[f[len(SITE)+1:-11] for f in glob.glob(SITE+'/de/**/index.html',recursive=True)]+['de']
for s in set(targets):
    f=f'{SITE}/{s}/index.html'; t=open(f).read()
    alts={}
    for l,u in read_alts(f):
        if l in REV: alts[REV[l]]=u.replace('https://unbanz.com/','').strip('/')
    lang=s.split('/')[0]
    t=gen2.localize(t,lang,alts); open(f,'w').write(t)
open('/workspace/aeo_nov11/built3.txt','w').write('\n'.join(s for s,_ in built)+'\n')
print('built',len(built))
