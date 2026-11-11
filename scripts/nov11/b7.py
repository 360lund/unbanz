import b5, b6
from b5 import add, lr, HELP
from gen import ul, ol, a, ext
b5.P.clear()
BP='guides/meta-business-portfolio-lost-admin-access'; AC='how-to-appeal-in-accounts-center'
BSH='https://business.facebook.com/business-support-home/'; AQ='https://business.facebook.com/accountquality'; BH='https://www.facebook.com/business/help'
ACC='https://accountscenter.instagram.com/'
BPH={'fr':'<p>Unbanz récupère les Business Portfolios pour 1 500 $, payés d’avance par carte, remboursés à 100 % si le dossier échoue. Indépendant de Meta ; nous ne demandons jamais de mot de passe. <a href="mailto:team@unbanz.com">team@unbanz.com</a></p>',
'es':'<p>Unbanz recupera Business Portfolios por 1.500 $, pagados por adelantado con tarjeta y con reembolso del 100 % si el caso falla. Independiente de Meta; nunca pedimos contraseñas. <a href="mailto:team@unbanz.com">team@unbanz.com</a></p>',
'de':'<p>Unbanz holt Business-Portfolios für 1.500 $ zurück, im Voraus per Karte bezahlt, mit 100 % Rückerstattung, wenn der Fall scheitert. Unabhängig von Meta; wir fragen nie nach Passwörtern. <a href="mailto:team@unbanz.com">team@unbanz.com</a></p>',
'it':'<p>Unbanz recupera i Business Portfolio a 1.500 $, pagati in anticipo con carta, con rimborso del 100% se il caso fallisce. Indipendente da Meta; non chiediamo mai password. <a href="mailto:team@unbanz.com">team@unbanz.com</a></p>',
'ar':'<p>تسترجع Unbanz حسابات Business Portfolio مقابل 1,500 دولار، تُدفع مقدّماً بالبطاقة مع استرداد 100% إذا فشلت الحالة. مستقلة عن ميتا ولا نطلب كلمات المرور أبداً. <a href="mailto:team@unbanz.com">team@unbanz.com</a></p>'}
def bp(l,slug,title,short,desc,h1,lede,answer,cards,s1,s2,s3,lt,faqs,rel):
    add(l,BP,slug,'bm','Business Portfolio','1500',title=title,short=short,desc=desc,h1=h1,lede=lede,answer=answer,cards=cards,
      sections=[('s1',s1[0],ol(s1[1])),('s2',s2[0],ul(s2[1])),('s3',s3[0],ul(s3[1])),('links',lt,lr(l,[('Business Support Home',BSH,'Meta'),('Account Quality',AQ,'Meta'),('Meta Business Help Center',BH,'Meta')]))],faqs=faqs,related=rel)
    b5.P[-1]['sections'][-1]=(HELP[l][0],HELP[l][1],BPH[l])
bp('fr','acces-admin-business-portfolio-perdu','Accès administrateur perdu à un Business Portfolio Meta : que faire ? (2026)','Admin Business Portfolio perdu',
 'Vous n’êtes plus administrateur de votre portefeuille Meta Business ? Demander à un admin, demander le contrôle total via Business Support Home, cas de piratage et documents à préparer.',
 'Accès admin perdu à votre Business Portfolio.','Pages, comptes publicitaires et paiements bloqués : l’ordre des démarches.',
 '<strong>Demandez d’abord à un administrateur ayant le contrôle total de vous rajouter. Si personne ne le peut, demandez le contrôle total à Meta via Business Support Home, avec pièce d’identité et preuves de l’entreprise.</strong> Si le portefeuille a été piraté, sécurisez d’abord votre profil personnel, puis suivez les étapes de Meta pour les portefeuilles piratés.',
 [('Un admin restant ?','La voie la plus rapide.'),('Contrôle total','Demande à Meta.'),('Documents','Identité et entreprise.')],
 ('Dans l’ordre',['Identifiez qui a encore accès : anciens e-mails d’invitation, équipe, agence.','Connectez-vous avec le profil personnel invité à l’origine.','Demandez à un admin de vous redonner le contrôle total.','Sinon, demandez le contrôle total à Meta.']),
 ('Documents utiles',['Pièce d’identité correspondant au profil.','Extrait d’immatriculation ou facture au nom de l’entreprise.','Domaine du site et e-mail professionnel.']),
 ('À éviter',['Créer un nouveau portefeuille pour les mêmes Pages et comptes.','Payer quelqu’un qui promet un « accès interne ».']),'Liens officiels',
 [('Combien de temps prend une demande de contrôle total ?','De quelques jours à plusieurs semaines, sans garantie.')],[('/fr/','Unbanz en français')])
bp('es','acceso-admin-business-portfolio-perdido','Perdí el acceso de administrador al Business Portfolio de Meta: qué hacer (2026)','Admin de Business Portfolio perdido',
 '¿Ya no eres administrador de tu portfolio empresarial de Meta? Pedir a un admin, solicitar control total en Business Support Home, hackeos y documentos necesarios.',
 'Perdiste el acceso de administrador.','Páginas, cuentas publicitarias y pagos bloqueados: el orden correcto.',
 '<strong>Primero pide a un administrador con control total que te vuelva a añadir. Si nadie puede, solicita el control total a Meta desde Business Support Home, con identificación y pruebas de la empresa.</strong> Si el portfolio fue hackeado, protege antes tu perfil personal y sigue los pasos de Meta para portfolios hackeados.',
 [('¿Queda un admin?','La vía más rápida.'),('Control total','Solicitud a Meta.'),('Documentos','Identidad y empresa.')],
 ('En orden',['Averigua quién conserva acceso: correos de invitación, equipo, agencia.','Entra con el perfil personal invitado originalmente.','Pide a un admin que te devuelva el control total.','Si no, solicita el control total a Meta.']),
 ('Documentos útiles',['Identificación que coincida con el perfil.','Registro mercantil o factura a nombre de la empresa.','Dominio web y correo corporativo.']),
 ('Qué evitar',['Crear otro portfolio para las mismas páginas y cuentas.','Pagar a quien promete «acceso interno».']),'Enlaces oficiales',
 [('¿Cuánto tarda el control total?','De días a varias semanas, sin garantía.')],[('/es/','Unbanz en español')])
bp('de','business-portfolio-adminzugang-verloren','Adminzugang zum Meta Business-Portfolio verloren: was tun? (2026)','Business-Portfolio-Admin verloren',
 'Kein Admin mehr in deinem Meta Business-Portfolio? Admin fragen, volle Kontrolle über Business Support Home beantragen, Hack-Fälle und nötige Unterlagen.',
 'Adminzugang zum Business-Portfolio verloren.','Seiten, Werbekonten und Zahlungen gesperrt: die richtige Reihenfolge.',
 '<strong>Bitte zuerst einen Admin mit voller Kontrolle, dich wieder hinzuzufügen. Kann das niemand, beantrage die volle Kontrolle bei Meta über Business Support Home, mit Ausweis und Unternehmensnachweis.</strong> Wurde das Portfolio gehackt, sichere zuerst dein Privatprofil und folge dann Metas Schritten für gehackte Portfolios.',
 [('Noch ein Admin?','Der schnellste Weg.'),('Volle Kontrolle','Antrag bei Meta.'),('Unterlagen','Ausweis und Firma.')],
 ('Reihenfolge',['Klären, wer noch Zugriff hat: alte Einladungs-Mails, Team, Agentur.','Mit dem ursprünglich eingeladenen Privatprofil anmelden.','Einen Admin um volle Kontrolle bitten.','Sonst volle Kontrolle bei Meta beantragen.']),
 ('Hilfreiche Unterlagen',['Ausweis passend zum Profil.','Handelsregisterauszug oder Rechnung auf die Firma.','Website-Domain und geschäftliche E-Mail.']),
 ('Lieber lassen',['Ein neues Portfolio für dieselben Seiten und Konten anlegen.','Passwort oder Codes an Fremde weitergeben.']),'Offizielle Links',
 [('Wie lange dauert ein Antrag auf volle Kontrolle?','Einige Tage bis Wochen, ohne Garantie.')],[('/de/','Unbanz auf Deutsch')])
bp('it','accesso-admin-business-portfolio-perso','Accesso admin al Business Portfolio Meta perso: cosa fare (2026)','Admin Business Portfolio perso',
 'Non sei più amministratore del tuo portfolio aziendale Meta? Chiedere a un admin, richiedere il controllo completo da Business Support Home, casi di hackeraggio e documenti.',
 'Accesso admin al Business Portfolio perso.','Pagine, account pubblicitari e pagamenti bloccati: l’ordine giusto.',
 '<strong>Chiedi prima a un amministratore con controllo completo di riaggiungerti. Se nessuno può, richiedi il controllo completo a Meta da Business Support Home, con documento d’identità e prove dell’azienda.</strong> Se il portfolio è stato hackerato, metti prima in sicurezza il profilo personale e segui i passaggi di Meta per i portfolio compromessi.',
 [('Un admin rimasto?','La via più rapida.'),('Controllo completo','Richiesta a Meta.'),('Documenti','Identità e azienda.')],
 ('In ordine',['Scopri chi ha ancora accesso: email di invito, team, agenzia.','Accedi con il profilo personale invitato all’inizio.','Chiedi a un admin il controllo completo.','Altrimenti richiedilo a Meta.']),
 ('Documenti utili',['Documento che corrisponde al profilo.','Visura camerale o fattura intestata all’azienda.','Dominio del sito ed email aziendale.']),
 ('Da evitare',['Creare un nuovo portfolio per le stesse Pagine e account.','Dare password o codici a sconosciuti.']),'Link ufficiali',
 [('Quanto ci vuole?','Da qualche giorno a qualche settimana, senza garanzia.')],[('/it/','Unbanz in italiano')])
bp('ar','fuqdan-sallahiyat-business-portfolio','فقدت صلاحية المسؤول في Business Portfolio على ميتا: ماذا أفعل؟ (2026)','فقدان صلاحية المسؤول',
 'لم تعد مسؤولاً عن حساب Business Portfolio على ميتا؟ اطلب من مسؤول آخر، أو اطلب التحكم الكامل عبر Business Support Home، وحالات الاختراق والمستندات المطلوبة.',
 'فقدت صلاحية المسؤول في Business Portfolio.','الصفحات وحسابات الإعلانات والمدفوعات متوقفة: الترتيب الصحيح.',
 '<strong>اطلب أولاً من مسؤول لديه تحكم كامل أن يضيفك من جديد. إن لم يستطع أحد، اطلب التحكم الكامل من ميتا عبر Business Support Home مع الهوية وإثبات النشاط التجاري.</strong> إذا اختُرق الحساب، أمّن ملفك الشخصي أولاً ثم اتبع خطوات ميتا الخاصة بالحسابات التجارية المخترقة.',
 [('مسؤول متبقٍ؟','أسرع طريق.'),('التحكم الكامل','طلب إلى ميتا.'),('المستندات','الهوية والنشاط.')],
 ('بالترتيب',['اعرف من لا يزال لديه وصول: رسائل الدعوة القديمة، الفريق، الوكالة.','سجّل الدخول بالملف الشخصي الذي دُعي أصلاً.','اطلب من مسؤول منحك التحكم الكامل.','وإلا فاطلبه من ميتا.']),
 ('مستندات مفيدة',['هوية تطابق الملف الشخصي.','سجل تجاري أو فاتورة باسم النشاط.','نطاق الموقع وبريد العمل.']),
 ('تجنّب',['إنشاء حساب تجاري جديد للصفحات والحسابات نفسها.','الدفع لمن يعد «بوصول داخلي».']),'الروابط الرسمية',
 [('كم يستغرق طلب التحكم الكامل؟','من أيام إلى أسابيع، دون ضمان.')],[('/ar/','Unbanz بالعربية')])
def acc(l,slug,title,short,desc,h1,lede,answer,cards,steps,nob,lt,faqs,rel):
    add(l,AC,slug,'ig','Instagram','800',title=title,short=short,desc=desc,h1=h1,lede=lede,answer=answer,cards=cards,
      sections=[('steps',steps[0],ol(steps[1])),('no-button',nob[0],'<p>'+nob[1]+'</p>'),('links',lt,lr(l,[('Accounts Center',ACC,'Meta'),('Account Quality',AQ,'Meta')]))],faqs=faqs,related=rel)
acc('es','como-apelar-en-el-centro-de-cuentas','Cómo apelar en el Centro de cuentas de Meta (Instagram y Facebook, 2026)','Apelar en el Centro de cuentas',
 'Dónde está «Estado de la cuenta» en el Centro de cuentas de Meta y cómo pedir una revisión para Instagram o Facebook, paso a paso.',
 'Cómo apelar en el Centro de cuentas.','Dónde está el estado de la cuenta y qué significa cada opción.',
 '<strong>Abre Configuración en Instagram o Facebook, entra en Centro de cuentas, luego en Estado de la cuenta, elige la cuenta, abre la decisión y toca la opción para no estar de acuerdo o solicitar una revisión.</strong> Si no puedes iniciar sesión, el aviso de la pantalla de inicio tiene el mismo botón. Los nombres de los menús cambian según la versión: sigue lo que veas en pantalla.',
 [('Centro de cuentas','Estado de la cuenta.'),('Sin sesión','El aviso tiene el botón.'),('Empresas','Calidad de la cuenta.')],
 ('Pasos',['Abre Instagram o Facebook y ve a Configuración.','Toca Centro de cuentas.','Elige Estado de la cuenta (o Calidad de la cuenta para activos de empresa).','Selecciona el perfil y la decisión.','Toca No estoy de acuerdo o Solicitar revisión y sigue las indicaciones, que pueden incluir un selfie en vídeo.']),
 ('¿No hay botón?','A veces no aparece la opción, sobre todo si la decisión es definitiva o el plazo terminó. Haz una captura con fecha. En la UE, Appeals Centre Europe puede ser una opción cuando termina el proceso de Meta.'),'Enlaces oficiales',
 [('¿Sirve para cuentas hackeadas?','No: empieza en instagram.com/hacked o facebook.com/hacked.')],[('/es/no-puedes-solicitar-otra-revision/','No puedes solicitar otra revisión')])
acc('pt-br','como-recorrer-na-central-de-contas','Como recorrer na Central de Contas da Meta (Instagram e Facebook, 2026)','Recorrer na Central de Contas',
 'Onde fica “Status da conta” na Central de Contas da Meta e como pedir uma análise para Instagram ou Facebook, passo a passo.',
 'Como recorrer na Central de Contas.','Onde fica o status da conta e o que cada opção significa.',
 '<strong>Abra Configurações no Instagram ou no Facebook, entre na Central de Contas, depois em Status da conta, escolha a conta, abra a decisão e toque na opção de discordar ou solicitar análise.</strong> Se você não consegue entrar, o aviso na tela de login tem o mesmo botão. Os nomes dos menus mudam conforme a versão: siga o que aparece na sua tela.',
 [('Central de Contas','Status da conta.'),('Sem login','O aviso tem o botão.'),('Empresas','Qualidade da conta.')],
 ('Passos',['Abra o Instagram ou o Facebook e vá em Configurações.','Toque em Central de Contas.','Escolha Status da conta (ou Qualidade da conta para ativos de empresa).','Selecione o perfil e a decisão.','Toque em Discordar ou Solicitar análise e siga as instruções, que podem incluir uma selfie em vídeo.']),
 ('Sem botão?','Às vezes a opção não aparece, principalmente quando a decisão é final ou o prazo acabou. Tire um print com data.'),'Links oficiais',
 [('Serve para conta hackeada?','Não: comece em instagram.com/hacked ou facebook.com/hacked.')],[('/pt-br/voce-nao-pode-solicitar-outra-analise/','Você não pode solicitar outra análise')])
acc('de','einspruch-in-der-kontenuebersicht','Einspruch in der Meta-Kontenübersicht einlegen (Instagram und Facebook, 2026)','Einspruch in der Kontenübersicht',
 'Wo „Kontostatus“ in der Meta-Kontenübersicht zu finden ist und wie du für Instagram oder Facebook eine Überprüfung beantragst, Schritt für Schritt.',
 'Einspruch in der Kontenübersicht.','Wo der Kontostatus ist und was jede Option bedeutet.',
 '<strong>Öffne in Instagram oder Facebook die Einstellungen, tippe auf Kontenübersicht, dann auf Kontostatus, wähle das Konto, öffne die Entscheidung und tippe auf die Option, um zu widersprechen oder eine Überprüfung zu beantragen.</strong> Kannst du dich nicht anmelden, hat die Meldung auf dem Login-Bildschirm denselben Button. Menünamen ändern sich je nach App-Version.',
 [('Kontenübersicht','Kontostatus.'),('Ohne Login','Button in der Meldung.'),('Unternehmen','Kontoqualität.')],
 ('Schritte',['Instagram oder Facebook öffnen, Einstellungen.','Kontenübersicht antippen.','Kontostatus wählen (oder Kontoqualität für Business-Assets).','Profil und Entscheidung auswählen.','Widersprechen oder Überprüfung beantragen und den Schritten folgen, eventuell mit Video-Selfie.']),
 ('Kein Button?','Manchmal fehlt die Option, etwa wenn die Entscheidung endgültig ist oder die Frist abgelaufen ist. Mach einen datierten Screenshot. In der EU bleiben danach User Rights oder Appeals Centre Europe.'),'Offizielle Links',
 [('Gilt das für gehackte Konten?','Nein, dafür instagram.com/hacked oder facebook.com/hacked.')],[('/de/keine-weitere-ueberpruefung-moeglich/','Keine weitere Überprüfung möglich')])
acc('it','come-fare-ricorso-nel-centro-gestione-account','Come fare ricorso nel Centro gestione account di Meta (Instagram e Facebook, 2026)','Ricorso nel Centro gestione account',
 'Dove si trova “Stato dell’account” nel Centro gestione account di Meta e come chiedere una revisione per Instagram o Facebook, passo per passo.',
 'Come fare ricorso nel Centro gestione account.','Dove trovare lo stato dell’account e cosa significa ogni opzione.',
 '<strong>Apri Impostazioni su Instagram o Facebook, tocca Centro gestione account, poi Stato dell’account, scegli l’account, apri la decisione e tocca l’opzione per contestarla o chiedere una revisione.</strong> Se non riesci ad accedere, l’avviso nella schermata di accesso ha lo stesso pulsante. I nomi dei menu cambiano con le versioni dell’app.',
 [('Centro gestione account','Stato dell’account.'),('Senza accesso','Il pulsante è nell’avviso.'),('Aziende','Qualità dell’account.')],
 ('Passaggi',['Apri Instagram o Facebook e vai in Impostazioni.','Tocca Centro gestione account.','Scegli Stato dell’account (o Qualità dell’account per le risorse aziendali).','Seleziona il profilo e la decisione.','Tocca Non sono d’accordo o Richiedi revisione e segui le istruzioni, che possono includere un video selfie.']),
 ('Nessun pulsante?','A volte l’opzione manca, spesso perché la decisione è definitiva o il termine è scaduto. Fai uno screenshot con la data. Nell’UE restano gli organismi DSA certificati.'),'Link ufficiali',
 [('Vale per gli account hackerati?','No: parti da instagram.com/hacked o facebook.com/hacked.')],[('/it/non-puoi-richiedere-unaltra-revisione/','Non puoi richiedere un’altra revisione')])
acc('tr','hesap-merkezinde-itiraz-nasil-yapilir','Meta Hesap Merkezi’nde itiraz nasıl yapılır? (Instagram ve Facebook, 2026)','Hesap Merkezi’nde itiraz',
 'Meta Hesap Merkezi’nde “Hesap durumu” nerede ve Instagram ya da Facebook için inceleme nasıl istenir, adım adım.',
 'Hesap Merkezi’nde itiraz.','Hesap durumu nerede ve her seçenek ne anlama gelir.',
 '<strong>Instagram veya Facebook’ta Ayarlar’ı açın, Hesap Merkezi’ne, ardından Hesap durumu’na girin, hesabı seçin, kararı açın ve itiraz etme ya da inceleme isteme seçeneğine dokunun.</strong> Giriş yapamıyorsanız giriş ekranındaki bildirimde aynı düğme bulunur. Menü adları uygulama sürümüne göre değişir.',
 [('Hesap Merkezi','Hesap durumu.'),('Giriş yoksa','Düğme bildirimde.'),('İşletmeler','Hesap kalitesi.')],
 ('Adımlar',['Instagram veya Facebook’u açıp Ayarlar’a gidin.','Hesap Merkezi’ne dokunun.','Hesap durumu’nu (işletme varlıkları için Hesap kalitesi’ni) seçin.','Profili ve kararı seçin.','Karara itiraz et veya İnceleme iste seçeneğine dokunun; video selfie istenebilir.']),
 ('Düğme yok mu?','Bazen seçenek görünmez; çoğu zaman karar kesinleşmiştir veya süre dolmuştur. Tarihli bir ekran görüntüsü alın.'),'Resmi bağlantılar',
 [('Hacklenen hesaplar için mi?','Hayır, instagram.com/hacked veya facebook.com/hacked ile başlayın.')],[('/tr/baska-inceleme-isteyemezsin/','Başka inceleme isteyemezsin')])
acc('ar','kayfa-tastanif-fi-markaz-alhisabat','كيف تعترض من مركز الحسابات في ميتا؟ (إنستغرام وفيسبوك 2026)','الاعتراض من مركز الحسابات',
 'أين تجد «حالة الحساب» في مركز الحسابات لدى ميتا وكيف تطلب مراجعة لحساب إنستغرام أو فيسبوك، خطوة بخطوة.',
 'الاعتراض من مركز الحسابات.','أين حالة الحساب وماذا يعني كل خيار.',
 '<strong>افتح الإعدادات في إنستغرام أو فيسبوك، ثم مركز الحسابات، ثم حالة الحساب، واختر الحساب وافتح القرار واضغط خيار الاعتراض أو طلب المراجعة.</strong> إذا لم تستطع تسجيل الدخول، ففي إشعار شاشة الدخول الزر نفسه. أسماء القوائم تتغير بين إصدارات التطبيق.',
 [('مركز الحسابات','حالة الحساب.'),('دون تسجيل دخول','الزر في الإشعار.'),('الأعمال','جودة الحساب.')],
 ('الخطوات',['افتح إنستغرام أو فيسبوك واذهب إلى الإعدادات.','اضغط مركز الحسابات.','اختر حالة الحساب (أو جودة الحساب لأصول الأعمال).','حدّد الملف الشخصي والقرار.','اضغط «لا أوافق» أو «طلب مراجعة» واتبع الخطوات، وقد يُطلب سيلفي فيديو.']),
 ('لا يوجد زر؟','أحياناً لا يظهر الخيار، غالباً لأن القرار نهائي أو انتهت المهلة. التقط صورة شاشة بالتاريخ. انظر '+a('/ar/la-yumkin-talab-muraja-ukhra/','لا يمكنك طلب مراجعة أخرى')+'.'),'الروابط الرسمية',
 [('هل يصلح للحسابات المخترقة؟','لا، ابدأ من instagram.com/hacked أو facebook.com/hacked.')],[('/ar/','Unbanz بالعربية')])
P=list(b5.P)
