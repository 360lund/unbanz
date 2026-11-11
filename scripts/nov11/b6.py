from b5 import P as _P, add, lr, HELP, CR, H, IGD, FBD, UR
from gen import ul, ol, a, ext
P=[]
import b5
b5.P.clear()
HELP['ar']=('musaada','تفضّل أن نتولّى الأمر؟','<p>تتولّى Unbanz حسابات إنستغرام مقابل 800 دولار وفيسبوك مقابل 900 دولار، تُدفع مقدّماً بالبطاقة مع استرداد 100% إذا فشلت الحالة. عادةً 3 إلى 7 أيام من بدء العمل، دون ضمان؛ القرار النهائي لميتا. Unbanz مستقلة عن ميتا ولا تطلب أبداً كلمات المرور أو الرموز. راسلنا على <a href="mailto:team@unbanz.com">team@unbanz.com</a>.</p>')
CR['ar']=(('الأدلة','/ar/'),'الرئيسية / الأدلة'); H['ar']=('الرابط','الغرض')
LK='facebook-and-instagram-disabled-together-linked-accounts'; AC='https://accountscenter.instagram.com/'; AS='https://help.instagram.com/338481628002750'
def linked(l,slug,title,short,desc,h1,lede,answer,cards,why,steps,lt,faqs,rel):
    add(l,LK,slug,'fb','Facebook + Instagram','900',title=title,short=short,desc=desc,h1=h1,lede=lede,answer=answer,cards=cards,
      sections=[('pourquoi' if l=='fr' else 'why',why[0],ul(why[1])),('steps',steps[0],ol(steps[1])),('links',lt,lr(l,[(lt.split(':')[0] if False else 'Instagram',IGD,'Meta'),('Facebook',FBD,'Meta'),('Accounts Center',AC,'Meta')]))],faqs=faqs,related=rel)
linked('fr','facebook-et-instagram-desactives-en-meme-temps','Facebook et Instagram désactivés en même temps : comptes liés (2026)','Facebook et Instagram désactivés ensemble',
 'Vos comptes Facebook et Instagram ont été désactivés le même jour ? Pourquoi une décision en entraîne d’autres via l’Espace comptes, et dans quel ordre faire appel.',
 'Facebook et Instagram désactivés ensemble.','Quand des comptes partagent l’Espace comptes, un téléphone, un e-mail ou un appareil, une décision peut toucher les autres. Mis à jour le 11 novembre 2026.',
 '<strong>Repérez le compte désactivé en premier et faites appel pour celui-là d’abord : les autres sont souvent désactivés parce qu’ils lui sont liés.</strong> Faites appel pour chaque compte depuis sa propre notification, précisez qu’ils appartiennent à la même personne et ne créez pas de nouveau compte. Meta prend la décision finale.',
 [('Le premier compte','Commencez par lui.'),('Chaque notification','Un appel par compte.'),('Pas de nouveau compte','Il serait lié aussi.')],
 ('Pourquoi tout tombe en même temps',['Comptes reliés dans l’Espace comptes.','Même numéro de téléphone ou e-mail.','Même appareil ou même réseau.','Un compte professionnel géré depuis un profil personnel sanctionné.']),
 ('Dans quel ordre',['Retrouvez la date de chaque notification.','Faites appel pour le compte le plus ancien en premier.','Puis pour chaque autre compte, depuis sa notification.','Mentionnez que tous les comptes vous appartiennent.']),'Liens officiels',
 [('Faut-il délier les comptes dans l’Espace comptes ?','Non, pas pendant un appel : cela ne lève pas la décision.')],[('/fr/liens-officiels-appel-meta-instagram-facebook/','Liens officiels d’appel Meta')])
linked('es','facebook-e-instagram-desactivados-a-la-vez','Facebook e Instagram desactivados a la vez: cuentas vinculadas (2026)','Facebook e Instagram desactivados a la vez',
 '¿Tus cuentas de Facebook e Instagram se desactivaron el mismo día? Por qué una decisión arrastra a las demás a través del Centro de cuentas y en qué orden apelar.',
 'Facebook e Instagram desactivados a la vez.','Cuando las cuentas comparten Centro de cuentas, teléfono, correo o dispositivo, una decisión puede afectar a las demás. Actualizado el 11 de noviembre de 2026.',
 '<strong>Identifica la cuenta que se desactivó primero y apela esa antes: las demás suelen caer porque están vinculadas.</strong> Apela cada cuenta desde su propio aviso, indica que son de la misma persona y no crees cuentas nuevas. Meta toma la decisión final.',
 [('La primera cuenta','Empieza por ella.'),('Cada aviso','Una apelación por cuenta.'),('Sin cuentas nuevas','También se vinculan.')],
 ('Por qué caen juntas',['Cuentas unidas en el Centro de cuentas.','Mismo teléfono o correo.','Mismo dispositivo o red.','Cuenta profesional gestionada desde un perfil personal sancionado.']),
 ('En qué orden',['Busca la fecha de cada aviso.','Apela primero la cuenta más antigua.','Después cada una de las demás desde su aviso.','Indica que todas son tuyas.']),'Enlaces oficiales',
 [('¿Desvinculo las cuentas en el Centro de cuentas?','No durante la apelación: no levanta la decisión.')],[('/es/enlaces-oficiales-apelacion-meta-instagram-facebook/','Enlaces oficiales de apelación Meta')])
linked('pt-br','facebook-e-instagram-desativados-juntos','Facebook e Instagram desativados juntos: contas vinculadas (2026)','Facebook e Instagram desativados juntos',
 'Suas contas do Facebook e do Instagram foram desativadas no mesmo dia? Por que uma decisão derruba as outras pela Central de Contas e em que ordem recorrer.',
 'Facebook e Instagram desativados juntos.','Quando as contas compartilham Central de Contas, telefone, e-mail ou aparelho, uma decisão pode afetar as outras. Atualizado em 11 de novembro de 2026.',
 '<strong>Descubra qual conta foi desativada primeiro e recorra por ela antes: as outras costumam cair porque estão vinculadas.</strong> Recorra por cada conta no próprio aviso, diga que são da mesma pessoa e não crie contas novas. A Meta dá a palavra final.',
 [('A primeira conta','Comece por ela.'),('Cada aviso','Um recurso por conta.'),('Sem conta nova','Também seria vinculada.')],
 ('Por que caem juntas',['Contas ligadas na Central de Contas.','Mesmo telefone ou e-mail.','Mesmo aparelho ou rede.','Conta profissional gerida por um perfil pessoal punido.']),
 ('Em que ordem',['Veja a data de cada aviso.','Recorra primeiro pela conta mais antiga.','Depois por cada uma das outras, no próprio aviso.','Diga que todas são suas.']),'Links oficiais',
 [('Devo desvincular as contas?','Não durante o recurso: isso não derruba a decisão.')],[('/pt-br/links-oficiais-contestacao-meta-instagram-facebook/','Links oficiais de contestação Meta')])
linked('de','facebook-und-instagram-gleichzeitig-deaktiviert','Facebook und Instagram gleichzeitig deaktiviert: verknüpfte Konten (2026)','Facebook und Instagram gleichzeitig deaktiviert',
 'Facebook- und Instagram-Konto am selben Tag deaktiviert? Warum eine Entscheidung über die Kontenübersicht andere Konten mitreißt und in welcher Reihenfolge du Einspruch einlegst.',
 'Facebook und Instagram gleichzeitig deaktiviert.','Teilen Konten Kontenübersicht, Telefonnummer, E-Mail oder Gerät, kann eine Entscheidung die anderen treffen. Aktualisiert am 11. November 2026.',
 '<strong>Finde das Konto, das zuerst deaktiviert wurde, und leg dafür zuerst Einspruch ein: Die anderen fallen oft nur, weil sie verknüpft sind.</strong> Leg für jedes Konto über seine eigene Meldung Einspruch ein, schreib, dass alle derselben Person gehören, und leg keine neuen Konten an. Die Entscheidung trifft Meta.',
 [('Erstes Konto','Damit anfangen.'),('Jede Meldung','Ein Einspruch pro Konto.'),('Kein neues Konto','Wird ebenfalls verknüpft.')],
 ('Warum alles gleichzeitig fällt',['Konten in der Kontenübersicht verbunden.','Dieselbe Nummer oder E-Mail.','Dasselbe Gerät oder Netzwerk.','Ein Business-Konto, das über ein gesperrtes Privatprofil verwaltet wird.']),
 ('Reihenfolge',['Datum jeder Meldung notieren.','Zuerst für das älteste Konto Einspruch einlegen.','Dann für jedes weitere über dessen Meldung.','Erwähnen, dass alle Konten dir gehören.']),'Offizielle Links',
 [('Soll ich die Konten trennen?','Nicht während des Einspruchs; das hebt die Entscheidung nicht auf.')],[('/de/meta-einspruch-links-instagram-facebook/','Meta-Einspruchslinks')])
linked('it','facebook-e-instagram-disattivati-insieme','Facebook e Instagram disattivati insieme: account collegati (2026)','Facebook e Instagram disattivati insieme',
 'Account Facebook e Instagram disattivati lo stesso giorno? Perché una decisione si estende agli altri tramite il Centro gestione account e in che ordine fare ricorso.',
 'Facebook e Instagram disattivati insieme.','Quando gli account condividono Centro gestione account, telefono, email o dispositivo, una decisione può colpire gli altri. Aggiornato l’11 novembre 2026.',
 '<strong>Trova l’account disattivato per primo e fai ricorso prima per quello: gli altri spesso cadono solo perché collegati.</strong> Fai ricorso per ogni account dal suo avviso, specifica che appartengono alla stessa persona e non creare nuovi account. La decisione finale è di Meta.',
 [('Il primo account','Parti da lì.'),('Ogni avviso','Un ricorso per account.'),('Niente nuovi account','Verrebbero collegati.')],
 ('Perché cadono insieme',['Account uniti nel Centro gestione account.','Stesso telefono o email.','Stesso dispositivo o rete.','Account professionale gestito da un profilo personale sanzionato.']),
 ('In che ordine',['Annota la data di ogni avviso.','Fai ricorso prima per l’account più vecchio.','Poi per ciascuno degli altri dal suo avviso.','Specifica che sono tutti tuoi.']),'Link ufficiali',
 [('Devo scollegare gli account?','Non durante il ricorso: non annulla la decisione.')],[('/it/link-ricorso-meta-instagram-facebook/','Link di ricorso Meta')])
linked('tr','facebook-ve-instagram-ayni-anda-kapatildi','Facebook ve Instagram aynı anda devre dışı: bağlantılı hesaplar (2026)','Facebook ve Instagram aynı anda kapatıldı',
 'Facebook ve Instagram hesaplarınız aynı gün mü kapatıldı? Bir kararın Hesap Merkezi üzerinden diğer hesapları neden etkilediği ve hangi sırayla itiraz edileceği.',
 'Facebook ve Instagram aynı anda kapatıldı.','Hesaplar Hesap Merkezi’ni, telefonu, e-postayı veya cihazı paylaşıyorsa bir karar diğerlerini de etkileyebilir. 11 Kasım 2026’da güncellendi.',
 '<strong>İlk kapatılan hesabı bulun ve önce onun için itiraz edin: diğerleri çoğu zaman ona bağlı oldukları için kapanır.</strong> Her hesap için kendi bildiriminden itiraz edin, hepsinin aynı kişiye ait olduğunu belirtin ve yeni hesap açmayın. Son kararı Meta verir.',
 [('İlk hesap','Oradan başlayın.'),('Her bildirim','Hesap başına bir itiraz.'),('Yeni hesap yok','O da bağlanır.')],
 ('Neden hepsi birlikte kapanır',['Hesap Merkezi’nde bağlı hesaplar.','Aynı telefon veya e-posta.','Aynı cihaz veya ağ.','Yaptırım almış kişisel profilden yönetilen işletme hesabı.']),
 ('Hangi sırayla',['Her bildirimin tarihini not edin.','Önce en eski hesap için itiraz edin.','Sonra diğerleri için kendi bildirimlerinden.','Hepsinin size ait olduğunu belirtin.']),'Resmi bağlantılar',
 [('Hesapların bağlantısını kaldırmalı mıyım?','İtiraz sırasında hayır; kararı kaldırmaz.')],[('/tr/meta-itiraz-linkleri/','Meta itiraz linkleri')])
linked('ar','facebook-instagram-tatil-maan','تعطيل فيسبوك وإنستغرام معاً: الحسابات المرتبطة (2026)','فيسبوك وإنستغرام معطّلان معاً',
 'هل عُطّل حسابا فيسبوك وإنستغرام في اليوم نفسه؟ لماذا يمتد قرار واحد إلى الحسابات الأخرى عبر مركز الحسابات، وبأي ترتيب تعترض.',
 'فيسبوك وإنستغرام معطّلان معاً.','عندما تتشارك الحسابات مركز الحسابات أو الهاتف أو البريد أو الجهاز، قد يطال قرار واحد الحسابات الأخرى. تحديث 11 نوفمبر 2026.',
 '<strong>حدّد الحساب الذي عُطّل أولاً واعترض عليه قبل غيره: الحسابات الأخرى تُعطَّل غالباً لأنها مرتبطة به.</strong> اعترض على كل حساب من إشعاره الخاص، واذكر أنها لشخص واحد، ولا تنشئ حسابات جديدة. القرار النهائي لميتا.',
 [('الحساب الأول','ابدأ به.'),('كل إشعار','اعتراض لكل حساب.'),('لا حسابات جديدة','ستُربط أيضاً.')],
 ('لماذا تسقط معاً',['حسابات مرتبطة في مركز الحسابات.','الهاتف أو البريد نفسه.','الجهاز أو الشبكة نفسها.','حساب تجاري يُدار من ملف شخصي عليه عقوبة.']),
 ('بأي ترتيب',['دوّن تاريخ كل إشعار.','اعترض أولاً على الحساب الأقدم.','ثم على كل حساب آخر من إشعاره.','اذكر أنها كلها ملكك.']),'الروابط الرسمية',
 [('هل أفصل الحسابات في مركز الحسابات؟','ليس أثناء الاعتراض؛ ذلك لا يلغي القرار.')],[('/ar/rawabit-istinaf-meta/','روابط الاستئناف الرسمية')])
def review(l,slug,title,short,desc,h1,lede,answer,cards,dur,lt,faqs,rel):
    add(l,UR,slug,'ig','Instagram','800',title=title,short=short,desc=desc,h1=h1,lede=lede,answer=answer,cards=cards,
      sections=[('during',dur[0],ul(dur[1])),('links',lt,lr(l,[('Account Status',AS,'Instagram'),('Instagram',IGD,'Meta'),('Accounts Center',AC,'Meta')]))],faqs=faqs,related=rel)
review('fr','instagram-votre-compte-est-en-cours-d-examen','« Votre compte est en cours d’examen » sur Instagram : que faire ? (2026)','Compte en cours d’examen',
 'Instagram affiche « Votre compte est en cours d’examen » ou « Nous examinons votre compte » ? Ce que cela veut dire, combien de temps cela peut prendre et quoi éviter.',
 '« Votre compte est en cours d’examen. »','Ce qui se passe pendant l’examen et comment ne pas l’aggraver. Mis à jour le 11 novembre 2026.',
 '<strong>L’examen signifie qu’Instagram a reçu votre appel, votre pièce d’identité ou votre selfie vidéo et qu’une décision est en attente.</strong> Il n’y a pas de délai fixe. N’envoyez pas d’appels en double, ne créez pas de compte et gardez votre e-mail et votre téléphone joignables.',
 [('Décision en attente','Pas de délai fixe.'),('Pas de doublons','Cela n’accélère rien.'),('Même appareil','Sans VPN.')],
 ('Pendant l’examen',['Surveillez l’e-mail lié au compte, y compris les spams.','Ne changez pas d’e-mail ou de numéro sauf demande.','Gardez une capture datée de l’écran.','Si le message devient « Vous ne pouvez pas demander un autre examen », voyez '+a('/fr/vous-ne-pouvez-pas-demander-un-autre-examen/','ce guide')+'.']),'Liens officiels',
 [('Combien de temps dure l’examen ?','De quelques jours à quelques semaines, sans garantie.')],[('/fr/','Unbanz en français')])
review('es','instagram-tu-cuenta-esta-en-revision','«Tu cuenta está en revisión» en Instagram: qué hacer (2026)','Cuenta en revisión',
 '¿Instagram muestra «Tu cuenta está en revisión» o «Estamos revisando tu cuenta»? Qué significa, cuánto puede tardar y qué evitar.',
 '«Tu cuenta está en revisión.»','Qué pasa durante la revisión y cómo no empeorarla. Actualizado el 11 de noviembre de 2026.',
 '<strong>La revisión significa que Instagram recibió tu apelación, tu documento o tu selfie en vídeo y que hay una decisión pendiente.</strong> No hay un plazo fijo. No envíes apelaciones duplicadas, no crees cuentas y mantén tu correo y teléfono accesibles.',
 [('Decisión pendiente','Sin plazo fijo.'),('Sin duplicados','No acelera.'),('Mismo dispositivo','Sin VPN.')],
 ('Durante la revisión',['Revisa el correo de la cuenta, también el spam.','No cambies correo ni número si no te lo piden.','Guarda una captura con fecha.','Si cambia a «No puedes solicitar otra revisión», mira '+a('/es/no-puedes-solicitar-otra-revision/','esta guía')+'.']),'Enlaces oficiales',
 [('¿Cuánto dura la revisión?','De unos días a varias semanas, sin garantía.')],[('/es/','Unbanz en español')])
review('pt-br','instagram-sua-conta-esta-em-analise','“Sua conta está em análise” no Instagram: o que fazer (2026)','Conta em análise',
 'O Instagram mostra “Sua conta está em análise” ou “Estamos analisando sua conta”? O que significa, quanto pode demorar e o que evitar.',
 '“Sua conta está em análise.”','O que acontece durante a análise e como não piorar. Atualizado em 11 de novembro de 2026.',
 '<strong>A análise significa que o Instagram recebeu seu recurso, documento ou selfie em vídeo e que há uma decisão pendente.</strong> Não existe prazo fixo. Não envie recursos repetidos, não crie contas e mantenha e-mail e telefone acessíveis.',
 [('Decisão pendente','Sem prazo fixo.'),('Sem repetições','Não acelera.'),('Mesmo aparelho','Sem VPN.')],
 ('Durante a análise',['Confira o e-mail da conta, inclusive o spam.','Não troque e-mail ou número sem pedido.','Guarde um print com data.','Se virar “Você não pode solicitar outra análise”, veja '+a('/pt-br/voce-nao-pode-solicitar-outra-analise/','este guia')+'.']),'Links oficiais',
 [('Quanto tempo leva a análise?','De alguns dias a algumas semanas, sem garantia.')],[('/pt-br/','Unbanz em português')])
review('de','instagram-dein-konto-wird-ueberprueft','„Dein Konto wird überprüft“ bei Instagram: was tun? (2026)','Konto wird überprüft',
 'Instagram zeigt „Dein Konto wird überprüft“ oder „Wir überprüfen dein Konto“? Was das bedeutet, wie lange es dauern kann und was du vermeiden solltest.',
 '„Dein Konto wird überprüft.“','Was während der Prüfung passiert und wie du sie nicht verschlechterst. Aktualisiert am 11. November 2026.',
 '<strong>Die Prüfung bedeutet, dass Instagram deinen Einspruch, Ausweis oder dein Video-Selfie erhalten hat und eine Entscheidung aussteht.</strong> Eine feste Dauer gibt es nicht. Schick keine doppelten Einsprüche, leg keine Konten an und bleib per E-Mail und Telefon erreichbar.',
 [('Entscheidung offen','Keine feste Dauer.'),('Keine Duplikate','Beschleunigt nichts.'),('Gleiches Gerät','Ohne VPN.')],
 ('Während der Prüfung',['E-Mails zum Konto prüfen, auch im Spam.','E-Mail oder Nummer nur ändern, wenn verlangt.','Datierten Screenshot behalten.','Wird daraus „Du kannst keine weitere Überprüfung beantragen“, lies '+a('/de/keine-weitere-ueberpruefung-moeglich/','diesen Ratgeber')+'.']),'Offizielle Links',
 [('Wie lange dauert die Prüfung?','Einige Tage bis einige Wochen, ohne Garantie.')],[('/de/','Unbanz auf Deutsch')])
P=list(b5.P)
