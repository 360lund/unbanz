# -*- coding: utf-8 -*-
from lib import *
import core, es_services, es_guides

SLUGS = {
 'home': '', 'services': 'servicios', 'pricing': 'precio-recuperar-cuenta', 'faq': 'preguntas-frecuentes', 'contact': 'contacto',
 'reviews': 'opiniones', 'about': 'quienes-somos', 'how': 'como-funciona', 'legit': 'es-unbanz-fiable',
 'ig': 'recuperar-cuenta-instagram', 'fb': 'recuperar-cuenta-facebook', 'ad': 'recuperar-cuenta-publicitaria',
 'snap': 'recuperar-cuenta-snapchat', 'fake': 'denunciar-cuenta-falsa', 'imp': 'denunciar-suplantacion-de-identidad',
 'har': 'denunciar-cuenta-de-acoso', 'user': 'reclamar-nombre-de-usuario-instagram',
 'ig-disabled': 'cuenta-de-instagram-desactivada', 'ig-hacked': 'cuenta-de-instagram-hackeada',
 'appeal-time': 'cuanto-tarda-la-apelacion-de-instagram', 'appeal-denied': 'apelacion-de-instagram-rechazada',
 'deleted': 'cuenta-de-instagram-eliminada-o-desactivada', 'no-button': 'instagram-sin-boton-de-apelar',
 'blocked': 'instagram-restringimos-ciertas-actividades', 'ad-disabled': 'cuenta-publicitaria-de-facebook-desactivada',
 'fb-appeal': 'cuenta-de-facebook-desactivada-apelar', 'fb-hacked': 'cuenta-de-facebook-hackeada',
 'inactive-user': 'nombre-de-usuario-de-instagram-cuenta-inactiva', 'report-fake': 'denunciar-cuenta-falsa-con-mis-fotos',
 'scams': 'estafas-al-recuperar-cuentas-aviso', 'sextortion': 'sextorsion-en-instagram-que-hacer',
 'support': 'contactar-con-instagram-o-meta-desde-espana', 'rights': 'dsa-derecho-a-recurrir-decisiones-de-meta',
}

WA_DEFAULT = 'Hola%20Unbanz%2C%20necesito%20ayuda%20con%20una%20cuenta%20(ES)'

S = dict(
 code='es', dir='es', html_lang='es', og_locale='es_ES', country='España', js_code='es', tag='(ES)',
 wa_default=WA_DEFAULT, mail_subj='Ayuda%20con%20mi%20cuenta',
 offer_desc='El precio lo conoces en la conversación, después de explicarnos tu situación y antes de que empiece el trabajo. Preguntar no cuesta nada.',
 og_alt='Unbanz: ayuda con cuentas de Instagram, Facebook y Snapchat',
 skip='Saltar al contenido', nav_aria='Menú principal', mnav_aria='Menú móvil',
 n_home='Inicio', n_services='Servicios', n_user='Nombres de usuario', n_reviews='Opiniones', n_faq='Preguntas', n_contact='Contacto', n_how='Cómo funciona',
 menu_open='Abrir menú', menu_close='Cerrar menú',
 foot_links=[('services', 'Servicios'), ('ig', 'Instagram'), ('fb', 'Facebook'), ('snap', 'Snapchat'), ('ad', 'Cuentas publicitarias'),
             ('fake', 'Cuentas falsas'), ('imp', 'Suplantación'), ('har', 'Acoso'), ('user', 'Nombres de usuario'), ('pricing', 'Precio'),
             ('how', 'Cómo funciona'), ('faq', 'FAQ'), ('reviews', 'Opiniones'), ('legit', '¿Es Unbanz fiable?'), ('contact', 'Contacto')],
 foot_tag='Recuperar cuentas &amp; denunciar perfiles.<br>Habla directamente con nosotros.',
 foot_indep='Servicio independiente. Sin afiliación con Meta.',
 mc_wa='Escríbenos por WhatsApp', mc_mail='Correo',
 cta_quote='Pide un precio por WhatsApp', cta_mail='Escríbenos un correo',
 hero_wa='Hablemos por WhatsApp', hero_mail='¿Prefieres el correo?',
 write_us='Escríbenos', see_detail='Ver los detalles',
 faq_eyebrow='PREGUNTAS FRECUENTES', faq_eyebrow2='TUS DUDAS', faq_title='Lo que conviene saber.',
 proof_title='Cuéntanos qué ha pasado.', related='Páginas relacionadas', related_services='Todos los servicios',
 crumb_guides='Guías', crumb_services='Servicios', help_h2='¿Quieres ayuda?', guides_h2='Guías relacionadas',
 std_howto=('<h2 id="con-unbanz">Cómo funciona con Unbanz</h2><ol><li>Nos envías tu nombre de usuario y una captura del aviso por WhatsApp o correo.</li>'
            '<li>Te decimos con sinceridad si podemos ayudarte. El precio lo conoces en la conversación, después de explicarnos tu situación y antes de que empiece el trabajo. Preguntar no cuesta nada.</li>'
            '<li>Preparamos la solicitud y la enviamos por el proceso oficial de la plataforma.</li>'
            '<li>Te mantenemos al tanto hasta que haya una respuesta.</li></ol>'
            '<p>La atención es principalmente en inglés; con un mensaje corto con tu nombre de usuario, la captura y la fecha basta para empezar.</p>'),
 std_safe=('<h2 id="con-cuidado">Ten cuidado</h2><p>Nadie necesita tu contraseña ni tus códigos de acceso para ayudarte. Nosotros tampoco. '
           'Si alguien te ofrece por mensaje privado "solucionarlo todo", te pide iniciar sesión desde un enlace o dice tener un contacto en Meta, no sigas adelante. '
           'Unbanz nunca te pide tus datos de acceso y no finge tener un acceso especial: usamos las mismas vías oficiales que tú.</p>'),
 std_about=('<h2 id="sobre-unbanz">Sobre Unbanz</h2><p>Unbanz (unbanz.com) es un servicio independiente que ayuda a particulares, empresas y agencias con las solicitudes para recuperar cuentas desactivadas de Instagram, Facebook y Snapchat, '
            'con la denuncia de cuentas que incumplen las normas a través de las herramientas oficiales, con las solicitudes de nombres de usuario y con la recuperación de cuentas publicitarias de Meta. '
            'Unbanz no es Unbanx ni unbanx.me y no tiene afiliación con Meta. Consulta también <a href="@@legit@@">¿Es Unbanz fiable?</a></p>'),
 block3=[('Vivas donde vivas', 'Trabajamos a distancia, por WhatsApp o correo, con clientes de España, Europa y el resto del mundo. La atención es principalmente en inglés.'),
         ('Primero el precio', 'Conoces el precio antes de que empiece el trabajo: te lo decimos en la conversación, después de que nos expliques tu situación.'),
         ('Tu contraseña es tuya', 'Solo necesitamos tu nombre de usuario y el aviso. Tu contraseña y tus códigos se quedan contigo.')],
 price_h2='Conoce el precio<br>antes de empezar.', price_p='Escríbenos por WhatsApp o por correo, cuéntanos la situación y te decimos cuánto cuesta.',
 price_link='Cómo se calcula el precio',
 vt_transcript='Transcripción (en inglés)', vt_play='Reproducir vídeo',
 vt_titles=[('Client on claiming an inactive Instagram username with Unbanz', 'Reproducir vídeo: cliente sobre cómo reclamar un nombre de usuario inactivo de Instagram', 'Cliente: opinión en vídeo sobre una solicitud de nombre de usuario de Instagram', 'Username claim', 'Nombre de usuario'),
            ('Management agency owner on working with Unbanz', 'Reproducir vídeo: dueño de una agencia sobre trabajar con Unbanz', 'Dueño de agencia: opinión en vídeo sobre trabajar con Unbanz', 'Agency owner', 'Dueño de agencia'),
            ('Restricted Facebook ad account restored by Unbanz', 'Reproducir vídeo: cuenta publicitaria de Facebook restringida y recuperada', 'Cliente: opinión en vídeo sobre una cuenta publicitaria restringida', 'Ad account', 'Cuenta publicitaria')],
 js_services="['unban', 'Recuperar mi cuenta'], ['ban', 'Denunciar una cuenta'], ['username', 'Nombre de usuario'], ['ad', 'Cuenta publicitaria'], ['other', 'Otra cosa']",
 js_eyebrow='ESCRÍBENOS', js_title='¿Con qué necesitas ayuda?', js_legend_service='Servicio', js_legend_platform='Plataforma',
 js_reason_label='Motivo breve <span>(opcional)</span>', js_placeholder='p. ej. desactivada tras iniciar sesión en un móvil nuevo',
 js_continue='Continuar en WhatsApp', js_email='Prefiero el correo', js_note='No envíes nunca contraseñas ni códigos de acceso.', js_close='Cerrar',
 js_mail_subject='Ayuda con mi cuenta',
 js_sentence=("""    const base = s === 'unban' ? `Quiero recuperar mi cuenta de ${pl}`
      : s === 'ban' ? `Quiero denunciar una cuenta de ${pl}`
      : s === 'username' ? `Quiero reclamar un nombre de usuario de ${pl}`
      : s === 'ad' ? (pl === 'Instagram' || pl === 'Facebook' ? `Necesito ayuda con mi cuenta publicitaria de Meta (${pl})` : `Necesito ayuda con una cuenta publicitaria en ${pl}`)
      : `Necesito ayuda con mi cuenta de ${pl}`;
    const reason = modal.querySelector('#cm-reason').value.replace(/\\s+/g, ' ').trim();
    return `Hola Unbanz, ${base}.` + (reason ? ` Motivo: ${reason}` : '') + ' %TAG%' + (window.unbanzViaTag ? ` ${window.unbanzViaTag}` : '');"""),
 llms=dict(
   header='## Español (España)',
   intro='Unbanz también está disponible en español, para quien en España busca ayuda con una cuenta de Instagram, Facebook o Snapchat desactivada, bloqueada o hackeada. La atención es principalmente en inglés.',
   facts_label='### Datos clave (español)',
   facts=('- Unbanz es un servicio independiente y no tiene afiliación con Meta. Todo se hace por las vías oficiales de la plataforma; la decisión siempre es de la plataforma.\n'
          '- El precio lo conoces en la conversación, después de explicar la situación y antes de que empiece el trabajo. Preguntar no cuesta nada.\n'
          '- Unbanz nunca pide tu contraseña ni tus códigos de acceso.\n'
          '- Solo en las solicitudes de nombre de usuario: si la solicitud no prospera, se devuelve el 100 % del importe (ver /refund-policy/).\n'
          '- Contacto: WhatsApp +1 934 201 2490 o team@unbanz.com.'),
   pages_label='### Páginas en español', qa_label='### Respuestas breves (español)',
   qa=[('¿Cómo recupero mi cuenta de Instagram si la han desactivado?', 'Abre el aviso en la app, apela una sola vez por el formulario oficial y guarda una captura; si no funciona, Unbanz puede preparar y enviar la solicitud por ti.', 'ig-disabled'),
       ('¿Cuánto cuesta recuperar una cuenta?', 'El precio depende de la cuenta y de la situación. Unbanz lo indica en la conversación, antes de empezar el trabajo; preguntar no cuesta nada.', 'pricing'),
       ('¿Es fiable Unbanz?', 'Unbanz es un servicio independiente con un solo sitio web, un correo, condiciones por escrito y opiniones en vídeo de clientes; nunca pide tu contraseña.', 'legit')]),
)

C = {}
C['services'] = dict(
 title='Recuperar cuenta de Instagram, Facebook y Snapchat: servicios',
 desc='Ayuda con cuentas desactivadas o hackeadas, denuncia de cuentas falsas y solicitudes de nombre de usuario. Por las vías oficiales.',
 nav='Servicios', h1='Servicios: recuperar cuentas y denunciar perfiles.',
 lead='Instagram, Facebook, Snapchat y cuentas publicitarias de Meta. Envíanos tu nombre de usuario y el aviso y te decimos con sinceridad si podemos ayudarte. Todo se hace por las vías oficiales de la plataforma.',
 eyebrow='TU SITUACIÓN', h2='¿Con qué necesitas ayuda?',
 rows=[('Recuperar cuenta de Instagram', 'Desactivada, suspendida o hackeada: apelación y recuperación por las vías oficiales.', 'ig', 'unban'),
       ('Recuperar cuenta de Facebook', 'Perfiles desactivados o hackeados y páginas restringidas.', 'fb', 'unban'),
       ('Recuperar cuenta de Snapchat', 'Cuentas de Snapchat bloqueadas o desactivadas.', 'snap', 'unban'),
       ('Cuentas publicitarias', 'Cuentas publicitarias y portfolios comerciales de Meta restringidos o desactivados.', 'ad', 'ad'),
       ('Denunciar cuentas falsas', 'Denunciar perfiles falsos con las herramientas oficiales de la plataforma.', 'fake', 'ban'),
       ('Denunciar suplantación', 'Alguien se hace pasar por ti o por tu empresa.', 'imp', 'ban'),
       ('Denunciar acoso', 'Cuentas que te acosan o te amenazan.', 'har', 'ban'),
       ('Reclamar un nombre de usuario', 'Nombres de usuario inactivos u ocupados, por los procesos oficiales de la plataforma.', 'user', 'username')],
 faq=[('¿Con qué plataformas ayudáis?', 'Instagram, Facebook, Snapchat y cuentas publicitarias de Meta.'),
      ('¿Cómo funciona?', 'Nos envías el nombre de usuario y una captura del aviso. Te decimos con sinceridad si podemos ayudarte y te indicamos el precio en la conversación, antes de que empiece el trabajo.'),
      ('¿Puedo hacerlo yo mismo?', 'Sí. Apelar, el formulario de recuperación de cuentas hackeadas y la denuncia de una cuenta son gratuitos y oficiales. Nosotros ayudamos si se atasca o si prefieres delegarlo.'),
      ('¿Tiene Unbanz relación con Meta?', 'No. Unbanz es independiente y usa las mismas vías oficiales que tú. La decisión siempre es de la plataforma.')],
 related=['ig', 'fb', 'snap', 'ad', 'user', 'pricing', 'how', 'legit'])

FAQ_ALL = [
 ('Mi cuenta de Instagram está desactivada. ¿Qué puedo hacer?', 'Inicia sesión, abre el aviso y apela una sola vez por el formulario oficial; normalmente dispones de unos 180 días. Haz una captura del aviso. Consulta la guía <a href="@@ig-disabled@@">cuenta de Instagram desactivada</a>.'),
 ('Me han hackeado la cuenta y han cambiado el correo. ¿Hay esperanza?', 'A menudo sí, con las herramientas oficiales de Instagram (instagram.com/hacked y la verificación con vídeo selfie). Consulta <a href="@@ig-hacked@@">cuenta de Instagram hackeada</a>.'),
 ('¿Cuánto cuesta recuperar una cuenta?', 'El precio depende de la cuenta y de la situación. Te lo decimos en la conversación, después de que nos cuentes qué ha pasado y antes de que empiece el trabajo. Preguntar no cuesta nada. Consulta <a href="@@pricing@@">precio</a>.'),
 ('¿Cuánto se tarda?', 'Meta y Snapchat no publican un plazo de respuesta. Puede llegar a los pocos días o pasadas varias semanas. No prometemos ninguna fecha, pero te mantenemos informado.'),
 ('¿Necesitáis mi contraseña?', 'No, nunca. Basta con un nombre de usuario o el enlace del perfil y una captura del aviso. No compartas tu contraseña ni tus códigos con nadie.'),
 ('¿Tiene Unbanz relación con Meta?', 'No. Unbanz es un servicio independiente. Usamos las vías oficiales de la plataforma y la decisión siempre es de la plataforma. Consulta <a href="@@legit@@">¿Es Unbanz fiable?</a>'),
 ('¿Ayudáis también a denunciar cuentas falsas?', 'Sí, ayudamos a denunciar cuentas falsas, de suplantación y de acoso con las herramientas oficiales de denuncia de la plataforma. Consulta <a href="@@fake@@">denunciar cuenta falsa</a>.'),
 ('¿Podéis reclamar un nombre de usuario por mí?', 'Ayudamos con las solicitudes de un nombre de usuario inactivo u ocupado por los procesos oficiales de la plataforma, por ejemplo una denuncia por marca registrada o por suplantación. La decisión es de la plataforma. Consulta <a href="@@user@@">reclamar un nombre de usuario</a>.'),
 ('¿Qué pasa si fracasa una solicitud de nombre de usuario?', 'Se te devuelve el 100 % del importe. Solo se aplica a las solicitudes de nombre de usuario; consulta la <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (en inglés).'),
 ('¿Cómo contacto con vosotros?', 'Por WhatsApp o por correo a team@unbanz.com. La atención es principalmente en inglés; basta un mensaje corto con tu nombre de usuario, una captura y la fecha. Consulta <a href="@@contact@@">contacto</a>.'),
 ('¿Puedo recuperar mi cuenta publicitaria de Meta?', 'Ayudamos con cuentas publicitarias y portfolios comerciales restringidos o desactivados por los procesos oficiales de revisión de Meta. Consulta <a href="@@ad@@">recuperar cuenta publicitaria</a>.'),
 ('¿Es gratis intentarlo por mi cuenta?', 'Sí. Apelar, el formulario de recuperación y las denuncias son gratuitos. Intenta primero eso si el botón oficial está disponible.'),
]
C['faq'] = dict(
 title='Preguntas frecuentes sobre recuperar una cuenta',
 desc='Respuestas a las preguntas que más nos hacen sobre cuentas desactivadas, hackeadas y bloqueadas, el precio, la contraseña y las vías oficiales.',
 nav='Preguntas frecuentes', crumb='Preguntas', h1='Preguntas frecuentes.',
 lead='Respuestas breves y sinceras sobre cuentas de Instagram, Facebook y Snapchat, cómo trabajamos y qué puedes hacer tú gratis.',
 items=FAQ_ALL, faq_h2='Lo que conviene saber.', related=['ig', 'fb', 'user', 'pricing', 'how', 'legit', 'contact'])

C['contact'] = dict(
 title='Contacto: ayuda con tu cuenta de Instagram o Facebook',
 desc='Escríbenos por WhatsApp o correo. Envía tu nombre de usuario y una captura del aviso; la atención es principalmente en inglés.',
 nav='Contacto', eyebrow='CONTACTO', h1='Cuéntanos qué ha pasado.',
 p1='Elige lo que necesitas y abrimos WhatsApp con un mensaje ya preparado. Puedes modificarlo antes de enviarlo.',
 opts=[('Recuperar cuenta de Instagram', 'Hola Unbanz, quiero recuperar mi cuenta de Instagram.', 'unban'),
       ('Recuperar cuenta de Facebook', 'Hola Unbanz, quiero recuperar mi cuenta de Facebook.', 'unban'),
       ('Recuperar cuenta de Snapchat', 'Hola Unbanz, quiero recuperar mi cuenta de Snapchat.', 'unban'),
       ('Denunciar una cuenta', 'Hola Unbanz, quiero denunciar una cuenta.', 'ban'),
       ('Reclamar un nombre de usuario', 'Hola Unbanz, quiero reclamar un nombre de usuario.', 'username'),
       ('Cuenta publicitaria', 'Hola Unbanz, necesito ayuda con una cuenta publicitaria de Meta.', 'ad')],
 mail_h2='¿Prefieres el correo?', mail_p='Escribe a team@unbanz.com e indica tu nombre de usuario o el enlace del perfil, una captura del aviso y la fecha en que ocurrió.',
 what_h2='Qué puedes enviarnos', what_p='Tu @usuario o el enlace del perfil, una captura del aviso y la fecha. Si es una cuenta publicitaria, también el ID de la cuenta. No envíes nunca una contraseña ni un código de acceso.',
 social_h2='También en', social_p='Somos @unbanzhq en Instagram y X. Para datos de cuentas, es mejor usar WhatsApp o el correo.',
 lang_h2='Idioma', lang_p='La atención es principalmente en inglés. Un mensaje corto con el nombre de usuario, la captura y la fecha basta para empezar.',
 note='Servicio independiente. Sin afiliación con Meta. Nunca te pedimos la contraseña.')

C['reviews'] = dict(
 title='Opiniones: vídeos de clientes de Unbanz',
 desc='Vídeos de clientes que trabajaron con Unbanz: un nombre de usuario, una agencia y una cuenta publicitaria restringida. En inglés.',
 nav='Opiniones', h1='Clientes en sus palabras.',
 p='Tres clientes cuentan con sus propias palabras cómo fue trabajar con Unbanz. Los vídeos y las transcripciones están en inglés.',
 video_aria='Opiniones en vídeo de clientes', mail='O escríbenos un correo', pick='¿De qué se trata?',
 pick_opts=[('Recuperar una cuenta', 'Hola Unbanz, quiero recuperar mi cuenta.', 'unban'), ('Nombre de usuario', 'Hola Unbanz, quiero reclamar un nombre de usuario.', 'username'), ('Cuenta publicitaria', 'Hola Unbanz, necesito ayuda con una cuenta publicitaria.', 'ad')],
 q_h2='Preguntas sobre estas opiniones.',
 faq=[('¿De dónde salen estas opiniones?', 'Son vídeos de clientes que han trabajado con Unbanz. Puedes verlos aquí mismo y leer la transcripción.'),
      ('¿En qué idioma están los vídeos?', 'En inglés. Debajo de cada vídeo está la transcripción, también en inglés.'),
      ('¿Puedo hacer una pregunta antes de decidir?', 'Sí. Escríbenos por WhatsApp o por correo. Preguntar no cuesta nada.')])

C['home'] = dict(
 title='Recuperar cuenta de Instagram: ayuda con cuentas bloqueadas',
 desc='¿Cuenta de Instagram o Facebook desactivada, suspendida o hackeada? Envía tu nombre de usuario y el aviso: preparamos la solicitud por las vías oficiales.',
 skip='Saltar a los servicios', home_aria='Unbanz, ir arriba',
 h1a='Recuperar cuenta', h1b='de Instagram.',
 hero_p='¿Desactivada, suspendida o hackeada? Envíanos tu nombre de usuario y el aviso: preparamos la solicitud por las vías oficiales de Instagram, Facebook y Snapchat.',
 intro_eyebrow='CUENTAS &amp; DENUNCIAS', intro_h2='¿Cuenta bloqueada? Envíanos los detalles.',
 intro_p=('Unbanz (unbanz.com) es un servicio independiente para Instagram, Facebook y Snapchat: apelaciones y nuevas revisiones de cuentas desactivadas o bloqueadas, denuncia de cuentas falsas con las herramientas oficiales, '
          'solicitudes de nombre de usuario y ayuda con cuentas publicitarias de Meta. Nos envías el nombre de usuario y una captura del aviso y te decimos con sinceridad si podemos ayudarte. '
          'Servicio independiente, sin afiliación con Meta y sin relación con Unbanx. ¿Prefieres empezar por tu cuenta? Lee antes la guía <a href="@@appeal-denied@@">apelación de Instagram rechazada</a>.'),
 exp_eyebrow='TU SITUACIÓN', exp_h2='¿Con qué necesitas ayuda?',
 rows=[('Recuperar cuenta de Instagram', 'Desactivada, suspendida o hackeada.', 'ig', 'unban'),
       ('Cuenta de Facebook', 'Perfiles desactivados o hackeados, páginas restringidas.', 'fb', 'unban'),
       ('Cuentas falsas y suplantación', 'Denuncia con las herramientas oficiales.', 'fake', 'ban'),
       ('Nombres de usuario', 'Nombres de usuario inactivos u ocupados.', 'user', 'username'),
       ('Cuentas publicitarias', 'Cuentas publicitarias y portfolios comerciales restringidos.', 'ad', 'ad')],
 vt_eyebrow='CLIENTES', vt_h2='En sus propias palabras.', vt_note='Vídeos y transcripciones en inglés.', vt_all='Todas las opiniones',
 pw_eyebrow='TU CONTRASEÑA', pw_zero='contraseñas pedidas', pw_note='Un nombre de usuario y una captura bastan. Te mantenemos informado en todo momento.',
 how_eyebrow='CÓMO FUNCIONA', how_h2='Envía los detalles. Nosotros nos encargamos del resto.',
 steps=['Envía tu nombre de usuario y el aviso.', 'Conoce el precio antes de que empiece el trabajo.', 'Enviamos la solicitud por el proceso oficial.'], how_link='Cómo funciona',
 pr_eyebrow='PRECIO', pr_h2='El precio, antes de empezar.',
 pr_p='El precio depende de la cuenta, de la situación y del trabajo necesario. Te lo decimos en la conversación, después de que nos cuentes qué ha pasado. Preguntar no cuesta nada.',
 pr_cta='Pide un precio',
 pr_notes=[('Primero el precio', 'Lo sabes antes de que empiece el trabajo.'), ('Vías oficiales', 'Apelaciones y denuncias, sin atajos.'), ('Sin contraseña', 'Tu contraseña se queda contigo.')],
 pr_link='El precio y de qué depende',
 faq_eyebrow='RESPUESTAS BREVES', faq_h2='Antes de escribirnos.',
 faq=[('Mi cuenta de Instagram está desactivada. ¿Y ahora?', 'Inicia sesión, abre el aviso y apela una sola vez; normalmente hay unos 180 días. Haz una captura. Consulta la <a href="@@ig-disabled@@">guía</a>.'),
      ('¿Es fiable Unbanz?', 'Unbanz es un servicio independiente: un solo sitio web, un correo, condiciones por escrito y opiniones en vídeo de clientes. Nunca pedimos tu contraseña. Consulta <a href="@@legit@@">¿Es Unbanz fiable?</a>'),
      ('¿Cuánto cuesta?', 'Depende de la cuenta y de la situación. Conoces el precio en la conversación, antes de que empiece el trabajo. Preguntar no cuesta nada.'),
      ('¿Necesitáis mi contraseña?', 'No. Basta con un nombre de usuario y una captura del aviso.'),
      ('¿Atendéis en español?', 'La atención es principalmente en inglés. Un mensaje corto con tu nombre de usuario, la captura y la fecha basta para empezar.'),
      ('¿Puedo reclamar un nombre de usuario inactivo?', 'A veces sí, por los procesos oficiales de la plataforma. La decisión es de la plataforma. Si una solicitud de nombre de usuario fracasa, se te devuelve el 100 % del importe. Consulta <a href="@@user@@">reclamar un nombre de usuario</a>.')],
 cl_eyebrow='CONTACTO', cl_h2='Cuéntanos qué ha pasado.',
 cl_p='La atención es principalmente en inglés. Tu nombre de usuario, una captura y la fecha bastan para empezar.')

def make():
    site = Site(S, SLUGS)
    core.home_page(site, C); core.services_page(site, C); core.faq_page(site, C); core.contact_page(site, C); core.reviews_page(site, C)
    es_services.add(site); es_guides.add(site)
    return site
