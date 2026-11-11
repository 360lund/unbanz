# Round 2: extends gen.py with ar/it/tr and a native shell (header/footer/UI) for de/ar/it/tr.
import re, html, gen
from gen import a
for l,d in [('ar','11 نوفمبر 2026'),('it','11 novembre 2026'),('tr','11 Kasım 2026')]: gen.DH[l]=d
gen.UPD.update({'ar':'آخر تحديث','it':'Aggiornato il','tr':'Güncellendi:'})
for l in ('ar','it','tr'): gen.TPL[l]='tiktok-appeal-links-and-forms-directory'
gen.LOC.update({'ar':'ar_AE','it':'it_IT','tr':'tr_TR'}); gen.HL.update({'ar':'ar','it':'it','tr':'tr'})
gen.CTA.update({'ar':('راسلنا على واتساب','تفضّل البريد الإلكتروني؟ ↗︎'),'it':('Scrivici su WhatsApp','Preferisci l’email? ↗︎'),'tr':('WhatsApp’tan yazın','E-posta mı tercih edersiniz? ↗︎')})
gen.ABOUT.update({
 'ar':('عن Unbanz','Unbanz (unbanz.com) خدمة مستقلة تساعد في استرجاع حسابات إنستغرام وفيسبوك وتيك توك ويوتيوب وسناب شات وحسابات إعلانات ميتا المعطّلة أو الموقوفة أو المخترقة، واسترجاع صفحات فيسبوك، والمطالبة بأسماء المستخدمين. الأسعار ثابتة وتُدفع مقدّماً، مع استرداد كامل بنسبة 100% إذا فشلت الحالة. التواصل: team@unbanz.com. لسنا تابعين لميتا أو تيك توك أو سناب أو غوغل.'),
 'it':('Chi è Unbanz','Unbanz (unbanz.com) è un servizio indipendente che aiuta a recuperare account Instagram, Facebook, TikTok, YouTube, Snapchat e pubblicitari Meta disattivati, sospesi o hackerati, Pagine Facebook e nomi utente. Prezzi fissi pagati in anticipo, con rimborso del 100% se il caso non va a buon fine. Contatto: team@unbanz.com. Non affiliato a Meta, TikTok, Snap o Google.'),
 'tr':('Unbanz hakkında','Unbanz (unbanz.com), devre dışı bırakılmış, askıya alınmış veya hacklenmiş Instagram, Facebook, TikTok, YouTube, Snapchat ve Meta reklam hesaplarını, Facebook Sayfalarını ve kullanıcı adlarını geri almaya yardımcı olan bağımsız bir hizmettir. Sabit ücretler peşin ödenir; vaka başarısız olursa %100 iade edilir. İletişim: team@unbanz.com. Meta, TikTok, Snap veya Google ile bağlantılı değildir.')})
REL={'ar':'صفحات ذات صلة','it':'Pagine correlate','tr':'İlgili sayfalar','de':'Verwandte Seiten'}
HUB={'en':'/','fr':'/fr/','es':'/es/','pt-br':'/pt-br/','nl':'/nl/','de':'/de/','ar':'/ar/','it':'/it/','tr':'/tr/'}
LN={'en':'English','fr':'Français','es':'Español','pt-br':'Português','nl':'Nederlands','de':'Deutsch','ar':'العربية','it':'Italiano','tr':'Türkçe'}
L={
'de':dict(skip='Zum Inhalt springen',menu='Menü öffnen',mainnav='Hauptnavigation',mobnav='Mobile Navigation',
  nav=[('/de/','Start'),('/de/instagram-konto-deaktiviert/','Instagram'),('/de/facebook-konto-deaktiviert/','Facebook'),('/de/instagram-nutzername-beanspruchen/','Nutzernamen'),('/de/preise/','Preise'),('/contact/','Kontakt')],
  tag='Konto- &amp; Nutzernamen-Wiederherstellung.<br>Sprich direkt mit uns.',
  foot=[('/de/','Alle Ratgeber'),('/de/meta-einspruch-links-instagram-facebook/','Meta-Einspruchslinks'),('/de/meta-kontaktieren/','Meta kontaktieren'),('/de/instagram-konto-deaktiviert/','Instagram deaktiviert'),('/de/instagram-gehackt/','Instagram gehackt'),('/de/facebook-konto-deaktiviert/','Facebook deaktiviert'),('/de/facebook-seite-wiederherstellen/','Facebook-Seiten'),('/de/meta-werbekonto-eingeschraenkt/','Werbekonten'),('/de/instagram-nutzername-beanspruchen/','Nutzernamen'),('/de/tiktok-konto-gesperrt/','TikTok'),('/de/youtube-kanal-gekuendigt/','YouTube'),('/de/preise/','Preise')],
  indep='Unabhängiger Dienst. Nicht mit Meta verbunden.',mob=('Schreib uns auf WhatsApp','E-Mail'),
  clients='KUNDEN',said='Was Kunden sagen',transcript='Transkript',qa='KURZE ANTWORTEN',good='Gut zu wissen.',tell='Sag uns, was passiert ist.',email='E-Mail schreiben',privacy=('Datenschutz (EN)','AGB (EN)')),
'ar':dict(skip='انتقل إلى المحتوى',menu='فتح القائمة',mainnav='التنقل الرئيسي',mobnav='تنقل الجوال',
  nav=[('/ar/','الرئيسية'),('/ar/instagram-hisab-muattal/','إنستغرام'),('/ar/facebook-hisab-muattal/','فيسبوك'),('/ar/rawabit-istinaf-meta/','روابط الاعتراض'),('/ar/asaar/','الأسعار'),('/contact/','تواصل معنا')],
  tag='استرجاع الحسابات وأسماء المستخدمين.<br>تحدّث معنا مباشرة.',
  foot=[('/ar/','كل الأدلة بالعربية'),('/ar/rawabit-istinaf-meta/','روابط الاعتراض الرسمية من ميتا'),('/ar/tawasul-maa-meta/','التواصل مع دعم ميتا'),('/ar/instagram-hisab-muattal/','إنستغرام معطّل'),('/ar/instagram-mukhtaraq/','إنستغرام مخترق'),('/ar/facebook-hisab-muattal/','فيسبوك معطّل'),('/ar/safhat-facebook/','صفحات فيسبوك'),('/ar/hisab-ilanat-meta-muqayyad/','حسابات الإعلانات'),('/ar/ism-mustakhdim-instagram/','أسماء المستخدمين'),('/ar/tiktok-mahzur/','تيك توك'),('/ar/asaar/','الأسعار')],
  indep='خدمة مستقلة. غير تابعة لميتا.',mob=('راسلنا على واتساب','البريد'),
  clients='عملاؤنا',said='ماذا يقول العملاء',transcript='النص (بالإنجليزية)',qa='إجابات سريعة',good='من المفيد معرفته.',tell='أخبرنا بما حدث.',email='راسلنا بالبريد',privacy=('الخصوصية (EN)','الشروط (EN)')),
'it':dict(skip='Vai al contenuto',menu='Apri il menu',mainnav='Navigazione principale',mobnav='Navigazione mobile',
  nav=[('/it/','Home'),('/it/account-instagram-disattivato/','Instagram'),('/it/account-facebook-disattivato/','Facebook'),('/it/link-ricorso-meta-instagram-facebook/','Link di ricorso'),('/it/prezzi/','Prezzi'),('/contact/','Contatti')],
  tag='Recupero account &amp; nomi utente.<br>Parla direttamente con noi.',
  foot=[('/it/','Tutte le guide in italiano'),('/it/link-ricorso-meta-instagram-facebook/','Link di ricorso Meta'),('/it/contattare-assistenza-meta/','Contattare Meta'),('/it/account-instagram-disattivato/','Instagram disattivato'),('/it/instagram-hackerato/','Instagram hackerato'),('/it/account-facebook-disattivato/','Facebook disattivato'),('/it/account-pubblicitario-meta-limitato/','Account pubblicitari'),('/it/nome-utente-instagram/','Nomi utente'),('/it/account-tiktok-bannato/','TikTok'),('/it/prezzi/','Prezzi')],
  indep='Servizio indipendente. Non affiliato a Meta.',mob=('Scrivici su WhatsApp','Email'),
  clients='CLIENTI',said='Cosa dicono i clienti',transcript='Trascrizione (in inglese)',qa='RISPOSTE RAPIDE',good='Da sapere.',tell='Raccontaci cosa è successo.',email='Scrivici un’email',privacy=('Privacy (EN)','Termini (EN)')),
'tr':dict(skip='İçeriğe geç',menu='Menüyü aç',mainnav='Ana gezinme',mobnav='Mobil gezinme',
  nav=[('/tr/','Ana sayfa'),('/tr/instagram-hesabi-devre-disi/','Instagram'),('/tr/facebook-hesabi-devre-disi/','Facebook'),('/tr/meta-itiraz-linkleri/','İtiraz linkleri'),('/tr/fiyatlar/','Fiyatlar'),('/contact/','İletişim')],
  tag='Hesap &amp; kullanıcı adı kurtarma.<br>Bizimle doğrudan konuşun.',
  foot=[('/tr/','Tüm Türkçe rehberler'),('/tr/meta-itiraz-linkleri/','Meta itiraz linkleri'),('/tr/meta-destek-ile-iletisim/','Meta ile iletişim'),('/tr/instagram-hesabi-devre-disi/','Instagram devre dışı'),('/tr/instagram-hacklendi/','Instagram hacklendi'),('/tr/facebook-hesabi-devre-disi/','Facebook devre dışı'),('/tr/meta-reklam-hesabi-kisitlandi/','Reklam hesapları'),('/tr/instagram-kullanici-adi/','Kullanıcı adları'),('/tr/tiktok-hesabi-banlandi/','TikTok'),('/tr/fiyatlar/','Fiyatlar')],
  indep='Bağımsız hizmet. Meta ile bağlantılı değildir.',mob=('WhatsApp’tan yazın','E-posta'),
  clients='MÜŞTERİLER',said='Müşterilerimiz ne diyor',transcript='Döküm (İngilizce)',qa='KISA YANITLAR',good='Bilmeniz gerekenler.',tell='Ne olduğunu anlatın.',email='E-posta gönderin',privacy=('Gizlilik (EN)','Şartlar (EN)'))}
LBL={'de': ['Facebook-Werbekonto', 'Nutzername', 'Agenturinhaber', 'Werbekonto', 'Instagram-Nutzername'], 'ar': ['حساب إعلانات فيسبوك', 'اسم مستخدم', 'صاحب وكالة', 'حساب إعلانات', 'اسم مستخدم إنستغرام'], 'it': ['Account pubblicitario Facebook', 'Nome utente', 'Titolare di agenzia', 'Account pubblicitario', 'Nome utente Instagram'], 'tr': ['Facebook reklam hesabı', 'Kullanıcı adı', 'Ajans sahibi', 'Reklam hesabı', 'Instagram kullanıcı adı']}
def langlinks(lang,alts):
    alts=alts or {}
    out=''
    for l in ('en','fr','es','pt-br','nl','de','ar','it','tr'):
        if l==lang: continue
        href='/'+alts[l].strip('/')+'/' if alts.get(l) is not None and alts.get(l)!='' else ('/' if l=='en' and alts.get('en')=='' else HUB[l])
        out+=f'<a href="{href}" hreflang="{gen.HL.get(l,l)}" lang="{gen.HL.get(l,l)}">{LN[l]}</a>'
    return out
def localize(out,lang,alts=None):
    S=L[lang]
    hdr=(f'<header class="service-header container"><a class="wordmark" href="{HUB[lang]}">unbanz.</a><nav class="desktop-nav" aria-label="{S["mainnav"]}">'+''.join(a(h,t) for h,t in S['nav'][1:])+
         f'</nav><button class="menu-button" aria-label="{S["menu"]}" aria-expanded="false" aria-controls="mobile-nav"><span></span><span></span><span></span></button></header>'
         f'<nav class="mobile-nav" id="mobile-nav" hidden aria-label="{S["mobnav"]}">'+''.join(a(h,t) for h,t in S['nav'])+'</nav>')
    out=re.sub(r'<header class="service-header container">.*?</header>\s*<nav class="mobile-nav".*?</nav>',lambda m:hdr,out,count=1,flags=re.S)
    ft=(f'<footer class="site-footer container"><div class="footer-top"><a class="wordmark" href="{HUB[lang]}">unbanz.</a><p>{S["tag"]}</p><div class="footer-links">'+''.join(a(h,t) for h,t in S['foot'])+
        langlinks(lang,alts)+f'<a href="/privacy/" hreflang="en" lang="en">{S["privacy"][0]}</a><a href="/terms/" hreflang="en" lang="en">{S["privacy"][1]}</a></div></div>'
        f'<div class="footer-bottom"><span>© <span id="year">2026</span> Unbanz</span><span>{S["indep"]}</span><a href="mailto:team@unbanz.com?subject=Account%20help">team@unbanz.com</a></div></footer>')
    out=re.sub(r'<footer class="site-footer container">.*?</footer>',lambda m:ft,out,count=1,flags=re.S)
    out=re.sub(r'(<div class="mobile-contact"><a[^>]*>)[^<]*(<span aria-hidden="true">↗︎</span></a><a href="mailto:[^"]*">)[^<]*(</a>)',lambda m:m.group(1)+S['mob'][0]+' '+m.group(2)+S['mob'][1]+m.group(3),out,count=1)
    out=re.sub(r'<nav class="related-services container"[^>]*>.*?</nav>','',out,flags=re.S)
    for x,y in [('>CLIENTS<','>'+S['clients']+'<'),('>What clients say<','>'+S['said']+'<'),('<summary>Transcript</summary>','<summary>'+S['transcript']+'</summary>'),('>QUICK ANSWERS<','>'+S['qa']+'<'),('<h2>Good to know.</h2>','<h2>'+S['good']+'</h2>'),('<h2>Tell us what you need.</h2>','<h2>'+S['tell']+'</h2>'),('>Email us<','>'+S['email']+'<'),('Message us on WhatsApp',gen.CTA[lang][0]),('Skip to content',S['skip']),('Main navigation',S['mainnav']),('aria-label="Open menu"','aria-label="'+S['menu']+'"'),
                ('>KURZE ANTWORTEN<','>'+S['qa']+'<'),('<h2>Gut zu wissen.</h2>','<h2>'+S['good']+'</h2>'),('<h2>Sag uns, was passiert ist.</h2>','<h2>'+S['tell']+'</h2>'),('>E-Mail schreiben<','>'+S['email']+'<'),('Schreib uns auf WhatsApp',gen.CTA[lang][0]),('>Was Kunden sagen<','>'+S['said']+'<'),('Zum Inhalt springen',S['skip'])]:
        out=out.replace(x,y)
    for x,y in zip(['Facebook ad account','Username claim','Agency owner','Ad account','Instagram username'],LBL[lang]): out=out.replace('>'+x+'<','>'+y+'<')
    # testimonial quotes are English video transcripts: mark them
    out=re.sub(r'<blockquote(?![^>]*lang=)','<blockquote lang="en"',out)
    if lang=='ar': out=re.sub(r'<html lang="ar"(?! dir)','<html lang="ar" dir="rtl"',out,count=1)
    return out
def build(p):
    url=gen.build(p)
    lang=p.get('lang','en')
    if lang in L:
        f=f"{gen.SITE}/{p['slug'].strip('/')}/index.html"
        t=open(f).read()
        if lang!='de' or True:
            t=t.replace('<h2 id="related">Related</h2>',f'<h2 id="related">{REL.get(lang,"Related")}</h2>')
        open(f,'w').write(localize(t,lang,p.get('alts')))
    return url
