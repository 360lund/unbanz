// Email topic picker v3 (Nov 15 2026): two-step sheet. Step 1 = topic cards (grouped, icons), step 2 = username +
// optional "how did you hear" + sticky "Write the email". Mobile: bottom sheet with drag handle; desktop: centered modal.
// Same output as v2: intercepts team@unbanz.com mailto clicks, same topic values, same subject/body template, and
// "How I heard about Unbanz: …" appended to the body (what hear-source.js did). Tracking: the dialog keeps .cm-dialog,
// the topic cards keep .cm-pill[data-group="service"][aria-pressed] and the final link keeps data-service/data-platform.
// The plain mailto href stays as the no-JS fallback. Email is the only contact channel.
// After a first "Write the email" click, show a success state and do not open mailto again for 6 hours on this
// browser (localStorage: timestamp + username when present). There is no server lead-mail API to dedupe.
(function () {
  try {
    if (document.body && document.body.classList.contains('cta-hold')) return;
    var lang = (document.documentElement.lang || 'en').toLowerCase().slice(0, 2);
    var LANGS = {
      en: {
        eyebrow: 'EMAIL US', title: 'What do you need help with?',
        hint: 'Pick one and your email opens with a short template ready to fill in.',
        user: 'Your username or profile link', opt: '(optional)', ph: '@username or link',
        go: 'Write the email', note: 'Never send passwords or login codes.', close: 'Close',
        ok: 'Got it. We\'ll email you shortly, usually within the hour. Check your inbox and spam.',
        hi: 'Hi Unbanz', f: ['My issue', 'My username or profile link', 'What the notice says', 'Did I already appeal', 'Country'], bye: 'Thanks',
        back: 'Back', change: 'Change', gIg: 'Instagram', gFb: 'Facebook', gAds: 'Ads & Business', gOther: 'Other platforms', step: 'Step %s of 2',
        hear: ['How did you hear about us?', 'Skip', 'ChatGPT or another AI assistant', 'Google or another search engine', 'A person I know', 'Instagram, Facebook or another app', 'Somewhere else'],
        t: [
          ['ig_disabled', 'Instagram disabled / suspended', 'Instagram disabled - help', 'Instagram account disabled', 'Instagram'],
          ['ig_hacked', 'Instagram hacked', 'Instagram hacked - help', 'Instagram account hacked', 'Instagram'],
          ['fb', 'Facebook disabled / hacked', 'Facebook account - help', 'Facebook account disabled or hacked', 'Facebook'],
          ['ad', 'Ad account restricted', 'Ad account restricted - help', 'Ad account restricted or disabled', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - help', 'Business Portfolio / Business Manager restricted', 'Facebook'],
          ['username', 'Username', 'Username claim - help', 'Username claim', 'Instagram'],
          ['snap', 'Snapchat', 'Snapchat account - help', 'Snapchat account locked or banned', 'Snapchat'],
          ['page', 'Facebook Page', 'Facebook Page - help', 'Facebook Page disabled or restricted', 'Facebook'],
          ['tiktok', 'TikTok', 'TikTok account - help', 'TikTok account banned or suspended', 'TikTok'],
          ['youtube', 'YouTube channel', 'YouTube channel - help', 'YouTube channel terminated or hacked', 'YouTube'],
          ['whatsapp', 'WhatsApp number', 'WhatsApp number - help', 'WhatsApp number banned', 'WhatsApp'],
          ['other', 'Other', 'Account help', 'Other', '']
        ]
      },
      fr: {
        eyebrow: 'ÉCRIVEZ-NOUS', title: 'Pour quoi avez-vous besoin d’aide ?',
        hint: 'Choisissez une option : votre e-mail s’ouvre avec un court modèle à compléter.',
        user: 'Votre nom d’utilisateur ou lien du profil', opt: '(facultatif)', ph: '@pseudo ou lien',
        go: 'Écrire l’e-mail', note: 'N’envoyez jamais de mot de passe ni de code de connexion.', close: 'Fermer',
        ok: 'C’est noté. Nous vous écrirons sous peu, en général dans l’heure. Vérifiez votre boîte de réception et vos spams.',
        hi: 'Bonjour Unbanz', f: ['Mon problème', 'Mon nom d’utilisateur ou lien du profil', 'Ce que dit la notification', 'Ai-je déjà fait appel', 'Pays'], bye: 'Merci',
        back: 'Retour', change: 'Modifier', gIg: 'Instagram', gFb: 'Facebook', gAds: 'Publicité et Business', gOther: 'Autres plateformes', step: 'Étape %s sur 2',
        hear: ['Comment nous avez-vous connus ?', 'Passer', 'ChatGPT ou un autre assistant', 'Google ou un autre moteur', 'Une personne que je connais', 'Instagram, Facebook ou une autre app', 'Ailleurs'],
        t: [
          ['ig_disabled', 'Instagram désactivé / suspendu', 'Instagram désactivé - aide', 'Compte Instagram désactivé', 'Instagram'],
          ['ig_hacked', 'Instagram piraté', 'Instagram piraté - aide', 'Compte Instagram piraté', 'Instagram'],
          ['fb', 'Facebook désactivé / piraté', 'Compte Facebook - aide', 'Compte Facebook désactivé ou piraté', 'Facebook'],
          ['ad', 'Compte publicitaire restreint', 'Compte publicitaire restreint - aide', 'Compte publicitaire restreint ou désactivé', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - aide', 'Business Portfolio / Business Manager restreint', 'Facebook'],
          ['username', 'Nom d’utilisateur', 'Nom d’utilisateur - aide', 'Récupérer un nom d’utilisateur', 'Instagram'],
          ['snap', 'Snapchat', 'Compte Snapchat - aide', 'Compte Snapchat bloqué ou banni', 'Snapchat'],
          ['page', 'Page Facebook', 'Page Facebook - aide', 'Page Facebook désactivée ou restreinte', 'Facebook'],
          ['tiktok', 'TikTok', 'Compte TikTok - aide', 'Compte TikTok banni ou suspendu', 'TikTok'],
          ['youtube', 'Chaîne YouTube', 'Chaîne YouTube - aide', 'Chaîne YouTube résiliée ou piratée', 'YouTube'],
          ['whatsapp', 'Numéro WhatsApp', 'Numéro WhatsApp - aide', 'Numéro WhatsApp banni', 'WhatsApp'],
          ['other', 'Autre', 'Aide pour un compte', 'Autre', '']
        ]
      },
      nl: {
        eyebrow: 'MAIL ONS', title: 'Waar heb je hulp bij nodig?',
        hint: 'Kies er één en je e-mail opent met een kort sjabloon om in te vullen.',
        user: 'Je gebruikersnaam of profiellink', opt: '(optioneel)', ph: '@gebruikersnaam of link',
        go: 'Schrijf de e-mail', note: 'Stuur nooit wachtwoorden of inlogcodes.', close: 'Sluiten',
        ok: 'Begrepen. We mailen je zo, meestal binnen een uur. Check je inbox en spam.',
        hi: 'Hoi Unbanz', f: ['Mijn probleem', 'Mijn gebruikersnaam of profiellink', 'Wat er in de melding staat', 'Heb ik al bezwaar gemaakt', 'Land'], bye: 'Bedankt',
        back: 'Terug', change: 'Wijzigen', gIg: 'Instagram', gFb: 'Facebook', gAds: 'Advertenties en Business', gOther: 'Andere platforms', step: 'Stap %s van 2',
        hear: ['Hoe heb je ons gevonden?', 'Overslaan', 'ChatGPT of een andere AI', 'Google of een andere zoekmachine', 'Iemand die ik ken', 'Instagram, Facebook of een andere app', 'Ergens anders'],
        t: [
          ['ig_disabled', 'Instagram uitgeschakeld / geschorst', 'Instagram uitgeschakeld - hulp', 'Instagram-account uitgeschakeld', 'Instagram'],
          ['ig_hacked', 'Instagram gehackt', 'Instagram gehackt - hulp', 'Instagram-account gehackt', 'Instagram'],
          ['fb', 'Facebook uitgeschakeld / gehackt', 'Facebook-account - hulp', 'Facebook-account uitgeschakeld of gehackt', 'Facebook'],
          ['ad', 'Advertentieaccount beperkt', 'Advertentieaccount beperkt - hulp', 'Advertentieaccount beperkt of uitgeschakeld', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - hulp', 'Business Portfolio / Business Manager beperkt', 'Facebook'],
          ['username', 'Gebruikersnaam', 'Gebruikersnaam - hulp', 'Gebruikersnaam claimen', 'Instagram'],
          ['snap', 'Snapchat', 'Snapchat-account - hulp', 'Snapchat-account geblokkeerd of verbannen', 'Snapchat'],
          ['page', 'Facebookpagina', 'Facebookpagina - hulp', 'Facebookpagina uitgeschakeld of beperkt', 'Facebook'],
          ['tiktok', 'TikTok', 'TikTok-account - hulp', 'TikTok-account verbannen of geschorst', 'TikTok'],
          ['youtube', 'YouTube-kanaal', 'YouTube-kanaal - hulp', 'YouTube-kanaal beëindigd of gehackt', 'YouTube'],
          ['whatsapp', 'WhatsApp-nummer', 'WhatsApp-nummer - hulp', 'WhatsApp-nummer verbannen', 'WhatsApp'],
          ['other', 'Anders', 'Hulp met mijn account', 'Anders', '']
        ]
      },
      es: {
        eyebrow: 'ESCRÍBENOS', title: '¿Con qué necesitas ayuda?',
        hint: 'Elige una opción y tu correo se abrirá con una plantilla corta lista para rellenar.',
        user: 'Tu nombre de usuario o enlace del perfil', opt: '(opcional)', ph: '@usuario o enlace',
        go: 'Escribir el correo', note: 'Nunca envíes contraseñas ni códigos de acceso.', close: 'Cerrar',
        ok: 'Listo. Te escribiremos en breve, normalmente en menos de una hora. Revisa tu bandeja de entrada y el spam.',
        hi: 'Hola, Unbanz', f: ['Mi problema', 'Mi nombre de usuario o enlace del perfil', 'Qué dice el aviso', '¿Ya he apelado?', 'País'], bye: 'Gracias',
        back: 'Atrás', change: 'Cambiar', gIg: 'Instagram', gFb: 'Facebook', gAds: 'Anuncios y Business', gOther: 'Otras plataformas', step: 'Paso %s de 2',
        hear: ['¿Cómo nos conociste?', 'Omitir', 'ChatGPT u otro asistente', 'Google u otro buscador', 'Una persona que conozco', 'Instagram, Facebook u otra app', 'En otro sitio'],
        t: [
          ['ig_disabled', 'Instagram desactivado / suspendido', 'Instagram desactivado - ayuda', 'Cuenta de Instagram desactivada', 'Instagram'],
          ['ig_hacked', 'Instagram hackeado', 'Instagram hackeado - ayuda', 'Cuenta de Instagram hackeada', 'Instagram'],
          ['fb', 'Facebook desactivado / hackeado', 'Cuenta de Facebook - ayuda', 'Cuenta de Facebook desactivada o hackeada', 'Facebook'],
          ['ad', 'Cuenta publicitaria restringida', 'Cuenta publicitaria restringida - ayuda', 'Cuenta publicitaria restringida o desactivada', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - ayuda', 'Business Portfolio / Business Manager restringido', 'Facebook'],
          ['username', 'Nombre de usuario', 'Nombre de usuario - ayuda', 'Reclamar un nombre de usuario', 'Instagram'],
          ['snap', 'Snapchat', 'Cuenta de Snapchat - ayuda', 'Cuenta de Snapchat bloqueada o baneada', 'Snapchat'],
          ['page', 'Página de Facebook', 'Página de Facebook - ayuda', 'Página de Facebook desactivada o restringida', 'Facebook'],
          ['tiktok', 'TikTok', 'Cuenta de TikTok - ayuda', 'Cuenta de TikTok baneada o suspendida', 'TikTok'],
          ['youtube', 'Canal de YouTube', 'Canal de YouTube - ayuda', 'Canal de YouTube cancelado o hackeado', 'YouTube'],
          ['whatsapp', 'Número de WhatsApp', 'Número de WhatsApp - ayuda', 'Número de WhatsApp baneado', 'WhatsApp'],
          ['other', 'Otro', 'Ayuda con una cuenta', 'Otro', '']
        ]
      },
      pt: {
        eyebrow: 'ENVIE UM E-MAIL', title: 'Com o que você precisa de ajuda?',
        hint: 'Escolha uma opção e seu e-mail abre com um modelo curto pronto para preencher.',
        user: 'Seu nome de usuário ou link do perfil', opt: '(opcional)', ph: '@usuario ou link',
        go: 'Escrever o e-mail', note: 'Nunca envie senhas nem códigos de acesso.', close: 'Fechar',
        ok: 'Recebido. Vamos te escrever em breve, geralmente em até uma hora. Confira sua caixa de entrada e o spam.',
        hi: 'Olá, Unbanz', f: ['Meu problema', 'Meu nome de usuário ou link do perfil', 'O que diz o aviso', 'Já fiz recurso?', 'País'], bye: 'Obrigado',
        back: 'Voltar', change: 'Alterar', gIg: 'Instagram', gFb: 'Facebook', gAds: 'Anúncios e Business', gOther: 'Outras plataformas', step: 'Etapa %s de 2',
        hear: ['Como você nos encontrou?', 'Pular', 'ChatGPT ou outro assistente', 'Google ou outro buscador', 'Uma pessoa que eu conheço', 'Instagram, Facebook ou outro app', 'Em outro lugar'],
        t: [
          ['ig_disabled', 'Instagram desativado / suspenso', 'Instagram desativado - ajuda', 'Conta do Instagram desativada', 'Instagram'],
          ['ig_hacked', 'Instagram hackeado', 'Instagram hackeado - ajuda', 'Conta do Instagram hackeada', 'Instagram'],
          ['fb', 'Facebook desativado / hackeado', 'Conta do Facebook - ajuda', 'Conta do Facebook desativada ou hackeada', 'Facebook'],
          ['ad', 'Conta de anúncios restrita', 'Conta de anúncios restrita - ajuda', 'Conta de anúncios restrita ou desativada', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - ajuda', 'Business Portfolio / Business Manager restrito', 'Facebook'],
          ['username', 'Nome de usuário', 'Nome de usuário - ajuda', 'Recuperar um nome de usuário', 'Instagram'],
          ['snap', 'Snapchat', 'Conta do Snapchat - ajuda', 'Conta do Snapchat bloqueada ou banida', 'Snapchat'],
          ['page', 'Página do Facebook', 'Página do Facebook - ajuda', 'Página do Facebook desativada ou restrita', 'Facebook'],
          ['tiktok', 'TikTok', 'Conta do TikTok - ajuda', 'Conta do TikTok banida ou suspensa', 'TikTok'],
          ['youtube', 'Canal do YouTube', 'Canal do YouTube - ajuda', 'Canal do YouTube encerrado ou hackeado', 'YouTube'],
          ['whatsapp', 'Número do WhatsApp', 'Número do WhatsApp - ajuda', 'Número do WhatsApp banido', 'WhatsApp'],
          ['other', 'Outro', 'Ajuda com uma conta', 'Outro', '']
        ]
      },
      de: {
        eyebrow: 'E-MAIL', title: 'Wobei brauchen Sie Hilfe?',
        hint: 'Wählen Sie eine Option. Ihre E-Mail öffnet sich mit einer kurzen Vorlage zum Ausfüllen.',
        user: 'Ihr Benutzername oder Profillink', opt: '(optional)', ph: '@benutzername oder Link',
        go: 'E-Mail schreiben', note: 'Senden Sie niemals Passwörter oder Anmeldecodes.', close: 'Schließen',
        ok: 'Alles klar. Wir schreiben Ihnen in Kürze, in der Regel innerhalb einer Stunde. Prüfen Sie Ihren Posteingang und den Spam-Ordner.',
        hi: 'Hallo Unbanz', f: ['Mein Problem', 'Mein Benutzername oder Profillink', 'Was in der Meldung steht', 'Habe ich schon Einspruch eingelegt', 'Land'], bye: 'Danke',
        back: 'Zurück', change: 'Ändern', gIg: 'Instagram', gFb: 'Facebook', gAds: 'Werbung & Business', gOther: 'Andere Plattformen', step: 'Schritt %s von 2',
        hear: ['Wie haben Sie von uns erfahren?', 'Überspringen', 'ChatGPT oder ein anderer KI-Assistent', 'Google oder eine andere Suchmaschine', 'Eine Person, die ich kenne', 'Instagram, Facebook oder eine andere App', 'Anderswo'],
        t: [
          ['ig_disabled', 'Instagram deaktiviert / gesperrt', 'Instagram deaktiviert - Hilfe', 'Instagram-Konto deaktiviert', 'Instagram'],
          ['ig_hacked', 'Instagram gehackt', 'Instagram gehackt - Hilfe', 'Instagram-Konto gehackt', 'Instagram'],
          ['fb', 'Facebook deaktiviert / gehackt', 'Facebook-Konto - Hilfe', 'Facebook-Konto deaktiviert oder gehackt', 'Facebook'],
          ['ad', 'Werbekonto eingeschränkt', 'Werbekonto eingeschränkt - Hilfe', 'Werbekonto eingeschränkt oder deaktiviert', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - Hilfe', 'Business Portfolio / Business Manager eingeschränkt', 'Facebook'],
          ['username', 'Benutzername', 'Benutzername - Hilfe', 'Benutzernamen beanspruchen', 'Instagram'],
          ['snap', 'Snapchat', 'Snapchat-Konto - Hilfe', 'Snapchat-Konto gesperrt oder gebannt', 'Snapchat'],
          ['page', 'Facebook-Seite', 'Facebook-Seite - Hilfe', 'Facebook-Seite deaktiviert oder eingeschränkt', 'Facebook'],
          ['tiktok', 'TikTok', 'TikTok-Konto - Hilfe', 'TikTok-Konto gebannt oder gesperrt', 'TikTok'],
          ['youtube', 'YouTube-Kanal', 'YouTube-Kanal - Hilfe', 'YouTube-Kanal gekündigt oder gehackt', 'YouTube'],
          ['whatsapp', 'WhatsApp-Nummer', 'WhatsApp-Nummer - Hilfe', 'WhatsApp-Nummer gesperrt', 'WhatsApp'],
          ['other', 'Sonstiges', 'Hilfe mit einem Konto', 'Sonstiges', '']
        ]
      },
      it: {
        eyebrow: 'SCRIVICI', title: 'Con cosa ti serve aiuto?',
        hint: 'Scegli un’opzione: la tua email si apre con un breve modello da compilare.',
        user: 'Il tuo nome utente o link del profilo', opt: '(facoltativo)', ph: '@nomeutente o link',
        go: 'Scrivi l’email', note: 'Non inviare mai password o codici di accesso.', close: 'Chiudi',
        ok: 'Ricevuto. Ti scriveremo a breve, di solito entro un’ora. Controlla la posta in arrivo e lo spam.',
        hi: 'Ciao Unbanz', f: ['Il mio problema', 'Il mio nome utente o link del profilo', 'Cosa dice l’avviso', 'Ho già fatto ricorso?', 'Paese'], bye: 'Grazie',
        back: 'Indietro', change: 'Cambia', gIg: 'Instagram', gFb: 'Facebook', gAds: 'Annunci e Business', gOther: 'Altre piattaforme', step: 'Passo %s di 2',
        hear: ['Come ci hai conosciuto?', 'Salta', 'ChatGPT o un altro assistente IA', 'Google o un altro motore di ricerca', 'Una persona che conosco', 'Instagram, Facebook o un’altra app', 'Altrove'],
        t: [
          ['ig_disabled', 'Instagram disattivato / sospeso', 'Instagram disattivato - aiuto', 'Account Instagram disattivato', 'Instagram'],
          ['ig_hacked', 'Instagram hackerato', 'Instagram hackerato - aiuto', 'Account Instagram hackerato', 'Instagram'],
          ['fb', 'Facebook disattivato / hackerato', 'Account Facebook - aiuto', 'Account Facebook disattivato o hackerato', 'Facebook'],
          ['ad', 'Account pubblicitario limitato', 'Account pubblicitario limitato - aiuto', 'Account pubblicitario limitato o disattivato', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - aiuto', 'Business Portfolio / Business Manager limitato', 'Facebook'],
          ['username', 'Nome utente', 'Nome utente - aiuto', 'Rivendicare un nome utente', 'Instagram'],
          ['snap', 'Snapchat', 'Account Snapchat - aiuto', 'Account Snapchat bloccato o bannato', 'Snapchat'],
          ['page', 'Pagina Facebook', 'Pagina Facebook - aiuto', 'Pagina Facebook disattivata o limitata', 'Facebook'],
          ['tiktok', 'TikTok', 'Account TikTok - aiuto', 'Account TikTok bannato o sospeso', 'TikTok'],
          ['youtube', 'Canale YouTube', 'Canale YouTube - aiuto', 'Canale YouTube chiuso o hackerato', 'YouTube'],
          ['whatsapp', 'Numero WhatsApp', 'Numero WhatsApp - aiuto', 'Numero WhatsApp bannato', 'WhatsApp'],
          ['other', 'Altro', 'Aiuto per un account', 'Altro', '']
        ]
      },
      tr: {
        eyebrow: 'E-POSTA', title: 'Hangi konuda yardıma ihtiyacınız var?',
        hint: 'Birini seçin; e-postanız doldurmaya hazır kısa bir şablonla açılır.',
        user: 'Kullanıcı adınız veya profil bağlantınız', opt: '(isteğe bağlı)', ph: '@kullaniciadi veya bağlantı',
        go: 'E-postayı yaz', note: 'Şifrenizi veya giriş kodlarınızı asla göndermeyin.', close: 'Kapat',
        ok: 'Anladık. Kısa süre içinde, genellikle bir saat içinde e-posta göndereceğiz. Gelen kutunuzu ve spam klasörünüzü kontrol edin.',
        hi: 'Merhaba Unbanz', f: ['Sorunum', 'Kullanıcı adım veya profil bağlantım', 'Bildirimde ne yazıyor', 'Daha önce itiraz ettim mi', 'Ülke'], bye: 'Teşekkürler',
        back: 'Geri', change: 'Değiştir', gIg: 'Instagram', gFb: 'Facebook', gAds: 'Reklam ve Business', gOther: 'Diğer platformlar', step: 'Adım %s / 2',
        hear: ['Bizi nereden duydunuz?', 'Atla', 'ChatGPT veya başka bir yapay zekâ asistanı', 'Google veya başka bir arama motoru', 'Tanıdığım biri', 'Instagram, Facebook veya başka bir uygulama', 'Başka bir yer'],
        t: [
          ['ig_disabled', 'Instagram devre dışı / askıya alındı', 'Instagram devre dışı - yardım', 'Instagram hesabı devre dışı', 'Instagram'],
          ['ig_hacked', 'Instagram hacklendi', 'Instagram hacklendi - yardım', 'Instagram hesabı hacklendi', 'Instagram'],
          ['fb', 'Facebook devre dışı / hacklendi', 'Facebook hesabı - yardım', 'Facebook hesabı devre dışı veya hacklendi', 'Facebook'],
          ['ad', 'Reklam hesabı kısıtlandı', 'Reklam hesabı kısıtlandı - yardım', 'Reklam hesabı kısıtlandı veya devre dışı', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - yardım', 'Business Portfolio / Business Manager kısıtlandı', 'Facebook'],
          ['username', 'Kullanıcı adı', 'Kullanıcı adı - yardım', 'Kullanıcı adı talebi', 'Instagram'],
          ['snap', 'Snapchat', 'Snapchat hesabı - yardım', 'Snapchat hesabı kilitlendi veya yasaklandı', 'Snapchat'],
          ['page', 'Facebook Sayfası', 'Facebook Sayfası - yardım', 'Facebook Sayfası devre dışı veya kısıtlandı', 'Facebook'],
          ['tiktok', 'TikTok', 'TikTok hesabı - yardım', 'TikTok hesabı yasaklandı veya askıya alındı', 'TikTok'],
          ['youtube', 'YouTube kanalı', 'YouTube kanalı - yardım', 'YouTube kanalı kapatıldı veya hacklendi', 'YouTube'],
          ['whatsapp', 'WhatsApp numarası', 'WhatsApp numarası - yardım', 'WhatsApp numarası yasaklandı', 'WhatsApp'],
          ['other', 'Diğer', 'Hesap yardımı', 'Diğer', '']
        ]
      },
      ar: {
        eyebrow: 'راسلنا', title: 'بماذا تحتاج المساعدة؟',
        hint: 'اختر خيارًا وسيفتح بريدك الإلكتروني مع نموذج قصير جاهز للتعبئة.',
        user: 'اسم المستخدم أو رابط الملف الشخصي', opt: '(اختياري)', ph: '@اسم المستخدم أو رابط',
        go: 'اكتب البريد', note: 'لا ترسل كلمات المرور أو رموز الدخول أبدًا.', close: 'إغلاق',
        ok: 'تم. سنراسلك قريبًا، عادةً خلال ساعة. تحقق من صندوق الوارد والرسائل غير المرغوب فيها.',
        hi: 'مرحبًا Unbanz', f: ['مشكلتي', 'اسم المستخدم أو رابط الملف الشخصي', 'ما يقوله الإشعار', 'هل قدّمت طعنًا من قبل', 'البلد'], bye: 'شكرًا',
        back: 'رجوع', change: 'تغيير', gIg: 'إنستغرام', gFb: 'فيسبوك', gAds: 'الإعلانات والأعمال', gOther: 'منصات أخرى', step: 'الخطوة %s من 2',
        hear: ['كيف عرفت عنا؟', 'تخطي', 'ChatGPT أو مساعد ذكاء اصطناعي آخر', 'Google أو محرك بحث آخر', 'شخص أعرفه', 'إنستغرام أو فيسبوك أو تطبيق آخر', 'مكان آخر'],
        t: [
          ['ig_disabled', 'إنستغرام معطّل / موقوف', 'إنستغرام معطّل - مساعدة', 'حساب إنستغرام معطّل', 'Instagram'],
          ['ig_hacked', 'إنستغرام مخترق', 'إنستغرام مخترق - مساعدة', 'حساب إنستغرام مخترق', 'Instagram'],
          ['fb', 'فيسبوك معطّل / مخترق', 'حساب فيسبوك - مساعدة', 'حساب فيسبوك معطّل أو مخترق', 'Facebook'],
          ['ad', 'حساب إعلانات مقيّد', 'حساب إعلانات مقيّد - مساعدة', 'حساب إعلانات مقيّد أو معطّل', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - مساعدة', 'Business Portfolio / Business Manager مقيّد', 'Facebook'],
          ['username', 'اسم المستخدم', 'اسم المستخدم - مساعدة', 'المطالبة باسم مستخدم', 'Instagram'],
          ['snap', 'سناب شات', 'حساب سناب شات - مساعدة', 'حساب سناب شات مقفل أو محظور', 'Snapchat'],
          ['page', 'صفحة فيسبوك', 'صفحة فيسبوك - مساعدة', 'صفحة فيسبوك معطّلة أو مقيّدة', 'Facebook'],
          ['tiktok', 'تيك توك', 'حساب تيك توك - مساعدة', 'حساب تيك توك محظور أو موقوف', 'TikTok'],
          ['youtube', 'قناة يوتيوب', 'قناة يوتيوب - مساعدة', 'قناة يوتيوب مُنهاة أو مخترقة', 'YouTube'],
          ['whatsapp', 'رقم واتساب', 'رقم واتساب - مساعدة', 'رقم واتساب محظور', 'WhatsApp'],
          ['other', 'أخرى', 'مساعدة في حساب', 'أخرى', '']
        ]
      },
      zh: {
        eyebrow: '電郵聯絡', title: '您需要哪方面的協助？',
        hint: '選擇一項，您的電子郵件會開啟並附上可直接填寫的簡短範本。',
        user: '您的使用者名稱或個人檔案連結', opt: '（選填）', ph: '@使用者名稱或連結',
        go: '撰寫電子郵件', note: '請勿傳送密碼或登入驗證碼。', close: '關閉',
        ok: '收到了。我們會盡快回信，通常在一小時內。請查看收件箱和垃圾郵件。',
        hi: '您好 Unbanz', f: ['我的問題', '我的使用者名稱或個人檔案連結', '通知內容', '我是否已提出申訴', '國家／地區'], bye: '謝謝',
        back: '返回', change: '更改', gIg: 'Instagram', gFb: 'Facebook', gAds: '廣告與企業', gOther: '其他平台', step: '第 %s 步，共 2 步',
        hear: ['您是如何得知我們的？', '略過', 'ChatGPT 或其他 AI 助理', 'Google 或其他搜尋引擎', '我認識的人', 'Instagram、Facebook 或其他應用程式', '其他地方'],
        t: [
          ['ig_disabled', 'Instagram 遭停用／停權', 'Instagram 遭停用 - 協助', 'Instagram 帳號遭停用', 'Instagram'],
          ['ig_hacked', 'Instagram 遭盜用', 'Instagram 遭盜用 - 協助', 'Instagram 帳號遭盜用', 'Instagram'],
          ['fb', 'Facebook 遭停用／盜用', 'Facebook 帳號 - 協助', 'Facebook 帳號遭停用或盜用', 'Facebook'],
          ['ad', '廣告帳號受限', '廣告帳號受限 - 協助', '廣告帳號受限或遭停用', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - 協助', 'Business Portfolio / Business Manager 受限', 'Facebook'],
          ['username', '使用者名稱', '使用者名稱 - 協助', '申請使用者名稱', 'Instagram'],
          ['snap', 'Snapchat', 'Snapchat 帳號 - 協助', 'Snapchat 帳號遭鎖定或封禁', 'Snapchat'],
          ['page', 'Facebook 粉絲專頁', 'Facebook 粉絲專頁 - 協助', 'Facebook 粉絲專頁遭停用或受限', 'Facebook'],
          ['tiktok', 'TikTok', 'TikTok 帳號 - 協助', 'TikTok 帳號遭封禁或停權', 'TikTok'],
          ['youtube', 'YouTube 頻道', 'YouTube 頻道 - 協助', 'YouTube 頻道遭終止或盜用', 'YouTube'],
          ['whatsapp', 'WhatsApp 號碼', 'WhatsApp 號碼 - 協助', 'WhatsApp 號碼遭封禁', 'WhatsApp'],
          ['other', '其他', '帳號協助', '其他', '']
        ]
      }
    };
    var L = LANGS[lang];
    if (!L) return;
    var MAIL = 'team@unbanz.com';
    var HEAR_VALUES = ['', 'ChatGPT or another AI assistant', 'Google or another search engine', 'A person I know', 'Instagram, Facebook or another app', 'Somewhere else'];
    var GROUPS = [['gIg', ['ig_disabled', 'ig_hacked', 'username']], ['gFb', ['fb', 'page']], ['gAds', ['ad', 'bm']], ['gOther', ['tiktok', 'snap', 'youtube', 'whatsapp', 'other']]];
    var S = function (d) { return '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + d + '</svg>'; };
    var ICON = {
      ig_disabled: S('<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="3.8"/><circle cx="17.2" cy="6.8" r=".6" fill="currentColor"/>'),
      ig_hacked: S('<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 7.6-1.7"/><path d="M12 14.5v2.5"/>'),
      username: S('<circle cx="12" cy="12" r="3.6"/><path d="M15.6 12v1.4a2.6 2.6 0 0 0 5.2 0V12a8.8 8.8 0 1 0-3.5 7"/>'),
      fb: S('<path d="M14.5 21v-7.5h2.6l.4-3.1h-3V8.6c0-.9.3-1.5 1.6-1.5h1.6V4.4a21 21 0 0 0-2.4-.1c-2.4 0-4 1.4-4 4.1v2h-2.6v3.1h2.6V21"/>'),
      page: S('<path d="M5 21V4"/><path d="M5 4.5h11.5l-2 4 2 4H5"/>'),
      ad: S('<path d="M4 10.5v3a1.5 1.5 0 0 0 1.5 1.5H7l9 4.5V4.5L7 9H5.5A1.5 1.5 0 0 0 4 10.5Z"/><path d="M8.5 15.2 10 20"/><path d="M19 9.5a3.5 3.5 0 0 1 0 5"/>'),
      bm: S('<rect x="3.5" y="7.5" width="17" height="12" rx="2.5"/><path d="M9 7.5V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1.5"/><path d="M3.5 12.5h17"/>'),
      tiktok: S('<path d="M13.5 3.5v11.2a3.3 3.3 0 1 1-3.3-3.3"/><path d="M13.5 3.5c.4 2.6 2.2 4.4 4.8 4.6"/>'),
      snap: S('<path d="M12 3.6c2.9 0 4.6 2.1 4.6 4.8v2.2l1.9-.5c.5 0 .7.6.3.9l-2 1.2c.6 1.7 1.9 3 3.6 3.5-.3.8-1.4 1-2.4 1.2l-.4 1.3-1.6-.2c-1 0-1.8 1.4-4 1.4s-3-1.4-4-1.4l-1.6.2-.4-1.3c-1-.2-2.1-.4-2.4-1.2 1.7-.5 3-1.8 3.6-3.5l-2-1.2c-.4-.3-.2-.9.3-.9l1.9.5V8.4c0-2.7 1.7-4.8 4.6-4.8Z"/>'),
      youtube: S('<rect x="2.8" y="5.5" width="18.4" height="13" rx="4"/><path d="m10.2 9.2 4.8 2.8-4.8 2.8Z" fill="currentColor"/>'),
      whatsapp: S('<path d="M4.2 19.8 5.4 16A8 8 0 1 1 8.4 18.8Z"/><path d="M9.3 8.6c.2-.4.6-.5.9-.4l.6 1.5c.1.3 0 .5-.2.7l-.4.5c.5 1 1.3 1.8 2.3 2.3l.5-.4c.2-.2.5-.3.7-.2l1.5.6c.2.3 0 .8-.4 1-1 .7-2.6.3-4.3-1.3-1.6-1.6-2.1-3.3-1.2-4.3Z"/>'),
      other: S('<circle cx="12" cy="12" r="8.5"/><path d="M9.7 9.6a2.4 2.4 0 1 1 3.3 2.2c-.6.3-1 .8-1 1.5v.4"/><circle cx="12" cy="16.6" r=".5" fill="currentColor"/>')
    };
    var CHECK = '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>';
    var CHEV = '<svg class="mp-chev" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m9 6 6 6-6 6"/></svg>';
    var BACK = '<svg class="mp-flip" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m15 6-6 6 6 6"/></svg>';
    var X = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg>';
    var CSS = ".mp3.cm-backdrop{align-items:center;justify-content:center;padding:24px;background:rgba(25,62,105,.32);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);transition:opacity .28s ease}.mp3 .mp-sheet.cm-dialog{display:flex;flex-direction:column;width:min(680px,100%);max-width:680px;max-height:min(760px,calc(100vh - 48px));max-height:min(760px,calc(100dvh - 48px));padding:0;overflow:hidden;border-radius:28px;background:var(--paper,#f7fafc);color:var(--ink,#25415d);box-shadow:0 30px 80px -20px rgba(25,62,105,.45),0 0 0 1px rgba(25,62,105,.06);transform:translate3d(0,14px,0) scale(.975);opacity:0;transition:transform .42s cubic-bezier(.2,.9,.25,1),opacity .28s ease;outline:none}.mp3.cm-backdrop.is-open .mp-sheet.cm-dialog{transform:none;opacity:1}.mp3 .mp-sheet.mp-morph{transition:height .32s cubic-bezier(.2,.9,.25,1),transform .42s cubic-bezier(.2,.9,.25,1)}.mp3 .mp-sheet.mp-dragging{transition:none}.mp3 .mp-drag{flex:none;padding:10px 12px 0;touch-action:none;-webkit-user-select:none;user-select:none}.mp3 .mp-grab{display:none;width:40px;height:5px;margin:0 auto 4px;border-radius:99px;background:#c9d9e6}.mp3 .mp-bar{display:grid;grid-template-columns:44px 1fr 44px;align-items:center}.mp3 .mp-back,.mp3 .mp-x.cm-close{position:static;display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;margin:0;padding:0;border:0;border-radius:50%;background:transparent;color:var(--ink,#25415d);cursor:pointer;transition:background-color .15s ease,transform .12s ease}.mp3 .mp-x.cm-close{background:#e5eff6}.mp3 .mp-back:hover,.mp3 .mp-x.cm-close:hover{background:#dcecf7}.mp3 .mp-back:active,.mp3 .mp-x.cm-close:active{transform:scale(.92)}.mp3 .mp-sheet[data-step=\"1\"] .mp-back{visibility:hidden}.mp3 .mp-prog{display:flex;justify-content:center;gap:6px}.mp3 .mp-prog i{display:block;width:18px;height:5px;border-radius:99px;background:#d6e5f0;transition:width .3s cubic-bezier(.2,.9,.25,1),background-color .3s ease}.mp3 .mp-prog i.on{width:30px;background:var(--blue,#2d719f)}.mp3 .mp-body{flex:1 1 auto;min-height:0;overflow-y:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch}.mp3 .mp-step{padding:2px 24px 18px}.mp3 .mp-step[hidden]{display:none}.mp3 .mp-in{animation:mp3in .32s cubic-bezier(.2,.9,.25,1) both}@keyframes mp3in{from{opacity:0;transform:translate3d(var(--mp-dx,24px),0,0)}to{opacity:1;transform:none}}[dir=\"rtl\"] .mp3 .mp-in{animation-name:mp3inr}@keyframes mp3inr{from{opacity:0;transform:translate3d(calc(var(--mp-dx,24px) * -1),0,0)}to{opacity:1;transform:none}}[dir=\"rtl\"] .mp3 .mp-flip,[dir=\"rtl\"] .mp3 .mp-chev{transform:scaleX(-1)}.mp3 .mp-eye.cm-eyebrow{margin:4px 0 6px;font-size:12px;letter-spacing:.08em;color:var(--muted,#5b7690)}.mp3 .mp-step h2{margin:0 0 6px;font-size:30px;font-weight:400;line-height:1.12;letter-spacing:-.01em;color:var(--ink,#25415d)}.mp3 .mp-hint.cm-hint{margin:0 0 6px;font-size:14px;line-height:1.5;color:var(--muted,#5b7690)}.mp3 .mp-gl{margin:16px 0 8px;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--muted,#5b7690)}.mp3 .mp-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.mp3 .mp-card.cm-pill{position:relative;display:flex;align-items:center;gap:10px;width:100%;min-height:58px;margin:0;padding:9px 30px 9px 10px;border:1px solid #dbe7f0;border-radius:16px;background:#fff;color:var(--ink,#25415d);font:inherit;font-size:14px;font-weight:500;line-height:1.25;text-align:start;cursor:pointer;box-shadow:0 1px 2px rgba(25,62,105,.05);-webkit-tap-highlight-color:transparent;transition:transform .14s cubic-bezier(.2,.9,.25,1),border-color .18s ease,background-color .18s ease,box-shadow .18s ease}[dir=\"rtl\"] .mp3 .mp-card.cm-pill{padding:9px 10px 9px 30px}.mp3 .mp-card.cm-pill:hover{border-color:#b9d3e6;background:#fff;box-shadow:0 4px 14px -6px rgba(25,62,105,.25)}.mp3 .mp-card.cm-pill:active{transform:scale(.97)}.mp3 .mp-card.cm-pill:focus-visible,.mp3 .mp-sel:focus-visible,.mp3 .mp-back:focus-visible,.mp3 .mp-x:focus-visible,.mp3 .mp-go:focus-visible{outline:3px solid #6db4ed;outline-offset:2px}.mp3 .mp-card.cm-pill[aria-pressed=\"true\"]{border-color:var(--blue,#2d719f);background:#f1f7fb;box-shadow:inset 0 0 0 1px var(--blue,#2d719f);color:var(--ink,#25415d)}.mp3 .mp-ic{display:inline-flex;flex:none;align-items:center;justify-content:center;width:38px;height:38px;border-radius:12px;background:#e7f1f8;color:var(--blue,#2d719f);transition:background-color .18s ease,color .18s ease}.mp3 .mp-card[aria-pressed=\"true\"] .mp-ic{background:var(--blue,#2d719f);color:#fff}.mp3 .mp-tx{min-width:0;overflow-wrap:anywhere}.mp3 .mp-ck{position:absolute;top:8px;inset-inline-end:8px;display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:var(--blue,#2d719f);color:#fff;transform:scale(0);opacity:0;transition:transform .26s cubic-bezier(.3,1.6,.5,1),opacity .15s ease}.mp3 .mp-card[aria-pressed=\"true\"] .mp-ck{transform:scale(1);opacity:1}.mp3 .mp-sel{display:flex;align-items:center;gap:12px;width:100%;min-height:66px;margin:6px 0 4px;padding:12px 14px;border:1px solid #dbe7f0;border-radius:18px;background:#fff;color:var(--ink,#25415d);font:inherit;text-align:start;cursor:pointer;transition:border-color .18s ease,transform .14s ease}.mp3 .mp-sel:hover{border-color:#b9d3e6}.mp3 .mp-sel:active{transform:scale(.985)}.mp3 .mp-sel .mp-ic{background:var(--blue,#2d719f);color:#fff}.mp3 .mp-sel-txw{display:flex;flex:1;min-width:0;flex-direction:column;gap:2px}.mp3 .mp-sel-tx{font-size:16px;font-weight:600;line-height:1.3}.mp3 .mp-sel-c{font-size:13px;color:var(--blue,#2d719f)}.mp3 .mp-chev{flex:none;color:var(--muted,#5b7690)}.mp3 .mp-label{display:block;margin:18px 0 8px;font-size:14px;font-weight:500;color:var(--ink,#25415d)}.mp3 .mp-label span{font-weight:400;color:var(--muted,#5b7690)}.mp3 .mp-input{display:block;box-sizing:border-box;width:100%;height:52px;margin:0;padding:0 16px;border:1px solid #cfdfeb;border-radius:14px;background:#fff;color:var(--ink,#25415d);font:inherit;font-size:16px;transition:border-color .15s ease,box-shadow .15s ease;-webkit-appearance:none;appearance:none}.mp3 .mp-input::placeholder{color:#8aa2b6}.mp3 .mp-input:focus{outline:none;border-color:var(--blue,#2d719f);box-shadow:0 0 0 4px rgba(45,113,159,.16)}.mp3 .mp-selwrap{position:relative}.mp3 .mp-selwrap:after{content:\"\";position:absolute;top:50%;inset-inline-end:16px;width:8px;height:8px;margin-top:-6px;border-right:2px solid #5b7690;border-bottom:2px solid #5b7690;transform:rotate(45deg);pointer-events:none}.mp3 .mp-select{padding-inline-end:42px;cursor:pointer}.mp3 .mp-foot{flex:none;padding:12px 24px 14px;padding-bottom:calc(14px + env(safe-area-inset-bottom,0px));border-top:1px solid #e3edf4;background:var(--paper,#f7fafc)}.mp3 .mp-sheet[data-step=\"1\"] .mp-act{display:none}.mp3 .mp-sheet[data-step=\"1\"] .mp-foot{padding-top:10px}.mp3 .mp-act.cm-actions{position:static;display:block;margin:0;padding:0;background:none}.mp3 .mp-go.button{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;min-height:54px;margin:0;padding:0 22px;border-radius:999px;font-size:16px;font-weight:600;opacity:1;box-shadow:0 10px 24px -10px rgba(45,113,159,.75);transition:transform .14s cubic-bezier(.2,.9,.25,1),filter .15s ease,box-shadow .15s ease}.mp3 .mp-go.button:hover{filter:brightness(1.07)}.mp3 .mp-go.button:active{transform:scale(.98)}.mp3 .mp-note.cm-note{margin:10px 0 0;font-size:12px;line-height:1.4;text-align:center;color:var(--muted,#5b7690)}.mp3 .mp-sheet[data-step=\"1\"] .mp-note.cm-note{margin:0}@media (max-width:640px){.mp3.cm-backdrop{align-items:flex-end;padding:0}.mp3 .mp-sheet.cm-dialog{width:100%;max-width:none;max-height:calc(100vh - 12px);max-height:calc(100dvh - 12px);border-radius:26px 26px 0 0;transform:translate3d(0,100%,0);opacity:1;transition:transform .5s cubic-bezier(.32,.72,0,1)}.mp3 .mp-sheet.mp-morph{transition:height .32s cubic-bezier(.2,.9,.25,1),transform .5s cubic-bezier(.32,.72,0,1)}.mp3 .mp-grab{display:block}.mp3 .mp-drag{padding:8px 10px 0;cursor:grab}.mp3 .mp-step{padding:0 18px 16px}.mp3 .mp-step h2{font-size:25px}.mp3 .mp-gl{margin:14px 0 7px}.mp3 .mp-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:7px}.mp3 .mp-eye.cm-eyebrow{display:none}.mp3 .mp-step h2{margin-top:2px}.mp3 .mp-hint.cm-hint{font-size:13.5px;line-height:1.45}.mp3 .mp-gl{margin:12px 0 6px;font-size:11.5px}.mp3 .mp-card.cm-pill{min-height:52px;gap:9px;padding:7px 26px 7px 8px;font-size:13px;line-height:1.2;border-radius:15px}[dir=\"rtl\"] .mp3 .mp-card.cm-pill{padding:7px 8px 7px 26px}.mp3 .mp-ic{width:32px;height:32px;border-radius:10px}.mp3 .mp-ic svg{width:19px;height:19px}.mp3 .mp-ck{top:6px;inset-inline-end:6px}.mp3 .mp-foot{padding:10px 18px 12px;padding-bottom:calc(12px + env(safe-area-inset-bottom,0px))}}@media (max-width:340px){.mp3 .mp-grid{grid-template-columns:1fr}}@media (prefers-reduced-motion:reduce){.mp3.cm-backdrop,.mp3 .mp-sheet.cm-dialog,.mp3 .mp-card.cm-pill,.mp3 .mp-ck,.mp3 .mp-prog i,.mp3 .mp-go.button,.mp3 .mp-sel,.mp3 .mp-back,.mp3 .mp-x{transition:none!important}.mp3 .mp-in{animation:none}.mp3 .mp-card.cm-pill:active,.mp3 .mp-go.button:active{transform:none}}.mp3 .mp-sheet[data-step=\"ok\"] .mp-back,.mp3 .mp-sheet[data-step=\"ok\"] .mp-prog,.mp3 .mp-sheet[data-step=\"ok\"] .mp-act{display:none}.mp3 .mp-sheet[data-step=\"ok\"] .mp-note.cm-note{display:none}.mp3 .mp-done{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:36px 28px 48px;text-align:center}.mp3 .mp-done[hidden]{display:none}.mp3 .mp-ok-ic{display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;margin:0 0 18px;border-radius:50%;background:var(--blue,#2d719f);color:#fff}.mp3 .mp-ok-ic svg{width:28px;height:28px}.mp3 .mp-done h2{margin:0;font-size:22px;font-weight:400;line-height:1.45;letter-spacing:-.01em;color:var(--ink,#25415d);max-width:26em;outline:none}@media (max-width:640px){.mp3 .mp-done{padding:24px 18px 36px}.mp3 .mp-done h2{font-size:19px;line-height:1.4}}";
    var modal, sheet, lastFocus, topic = null, input, hear, go, step = 1, busy = false, scrollY = 0, sending = false;
    var LS_KEY = 'unbanz_lead_submit_v1';
    var WINDOW_MS = 6 * 60 * 60 * 1000;
    var normUser = function (u) {
      u = String(u || '').trim().toLowerCase();
      u = u.replace(/^@+/, '');
      u = u.replace(/^https?:\/\/(www\.)?(instagram\.com|instagr\.am)\//, '').replace(/[\/?#].*$/, '');
      return u.slice(0, 120);
    };
    var normEmail = function (e) {
      return String(e || '').trim().toLowerCase();
    };
    var readStore = function () {
      try {
        var s = JSON.parse(localStorage.getItem(LS_KEY) || 'null');
        if (s && typeof s === 'object') return s;
      } catch (err) {}
      return { at: 0, emails: {}, users: {} };
    };
    var isRecent = function (email, user) {
      var now = Date.now(), s = readStore();
      if (s.at && (now - s.at) < WINDOW_MS) return true;
      var em = normEmail(email), us = normUser(user);
      if (em && s.emails && s.emails[em] && (now - s.emails[em]) < WINDOW_MS) return true;
      if (us && s.users && s.users[us] && (now - s.users[us]) < WINDOW_MS) return true;
      return false;
    };
    var record = function (email, user) {
      var now = Date.now(), s = readStore();
      s.at = now;
      s.emails = s.emails || {};
      s.users = s.users || {};
      var em = normEmail(email), us = normUser(user);
      if (em) s.emails[em] = now;
      if (us) s.users[us] = now;
      try { localStorage.setItem(LS_KEY, JSON.stringify(s)); } catch (err) {}
    };
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
    var find = function (k) { for (var i = 0; i < L.t.length; i++) if (L.t[i][0] === k) return L.t[i]; return null; };
    var infer = function () {
      var s = location.pathname.toLowerCase();
      if (/snapchat/.test(s)) return 'snap';
      if (/tiktok/.test(s)) return 'tiktok';
      if (/youtube/.test(s)) return 'youtube';
      if (/whatsapp/.test(s)) return 'whatsapp';
      if (/username|gebruikersnaam|pseudo|one-letter|\/og-/.test(s)) return 'username';
      if (/business-portfolio|business-manager|business-suite/.test(s)) return 'bm';
      if (/ad-account|ads-|meta-ad|advertentie|publicit|pixel/.test(s)) return 'ad';
      if (/instagram/.test(s)) return /hack|pirat|gehackt/.test(s) ? 'ig_hacked' : 'ig_disabled';
      if (/facebook/.test(s)) return /facebook-page|page-recovery|-page-|pagina-facebook|page-facebook|facebookpagina/.test(s) ? 'page' : 'fb';
      return null;
    };
    var href = function () {
      var t = find(topic) || find('other'), u = (input.value || '').replace(/[\r\n]+/g, ' ').trim().slice(0, 120);
      var body = L.hi + '\n\n' + L.f[0] + ': ' + t[3] + '\n' + L.f[1] + ': ' + u + '\n' + L.f[2] + ': \n' + L.f[3] + ': \n' + L.f[4] + ': \n\n' + L.bye;
      if (hear && hear.value) body += '\nHow I heard about Unbanz: ' + hear.value;
      return 'mailto:' + MAIL + '?subject=' + encodeURIComponent(t[2]) + '&body=' + encodeURIComponent(body);
    };
    var update = function () {
      var t = find(topic);
      go.href = href();
      go.setAttribute('aria-disabled', String(!t));
      go.classList.toggle('mp-off', !t);
      go.dataset.service = t ? t[0] : '';
      if (t && t[4]) go.dataset.platform = t[4]; else delete go.dataset.platform;
      modal.querySelectorAll('.cm-pill').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.value === topic)); });
      if (t) {
        modal.querySelector('.mp-sel-ic').innerHTML = ICON[t[0]] || '';
        modal.querySelector('.mp-sel-tx').textContent = t[1];
      }
    };
    var card = function (k) {
      var t = find(k); if (!t) return '';
      return '<button type="button" class="cm-pill mp-card" data-group="service" data-value="' + t[0] + '" aria-pressed="false">' +
        '<span class="mp-ic">' + (ICON[k] || '') + '</span><span class="mp-tx">' + esc(t[1]) + '</span><span class="mp-ck">' + CHECK + '</span></button>';
    };
    var build = function () {
      var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
      var groups = GROUPS.map(function (g, i) {
        return '<div class="mp-group"><p class="mp-gl" id="mp-g' + i + '">' + esc(L[g[0]]) + '</p><div class="mp-grid" role="group" aria-labelledby="mp-g' + i + '">' + g[1].map(card).join('') + '</div></div>';
      }).join('');
      var opts = HEAR_VALUES.map(function (v, i) { return '<option value="' + esc(v) + '">' + esc(L.hear[i + 1]) + '</option>'; }).join('');
      modal = document.createElement('div');
      modal.className = 'cm-backdrop mp-backdrop mp3';
      modal.hidden = true;
      modal.innerHTML = '<div class="cm-dialog mp-dialog mp-sheet" role="dialog" aria-modal="true" aria-labelledby="mp-title" tabindex="-1" data-step="1">' +
        '<div class="mp-drag"><span class="mp-grab" aria-hidden="true"></span>' +
        '<div class="mp-bar"><button type="button" class="mp-back" aria-label="' + esc(L.back) + '">' + BACK + '</button>' +
        '<div class="mp-prog" role="img" aria-label="' + esc(L.step.replace('%s', '1')) + '"><i class="on"></i><i></i></div>' +
        '<button type="button" class="cm-close mp-x" aria-label="' + esc(L.close) + '">' + X + '</button></div></div>' +
        '<div class="mp-body"><div class="mp-steps">' +
        '<section class="mp-step mp-s1" aria-labelledby="mp-title"><p class="eyebrow cm-eyebrow mp-eye">' + esc(L.eyebrow) + '</p>' +
        '<h2 id="mp-title">' + esc(L.title) + '</h2><p class="cm-hint mp-hint">' + esc(L.hint) + '</p>' + groups + '</section>' +
        '<section class="mp-step mp-s2" aria-labelledby="mp-sel-l" hidden>' +
        '<button type="button" class="mp-sel" aria-describedby="mp-sel-c"><span class="mp-ic mp-sel-ic"></span><span class="mp-sel-txw"><span class="mp-sel-tx" id="mp-sel-l"></span>' +
        '<span class="mp-sel-c" id="mp-sel-c">' + esc(L.change) + '</span></span>' + CHEV + '</button>' +
        '<label class="mp-label" for="mp-user">' + esc(L.user) + ' <span>' + esc(L.opt) + '</span></label>' +
        '<input id="mp-user" class="mp-input" type="text" maxlength="120" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="send" dir="auto" placeholder="' + esc(L.ph) + '">' +
        '<label class="mp-label" for="ubz-hear-mail">' + esc(L.hear[0]) + ' <span>' + esc(L.opt) + '</span></label>' +
        '<div class="mp-selwrap"><select id="ubz-hear-mail" class="mp-input mp-select">' + opts + '</select></div>' +
        '</section>' +
        '<section class="mp-step mp-done" hidden>' +
        '<div class="mp-ok-ic" aria-hidden="true">' + CHECK + '</div>' +
        '<h2 id="mp-ok-title" tabindex="-1">' + esc(L.ok) + '</h2>' +
        '</section></div></div>' +
        '<div class="mp-foot"><div class="cm-actions mp-act"><a class="button button-blue mp-go" href="mailto:' + MAIL + '">' + esc(L.go) + ' <span aria-hidden="true">↗︎</span></a></div>' +
        '<p class="cm-note mp-note">' + esc(L.note) + '</p></div></div>';
      document.body.appendChild(modal);
      sheet = modal.querySelector('.mp-sheet');
      input = modal.querySelector('#mp-user');
      hear = modal.querySelector('#ubz-hear-mail');
      go = modal.querySelector('.mp-go');
      modal.addEventListener('click', function (e) {
        var pill = e.target.closest('.cm-pill');
        if (pill) { topic = pill.dataset.value; update(); setTimeout(function () { show(2); }, reduce ? 0 : 160); return; }
        if (e.target.closest('.mp-back') || e.target.closest('.mp-sel')) { show(1); return; }
        if (e.target === modal || e.target.closest('.cm-close')) close();
      });
      input.addEventListener('input', update);
      hear.addEventListener('change', update);
      input.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go.click(); } });
      go.addEventListener('click', function (e) {
        if (!find(topic)) { e.preventDefault(); e.stopImmediatePropagation(); show(1); return; }
        if (sending || isRecent(null, input.value)) {
          e.preventDefault();
          e.stopImmediatePropagation();
          showDone(true);
          return;
        }
        sending = true;
        update();
        record(null, input.value);
        showDone(false);
      }, true);
      modal.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { e.preventDefault(); close(); return; }
        if (e.key === 'Tab') {
          var f = Array.prototype.filter.call(modal.querySelectorAll('button, a[href], input, select'), function (el) { return el.offsetParent !== null && !el.closest('[hidden]'); });
          if (!f.length) return;
          var first = f[0], last = f[f.length - 1];
          if (e.shiftKey && (document.activeElement === first || document.activeElement === sheet)) { e.preventDefault(); last.focus(); }
          else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        }
      });
      drag();
    };
    // Switch steps with a height morph and a short slide. Hidden step gets [hidden] so it is out of tab order and AT.
    var show = function (n, instant) {
      if (busy && !instant) return;
      var from = modal.querySelector('.mp-s' + step), to = modal.querySelector('.mp-s' + n);
      var prog = modal.querySelector('.mp-prog');
      prog.children[1].classList.toggle('on', n === 2);
      prog.setAttribute('aria-label', L.step.replace('%s', String(n)));
      sheet.setAttribute('data-step', String(n));
      if (n === step || instant || reduce) {
        from.hidden = n !== step; to.hidden = false; step = n; after(n); return;
      }
      busy = true;
      var h0 = sheet.offsetHeight;
      var dir = n > step ? 1 : -1;
      from.hidden = true; to.hidden = false;
      var h1 = sheet.offsetHeight;
      to.style.setProperty('--mp-dx', (dir * 28) + 'px');
      to.classList.add('mp-in');
      sheet.style.height = h0 + 'px'; void sheet.offsetHeight;
      sheet.classList.add('mp-morph'); sheet.style.height = h1 + 'px';
      step = n;
      setTimeout(function () { sheet.classList.remove('mp-morph'); sheet.style.height = ''; to.classList.remove('mp-in'); busy = false; }, 340);
      after(n);
    };
    var after = function (n) {
      modal.querySelector('.mp-body').scrollTop = 0;
      if (n === 2) {
        setTimeout(function () { try { input.focus({ preventScroll: true }); } catch (e) { input.focus(); } }, reduce ? 0 : 260);
      } else {
        var b = modal.querySelector('.cm-pill[aria-pressed="true"]');
        if (b && document.activeElement && modal.contains(document.activeElement)) b.focus({ preventScroll: false });
      }
    };
    // Drag the handle/top bar down to dismiss (touch + mouse). Small drags spring back.
    var drag = function () {
      var area = modal.querySelector('.mp-drag'), y0 = null, t0 = 0, dy = 0;
      area.addEventListener('pointerdown', function (e) {
        if (e.target.closest('button') || !matchMedia('(max-width: 640px)').matches) return;
        e.preventDefault(); y0 = e.clientY; t0 = Date.now(); dy = 0; sheet.classList.add('mp-dragging');
        try { area.setPointerCapture(e.pointerId); } catch (x) {}
      });
      area.addEventListener('pointermove', function (e) {
        if (y0 === null) return;
        dy = Math.max(0, e.clientY - y0);
        sheet.style.transform = 'translate3d(0,' + dy + 'px,0)';
      });
      var end = function () {
        if (y0 === null) return;
        var v = dy / Math.max(1, Date.now() - t0);
        y0 = null; sheet.classList.remove('mp-dragging'); sheet.style.transform = '';
        if (dy > 110 || (dy > 30 && v > 0.6)) close();
      };
      area.addEventListener('pointerup', end); area.addEventListener('pointercancel', end);
    };
    var lock = function (on) {
      var de = document.documentElement, b = document.body;
      if (on) {
        scrollY = window.scrollY || 0;
        de.classList.add('cm-lock');
        b.style.position = 'fixed'; b.style.top = (-scrollY) + 'px'; b.style.left = '0'; b.style.right = '0'; b.style.width = '100%';
      } else {
        de.classList.remove('cm-lock');
        b.style.position = ''; b.style.top = ''; b.style.left = ''; b.style.right = ''; b.style.width = '';
        var se = de.style.scrollBehavior; de.style.scrollBehavior = 'auto'; window.scrollTo(0, scrollY); de.style.scrollBehavior = se;
      }
    };
    var stripGo = function () {
      go.removeAttribute('href');
    };
    var showDone = function (stripNow) {
      if (!modal) build();
      var s1 = modal.querySelector('.mp-s1'), s2 = modal.querySelector('.mp-s2'), ok = modal.querySelector('.mp-done');
      if (s1) s1.hidden = true;
      if (s2) s2.hidden = true;
      if (ok) ok.hidden = false;
      sheet.setAttribute('data-step', 'ok');
      sheet.setAttribute('aria-labelledby', 'mp-ok-title');
      go.setAttribute('aria-disabled', 'true');
      go.classList.add('mp-off');
      go.setAttribute('tabindex', '-1');
      modal.querySelector('.mp-body').scrollTop = 0;
      // Keep href during the first click so the mailto can open, then drop it so a
      // later click cannot send again.
      if (stripNow) stripGo();
      else setTimeout(stripGo, 0);
    };
    var clearDone = function () {
      var ok = modal.querySelector('.mp-done');
      if (ok) ok.hidden = true;
      sheet.setAttribute('aria-labelledby', 'mp-title');
      go.removeAttribute('tabindex');
      sending = false;
    };
    var open = function (preset) {
      if (!modal) build();
      if (!modal.hidden && modal.classList.contains('is-open')) return;
      lastFocus = document.activeElement;
      if (isRecent(null, (input && input.value) || '')) {
        showDone(true);
        modal.hidden = false;
        lock(true);
        void modal.offsetWidth; modal.classList.add('is-open');
        var okTitle = modal.querySelector('#mp-ok-title');
        if (okTitle) try { okTitle.focus({ preventScroll: true }); } catch (err) {}
        return;
      }
      clearDone();
      var pre = (preset && find(preset)) ? preset : null;
      topic = pre || infer();
      if (pre === 'other') pre = null; // a generic "Other" link still starts at the topic cards, with Other preselected
      input.value = ''; hear.value = '';
      update();
      step = pre ? 1 : 2; show(pre ? 2 : 1, true);
      modal.hidden = false;
      lock(true);
      void modal.offsetWidth; modal.classList.add('is-open');
      if (pre) setTimeout(function () { input.focus({ preventScroll: true }); }, reduce ? 0 : 320);
      else sheet.focus({ preventScroll: true });
    };
    var close = function () {
      if (!modal || modal.hidden) return;
      modal.classList.remove('is-open');
      lock(false);
      setTimeout(function () { modal.hidden = true; }, reduce ? 0 : 320);
      if (lastFocus && lastFocus.focus) try { lastFocus.focus({ preventScroll: true }); } catch (e) {}
    };
    document.addEventListener('click', function (e) {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
      if (!a || a.closest('.cm-dialog') || !/^mailto:team@unbanz\.com/i.test(a.getAttribute('href') || '')) return;
      e.preventDefault();
      open(a.getAttribute('data-topic'));
    });
    window.unbanzMailPick = { open: open, close: close };
  } catch (e) {}
})();
