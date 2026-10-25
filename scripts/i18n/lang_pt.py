# -*- coding: utf-8 -*-
from lib import *
import core, pt_services, pt_guides

SLUGS = {
 'home': '', 'services': 'servicos', 'pricing': 'preco-recuperar-conta', 'faq': 'perguntas-frequentes', 'contact': 'contato',
 'reviews': 'avaliacoes', 'about': 'sobre-a-unbanz', 'how': 'como-funciona', 'legit': 'unbanz-e-confiavel',
 'ig': 'recuperar-conta-instagram', 'fb': 'recuperar-conta-facebook', 'ad': 'recuperar-conta-de-anuncios',
 'snap': 'recuperar-conta-snapchat', 'fake': 'denunciar-perfil-falso', 'imp': 'denunciar-personificacao',
 'har': 'denunciar-perfil-de-assedio', 'user': 'reivindicar-nome-de-usuario-instagram',
 'ig-disabled': 'conta-do-instagram-desativada', 'ig-hacked': 'conta-do-instagram-hackeada',
 'appeal-time': 'quanto-tempo-leva-a-contestacao-do-instagram', 'appeal-denied': 'contestacao-do-instagram-negada',
 'deleted': 'conta-do-instagram-excluida-ou-desativada', 'no-button': 'instagram-sem-botao-de-contestar',
 'blocked': 'instagram-restringimos-certas-atividades', 'ad-disabled': 'conta-de-anuncios-do-facebook-desativada',
 'fb-appeal': 'conta-do-facebook-desativada-contestar', 'fb-hacked': 'conta-do-facebook-hackeada',
 'inactive-user': 'nome-de-usuario-do-instagram-conta-inativa', 'report-fake': 'denunciar-perfil-falso-com-minhas-fotos',
 'scams': 'golpes-na-recuperacao-de-contas-alerta', 'sextortion': 'sextorsao-no-instagram-o-que-fazer',
 'support': 'falar-com-o-instagram-ou-a-meta-no-brasil', 'rights': 'onde-denunciar-golpes-e-crimes-online-no-brasil',
}

WA_DEFAULT = 'Ol%C3%A1%20Unbanz%2C%20preciso%20de%20ajuda%20com%20uma%20conta%20(PT)'

S = dict(
 code='pt-br', dir='pt-br', html_lang='pt-BR', og_locale='pt_BR', country='Brasil', js_code='pt', tag='(PT)',
 wa_default=WA_DEFAULT, mail_subj='Ajuda%20com%20minha%20conta',
 offer_desc='Você fica sabendo o preço na conversa, depois de explicar sua situação e antes de o trabalho começar. Perguntar não custa nada.',
 og_alt='Unbanz: ajuda com contas do Instagram, Facebook e Snapchat',
 skip='Ir para o conteúdo', nav_aria='Menu principal', mnav_aria='Menu para celular',
 n_home='Início', n_services='Serviços', n_user='Nomes de usuário', n_reviews='Avaliações', n_faq='Perguntas', n_contact='Contato', n_how='Como funciona',
 menu_open='Abrir menu', menu_close='Fechar menu',
 foot_links=[('services', 'Serviços'), ('ig', 'Instagram'), ('fb', 'Facebook'), ('snap', 'Snapchat'), ('ad', 'Contas de anúncios'),
             ('fake', 'Perfis falsos'), ('imp', 'Personificação'), ('har', 'Assédio'), ('user', 'Nomes de usuário'), ('pricing', 'Preço'),
             ('how', 'Como funciona'), ('faq', 'FAQ'), ('reviews', 'Avaliações'), ('legit', 'A Unbanz é confiável?'), ('contact', 'Contato')],
 foot_tag='Recuperar contas &amp; denunciar perfis.<br>Fale direto com a gente.',
 foot_indep='Serviço independente. Sem vínculo com a Meta.',
 mc_wa='Mande uma mensagem no WhatsApp', mc_mail='E-mail',
 cta_quote='Mande uma mensagem no WhatsApp', cta_mail='Mande um e-mail',
 hero_wa='Vamos conversar no WhatsApp', hero_mail='Prefere e-mail?',
 write_us='Fale com a gente', see_detail='Ver detalhes',
 faq_eyebrow='PERGUNTAS FREQUENTES', faq_eyebrow2='SUAS DÚVIDAS', faq_title='O que vale saber.',
 proof_title='Conte o que aconteceu.', related='Páginas relacionadas', related_services='Todos os serviços',
 crumb_guides='Guias', crumb_services='Serviços', help_h2='Quer ajuda?', guides_h2='Guias relacionados',
 std_howto=('<h2 id="com-a-unbanz">Como funciona com a Unbanz</h2><ol><li>Você nos envia seu nome de usuário e um print do aviso, pelo WhatsApp ou por e-mail.</li>'
            '<li>Dizemos com sinceridade se podemos ajudar. O preço você fica sabendo na conversa, depois de explicar sua situação e antes de o trabalho começar. Perguntar não custa nada.</li>'
            '<li>Preparamos o pedido e o enviamos pelo processo oficial da plataforma.</li>'
            '<li>Mantemos você informado até haver uma resposta.</li></ol>'
            '<p>O atendimento é principalmente em inglês; uma mensagem curta com seu nome de usuário, o print e a data já basta para começar.</p>'),
 std_safe=('<h2 id="cuidado">Fique atento</h2><p>Ninguém precisa da sua senha nem dos seus códigos de acesso para ajudar você. Nós também não. '
           'Se alguém oferece, por mensagem privada, "resolver tudo", pede que você entre por um link ou diz ter um contato na Meta, não siga em frente. '
           'A Unbanz nunca pede seus dados de acesso e não finge ter um acesso especial: usamos os mesmos caminhos oficiais que você.</p>'),
 std_about=('<h2 id="sobre-a-unbanz">Sobre a Unbanz</h2><p>A Unbanz (unbanz.com) é um serviço independente que ajuda pessoas, empresas e agências com pedidos para recuperar contas desativadas do Instagram, Facebook e Snapchat, '
            'com a denúncia de contas que violam as regras pelas ferramentas oficiais, com pedidos de nome de usuário e com a recuperação de contas de anúncios da Meta. '
            'A Unbanz não é a Unbanx nem unbanx.me e não tem vínculo com a Meta. Veja também <a href="@@legit@@">A Unbanz é confiável?</a></p>'),
 block3=[('Onde você estiver', 'Trabalhamos à distância, por WhatsApp ou e-mail, com clientes no Brasil, em Portugal e no resto do mundo. O atendimento é principalmente em inglês.'),
         ('Primeiro o preço', 'Você sabe o preço antes de o trabalho começar: informamos na conversa, depois de você explicar sua situação.'),
         ('Sua senha continua com você', 'Só precisamos do seu nome de usuário e do aviso. Sua senha e seus códigos ficam com você.')],
 price_h2='Saiba o preço<br>antes de começar.', price_p='Mande uma mensagem pelo WhatsApp ou por e-mail, conte a situação e dizemos quanto custa.',
 price_link='Como o preço é definido',
 vt_transcript='Transcrição (em inglês)', vt_play='Reproduzir vídeo',
 vt_titles=[('Client on claiming an inactive Instagram username with Unbanz', 'Reproduzir vídeo: cliente fala sobre reivindicar um nome de usuário inativo do Instagram', 'Cliente: avaliação em vídeo sobre um pedido de nome de usuário do Instagram', 'Username claim', 'Nome de usuário'),
            ('Management agency owner on working with Unbanz', 'Reproduzir vídeo: dono de agência fala sobre trabalhar com a Unbanz', 'Dono de agência: avaliação em vídeo sobre trabalhar com a Unbanz', 'Agency owner', 'Dono de agência'),
            ('Restricted Facebook ad account restored by Unbanz', 'Reproduzir vídeo: conta de anúncios do Facebook restrita e recuperada', 'Cliente: avaliação em vídeo sobre uma conta de anúncios restrita', 'Ad account', 'Conta de anúncios'),
            ('Client on getting an Instagram username held by an inactive account', 'Reproduzir vídeo: cliente fala sobre um nome de usuário do Instagram retido por uma conta inativa', 'Cliente: avaliação em vídeo sobre um nome de usuário do Instagram em uma conta inativa', 'Instagram username', 'Usuário do Instagram')],
 js_services="['unban', 'Recuperar minha conta'], ['ban', 'Denunciar uma conta'], ['username', 'Nome de usuário'], ['ad', 'Conta de anúncios'], ['other', 'Outra coisa']",
 js_eyebrow='FALE COM A GENTE', js_title='Com o que você precisa de ajuda?', js_legend_service='Serviço', js_legend_platform='Plataforma',
 js_reason_label='Motivo resumido <span>(opcional)</span>', js_placeholder='ex.: desativada depois de entrar num celular novo',
 js_continue='Continuar no WhatsApp', js_email='Prefiro e-mail', js_note='Nunca envie senhas nem códigos de acesso.', js_close='Fechar',
 js_mail_subject='Ajuda com minha conta',
 js_sentence=("""    const base = s === 'unban' ? `Quero recuperar minha conta do ${pl}`
      : s === 'ban' ? `Quero denunciar uma conta do ${pl}`
      : s === 'username' ? `Quero reivindicar um nome de usuário do ${pl}`
      : s === 'ad' ? (pl === 'Instagram' || pl === 'Facebook' ? `Preciso de ajuda com minha conta de anúncios da Meta (${pl})` : `Preciso de ajuda com uma conta de anúncios no ${pl}`)
      : `Preciso de ajuda com minha conta do ${pl}`;
    const reason = modal.querySelector('#cm-reason').value.replace(/\\s+/g, ' ').trim();
    return `Olá Unbanz, ${base}.` + (reason ? ` Motivo: ${reason}` : '') + ' %TAG%' + (window.unbanzViaTag ? ` ${window.unbanzViaTag}` : '');"""),
 llms=dict(
   header='## Português (Brasil)',
   intro='A Unbanz também atende em português do Brasil, para quem busca ajuda com uma conta do Instagram, Facebook ou Snapchat desativada, bloqueada ou hackeada. O atendimento é principalmente em inglês.',
   facts_label='### Fatos principais (português)',
   facts=('- A Unbanz é um serviço independente, sem vínculo com a Meta. Tudo passa pelos caminhos oficiais da plataforma; a decisão é sempre da plataforma.\n'
          '- O preço é informado na conversa, depois de a situação ser explicada e antes de o trabalho começar. Perguntar não custa nada.\n'
          '- A Unbanz nunca pede sua senha nem seus códigos de acesso.\n'
          '- Somente em pedidos de nome de usuário: se o pedido não der certo, o reembolso é de 100% (veja /refund-policy/).\n'
          '- Contato: WhatsApp +1 934 201 2490 ou team@unbanz.com.'),
   pages_label='### Páginas em português', qa_label='### Respostas curtas (português)',
   qa=[('Como recupero minha conta do Instagram se ela foi desativada?', 'Abra o aviso no app, conteste uma única vez pelo formulário oficial e guarde um print; se não funcionar, a Unbanz pode preparar e enviar o pedido por você.', 'ig-disabled'),
       ('Quanto custa recuperar uma conta?', 'O preço depende da conta e da situação. A Unbanz informa na conversa, antes de o trabalho começar; perguntar não custa nada.', 'pricing'),
       ('A Unbanz é confiável?', 'A Unbanz é um serviço independente, com um único site, um e-mail, termos por escrito e avaliações em vídeo de clientes; nunca pede sua senha.', 'legit')]),
)

C = {}
C['services'] = dict(
 title='Recuperar conta do Instagram, Facebook e Snapchat: serviços',
 desc='Ajuda com contas desativadas, bloqueadas ou hackeadas, com a denúncia de perfis falsos e de personificação e com pedidos de nome de usuário. Pelos caminhos oficiais.',
 nav='Serviços', h1='Serviços: recuperar contas e denunciar perfis.',
 lead='Instagram, Facebook, Snapchat e contas de anúncios da Meta. Envie seu nome de usuário e o aviso e dizemos com sinceridade se podemos ajudar. Tudo passa pelos caminhos oficiais da plataforma.',
 eyebrow='SUA SITUAÇÃO', h2='Com o que você precisa de ajuda?',
 rows=[('Recuperar conta do Instagram', 'Desativada, suspensa ou hackeada: contestação e recuperação pelos caminhos oficiais.', 'ig', 'unban'),
       ('Recuperar conta do Facebook', 'Perfis desativados ou hackeados e páginas restritas.', 'fb', 'unban'),
       ('Recuperar conta do Snapchat', 'Contas do Snapchat bloqueadas ou desativadas.', 'snap', 'unban'),
       ('Contas de anúncios', 'Contas de anúncios e portfólios empresariais da Meta restritos ou desativados.', 'ad', 'ad'),
       ('Denunciar perfis falsos', 'Denunciar perfis falsos pelas ferramentas oficiais da plataforma.', 'fake', 'ban'),
       ('Denunciar personificação', 'Alguém se passa por você ou pela sua empresa.', 'imp', 'ban'),
       ('Denunciar assédio', 'Contas que perseguem ou ameaçam você.', 'har', 'ban'),
       ('Reivindicar nome de usuário', 'Nomes de usuário inativos ou ocupados, pelos processos oficiais da plataforma.', 'user', 'username')],
 faq=[('Com quais plataformas vocês ajudam?', 'Instagram, Facebook, Snapchat e contas de anúncios da Meta.'),
      ('Como funciona?', 'Você envia o nome de usuário e um print do aviso. Dizemos com sinceridade se podemos ajudar e informamos o preço na conversa, antes de o trabalho começar.'),
      ('Posso fazer isso sozinho?', 'Pode. Contestar, o formulário de recuperação de contas hackeadas e a denúncia de uma conta são gratuitos e oficiais. Nós ajudamos se travar ou se você preferir delegar.'),
      ('A Unbanz tem vínculo com a Meta?', 'Não. A Unbanz é independente e usa os mesmos caminhos oficiais que você. A decisão é sempre da plataforma.')],
 related=['ig', 'fb', 'snap', 'ad', 'user', 'pricing', 'how', 'legit'])

FAQ_ALL = [
 ('Minha conta do Instagram foi desativada. O que posso fazer?', 'Entre na conta, abra o aviso e conteste uma única vez pelo formulário oficial; em geral há cerca de 180 dias para isso. Tire um print do aviso. Veja o guia <a href="@@ig-disabled@@">conta do Instagram desativada</a>.'),
 ('Hackearam minha conta e trocaram o e-mail. Ainda tem jeito?', 'Muitas vezes sim, pelas ferramentas oficiais do Instagram (instagram.com/hacked e a verificação por vídeo selfie). Veja <a href="@@ig-hacked@@">conta do Instagram hackeada</a>.'),
 ('Quanto custa recuperar uma conta?', 'O preço depende da conta e da situação. Informamos na conversa, depois de você contar o que aconteceu e antes de o trabalho começar. Perguntar não custa nada. Veja <a href="@@pricing@@">preço</a>.'),
 ('Quanto tempo leva?', 'A Meta e o Snapchat não publicam prazo de resposta. Pode chegar em poucos dias ou depois de várias semanas. Não prometemos data, mas mantemos você informado.'),
 ('Vocês precisam da minha senha?', 'Não, nunca. Basta um nome de usuário ou o link do perfil e um print do aviso. Não compartilhe sua senha nem seus códigos com ninguém.'),
 ('A Unbanz tem vínculo com a Meta?', 'Não. A Unbanz é um serviço independente. Usamos os caminhos oficiais da plataforma e a decisão é sempre da plataforma. Veja <a href="@@legit@@">A Unbanz é confiável?</a>'),
 ('Vocês também ajudam a denunciar perfis falsos?', 'Sim, ajudamos a denunciar perfis falsos, de personificação e de assédio pelas ferramentas oficiais de denúncia da plataforma. Veja <a href="@@fake@@">denunciar perfil falso</a>.'),
 ('Vocês podem reivindicar um nome de usuário para mim?', 'Ajudamos com pedidos de nome de usuário inativo ou ocupado pelos processos oficiais da plataforma, por exemplo uma denúncia de marca registrada ou de personificação. A decisão é da plataforma. Veja <a href="@@user@@">reivindicar nome de usuário</a>.'),
 ('E se um pedido de nome de usuário não der certo?', 'Você recebe 100% do valor de volta. Vale somente para pedidos de nome de usuário; veja a <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (em inglês).'),
 ('Como falo com vocês?', 'Pelo WhatsApp ou por e-mail para team@unbanz.com. O atendimento é principalmente em inglês; basta uma mensagem curta com seu nome de usuário, um print e a data. Veja <a href="@@contact@@">contato</a>.'),
 ('Posso recuperar minha conta de anúncios da Meta?', 'Ajudamos com contas de anúncios e portfólios empresariais restritos ou desativados pelos processos oficiais de análise da Meta. Veja <a href="@@ad@@">recuperar conta de anúncios</a>.'),
 ('É grátis tentar sozinho?', 'Sim. Contestar, o formulário de recuperação e as denúncias são gratuitos. Tente isso primeiro se o botão oficial estiver disponível.'),
]
C['faq'] = dict(
 title='Perguntas frequentes sobre recuperar uma conta',
 desc='Respostas para as dúvidas mais comuns sobre contas desativadas, hackeadas e bloqueadas, preço, senha e os caminhos oficiais.',
 nav='Perguntas frequentes', crumb='Perguntas', h1='Perguntas frequentes.',
 lead='Respostas curtas e sinceras sobre contas do Instagram, Facebook e Snapchat, como trabalhamos e o que você pode fazer de graça.',
 items=FAQ_ALL, faq_h2='O que vale saber.', related=['ig', 'fb', 'user', 'pricing', 'how', 'legit', 'contact'])

C['contact'] = dict(
 title='Contato: ajuda com sua conta do Instagram ou Facebook',
 desc='Fale com a gente pelo WhatsApp ou por e-mail. Envie seu nome de usuário e um print do aviso; o atendimento é principalmente em inglês.',
 nav='Contato', eyebrow='CONTATO', h1='Conte o que aconteceu.',
 p1='Escolha o que você precisa e abrimos o WhatsApp com uma mensagem já pronta. Você pode editá-la antes de enviar.',
 opts=[('Recuperar conta do Instagram', 'Olá Unbanz, quero recuperar minha conta do Instagram.', 'unban'),
       ('Recuperar conta do Facebook', 'Olá Unbanz, quero recuperar minha conta do Facebook.', 'unban'),
       ('Recuperar conta do Snapchat', 'Olá Unbanz, quero recuperar minha conta do Snapchat.', 'unban'),
       ('Denunciar uma conta', 'Olá Unbanz, quero denunciar uma conta.', 'ban'),
       ('Reivindicar nome de usuário', 'Olá Unbanz, quero reivindicar um nome de usuário.', 'username'),
       ('Conta de anúncios', 'Olá Unbanz, preciso de ajuda com uma conta de anúncios da Meta.', 'ad')],
 mail_h2='Prefere e-mail?', mail_p='Escreva para team@unbanz.com e informe seu nome de usuário ou o link do perfil, um print do aviso e a data em que aconteceu.',
 what_h2='O que você pode enviar', what_p='Seu @usuário ou o link do perfil, um print do aviso e a data. Em conta de anúncios, também o ID da conta. Nunca envie senha nem código de acesso.',
 social_h2='Também em', social_p='Somos @unbanzhq no Instagram e no X. Para dados de contas, prefira o WhatsApp ou o e-mail.',
 lang_h2='Idioma', lang_p='O atendimento é principalmente em inglês. Uma mensagem curta com nome de usuário, print e data basta para começar.',
 note='Serviço independente. Sem vínculo com a Meta. Nunca pedimos sua senha.')

C['reviews'] = dict(
 title='Avaliações: vídeos de clientes da Unbanz',
 desc='Veja vídeos de clientes que trabalharam com a Unbanz: um pedido de nome de usuário, uma agência e uma conta de anúncios restrita. Vídeos e transcrições em inglês.',
 nav='Avaliações', h1='Clientes com suas palavras.',
 p='Quatro clientes contam, com as próprias palavras, como foi trabalhar com a Unbanz. Os vídeos e as transcrições estão em inglês.',
 video_aria='Avaliações em vídeo de clientes', mail='Ou mande um e-mail', pick='Sobre o quê?',
 pick_opts=[('Recuperar uma conta', 'Olá Unbanz, quero recuperar minha conta.', 'unban'), ('Nome de usuário', 'Olá Unbanz, quero reivindicar um nome de usuário.', 'username'), ('Conta de anúncios', 'Olá Unbanz, preciso de ajuda com uma conta de anúncios.', 'ad')],
 q_h2='Perguntas sobre estas avaliações.',
 faq=[('De onde vêm estas avaliações?', 'São vídeos de clientes que trabalharam com a Unbanz. Você pode assistir aqui mesmo e ler a transcrição.'),
      ('Em que idioma estão os vídeos?', 'Em inglês. Abaixo de cada vídeo está a transcrição, também em inglês.'),
      ('Posso fazer uma pergunta antes de decidir?', 'Pode. Mande uma mensagem pelo WhatsApp ou por e-mail. Perguntar não custa nada.')])

C['home'] = dict(
 title='Recuperar conta do Instagram: ajuda com contas bloqueadas',
 desc='Conta do Instagram ou Facebook desativada, suspensa ou hackeada? Envie seu nome de usuário e o aviso: preparamos o pedido pelos caminhos oficiais.',
 skip='Ir para os serviços', home_aria='Unbanz, voltar ao topo',
 h1a='Recuperar conta', h1b='do Instagram.',
 hero_p='Desativada, suspensa ou hackeada? Envie seu nome de usuário e o aviso: preparamos o pedido pelos caminhos oficiais do Instagram, Facebook e Snapchat.',
 intro_eyebrow='CONTAS &amp; DENÚNCIAS', intro_h2='Conta bloqueada? Envie os detalhes.',
 intro_p=('A Unbanz (unbanz.com) é um serviço independente para Instagram, Facebook e Snapchat: contestação e nova análise de contas desativadas ou bloqueadas, denúncia de perfis falsos pelas ferramentas oficiais, '
          'pedidos de nome de usuário e ajuda com contas de anúncios da Meta. Você envia o nome de usuário e um print do aviso e dizemos com sinceridade se podemos ajudar. '
          'Serviço independente, sem vínculo com a Meta e sem relação com a Unbanx. Prefere começar sozinho? Leia antes o guia <a href="@@appeal-denied@@">contestação do Instagram negada</a>.'),
 exp_eyebrow='SUA SITUAÇÃO', exp_h2='Com o que você precisa de ajuda?',
 rows=[('Recuperar conta do Instagram', 'Desativada, suspensa ou hackeada.', 'ig', 'unban'),
       ('Conta do Facebook', 'Perfis desativados ou hackeados, páginas restritas.', 'fb', 'unban'),
       ('Perfis falsos e personificação', 'Denúncia pelas ferramentas oficiais.', 'fake', 'ban'),
       ('Nomes de usuário', 'Nomes de usuário inativos ou ocupados.', 'user', 'username'),
       ('Contas de anúncios', 'Contas de anúncios e portfólios empresariais restritos.', 'ad', 'ad')],
 vt_eyebrow='CLIENTES', vt_h2='Com as próprias palavras.', vt_note='Vídeos e transcrições em inglês.', vt_all='Todas as avaliações',
 pw_eyebrow='SUA SENHA', pw_zero='senhas pedidas', pw_note='Um nome de usuário e um print bastam. Mantemos você informado o tempo todo.',
 how_eyebrow='COMO FUNCIONA', how_h2='Envie os detalhes. A gente cuida do resto.',
 steps=['Envie seu nome de usuário e o aviso.', 'Saiba o preço antes de o trabalho começar.', 'Enviamos o pedido pelo processo oficial.'], how_link='Como funciona',
 pr_eyebrow='PREÇO', pr_h2='O preço, antes de começar.',
 pr_p='O preço depende da conta, da situação e do trabalho necessário. Informamos na conversa, depois de você contar o que aconteceu. Perguntar não custa nada.',
 pr_cta='Peça um preço',
 pr_notes=[('Primeiro o preço', 'Você sabe antes de o trabalho começar.'), ('Caminhos oficiais', 'Contestações e denúncias, sem atalhos.'), ('Sem senha', 'Sua senha fica com você.')],
 pr_link='O preço e do que ele depende',
 faq_eyebrow='RESPOSTAS CURTAS', faq_h2='Antes de falar com a gente.',
 faq=[('Minha conta do Instagram foi desativada. E agora?', 'Entre na conta, abra o aviso e conteste uma única vez; em geral há cerca de 180 dias. Tire um print. Veja o <a href="@@ig-disabled@@">guia</a>.'),
      ('A Unbanz é confiável?', 'A Unbanz é um serviço independente: um único site, um e-mail, termos por escrito e avaliações em vídeo de clientes. Nunca pedimos sua senha. Veja <a href="@@legit@@">A Unbanz é confiável?</a>'),
      ('Quanto custa?', 'Depende da conta e da situação. Você sabe o preço na conversa, antes de o trabalho começar. Perguntar não custa nada.'),
      ('Vocês precisam da minha senha?', 'Não. Basta um nome de usuário e um print do aviso.'),
      ('Vocês atendem em português?', 'O atendimento é principalmente em inglês. Uma mensagem curta com seu nome de usuário, o print e a data basta para começar.'),
      ('Posso reivindicar um nome de usuário inativo?', 'Às vezes sim, pelos processos oficiais da plataforma. A decisão é da plataforma. Se um pedido de nome de usuário não der certo, você recebe 100% do valor de volta. Veja <a href="@@user@@">reivindicar nome de usuário</a>.')],
 cl_eyebrow='CONTATO', cl_h2='Conte o que aconteceu.',
 cl_p='O atendimento é principalmente em inglês. Seu nome de usuário, um print e a data bastam para começar.')

def make():
    site = Site(S, SLUGS)
    core.home_page(site, C); core.services_page(site, C); core.faq_page(site, C); core.contact_page(site, C); core.reviews_page(site, C)
    pt_services.add(site); pt_guides.add(site)
    return site
