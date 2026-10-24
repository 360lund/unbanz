# -*- coding: utf-8 -*-
from lib import *

def P(*t):
    return ''.join('<p>%s</p>' % x for x in t)
def UL(*t):
    return '<ul>' + ''.join('<li>%s</li>' % x for x in t) + '</ul>'
def OL(*t):
    return '<ol>' + ''.join('<li>%s</li>' % x for x in t) + '</ol>'

HELP_IG = P('¿No te funciona el botón oficial o prefieres que te ayudemos? Envíanos tu nombre de usuario, una captura del aviso y la fecha. Te decimos con sinceridad si podemos ayudarte y te indicamos el precio en la conversación, antes de que empiece el trabajo. Preguntar no cuesta nada. La atención es principalmente en inglés.')
HELP_FB = P('Envíanos el enlace del perfil, una captura del aviso y la fecha. Te decimos con sinceridad si podemos ayudarte y te indicamos el precio en la conversación, antes de que empiece el trabajo. La atención es principalmente en inglés.')
HELP_AD = P('Envíanos el ID de la cuenta, una captura del aviso y la fecha. Te decimos con sinceridad si podemos ayudarte y te indicamos el precio en la conversación, antes de que empiece el trabajo. La atención es principalmente en inglés.')
HELP_REP = P('Envíanos los enlaces de las cuentas y las capturas. Te ayudamos a preparar y presentar una denuncia clara con las herramientas oficiales; la decisión es de la plataforma. El precio lo conoces en la conversación, antes de que empiece el trabajo. La atención es principalmente en inglés.')

def add(site):
    g = site.guide
    S = site.S

    # ================= core trust pages =================
    site.reg('pricing', 'guide', 'Precio: ¿cuánto cuesta recuperar una cuenta?',
             '¿Cuánto cuesta la ayuda con una cuenta de Instagram o Facebook? Depende de la situación y lo conoces antes de que empiece el trabajo.', 'Precio')
    site.build['pricing'] = lambda: site.guide_page('pricing',
        '¿Cuánto cuesta recuperar una cuenta de Instagram o Facebook?',
        'El precio depende de la cuenta, de la plataforma y del trabajo necesario. En Unbanz te lo decimos en la conversación, después de que nos expliques tu situación y antes de que empiece el trabajo; preguntar no cuesta nada. Meta no publica plazos de respuesta y nosotros no podemos prometer ninguno.',
        [('precio', 'De qué depende el precio', UL('La plataforma: Instagram, Facebook, Snapchat o una cuenta publicitaria de Meta.',
                                                  'El tipo de situación: desactivada, suspendida, hackeada, denunciar una cuenta falsa o una solicitud de nombre de usuario.',
                                                  'El número de cuentas o de denuncias.',
                                                  'El trabajo necesario: pruebas, comprobaciones y seguimiento.') + P('Un precio dado sin conocer tu situación no vale nada. Por eso primero preguntamos qué ha pasado.')),
         ('necesitamos', 'Qué necesitamos para responderte', P('Tu nombre de usuario o el enlace del perfil, una captura del aviso y la fecha. En una cuenta publicitaria, el ID de la cuenta. Nunca una contraseña ni un código.')),
         ('gratis', 'Los pasos oficiales son gratuitos', P('Apelar una desactivación, el formulario de recuperación de cuentas hackeadas y la denuncia de una cuenta no cuestan nada: son pasos oficiales que puedes dar tú. Nosotros ayudamos si se atascan, si el aviso no está claro o si prefieres delegarlo. Lee primero la guía <a href="@@appeal-denied@@">apelación rechazada</a>.')),
         ('refund', 'Solicitud de nombre de usuario: refund policy', P('Si una solicitud de nombre de usuario no prospera, se te devuelve el 100 % del importe. Solo se aplica a las solicitudes de nombre de usuario. Consulta la <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (en inglés).')),
         ('plazo', '¿Y cuánto se tarda?', P('Meta y Snapchat no publican un plazo de respuesta. Según la situación, puede llegar a los pocos días o pasadas varias semanas. No prometemos ninguna fecha, pero te mantenemos informado. Consulta <a href="@@appeal-time@@">cuánto tarda una apelación de Instagram</a>.')),
         ('alertas', 'Señales de alerta con los precios', UL('Te dan un importe sin preguntarte nada sobre tu situación.', 'Un servicio que te escribe primero.', 'Te piden tu contraseña, un código o acceso a tu correo.', 'Te prometen un resultado seguro.') + P('Consulta también <a href="@@scams@@">estafas al recuperar cuentas</a>.'))],
        [('¿Cuánto cuesta la ayuda con una cuenta de Instagram?', 'Depende de la cuenta y de la situación. Te decimos el precio en la conversación, después de que nos cuentes qué ha pasado y antes de que empiece el trabajo.'),
         ('¿Cuesta algo pedir un presupuesto?', 'No. Preguntar no cuesta nada y no te obliga a nada.'),
         ('¿Cuánto se tarda en recuperar una cuenta?', 'Meta no publica un plazo. Varía de unos días a varias semanas. No podemos prometer una fecha.'),
         ('¿Puedo hacerlo gratis por mi cuenta?', 'Sí, los pasos oficiales (apelación, formulario de recuperación, denuncia) son gratuitos. Nuestra ayuda es para quien prefiere delegarlo o se ha atascado.'),
         ('¿Debo enviar mi contraseña para que me den un precio?', 'No. Basta con un nombre de usuario y una captura. No compartas nunca tu contraseña ni tus códigos.'),
         ('¿Qué pasa si fracasa mi solicitud de nombre de usuario?', 'Se te devuelve el 100 % del importe. Solo se aplica a las solicitudes de nombre de usuario; consulta la <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (en inglés).')],
        ['ig', 'fb', 'user', 'appeal-time', 'how', 'legit'], HELP_IG, crumb_label=S['crumb_services'], std=False)

    g('how', 'Cómo funciona: recuperar una cuenta con Unbanz', 'Cómo funciona', 'Cómo funciona.',
      'Nos envías tu nombre de usuario y una captura del aviso. Te decimos con sinceridad si podemos ayudarte, te damos el precio antes de que empiece el trabajo y enviamos la solicitud por el proceso oficial de la plataforma.',
      [('pasos', 'Los pasos', OL('Envíanos tu nombre de usuario o el enlace del perfil, una captura del aviso y la fecha, por WhatsApp o por correo.',
                                 'Vemos tu situación y te decimos con sinceridad si podemos ayudarte. El precio lo conoces en la conversación, antes de que empiece el trabajo.',
                                 'Si aceptas, preparamos la solicitud y la enviamos por el proceso oficial: una apelación si hay desactivación, el formulario de recuperación si te han hackeado, las herramientas de denuncia si es una cuenta falsa.',
                                 'Te mantenemos al tanto de las respuestas. La decisión siempre es de la plataforma.')),
       ('vias', 'Las vías oficiales que usamos', P('Las apelaciones van por los procesos oficiales de recurso y revisión. Las cuentas falsas, de suplantación o de estafadores las denunciamos con las herramientas de denuncia de la propia plataforma. Las solicitudes de nombre de usuario usan la vía oficial que corresponde: una denuncia por marca registrada, una denuncia por suplantación o la vía de una cuenta inactiva.')),
       ('nunca', 'Lo que nunca hacemos', UL('Nunca te pedimos la contraseña ni los códigos de acceso.', 'Nunca compramos, vendemos ni transferimos cuentas.', 'No usamos bots, herramientas de captura de nombres ni denuncias falsas.', 'No fingimos ser nadie de Meta.')),
       ('idioma', 'Idioma y contacto', P('La atención es principalmente en inglés. Un mensaje corto con tu nombre de usuario, la captura y la fecha basta para empezar.'))],
      [('¿Cómo empiezo?', 'Escríbenos por WhatsApp o por correo con tu nombre de usuario, una captura del aviso y la fecha.'),
       ('¿Cuándo conozco el precio?', 'En la conversación, después de explicarnos tu situación y antes de que empiece el trabajo.'),
       ('¿Necesito dar una contraseña?', 'No. Nunca la pedimos.'),
       ('¿Decidís vosotros si vuelve mi cuenta?', 'No. La decisión siempre es de la plataforma. Nosotros preparamos y enviamos la solicitud.'),
       ('¿Atendéis en español?', 'La atención es principalmente en inglés. Un mensaje corto basta para empezar.')],
      ['ig', 'fb', 'user', 'pricing', 'legit', 'faq'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='Así funciona Unbanz: envías tu nombre de usuario y el aviso, conoces el precio antes de empezar y enviamos la solicitud por las vías oficiales.')

    g('legit', '¿Es Unbanz fiable? Lo que debes saber', '¿Es Unbanz fiable?', '¿Es Unbanz fiable?',
      'Unbanz es un servicio independiente con un solo sitio web, un correo, condiciones por escrito y opiniones en vídeo de clientes. Nunca pedimos tu contraseña, damos el precio antes de que empiece el trabajo y solo usamos las vías oficiales de la plataforma.',
      [('hechos', 'Datos que puedes comprobar tú mismo', UL('Un solo sitio web (unbanz.com), un correo (team@unbanz.com) y un número de WhatsApp.', '<a href="/terms/" hreflang="en" lang="en">Condiciones</a> por escrito y una <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a>.', 'Opiniones en vídeo de clientes, con transcripción, en la página <a href="@@reviews@@">Opiniones</a>.', 'No pagas nada por pedir un precio.')),
       ('no', 'Lo que Unbanz no es', P('Unbanz no tiene afiliación con Meta ni con Snapchat y no tiene acceso especial a sus empleados. Unbanz tampoco es Unbanx ni unbanx.me; las valoraciones de Unbanx no hablan de nosotros.')),
       ('vias', 'Cómo trabajamos', P('Todo pasa por las vías oficiales de la plataforma: formularios de apelación, formularios de recuperación y herramientas de denuncia. La decisión siempre es de la plataforma. Por eso nunca prometemos un resultado.')),
       ('seguro', 'Cómo reconocer un servicio de fiar', UL('Nunca te piden la contraseña ni los códigos de acceso.', 'Te dan el precio antes de que empiece el trabajo.', 'Te explican qué vía oficial usan.', 'No presumen de un contacto en Meta.') + P('Más en <a href="@@scams@@">estafas al recuperar cuentas</a>.'))],
      [('¿Tiene Unbanz relación con Meta?', 'No. Unbanz es un servicio independiente y usa las mismas vías oficiales que tú.'),
       ('¿Unbanz es lo mismo que Unbanx?', 'No. Unbanz (con z) es el servicio de unbanz.com. Unbanx o unbanx.me es otra cosa.'),
       ('¿Pedís mi contraseña?', 'Nunca. Basta con un nombre de usuario y una captura.'),
       ('¿Dónde puedo ver opiniones?', 'En la página <a href="@@reviews@@">Opiniones</a> hay vídeos de clientes con transcripciones, en inglés.'),
       ('¿Y si no quedo satisfecho?', 'Escríbenos a team@unbanz.com. En las solicitudes de nombre de usuario, si no prosperan, se devuelve el 100 %; consulta la <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (en inglés).')],
      ['reviews', 'pricing', 'how', 'scams', 'contact'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='Independiente, sin pedir contraseña, con el precio por adelantado y solo por vías oficiales. Así puedes comprobar si Unbanz es fiable.')

    g('about', 'Sobre Unbanz: un servicio independiente', 'Quiénes somos', 'Sobre Unbanz.',
      'Unbanz (unbanz.com) es un servicio online independiente para Instagram, Facebook y Snapchat: ayuda con cuentas desactivadas, denuncia de cuentas falsas y de suplantación, solicitudes de nombre de usuario y cuentas publicitarias de Meta.',
      [('que', 'Qué hacemos', UL('<a href="@@ig@@">Recuperar cuentas</a> tras una desactivación, suspensión o hackeo.', '<a href="@@fake@@">Denunciar</a> cuentas falsas, de suplantación y de acoso con las herramientas oficiales.', '<a href="@@user@@">Solicitudes de nombre de usuario</a> por los procesos oficiales.', '<a href="@@ad@@">Cuentas publicitarias de Meta</a> y portfolios comerciales.')),
       ('como', 'Cómo trabajamos', P('Nos envías el nombre de usuario y el aviso. Te decimos con sinceridad si podemos ayudarte y te damos el precio antes de que empiece el trabajo. Todo pasa por las vías oficiales de la plataforma, que siempre decide. Lee <a href="@@how@@">cómo funciona</a>.')),
       ('nunca', 'Lo que nunca hacemos', P('Nunca pedimos tu contraseña ni tus códigos de acceso, no compramos ni vendemos cuentas y no usamos bots ni denuncias falsas.')),
       ('indep', 'Independientes', P('Unbanz no tiene afiliación con Meta ni con Snapchat. No somos Unbanx ni unbanx.me. Nos encuentras como @unbanzhq en Instagram y X. Para las solicitudes de nombre de usuario hay una <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (en inglés): si la solicitud no prospera, se devuelve el 100 %.')),
       ('idioma', 'Idioma', P('Trabajamos con clientes de España, Europa y otros países. La atención es principalmente en inglés.'))],
      [('¿Qué es Unbanz?', 'Un servicio online independiente para Instagram, Facebook y Snapchat: ayuda con cuentas desactivadas, denuncia de cuentas falsas, solicitudes de nombre de usuario y cuentas publicitarias.'),
       ('¿Tiene Unbanz relación con Meta?', 'No. Unbanz es independiente.'),
       ('¿Cómo contacto con vosotros?', 'Por WhatsApp o por correo a team@unbanz.com. Consulta <a href="@@contact@@">contacto</a>.')],
      ['how', 'legit', 'reviews', 'pricing', 'contact'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='Unbanz es un servicio online independiente para Instagram, Facebook y Snapchat. Lee qué hacemos, cómo trabajamos y lo que nunca hacemos.')

    # ================= guides =================
    g('ig-disabled', 'Cuenta de Instagram desactivada: cómo apelar', 'Cuenta de Instagram desactivada',
      'Cuenta de Instagram desactivada: cómo apelar.',
      'Si Instagram te indica que tu cuenta está desactivada, inicia sesión, abre el aviso y apela una sola vez por el formulario oficial. A menudo dispones de unos 180 días. Haz una captura del aviso antes de tocar nada.',
      [('pasos', 'Qué puedes hacer ahora', OL('Inicia sesión con la cuenta y abre el aviso. Haz una captura.', 'Elige la opción de apelar o de solicitar revisión, si aparece.', 'Sigue los pasos, por ejemplo con un vídeo selfie o un código, y envíalo una sola vez.', 'Revisa tu correo, incluida la carpeta de spam, por si llega la respuesta de Instagram.')),
       ('errores', 'Errores habituales', UL('Apelar varias veces seguidas.', 'Crear una cuenta nueva para esquivar la restricción.', 'Compartir tu contraseña con alguien que dice "solucionarlo todo".')),
       ('sin', '¿No hay botón o no hay respuesta?', P('Consulta <a href="@@no-button@@">Instagram sin botón de apelar</a> y <a href="@@appeal-denied@@">apelación rechazada</a>.'))],
      [('¿Mi cuenta de Instagram desactivada se ha perdido para siempre?', 'No necesariamente. Si el aviso muestra la opción de apelar, aún puedes hacerlo. El aviso indica el plazo que corresponde a tu cuenta.'),
       ('¿Cuántas veces puedo apelar?', 'Una vez basta; enviar la apelación repetidamente no ayuda y puede crear confusión.'),
       ('¿Necesito ayuda para apelar?', 'No necesariamente. Es gratis y puedes hacerlo tú. Nosotros ayudamos si se atasca.'),
       ('¿Cuánto tarda la respuesta?', 'Instagram no publica un plazo. Consulta <a href="@@appeal-time@@">cuánto tarda una apelación</a>.'),
       ('¿Pedís mi contraseña?', 'Nunca.')],
      ['ig', 'appeal-time', 'no-button', 'appeal-denied', 'deleted'], HELP_IG,
      desc='¿Cuenta de Instagram desactivada? Abre el aviso, apela una sola vez por el formulario oficial y guarda una captura. Así se hace, paso a paso.')

    g('ig-hacked', 'Cuenta de Instagram hackeada: cómo recuperarla', 'Cuenta de Instagram hackeada',
      'Cuenta de Instagram hackeada: ¿y ahora qué?',
      '¿Han hackeado tu cuenta de Instagram y han cambiado el correo o la contraseña? Usa primero la vía oficial de recuperación (instagram.com/hacked) y la verificación con vídeo selfie. No compartas tu contraseña ni tus códigos con nadie.',
      [('pasos', 'Qué hacer de inmediato', OL('Busca en tu correo un mensaje de Instagram sobre un cambio de correo o de teléfono y usa el enlace para revertirlo.', 'Entra en instagram.com/hacked y sigue los pasos.', 'Si te la ofrecen, elige la verificación con vídeo selfie.', 'Cuando recuperes la cuenta, pon una contraseña nueva y activa la verificación en dos pasos.')),
       ('estafa', 'Cuidado con las falsas recuperaciones', P('Quien te ofrece por mensaje privado "recuperar" tu cuenta y te pide la contraseña o un código no es de fiar. Consulta <a href="@@scams@@">estafas al recuperar cuentas</a>.')),
       ('atasco', '¿No lo consigues?', P('Si te han cambiado todos los datos y el enlace ya no funciona, podemos ver qué pasos oficiales siguen abiertos.'))],
      [('¿Puedo recuperar una cuenta de Instagram hackeada?', 'A menudo sí, con las herramientas oficiales. Depende de lo que hayan cambiado y de lo que aún puedas demostrar.'),
       ('¿Y si los hackers han cambiado mi correo?', 'Busca en tu correo anterior un mensaje de Instagram para revertir el cambio, o usa instagram.com/hacked.'),
       ('¿Qué es el vídeo selfie?', 'Un paso de verificación con el que Instagram comprueba que eres el titular. Sigue las indicaciones de la app.'),
       ('¿Tengo que dar mi contraseña para que la recuperen?', 'No. Nadie necesita tu contraseña.'),
       ('¿Cuánto cuesta la ayuda?', 'El precio lo conoces en la conversación, antes de que empiece el trabajo.')],
      ['ig', 'scams', 'no-button', 'ig-disabled'], HELP_IG,
      desc='¿Cuenta de Instagram hackeada y con el correo o la contraseña cambiados? Usa instagram.com/hacked y el vídeo selfie. Así se hace, paso a paso.')

    g('appeal-time', 'Cuánto tarda una apelación de Instagram', 'Cuánto tarda una apelación',
      '¿Cuánto tarda una apelación de Instagram?',
      'Instagram no publica un plazo fijo de respuesta. Puede llegar a los pocos días o pasadas varias semanas. No podemos prometer una fecha; lo que sí ayuda es enviar una apelación clara y tener paciencia.',
      [('espera', 'Qué esperar', P('No existe un plazo oficial. Hay quien recibe respuesta en pocos días y quien tarda semanas. La respuesta suele llegar por correo y dentro de la app.')),
       ('hacer', 'Qué puedes hacer mientras esperas', UL('Mira tu correo y la carpeta de spam.', 'No vuelvas a apelar una y otra vez.', 'No crees una cuenta nueva para esquivar la restricción.', 'Guarda tus capturas.')),
       ('despues', 'Si la respuesta es negativa', P('Consulta <a href="@@appeal-denied@@">apelación de Instagram rechazada</a>.'))],
      [('¿Cuánto tarda una apelación de Instagram?', 'Instagram no indica un plazo fijo. Varía de unos días a varias semanas.'),
       ('¿Se puede acelerar?', 'No con un botón oficial. Una apelación completa y clara es lo mejor.'),
       ('¿Puede Unbanz acelerarla?', 'No podemos prometer ninguna fecha. Te ayudamos a presentar la solicitud con claridad y te mantenemos informado.'),
       ('¿Debo volver a apelar?', 'Normalmente no. Enviarla repetidamente no ayuda.')],
      ['ig-disabled', 'appeal-denied', 'no-button', 'ig'], HELP_IG,
      desc='¿Cuánto tarda una apelación de Instagram? No hay un plazo fijo: de unos días a varias semanas. Esto es lo que puedes hacer mientras esperas.')

    g('appeal-denied', 'Apelación de Instagram rechazada: qué puedes hacer', 'Apelación rechazada',
      'Apelación de Instagram rechazada: ¿y ahora qué?',
      'Si te han rechazado la apelación por la desactivación de tu cuenta de Instagram, la cuenta no está perdida automáticamente. Lee bien el aviso, comprueba si queda alguna opción y guarda las pruebas; no todas las cuentas pueden volver.',
      [('leer', 'Lee bien el aviso', P('¿Hay un botón para volver a solicitar una revisión o un enlace a un formulario? Úsalo. Si solo aparece una decisión final, la vía interna suele estar cerrada.')),
       ('opciones', 'Lo que a veces sigue siendo posible', UL('Otra vía oficial, si el motivo lo permite (por ejemplo, una cuenta hackeada).', 'Si la desactivación te afecta desde la UE, un recurso ante un organismo independiente de resolución de litigios bajo la DSA. Consulta <a href="@@rights@@">el derecho a recurrir bajo la DSA</a>.')),
       ('no', 'Lo que no ayuda', UL('Crear una cuenta nueva para esquivar la restricción.', 'Pagar a alguien que dice tener "un contacto en Meta".'))],
      [('Me han rechazado la apelación. ¿Se acabó?', 'No siempre, pero la vía interna suele quedar cerrada. Mira qué opciones sigue mostrando el aviso.'),
       ('¿Puedo apelar de nuevo?', 'Solo si el aviso ofrece esa opción.'),
       ('¿Puedo acudir a un organismo independiente?', 'En la UE, la DSA permite a veces acudir a un organismo de resolución extrajudicial de litigios. Consulta <a href="@@rights@@">el derecho a recurrir bajo la DSA</a>.'),
       ('¿Puede Unbanz recuperar la cuenta?', 'Vemos con sinceridad qué es posible. La decisión es de la plataforma y no prometemos ningún resultado.')],
      ['rights', 'ig-disabled', 'no-button', 'ig'], HELP_IG,
      desc='¿Te han rechazado la apelación de tu cuenta de Instagram? Cómo leer el aviso, qué puede quedar posible y por qué una cuenta nueva no ayuda.')

    g('deleted', '¿Cuenta de Instagram eliminada o desactivada?', '¿Eliminada o desactivada?',
      '¿Tu cuenta de Instagram está eliminada o desactivada?',
      'Una cuenta desactivada se puede recuperar a veces con una apelación; una cuenta eliminada de forma permanente, por ti o por Instagram, normalmente no. El aviso al iniciar sesión te dice cuál de las dos es.',
      [('desactivada', 'Desactivada', P('Al iniciar sesión ves un aviso de que tu cuenta está desactivada. Si hay opción de apelar, puede que la recuperes. Consulta <a href="@@ig-disabled@@">cuenta de Instagram desactivada</a>.')),
       ('eliminada', 'Eliminada', P('Si eliminaste tú la cuenta, durante un tiempo se puede revertir; después ya no. Si la eliminó Instagram de forma permanente, volver es poco habitual.')),
       ('comprobar', 'Cómo comprobarlo', UL('Intenta iniciar sesión y lee el aviso.', 'Busca mensajes de Instagram en tu correo.', 'Abre la página del perfil en un navegador y mira si sigue existiendo.'))],
      [('¿Cómo sé si mi cuenta está desactivada?', 'Al iniciar sesión ves un aviso de que la cuenta está desactivada, a menudo con una opción para apelar.'),
       ('¿Puede volver una cuenta eliminada?', 'Solo dentro del periodo que indica Instagram, y normalmente no si se eliminó de forma permanente.'),
       ('¿Por qué no encuentro mi perfil?', 'Puede estar desactivado, eliminado o haberte bloqueado otra cuenta.'),
       ('¿Puede ayudar Unbanz?', 'Si la cuenta está desactivada, vemos con sinceridad qué es posible.')],
      ['ig-disabled', 'ig', 'appeal-denied'], HELP_IG,
      desc='¿Tu cuenta de Instagram está eliminada o desactivada? Así ves la diferencia y qué sigue siendo posible en cada situación.')

    g('no-button', 'Instagram no muestra el botón de apelar: ¿y ahora?', 'Sin botón de apelar',
      'Instagram no muestra el botón para apelar.',
      'Si falta el botón para apelar, a veces el plazo ha vencido, la cuenta está desactivada de forma permanente o el aviso es de otro tipo. Mira primero qué aviso ves.',
      [('motivos', 'Posibles motivos', UL('El plazo para apelar ha terminado.', 'Ya apelaste y la decisión es definitiva.', 'Es una restricción o una cuenta hackeada y no una desactivación.', 'Un fallo temporal de la app.')),
       ('probar', 'Qué puedes probar', UL('Inicia sesión desde un navegador en instagram.com en lugar de la app.', 'Prueba desde otro dispositivo y una red que uses habitualmente.', 'Actualiza la app.', 'Si la cuenta está hackeada, usa instagram.com/hacked.')),
       ('derechos', 'En la UE', P('Si la vía interna está cerrada, mira <a href="@@rights@@">el derecho a recurrir bajo la DSA</a>.'))],
      [('¿Por qué no veo el botón de apelar?', 'Normalmente porque el plazo ha vencido, la decisión es definitiva o se trata de otro tipo de aviso.'),
       ('¿Ayuda crear una cuenta nueva?', 'No, y puede empeorarlo, porque esquivar la restricción va contra las normas.'),
       ('¿Puede Unbanz hacer que aparezca el botón?', 'No. Sí podemos ver qué vía oficial sigue abierta.'),
       ('¿Y si la cuenta está hackeada?', 'Entonces hay una vía distinta: instagram.com/hacked.')],
      ['ig-disabled', 'appeal-denied', 'rights', 'ig-hacked'], HELP_IG,
      desc='¿Instagram no muestra el botón para apelar? Estos son los motivos más habituales y lo que todavía puedes probar.')

    g('blocked', 'Instagram: "Restringimos ciertas actividades"', 'Acción bloqueada',
      'Instagram: "Restringimos ciertas actividades".',
      'Este aviso significa que Instagram limita temporalmente algunas acciones, a menudo tras mucha actividad en poco tiempo. Normalmente no es una desactivación. Haz una pausa, deja de automatizar y, si hay botón, puedes pedir una revisión.',
      [('que', 'Qué significa el aviso', P('Instagram limita temporalmente acciones como dar me gusta, seguir o comentar. La cuenta sigue existiendo.')),
       ('hacer', 'Qué puedes hacer', UL('Haz una pausa de uno o dos días y usa la app con normalidad.', 'Deja de usar apps de terceros o automatizaciones.', 'Si aparece "Soy yo" o "Informar de un problema", úsalo una sola vez.', 'Mira si tienes algún aviso en tu correo.')),
       ('repite', '¿Se repite?', P('Comprueba si te han hackeado la cuenta, cambia la contraseña y activa la verificación en dos pasos.'))],
      [('¿Cuánto dura la restricción?', 'Instagram no indica un plazo fijo; varía de horas a días.'),
       ('¿Está desactivada mi cuenta?', 'No, este aviso es una restricción temporal.'),
       ('¿Puedo quitarla?', 'No directamente. Lo que más ayuda es hacer una pausa y no usar automatizaciones.'),
       ('¿Puede ayudar Unbanz?', 'Si la restricción se mantiene o pasa algo más, envíanos el aviso.')],
      ['ig-disabled', 'ig-hacked', 'ig'], HELP_IG,
      desc='¿Instagram dice que restringe ciertas actividades? Qué significa, cuánto dura y qué puedes hacer tú mismo.')

    g('ad-disabled', 'Cuenta publicitaria de Facebook desactivada: ¿y ahora?', 'Cuenta publicitaria desactivada',
      'Cuenta publicitaria de Facebook desactivada: ¿y ahora?',
      'Si tu cuenta publicitaria está desactivada, mira en Calidad de la cuenta qué motivo indica Meta y solicita una revisión por la vía oficial. No cambies los anuncios a ciegas ni crees una cuenta nueva para esquivarlo.',
      [('leer', 'Busca el motivo', P('En Meta Business Suite o en el Administrador de anuncios, abre la página Calidad de la cuenta. Allí suele aparecer el motivo y si se puede solicitar una revisión.')),
       ('hacer', 'Qué puedes hacer', OL('Haz capturas del aviso y de los anuncios rechazados.', 'Solicita una revisión si el botón está disponible.', 'Comprueba que tu método de pago y los datos de la empresa son correctos.', 'Espera la respuesta y no envíes la solicitud una y otra vez.')),
       ('no', 'Lo que no debes hacer', UL('Crear una cuenta publicitaria nueva para esquivar la restricción.', 'Dar acceso a tu cuenta a alguien que dice "solucionarlo todo".'))],
      [('¿Por qué está desactivada mi cuenta publicitaria?', 'El motivo suele aparecer en Calidad de la cuenta: por ejemplo, un incumplimiento de las políticas de anuncios o un problema de pago.'),
       ('¿Puedo solicitar una revisión?', 'Sí, si Meta muestra esa opción. Hazlo una sola vez, de forma clara y completa.'),
       ('¿Puedo crear una cuenta nueva sin más?', 'Suele quedar restringida también y va contra las normas si es para esquivar la restricción.'),
       ('¿Puede ayudar Unbanz?', 'Sí, vemos con sinceridad qué es posible. La decisión es de Meta.')],
      ['ad', 'fb-appeal', 'appeal-denied'], HELP_AD, svc='ad',
      desc='¿Cuenta publicitaria de Facebook desactivada? Busca el motivo en Calidad de la cuenta, solicita una revisión clara y evita los errores habituales.')

    g('fb-appeal', 'Cuenta de Facebook desactivada: cómo apelar', 'Facebook desactivada: apelar',
      'Cuenta de Facebook desactivada: cómo apelar.',
      'Si tu cuenta de Facebook está desactivada, inicia sesión, abre el aviso y solicita una revisión con el botón oficial. Hazlo una sola vez, dentro del plazo que muestre Facebook, y guarda una captura.',
      [('pasos', 'Pasos', OL('Inicia sesión y lee el aviso. Haz una captura.', 'Elige "Solicitar revisión" o el botón equivalente.', 'Si te lo piden, añade un documento de identidad en la página oficial.', 'Espera la respuesta por correo y en tus notificaciones.')),
       ('ojo', 'Ojo', UL('No envíes la solicitud varias veces.', 'Envía tu documento de identidad solo desde la página oficial de Facebook.', 'No pagues a nadie que te prometa un resultado seguro: nadie puede hacerlo.')),
       ('sin', '¿No hay botón?', P('Consulta <a href="@@appeal-denied@@">apelación rechazada</a> y <a href="@@rights@@">el derecho a recurrir bajo la DSA</a>.'))],
      [('¿Cómo apelo en Facebook?', 'Con el botón para solicitar revisión en el aviso que aparece al iniciar sesión.'),
       ('¿Tengo que enviar un documento de identidad?', 'A veces. Hazlo solo desde la página oficial de Facebook.'),
       ('¿Cuánto tarda?', 'Facebook no indica un plazo fijo.'),
       ('¿Puede ayudar Unbanz?', 'Sí, vemos con sinceridad qué es posible. La decisión es de Facebook.')],
      ['fb', 'fb-hacked', 'appeal-time', 'ad-disabled'], HELP_FB,
      desc='¿Cuenta de Facebook desactivada? Solicita una revisión una sola vez con el botón oficial y guarda una captura. Así se hace, paso a paso.')

    g('fb-hacked', 'Cuenta de Facebook hackeada: qué hacer', 'Cuenta de Facebook hackeada',
      'Cuenta de Facebook hackeada: ¿y ahora qué?',
      'Si te han hackeado la cuenta de Facebook, entra en facebook.com/hacked y sigue los pasos oficiales. Comprueba también si han cambiado tu correo y después cambia la contraseña. No compartas códigos con nadie.',
      [('pasos', 'Qué hacer de inmediato', OL('Entra en facebook.com/hacked y sigue los pasos.', 'Busca en tu correo un mensaje sobre un cambio de correo y usa el enlace para revertirlo.', 'Cambia la contraseña y cierra sesión en los demás dispositivos.', 'Activa la verificación en dos pasos y revisa las páginas y cuentas publicitarias vinculadas.')),
       ('ojo', 'Cuidado', P('Quien te ofrece una "recuperación" y te pide la contraseña o un código no es de fiar. Consulta <a href="@@scams@@">estafas al recuperar cuentas</a>.')),
       ('empresa', 'Cuenta de empresa', P('Si hay páginas o cuentas publicitarias vinculadas, comprueba también quién es administrador y qué ha cambiado.'))],
      [('¿Cómo recupero mi cuenta de Facebook hackeada?', 'Con facebook.com/hacked y los pasos oficiales de recuperación.'),
       ('¿Y si han cambiado el correo?', 'Usa el enlace del mensaje de Facebook que llegó a tu correo anterior para revertir el cambio.'),
       ('¿Corren peligro también mis páginas y cuentas publicitarias?', 'Es posible. Comprueba administradores y métodos de pago en cuanto vuelvas a entrar.'),
       ('¿Debo dar mi contraseña para que la recuperen?', 'Nunca.')],
      ['fb', 'fb-appeal', 'scams', 'ig-hacked'], HELP_FB,
      desc='¿Cuenta de Facebook hackeada? Usa facebook.com/hacked, revierte el cambio de correo y protege la cuenta con verificación en dos pasos.')

    g('inactive-user', 'Nombre de usuario de una cuenta inactiva de Instagram', 'Nombre de usuario inactivo',
      '¿Puedes reclamar el nombre de usuario de una cuenta inactiva de Instagram?',
      'No hay un botón para quedarse con el nombre de usuario de una cuenta inactiva. Instagram solo tiene procesos oficiales, como una denuncia por marca registrada o por suplantación, y decide por su cuenta.',
      [('reglas', 'Cómo funciona', P('Un nombre de usuario no se compra ni se transfiere. Si la cuenta está realmente inactiva, puede existir una vía oficial; que Instagram la acepte lo decide la plataforma.')),
       ('vias', 'Qué vías existen', UL('Una denuncia por marca registrada, si el nombre es tu marca registrada.', 'Una denuncia por suplantación, si alguien se hace pasar por ti.', 'La vía oficial de las cuentas inactivas, si procede.')),
       ('evitar', 'Lo que debes evitar', UL('Comprar nombres de usuario a quien los ofrece.', 'Quien dice tener "un contacto en Meta".'))],
      [('¿Puedo quedarme directamente con el nombre de usuario de una cuenta inactiva?', 'No. Solo existe un proceso oficial y decide Instagram.'),
       ('¿Puedo comprar un nombre de usuario?', 'No, y quien lo ofrece va contra las normas o es un estafador.'),
       ('¿Cuánto cuesta la ayuda con una solicitud de nombre de usuario?', 'El precio lo conoces en la conversación, antes de que empiece el trabajo.'),
       ('¿Qué pasa si la solicitud no prospera?', 'Se te devuelve el 100 % del importe. Consulta la <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (en inglés).')],
      ['user', 'pricing', 'scams'], P('Envíanos el nombre de usuario que quieres y tu perfil. Te decimos con sinceridad qué vía oficial corresponde y te indicamos el precio en la conversación, antes de que empiece el trabajo. Si una solicitud de nombre de usuario no prospera, se te devuelve el 100 % del importe. La atención es principalmente en inglés.'),
      svc='username', desc='¿Puedes reclamar el nombre de usuario de una cuenta inactiva de Instagram? No hay botón; solo procesos oficiales. Qué vías hay y qué significan.')

    g('report-fake', 'Denunciar cuenta falsa con mis fotos en Instagram', 'Cuenta falsa con mis fotos',
      'Cuenta falsa con tus fotos: cómo denunciarla.',
      'Si alguien usa tus fotos para una cuenta falsa, denúncialo como suplantación desde los tres puntos del perfil. Guarda antes capturas con el enlace y la fecha, y no pidas a tus amigos que denuncien en masa.',
      [('pasos', 'Cómo denunciarla', OL('Guarda capturas y el enlace del perfil.', 'Abre el perfil, toca los tres puntos y elige Denunciar.', 'Elige la opción de que se hace pasar por ti o por alguien que conoces.', 'Sigue los pasos y guarda la confirmación.')),
       ('extra', 'Pasos adicionales', UL('Avisa a tus seguidores de que la cuenta es falsa.', 'Si te han pedido dinero o te han amenazado, presenta una denuncia ante la Policía Nacional o la Guardia Civil.', 'Si hay imágenes íntimas robadas, consulta <a href="@@sextortion@@">sextorsión</a>.')),
       ('no', 'Lo que no funciona', P('Las denuncias masivas o falsas. Una denuncia clara es mejor y es lo que evalúa la plataforma.'))],
      [('¿Cómo denuncio una cuenta que usa mis fotos?', 'Con Denunciar en el perfil y la opción de suplantación.'),
       ('¿Debo pedir que denuncien muchas personas?', 'No. No funciona y va contra las normas.'),
       ('¿Puede Unbanz denunciarla?', 'Te ayudamos a preparar y presentar la denuncia con las herramientas oficiales. La decisión es de la plataforma.'),
       ('¿Debo presentar una denuncia policial?', 'Si hay estafa, amenazas o chantaje, conviene hacerlo.')],
      ['fake', 'imp', 'har', 'scams'], HELP_REP, svc='ban',
      desc='¿Alguien usa tus fotos para una cuenta falsa en Instagram? Cómo denunciarla como suplantación y qué pruebas debes guardar.')

    g('scams', 'Estafas al recuperar cuentas: cómo reconocerlas', 'Estafas al recuperar cuentas',
      'Estafas al recuperar cuentas: cómo reconocerlas.',
      'Nadie necesita tu contraseña ni un código de acceso para recuperar tu cuenta. Quien los pide, te promete un resultado seguro o dice tener un contacto en Meta es un estafador.',
      [('senales', 'Señales de alerta', UL('Te escriben ellos primero, normalmente por mensaje privado o en un comentario.', 'Te piden la contraseña, un código o acceso a tu correo.', 'Te prometen un resultado seguro o dicen tener un contacto en Meta.', 'Quieren cobrar con tarjetas regalo, criptomonedas o un enlace.')),
       ('hacer', 'Qué puedes hacer', UL('No respondas y bloquea la cuenta.', 'Denúncialo en la app.', 'Si ya has pagado o compartido datos, cambia tus contraseñas y avisa a tu banco.', 'Consulta la Oficina de Seguridad del Internauta (INCIBE, teléfono 017) y, si procede, presenta una denuncia ante la Policía Nacional o la Guardia Civil.')),
       ('otra', 'Cómo es una ayuda de fiar', P('Un servicio de fiar nunca pide tu contraseña, da el precio antes de que empiece el trabajo y explica qué vía oficial usa. Consulta <a href="@@legit@@">¿Es Unbanz fiable?</a>'))],
      [('¿Cómo reconozco una estafa de recuperación de cuentas?', 'Te escriben ellos primero, te piden la contraseña o un código y te prometen un resultado seguro.'),
       ('¿Y si ya he pagado?', 'Contacta con tu banco, cambia tus contraseñas y avisa a INCIBE (017) y a la Policía Nacional o la Guardia Civil.'),
       ('¿Alguien tiene de verdad un contacto en Meta?', 'No se puede comprobar y es una historia típica de estafa.'),
       ('¿Pedís mi contraseña?', 'Nunca.')],
      ['legit', 'ig-hacked', 'fake', 'pricing'], HELP_IG,
      desc='Nadie necesita tu contraseña para recuperar tu cuenta. Estas son las señales de alerta de las estafas al recuperar cuentas.')

    g('sextortion', 'Sextorsión en Instagram: qué hacer', 'Sextorsión',
      'Sextorsión en Instagram: qué hacer.',
      'Si en Instagram te chantajean con imágenes íntimas, no pagues y corta el contacto. Guarda las pruebas, bloquea y denuncia la cuenta y presenta una denuncia ante la Policía Nacional o la Guardia Civil. No estás solo y no has hecho nada malo.',
      [('directo', 'Qué hacer de inmediato', OL('No pagues y no envíes más imágenes.', 'Haz capturas de los mensajes, del perfil y del nombre de usuario; no borres nada.', 'Bloquea y denuncia la cuenta en la app.', 'Presenta una denuncia ante la Policía Nacional o la Guardia Civil (112 si hay peligro inmediato).')),
       ('ayuda', 'Ayuda en España', UL('El teléfono 017 de INCIBE ofrece ayuda gratuita y confidencial ante problemas de ciberseguridad.', 'El Canal Prioritario de la Agencia Española de Protección de Datos (AEPD) permite pedir la retirada urgente de imágenes íntimas difundidas sin consentimiento.', 'Si la víctima es menor, la Fundación ANAR atiende en el 900 20 20 10.')),
       ('imagenes', 'Retirar imágenes', P('Denuncia las imágenes difundidas a la plataforma. No envíes nunca dinero para evitar que se difundan: normalmente solo trae más exigencias.'))],
      [('¿Debo pagar?', 'No. Pagar normalmente no lo detiene y trae nuevas exigencias.'),
       ('¿Debo denunciar?', 'Sí, conviene hacerlo. Guarda antes las pruebas.'),
       ('¿Dónde encuentro ayuda?', 'En la Policía Nacional o la Guardia Civil, en el 017 de INCIBE y en el Canal Prioritario de la AEPD. Si hay peligro inmediato, llama al 112.'),
       ('¿Puede ayudar Unbanz?', 'Podemos ayudar a denunciar la cuenta con las herramientas oficiales. Presenta primero la denuncia y guarda las pruebas.')],
      ['har', 'fake', 'scams'], HELP_REP, svc='ban',
      desc='¿Te chantajean con imágenes íntimas en Instagram? No pagues, guarda las pruebas, bloquea y denuncia la cuenta y acude a la policía.')

    g('support', 'Cómo contactar con Instagram o Meta desde España', 'Contactar con Instagram o Meta',
      'Cómo contactar con Instagram o Meta desde España.',
      'Instagram y Meta no tienen un teléfono de atención para usuarios normales. Se llega a ellos por el Centro de ayuda, la opción de informar de un problema en la app y los formularios oficiales. Los números que circulan por internet son casi siempre falsos.',
      [('vias', 'Las vías oficiales', UL('El Centro de ayuda de Instagram y Facebook.', 'En la app: Configuración, Ayuda, Informar de un problema.', 'Formularios oficiales de apelación, hackeo y suplantación.', 'Solo para quien tiene Meta Verified: el soporte que incluye.')),
       ('falsos', 'Teléfonos de soporte falsos', P('Si buscas un teléfono de Instagram y encuentras uno, es casi seguro una estafa. Consulta <a href="@@scams@@">estafas al recuperar cuentas</a>.')),
       ('ue', 'Tus derechos en la UE', P('Si te han restringido o eliminado la cuenta, la DSA te da derecho a una explicación y a recurrir. Consulta <a href="@@rights@@">el derecho a recurrir</a>.'))],
      [('¿Cómo llamo a Instagram?', 'No es posible para usuarios normales. Usa el Centro de ayuda y la opción de informar de un problema en la app.'),
       ('¿Es real un teléfono de Instagram que encuentro en internet?', 'Casi siempre no. Ten cuidado.'),
       ('¿Tiene Meta una oficina en España?', 'La entidad europea de Meta está en Irlanda. Para los litigios, el camino son las vías oficiales online.'),
       ('¿Puede ayudar Unbanz si la vía oficial se atasca?', 'Sí, vemos con sinceridad qué es posible. No tenemos afiliación con Meta.')],
      ['rights', 'scams', 'ig-disabled', 'ig'], HELP_IG,
      desc='¿Cómo contactar con Instagram o Meta desde España? No hay teléfono, pero sí vías oficiales. Y cómo reconocer los teléfonos de soporte falsos.')

    g('rights', 'DSA: derecho a recurrir las decisiones de Meta en la UE', 'DSA: derecho a recurrir',
      'DSA: tu derecho a recurrir una decisión de Meta.',
      'Con el Reglamento de Servicios Digitales (DSA), en la UE recibes una explicación si te restringen o desactivan la cuenta, puedes recurrir internamente y después acudir a un organismo independiente de resolución de litigios. Su decisión no es vinculante, pero Meta debe colaborar de buena fe.',
      [('explicacion', 'Qué derechos tienes', UL('Una explicación motivada de la decisión.', 'Un sistema interno de reclamaciones (la apelación), gratuito.', 'Después, la posibilidad de pedir a un organismo independiente y certificado de resolución de litigios que examine la decisión.')),
       ('como', 'Cómo hacerlo', OL('Apela primero por la vía interna de Instagram o Facebook y guarda la decisión.', 'Busca un organismo certificado, como Appeals Centre Europe, y sigue su procedimiento de solicitud.', 'Adjunta el aviso, la fecha y tus argumentos.')),
       ('supervision', 'Supervisión en España', P('En España, el Coordinador de Servicios Digitales es la Comisión Nacional de los Mercados y la Competencia (CNMC). Puedes presentar allí una reclamación sobre la conducta de una plataforma.')),
       ('ojo', 'Importante', P('La decisión de ese organismo no es vinculante y no está asegurado un resultado. No somos abogados y esto no es asesoramiento jurídico.'))],
      [('¿Qué es el derecho a recurrir de la DSA?', 'El derecho a recibir una explicación ante una restricción, a recurrir internamente y después a acudir a un organismo independiente.'),
       ('¿La decisión del organismo vincula a Meta?', 'No, pero Meta debe colaborar de buena fe.'),
       ('¿Cuánto cuesta?', 'Estos organismos no pueden cobrar a los usuarios nada o solo una cantidad simbólica.'),
       ('¿Puede Unbanz hacerlo por mí?', 'Podemos ver qué vía corresponde y ayudarte a presentarla con claridad. No es asesoramiento jurídico.')],
      ['appeal-denied', 'no-button', 'support', 'ig'], HELP_IG,
      desc='¿Qué es el derecho a recurrir de la DSA frente a Meta? Apelación interna, resolución extrajudicial de litigios y el papel de la CNMC en España.')
