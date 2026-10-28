# -*- coding: utf-8 -*-
from lib import *

def P(*t):
    return ''.join('<p>%s</p>' % x for x in t)
def UL(*t):
    return '<ul>' + ''.join('<li>%s</li>' % x for x in t) + '</ul>'
def OL(*t):
    return '<ol>' + ''.join('<li>%s</li>' % x for x in t) + '</ol>'

HELP_IG = P('O botão oficial não funciona ou você prefere que a gente ajude? Envie seu nome de usuário, um print do aviso e a data. Dizemos com sinceridade se podemos ajudar e informamos o preço na conversa, antes de o trabalho começar. Perguntar não custa nada. O atendimento é principalmente em inglês.')
HELP_FB = P('Envie o link do perfil, um print do aviso e a data. Dizemos com sinceridade se podemos ajudar e informamos o preço na conversa, antes de o trabalho começar. O atendimento é principalmente em inglês.')
HELP_AD = P('Envie o ID da conta, um print do aviso e a data. Dizemos com sinceridade se podemos ajudar e informamos o preço na conversa, antes de o trabalho começar. O atendimento é principalmente em inglês.')
HELP_REP = P('Envie os links das contas e os prints. Ajudamos a preparar e apresentar uma denúncia clara pelas ferramentas oficiais; a decisão é da plataforma. O preço você fica sabendo na conversa, antes de o trabalho começar. O atendimento é principalmente em inglês.')

def add(site):
    g = site.guide
    S = site.S

    # ================= core trust pages =================
    site.reg('pricing', 'guide', 'Preço: quanto custa recuperar uma conta?',
             'Quanto custa a ajuda com uma conta do Instagram ou Facebook? O preço depende da conta e da situação e você fica sabendo na conversa, antes de o trabalho começar.', 'Preço')
    site.build['pricing'] = lambda: site.guide_page('pricing',
        'Quanto custa recuperar uma conta do Instagram ou Facebook?',
        'O preço depende da conta, da plataforma e do trabalho necessário. Na Unbanz você fica sabendo na conversa, depois de explicar sua situação e antes de o trabalho começar; perguntar não custa nada. A Meta não publica prazos de resposta e não podemos prometer nenhum.',
        [('preco', 'Do que o preço depende', UL('A plataforma: Instagram, Facebook, Snapchat ou uma conta de anúncios da Meta.',
                                                'O tipo de situação: desativada, suspensa, hackeada, denunciar uma conta falsa ou um pedido de nome de usuário.',
                                                'O número de contas ou de denúncias.',
                                                'O trabalho necessário: provas, verificações e acompanhamento.') + P('Um preço dado sem conhecer sua situação não vale nada. Por isso primeiro perguntamos o que aconteceu.')),
         ('precisamos', 'O que precisamos para responder', P('Seu nome de usuário ou o link do perfil, um print do aviso e a data. Em conta de anúncios, o ID da conta. Nunca uma senha nem um código.')),
         ('gratis', 'Os passos oficiais são gratuitos', P('Contestar uma desativação, o formulário de recuperação de contas hackeadas e a denúncia de uma conta não custam nada: são passos oficiais que você mesmo pode dar. Ajudamos se travar, se o aviso não estiver claro ou se você preferir delegar. Leia antes o guia <a href="@@appeal-denied@@">contestação negada</a>.')),
         ('refund', 'Nome de usuário: refund policy', P('Se um pedido de nome de usuário não der certo, você recebe 100% do valor de volta. Vale somente para pedidos de nome de usuário. Veja a <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (em inglês).')),
         ('prazo', 'E quanto tempo leva?', P('A Meta e o Snapchat não publicam prazo de resposta. Dependendo da situação, pode chegar em poucos dias ou depois de várias semanas. Não prometemos data, mas mantemos você informado. Veja <a href="@@appeal-time@@">quanto tempo leva a contestação do Instagram</a>.')),
         ('alertas', 'Sinais de alerta nos preços', UL('Passam um valor sem perguntar nada sobre sua situação.', 'Um serviço que chama você primeiro.', 'Pedem sua senha, um código ou acesso ao seu e-mail.', 'Prometem um resultado certo.') + P('Veja também <a href="@@scams@@">golpes na recuperação de contas</a>.'))],
        [('Quanto custa a ajuda com uma conta do Instagram?', 'Depende da conta e da situação. Informamos o preço na conversa, depois de você contar o que aconteceu e antes de o trabalho começar.'),
         ('Custa algo pedir um orçamento?', 'Não. Perguntar não custa nada e não obriga a nada.'),
         ('Quanto tempo leva para recuperar uma conta?', 'A Meta não publica prazo. Varia de alguns dias a várias semanas. Não podemos prometer uma data.'),
         ('Posso fazer de graça por conta própria?', 'Sim, os passos oficiais (contestação, formulário de recuperação, denúncia) são gratuitos. Nossa ajuda é para quem prefere delegar ou travou.'),
         ('Preciso enviar minha senha para receber um preço?', 'Não. Basta um nome de usuário e um print. Nunca compartilhe sua senha nem seus códigos.'),
         ('E se meu pedido de nome de usuário não der certo?', 'Você recebe 100% do valor de volta. Vale somente para pedidos de nome de usuário; veja a <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (em inglês).')],
        ['ig', 'fb', 'user', 'appeal-time', 'how', 'legit'], HELP_IG, crumb_label=S['crumb_services'], std=False)

    g('how', 'Como funciona: recuperar uma conta com a Unbanz', 'Como funciona', 'Como funciona.',
      'Você envia seu nome de usuário e um print do aviso. Dizemos com sinceridade se podemos ajudar, informamos o preço antes de o trabalho começar e enviamos o pedido pelo processo oficial da plataforma.',
      [('passos', 'Os passos', OL('Envie seu nome de usuário ou o link do perfil, um print do aviso e a data, pelo WhatsApp ou por e-mail.',
                                 'Vemos sua situação e dizemos com sinceridade se podemos ajudar. O preço você fica sabendo na conversa, antes de o trabalho começar.',
                                 'Se você aceitar, preparamos o pedido e o enviamos pelo processo oficial: uma contestação se a conta foi desativada, o formulário de recuperação se foi hackeada, as ferramentas de denúncia se é um perfil falso.',
                                 'Mantemos você informado sobre as respostas. A decisão é sempre da plataforma.')),
       ('vias', 'Os caminhos oficiais que usamos', P('As contestações seguem os processos oficiais de recurso e análise. Perfis falsos, de personificação ou de golpistas são denunciados pelas ferramentas de denúncia da própria plataforma. Os pedidos de nome de usuário usam o caminho oficial que se aplica: uma denúncia de marca registrada, uma denúncia de personificação ou o caminho de uma conta inativa.')),
       ('nunca', 'O que nunca fazemos', UL('Nunca pedimos sua senha nem seus códigos de acesso.', 'Nunca compramos, vendemos nem transferimos contas.', 'Não usamos bots, ferramentas de captura de nomes nem denúncias falsas.', 'Não fingimos ser ninguém da Meta.')),
       ('idioma', 'Idioma e contato', P('O atendimento é principalmente em inglês. Uma mensagem curta com seu nome de usuário, o print e a data basta para começar.'))],
      [('Como começo?', 'Escreva para a gente pelo WhatsApp ou por e-mail com seu nome de usuário, um print do aviso e a data.'),
       ('Quando fico sabendo o preço?', 'Na conversa, depois de explicar sua situação e antes de o trabalho começar.'),
       ('Preciso passar uma senha?', 'Não. Nunca pedimos.'),
       ('Vocês decidem se minha conta volta?', 'Não. A decisão é sempre da plataforma. Nós preparamos e enviamos o pedido.'),
       ('Vocês atendem em português?', 'O atendimento é principalmente em inglês. Uma mensagem curta basta para começar.')],
      ['ig', 'fb', 'user', 'pricing', 'legit', 'faq'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='Veja como a Unbanz funciona: você envia seu nome de usuário e o aviso, sabe o preço antes de começar e enviamos o pedido pelos caminhos oficiais.')

    g('legit', 'A Unbanz é confiável? O que você precisa saber', 'A Unbanz é confiável?', 'A Unbanz é confiável?',
      'A Unbanz é um serviço independente com um único site, um e-mail, termos por escrito e avaliações em vídeo de clientes. Nunca pedimos sua senha, informamos o preço antes de o trabalho começar e só usamos os caminhos oficiais da plataforma.',
      [('fatos', 'Fatos que você mesmo pode conferir', UL('Um único site (unbanz.com), um e-mail (team@unbanz.com) e um número de WhatsApp.', '<a href="/terms/" hreflang="en" lang="en">Termos</a> por escrito e uma <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a>.', 'Avaliações em vídeo de clientes, com transcrição, na página <a href="@@reviews@@">Avaliações</a>.', 'Pedir um preço não custa nada.')),
       ('nao', 'O que a Unbanz não é', P('A Unbanz não tem vínculo com a Meta nem com o Snapchat e não tem acesso especial aos funcionários deles. A Unbanz também não é a Unbanx nem unbanx.me; avaliações da Unbanx não falam de nós.')),
       ('vias', 'Como trabalhamos', P('Tudo passa pelos caminhos oficiais da plataforma: formulários de contestação, formulários de recuperação e ferramentas de denúncia. A decisão é sempre da plataforma. Por isso nunca prometemos um resultado.')),
       ('seguro', 'Como reconhecer um serviço confiável', UL('Nunca pedem sua senha nem seus códigos de acesso.', 'Informam o preço antes de o trabalho começar.', 'Explicam qual caminho oficial usam.', 'Não se gabam de ter um contato na Meta.') + P('Mais em <a href="@@scams@@">golpes na recuperação de contas</a>.'))],
      [('A Unbanz tem vínculo com a Meta?', 'Não. A Unbanz é um serviço independente e usa os mesmos caminhos oficiais que você.'),
       ('A Unbanz é a mesma coisa que a Unbanx?', 'Não. Unbanz (com z) é o serviço do unbanz.com. Unbanx ou unbanx.me é outra coisa.'),
       ('Vocês pedem minha senha?', 'Nunca. Basta um nome de usuário e um print.'),
       ('Onde posso ver avaliações?', 'Na página <a href="@@reviews@@">Avaliações</a> há vídeos de clientes com transcrições, em inglês.'),
       ('E se eu não ficar satisfeito?', 'Escreva para team@unbanz.com. Nos pedidos de nome de usuário, se não derem certo, o reembolso é de 100%; veja a <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (em inglês).')],
      ['reviews', 'pricing', 'how', 'scams', 'contact'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='Independente, sem pedir senha, com o preço antes de começar e só por caminhos oficiais. Veja como conferir se a Unbanz é confiável.')

    g('about', 'Sobre a Unbanz: um serviço independente', 'Sobre a Unbanz', 'Sobre a Unbanz.',
      'A Unbanz (unbanz.com) é um serviço online independente para Instagram, Facebook e Snapchat: ajuda com contas desativadas, denúncia de perfis falsos e de personificação, pedidos de nome de usuário e contas de anúncios da Meta.',
      [('que', 'O que fazemos', UL('<a href="@@ig@@">Recuperar contas</a> depois de uma desativação, suspensão ou invasão.', '<a href="@@fake@@">Denunciar</a> perfis falsos, de personificação e de assédio pelas ferramentas oficiais.', '<a href="@@user@@">Pedidos de nome de usuário</a> pelos processos oficiais.', '<a href="@@ad@@">Contas de anúncios da Meta</a> e portfólios empresariais.')),
       ('como', 'Como trabalhamos', P('Você envia o nome de usuário e o aviso. Dizemos com sinceridade se podemos ajudar e informamos o preço antes de o trabalho começar. Tudo passa pelos caminhos oficiais da plataforma, que sempre decide. Leia <a href="@@how@@">como funciona</a>.')),
       ('nunca', 'O que nunca fazemos', P('Nunca pedimos sua senha nem seus códigos de acesso, não compramos nem vendemos contas e não usamos bots nem denúncias falsas.')),
       ('indep', 'Independentes', P('A Unbanz não tem vínculo com a Meta nem com o Snapchat. Não somos a Unbanx nem unbanx.me. Para pedidos de nome de usuário há uma <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (em inglês): se o pedido não der certo, o reembolso é de 100%.')),
       ('idioma', 'Idioma', P('Atendemos clientes do Brasil, de Portugal e de outros países. O atendimento é principalmente em inglês.'))],
      [('O que é a Unbanz?', 'Um serviço online independente para Instagram, Facebook e Snapchat: ajuda com contas desativadas, denúncia de perfis falsos, pedidos de nome de usuário e contas de anúncios.'),
       ('A Unbanz tem vínculo com a Meta?', 'Não. A Unbanz é independente.'),
       ('Como falo com vocês?', 'Pelo WhatsApp ou por e-mail para team@unbanz.com. Veja <a href="@@contact@@">contato</a>.')],
      ['how', 'legit', 'reviews', 'pricing', 'contact'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='A Unbanz é um serviço online independente para Instagram, Facebook e Snapchat. Veja o que fazemos, como trabalhamos e o que nunca fazemos.')

    # ================= guides =================
    g('ig-disabled', 'Conta do Instagram desativada: como contestar', 'Conta do Instagram desativada',
      'Conta do Instagram desativada: como contestar.',
      'Se o Instagram diz que sua conta foi desativada, entre na conta, abra o aviso e conteste uma única vez pelo formulário oficial. Muitas vezes você tem cerca de 180 dias. Tire um print do aviso antes de mexer em qualquer coisa.',
      [('passos', 'O que você pode fazer agora', OL('Entre na conta e abra o aviso. Tire um print.', 'Escolha a opção de contestar ou de pedir análise, se aparecer.', 'Siga os passos, por exemplo com um vídeo selfie ou um código, e envie uma única vez.', 'Confira seu e-mail, inclusive a caixa de spam, para ver se chegou a resposta do Instagram.')),
       ('erros', 'Erros comuns', UL('Contestar várias vezes seguidas.', 'Criar uma conta nova para driblar a restrição.', 'Passar sua senha para alguém que diz "resolver tudo".')),
       ('sem', 'Sem botão ou sem resposta?', P('Veja <a href="@@no-button@@">Instagram sem botão de contestar</a> e <a href="@@appeal-denied@@">contestação negada</a>.'))],
      [('Minha conta do Instagram desativada está perdida para sempre?', 'Não necessariamente. Se o aviso mostra a opção de contestar, você ainda pode fazer isso. O aviso indica o prazo da sua conta.'),
       ('Quantas vezes posso contestar?', 'Uma vez basta; enviar repetidamente não ajuda e pode causar confusão.'),
       ('Preciso de ajuda para contestar?', 'Não necessariamente. É gratuito e você mesmo pode fazer. Ajudamos se travar.'),
       ('Quanto tempo leva a resposta?', 'O Instagram não publica prazo. Veja <a href="@@appeal-time@@">quanto tempo leva uma contestação</a>.'),
       ('Vocês pedem minha senha?', 'Nunca.')],
      ['ig', 'appeal-time', 'no-button', 'appeal-denied', 'deleted'], HELP_IG,
      desc='Conta do Instagram desativada? Abra o aviso, conteste uma única vez pelo formulário oficial e guarde um print. Veja o passo a passo.')

    g('ig-hacked', 'Conta do Instagram hackeada: como recuperar', 'Conta do Instagram hackeada',
      'Conta do Instagram hackeada: e agora?',
      'Hackearam sua conta do Instagram e trocaram o e-mail ou a senha? Use primeiro o caminho oficial de recuperação (instagram.com/hacked) e a verificação por vídeo selfie. Não compartilhe sua senha nem seus códigos com ninguém.',
      [('passos', 'O que fazer de imediato', OL('Procure no seu e-mail uma mensagem do Instagram sobre troca de e-mail ou telefone e use o link para desfazer a mudança.', 'Acesse instagram.com/hacked e siga os passos.', 'Se for oferecida, escolha a verificação por vídeo selfie.', 'Quando recuperar a conta, defina uma senha nova e ative a verificação em duas etapas.')),
       ('golpe', 'Cuidado com falsas recuperações', P('Quem oferece, por mensagem privada, "recuperar" sua conta e pede a senha ou um código não é confiável. Veja <a href="@@scams@@">golpes na recuperação de contas</a>. Se perdeu dinheiro, veja <a href="@@rights@@">onde denunciar golpes e crimes online no Brasil</a>.')),
       ('travou', 'Não está conseguindo?', P('Se trocaram todos os dados e o link não funciona mais, podemos ver quais passos oficiais ainda estão abertos.'))],
      [('Dá para recuperar uma conta do Instagram hackeada?', 'Muitas vezes sim, pelas ferramentas oficiais. Depende do que mudaram e do que você ainda consegue comprovar.'),
       ('E se os hackers trocaram meu e-mail?', 'Procure no e-mail antigo uma mensagem do Instagram para desfazer a troca, ou use instagram.com/hacked.'),
       ('O que é o vídeo selfie?', 'Uma etapa de verificação em que o Instagram confere que você é o titular. Siga as instruções do app.'),
       ('Preciso passar minha senha para recuperarem?', 'Não. Ninguém precisa da sua senha.'),
       ('Quanto custa a ajuda?', 'O preço você fica sabendo na conversa, antes de o trabalho começar.')],
      ['ig', 'scams', 'no-button', 'ig-disabled'], HELP_IG,
      desc='Conta do Instagram hackeada, com e-mail ou senha trocados? Use instagram.com/hacked e o vídeo selfie. Veja o passo a passo.')

    g('appeal-time', 'Quanto tempo leva a contestação do Instagram', 'Quanto tempo leva a contestação',
      'Quanto tempo leva a contestação do Instagram?',
      'O Instagram não publica um prazo fixo de resposta. Pode chegar em poucos dias ou depois de várias semanas. Não podemos prometer uma data; o que ajuda é enviar uma contestação clara e ter paciência.',
      [('espera', 'O que esperar', P('Não existe prazo oficial. Alguns recebem resposta em poucos dias, outros esperam semanas. A resposta costuma chegar por e-mail e dentro do app.')),
       ('fazer', 'O que fazer enquanto espera', UL('Olhe seu e-mail e a caixa de spam.', 'Não conteste de novo e de novo.', 'Não crie uma conta nova para driblar a restrição.', 'Guarde seus prints.')),
       ('depois', 'Se a resposta for negativa', P('Veja <a href="@@appeal-denied@@">contestação do Instagram negada</a>.'))],
      [('Quanto tempo leva a contestação do Instagram?', 'O Instagram não indica prazo fixo. Varia de alguns dias a várias semanas.'),
       ('Dá para acelerar?', 'Não por um botão oficial. Uma contestação completa e clara é o melhor caminho.'),
       ('A Unbanz consegue acelerar?', 'Não podemos prometer data nenhuma. Ajudamos a apresentar o pedido com clareza e mantemos você informado.'),
       ('Devo contestar de novo?', 'Em geral não. Enviar repetidamente não ajuda.')],
      ['ig-disabled', 'appeal-denied', 'no-button', 'ig'], HELP_IG,
      desc='Quanto tempo leva a contestação do Instagram? Não há prazo fixo: de alguns dias a várias semanas. Veja o que fazer enquanto espera.')

    g('appeal-denied', 'Contestação do Instagram negada: o que fazer', 'Contestação negada',
      'Contestação do Instagram negada: e agora?',
      'Se negaram sua contestação da desativação da conta do Instagram, a conta não está perdida automaticamente. Leia bem o aviso, veja se sobrou alguma opção e guarde as provas; nem toda conta consegue voltar.',
      [('ler', 'Leia bem o aviso', P('Há um botão para pedir nova análise ou um link para um formulário? Use. Se só aparece uma decisão final, o caminho interno costuma estar fechado.')),
       ('opcoes', 'O que às vezes ainda é possível', UL('Outro caminho oficial, se o motivo permitir (por exemplo, uma conta hackeada).', 'Se foi golpe ou crime online, registrar um boletim de ocorrência e buscar orientação. Veja <a href="@@rights@@">onde denunciar golpes e crimes online no Brasil</a>.')),
       ('nao', 'O que não ajuda', UL('Criar uma conta nova para driblar a restrição.', 'Pagar a alguém que diz ter "um contato na Meta".'))],
      [('Negaram minha contestação. Acabou?', 'Nem sempre, mas o caminho interno costuma ficar fechado. Veja quais opções o aviso ainda mostra.'),
       ('Posso contestar de novo?', 'Só se o aviso oferecer essa opção.'),
       ('Existe outro lugar para recorrer?', 'Se houve golpe, invasão ou crime online, registre um B.O. e veja <a href="@@rights@@">onde denunciar no Brasil</a>.'),
       ('A Unbanz consegue recuperar a conta?', 'Vemos com sinceridade o que é possível. A decisão é da plataforma e não prometemos resultado.')],
      ['rights', 'ig-disabled', 'no-button', 'ig'], HELP_IG,
      desc='Negaram a contestação da sua conta do Instagram? Como ler o aviso, o que ainda pode ser possível e por que uma conta nova não ajuda.')

    g('deleted', 'Conta do Instagram excluída ou desativada?', 'Excluída ou desativada?',
      'Sua conta do Instagram foi excluída ou desativada?',
      'Uma conta desativada às vezes pode ser recuperada com uma contestação; uma conta excluída de forma permanente, por você ou pelo Instagram, normalmente não. O aviso ao entrar mostra qual é a sua situação.',
      [('desativada', 'Desativada', P('Ao entrar, você vê um aviso de que sua conta foi desativada. Se houver opção de contestar, talvez você a recupere. Veja <a href="@@ig-disabled@@">conta do Instagram desativada</a>.')),
       ('excluida', 'Excluída', P('Se você mesmo excluiu a conta, por um tempo dá para desfazer; depois, não. Se o Instagram a excluiu de forma permanente, voltar é incomum.')),
       ('conferir', 'Como conferir', UL('Tente entrar e leia o aviso.', 'Procure mensagens do Instagram no seu e-mail.', 'Abra a página do perfil num navegador e veja se ela ainda existe.'))],
      [('Como sei se minha conta está desativada?', 'Ao entrar, aparece um aviso de que a conta está desativada, em geral com uma opção de contestar.'),
       ('Uma conta excluída pode voltar?', 'Só dentro do prazo indicado pelo Instagram, e normalmente não se foi excluída de forma permanente.'),
       ('Por que não encontro meu perfil?', 'Ele pode estar desativado, excluído ou outra conta pode ter bloqueado você.'),
       ('A Unbanz pode ajudar?', 'Se a conta foi desativada, vemos com sinceridade o que é possível.')],
      ['ig-disabled', 'ig', 'appeal-denied'], HELP_IG,
      desc='Sua conta do Instagram foi excluída ou desativada? Veja a diferença e o que ainda é possível em cada situação.')

    g('no-button', 'Instagram não mostra o botão de contestar: e agora?', 'Sem botão de contestar',
      'Instagram não mostra o botão para contestar.',
      'Se o botão para contestar não aparece, às vezes o prazo acabou, a conta foi desativada de forma permanente ou o aviso é de outro tipo. Veja primeiro qual aviso aparece para você.',
      [('motivos', 'Possíveis motivos', UL('O prazo para contestar terminou.', 'Você já contestou e a decisão é definitiva.', 'É uma restrição ou uma conta hackeada e não uma desativação.', 'Uma falha temporária do app.')),
       ('tentar', 'O que você pode tentar', UL('Entre pelo navegador, em instagram.com, em vez do app.', 'Tente de outro aparelho e de uma rede que você usa sempre.', 'Atualize o app.', 'Se a conta foi hackeada, use instagram.com/hacked.')),
       ('direitos', 'Se for crime online', P('Se houve golpe ou crime, veja <a href="@@rights@@">onde denunciar golpes e crimes online no Brasil</a>.'))],
      [('Por que não vejo o botão de contestar?', 'Em geral porque o prazo acabou, a decisão é definitiva ou o aviso é de outro tipo.'),
       ('Criar uma conta nova ajuda?', 'Não, e pode piorar, porque driblar a restrição vai contra as regras.'),
       ('A Unbanz consegue fazer o botão aparecer?', 'Não. Mas podemos ver qual caminho oficial ainda está aberto.'),
       ('E se a conta foi hackeada?', 'Aí há outro caminho: instagram.com/hacked.')],
      ['ig-disabled', 'appeal-denied', 'rights', 'ig-hacked'], HELP_IG,
      desc='Instagram não mostra o botão para contestar? Veja os motivos mais comuns e o que ainda dá para tentar.')

    g('blocked', 'Instagram: "Restringimos certas atividades"', 'Ação bloqueada',
      'Instagram: "Restringimos certas atividades".',
      'Esse aviso significa que o Instagram limitou temporariamente algumas ações, muitas vezes depois de muita atividade em pouco tempo. Em geral não é uma desativação. Faça uma pausa, pare de automatizar e, se houver botão, peça uma análise.',
      [('que', 'O que o aviso significa', P('O Instagram limita temporariamente ações como curtir, seguir ou comentar. A conta continua existindo.')),
       ('fazer', 'O que você pode fazer', UL('Faça uma pausa de um ou dois dias e use o app normalmente.', 'Pare de usar apps de terceiros ou automações.', 'Se aparecer "Fui eu" ou "Informar um problema", use uma única vez.', 'Veja se há algum aviso no seu e-mail.')),
       ('repete', 'Se repetir', P('Confira se a conta foi hackeada, troque a senha e ative a verificação em duas etapas.'))],
      [('Quanto tempo dura a restrição?', 'O Instagram não indica prazo fixo; varia de horas a dias.'),
       ('Minha conta foi desativada?', 'Não, esse aviso é uma restrição temporária.'),
       ('Dá para remover?', 'Não diretamente. O que mais ajuda é fazer uma pausa e não usar automações.'),
       ('A Unbanz pode ajudar?', 'Se a restrição continuar ou houver algo mais, envie o aviso.')],
      ['ig-disabled', 'ig-hacked', 'ig'], HELP_IG,
      desc='O Instagram diz que restringiu certas atividades? Veja o que significa, quanto tempo dura e o que você mesmo pode fazer.')

    g('ad-disabled', 'Conta de anúncios do Facebook desativada: e agora?', 'Conta de anúncios desativada',
      'Conta de anúncios do Facebook desativada: e agora?',
      'Se sua conta de anúncios foi desativada, veja em Qualidade da conta qual motivo a Meta indica e peça uma análise pelo caminho oficial. Não mude os anúncios às cegas nem crie uma conta nova para driblar a restrição.',
      [('ler', 'Procure o motivo', P('No Meta Business Suite ou no Gerenciador de Anúncios, abra a página Qualidade da conta. Ali costuma aparecer o motivo e se é possível pedir uma análise.')),
       ('fazer', 'O que você pode fazer', OL('Tire prints do aviso e dos anúncios rejeitados.', 'Peça uma análise se o botão estiver disponível.', 'Confira se sua forma de pagamento e os dados da empresa estão corretos.', 'Espere a resposta e não envie o pedido repetidamente.')),
       ('nao', 'O que você não deve fazer', UL('Criar uma conta de anúncios nova para driblar a restrição.', 'Dar acesso à sua conta a quem diz "resolver tudo".'))],
      [('Por que minha conta de anúncios foi desativada?', 'O motivo costuma aparecer em Qualidade da conta: por exemplo, uma violação das políticas de anúncios ou um problema de pagamento.'),
       ('Posso pedir uma análise?', 'Sim, se a Meta mostrar essa opção. Faça uma única vez, de forma clara e completa.'),
       ('Posso simplesmente criar uma conta nova?', 'Ela costuma ficar restrita também e vai contra as regras se for para driblar a restrição.'),
       ('A Unbanz pode ajudar?', 'Sim, vemos com sinceridade o que é possível. A decisão é da Meta.')],
      ['ad', 'fb-appeal', 'appeal-denied'], HELP_AD, svc='ad',
      desc='Conta de anúncios do Facebook desativada? Veja o motivo em Qualidade da conta, peça uma análise clara e evite os erros comuns.')

    g('fb-appeal', 'Conta do Facebook desativada: como contestar', 'Facebook desativada: contestar',
      'Conta do Facebook desativada: como contestar.',
      'Se sua conta do Facebook foi desativada, entre, abra o aviso e peça uma análise pelo botão oficial. Faça isso uma única vez, dentro do prazo que o Facebook mostrar, e guarde um print.',
      [('passos', 'Passos', OL('Entre e leia o aviso. Tire um print.', 'Escolha "Solicitar análise" ou o botão equivalente.', 'Se for pedido, envie um documento de identidade na página oficial.', 'Espere a resposta por e-mail e nas suas notificações.')),
       ('atencao', 'Atenção', UL('Não envie o pedido várias vezes.', 'Envie seu documento de identidade somente pela página oficial do Facebook.', 'Não pague a ninguém que prometa um resultado certo: ninguém pode.')),
       ('sem', 'Não há botão?', P('Veja <a href="@@appeal-denied@@">contestação negada</a> e <a href="@@rights@@">onde denunciar golpes e crimes online no Brasil</a>.'))],
      [('Como contesto no Facebook?', 'Pelo botão de solicitar análise no aviso que aparece ao entrar.'),
       ('Preciso enviar um documento de identidade?', 'Às vezes. Envie somente pela página oficial do Facebook.'),
       ('Quanto tempo leva?', 'O Facebook não indica prazo fixo.'),
       ('A Unbanz pode ajudar?', 'Sim, vemos com sinceridade o que é possível. A decisão é do Facebook.')],
      ['fb', 'fb-hacked', 'appeal-time', 'ad-disabled'], HELP_FB,
      desc='Conta do Facebook desativada? Peça uma análise uma única vez pelo botão oficial e guarde um print. Veja o passo a passo.')

    g('fb-hacked', 'Conta do Facebook hackeada: o que fazer', 'Conta do Facebook hackeada',
      'Conta do Facebook hackeada: e agora?',
      'Se hackearam sua conta do Facebook, acesse facebook.com/hacked e siga os passos oficiais. Confira também se trocaram seu e-mail e depois mude a senha. Não compartilhe códigos com ninguém.',
      [('passos', 'O que fazer de imediato', OL('Acesse facebook.com/hacked e siga os passos.', 'Procure no e-mail uma mensagem sobre troca de e-mail e use o link para desfazer.', 'Mude a senha e saia das sessões nos outros aparelhos.', 'Ative a verificação em duas etapas e confira as páginas e contas de anúncios vinculadas.')),
       ('atencao', 'Cuidado', P('Quem oferece uma "recuperação" e pede a senha ou um código não é confiável. Veja <a href="@@scams@@">golpes na recuperação de contas</a>.')),
       ('empresa', 'Conta de empresa', P('Se houver páginas ou contas de anúncios vinculadas, confira também quem é administrador e o que mudou.'))],
      [('Como recupero minha conta do Facebook hackeada?', 'Com facebook.com/hacked e os passos oficiais de recuperação.'),
       ('E se trocaram o e-mail?', 'Use o link da mensagem do Facebook que chegou ao seu e-mail anterior para desfazer a troca.'),
       ('Minhas páginas e contas de anúncios também correm risco?', 'É possível. Confira administradores e formas de pagamento assim que voltar a entrar.'),
       ('Preciso passar minha senha para recuperarem?', 'Nunca.')],
      ['fb', 'fb-appeal', 'scams', 'ig-hacked'], HELP_FB,
      desc='Conta do Facebook hackeada? Use facebook.com/hacked, desfaça a troca de e-mail e proteja a conta com verificação em duas etapas.')

    g('inactive-user', 'Nome de usuário de uma conta inativa do Instagram', 'Nome de usuário inativo',
      'Dá para reivindicar o nome de usuário de uma conta inativa do Instagram?',
      'Não há um botão para ficar com o nome de usuário de uma conta inativa. O Instagram só tem processos oficiais, como uma denúncia de marca registrada ou de personificação, e decide por conta própria.',
      [('regras', 'Como funciona', P('Um nome de usuário não se compra nem se transfere. Se a conta está realmente inativa, pode existir um caminho oficial; se o Instagram aceita ou não, quem decide é a plataforma.')),
       ('vias', 'Quais caminhos existem', UL('Uma denúncia de marca registrada, se o nome é a sua marca registrada.', 'Uma denúncia de personificação, se alguém se passa por você.', 'O caminho oficial das contas inativas, se couber.')),
       ('evitar', 'O que você deve evitar', UL('Comprar nomes de usuário de quem os oferece.', 'Quem diz ter "um contato na Meta".'))],
      [('Posso simplesmente ficar com o nome de usuário de uma conta inativa?', 'Não. Só existe um processo oficial e quem decide é o Instagram.'),
       ('Posso comprar um nome de usuário?', 'Não, e quem oferece vai contra as regras ou é golpista.'),
       ('Quanto custa a ajuda com um pedido de nome de usuário?', 'O preço você fica sabendo na conversa, antes de o trabalho começar.'),
       ('E se o pedido não der certo?', 'Você recebe 100% do valor de volta. Veja a <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (em inglês).')],
      ['user', 'pricing', 'scams'], P('Envie o nome de usuário que você quer e seu perfil. Dizemos com sinceridade qual caminho oficial se aplica e informamos o preço na conversa, antes de o trabalho começar. Se um pedido de nome de usuário não der certo, você recebe 100% do valor de volta. O atendimento é principalmente em inglês.'),
      svc='username', desc='Dá para reivindicar o nome de usuário de uma conta inativa do Instagram? Não há botão; só processos oficiais. Veja quais caminhos existem.')

    g('report-fake', 'Denunciar perfil falso com minhas fotos no Instagram', 'Perfil falso com minhas fotos',
      'Perfil falso com suas fotos: como denunciar.',
      'Se alguém usa suas fotos num perfil falso, denuncie como personificação pelos três pontinhos do perfil. Antes, guarde prints com o link e a data, e não peça aos amigos para denunciar em massa.',
      [('passos', 'Como denunciar', OL('Guarde prints e o link do perfil.', 'Abra o perfil, toque nos três pontinhos e escolha Denunciar.', 'Escolha a opção de que a conta se passa por você ou por alguém que você conhece.', 'Siga os passos e guarde a confirmação.')),
       ('extra', 'Passos adicionais', UL('Avise seus seguidores de que o perfil é falso.', 'Se pediram dinheiro ou ameaçaram você, registre um boletim de ocorrência na Delegacia Virtual do seu estado. Veja <a href="@@rights@@">onde denunciar no Brasil</a>.', 'Se há imagens íntimas roubadas, veja <a href="@@sextortion@@">sextorsão</a>.')),
       ('nao', 'O que não funciona', P('Denúncias em massa ou falsas. Uma denúncia clara é melhor e é o que a plataforma avalia.'))],
      [('Como denuncio um perfil que usa minhas fotos?', 'Com Denunciar no perfil e a opção de personificação.'),
       ('Devo pedir que várias pessoas denunciem?', 'Não. Não funciona e vai contra as regras.'),
       ('A Unbanz pode denunciar?', 'Ajudamos a preparar e apresentar a denúncia pelas ferramentas oficiais. A decisão é da plataforma.'),
       ('Devo registrar um boletim de ocorrência?', 'Se houve golpe, ameaça ou extorsão, vale registrar.')],
      ['fake', 'imp', 'har', 'scams'], HELP_REP, svc='ban',
      desc='Alguém usa suas fotos num perfil falso no Instagram? Veja como denunciar como personificação e quais provas guardar.')

    g('scams', 'Golpes na recuperação de contas: como reconhecer', 'Golpes na recuperação de contas',
      'Golpes na recuperação de contas: como reconhecer.',
      'Ninguém precisa da sua senha nem de um código de acesso para recuperar sua conta. Quem pede, promete resultado certo ou diz ter um contato na Meta é golpista.',
      [('sinais', 'Sinais de alerta', UL('Eles chamam você primeiro, em geral por mensagem privada ou num comentário.', 'Pedem a senha, um código ou acesso ao seu e-mail.', 'Prometem resultado certo ou dizem ter um contato na Meta.', 'Querem receber por cartão-presente, criptomoeda ou um link.')),
       ('fazer', 'O que você pode fazer', UL('Não responda e bloqueie a conta.', 'Denuncie no app.', 'Se já pagou ou passou dados, troque suas senhas e avise seu banco; no Pix, peça ao banco para abrir a contestação pelo MED.', 'Registre um boletim de ocorrência na Delegacia Virtual e veja a orientação da SaferNet Brasil. Detalhes em <a href="@@rights@@">onde denunciar golpes e crimes online no Brasil</a>.')),
       ('outra', 'Como é uma ajuda confiável', P('Um serviço confiável nunca pede sua senha, informa o preço antes de o trabalho começar e explica qual caminho oficial usa. Veja <a href="@@legit@@">A Unbanz é confiável?</a>'))],
      [('Como reconheço um golpe de recuperação de contas?', 'Eles chamam você primeiro, pedem a senha ou um código e prometem resultado certo.'),
       ('E se eu já paguei?', 'Fale com seu banco, troque suas senhas e registre um B.O. Se foi por Pix, peça ao banco a contestação pelo MED.'),
       ('Alguém tem mesmo um contato na Meta?', 'Não dá para comprovar, e é uma história típica de golpe.'),
       ('Vocês pedem minha senha?', 'Nunca.')],
      ['legit', 'ig-hacked', 'fake', 'pricing'], HELP_IG,
      desc='Ninguém precisa da sua senha para recuperar sua conta. Veja os sinais de alerta dos golpes na recuperação de contas.')

    g('sextortion', 'Sextorsão no Instagram: o que fazer', 'Sextorsão',
      'Sextorsão no Instagram: o que fazer.',
      'Se alguém chantageia você com imagens íntimas no Instagram, não pague e corte o contato. Guarde as provas, bloqueie e denuncie a conta e registre um boletim de ocorrência. Você não está sozinho e não fez nada de errado.',
      [('direto', 'O que fazer de imediato', OL('Não pague e não envie mais imagens.', 'Tire prints das mensagens, do perfil e do nome de usuário; não apague nada.', 'Bloqueie e denuncie a conta no app.', 'Registre um boletim de ocorrência na Delegacia Virtual do seu estado ou numa delegacia (190 se houver perigo imediato).')),
       ('ajuda', 'Ajuda no Brasil', UL('A SaferNet Brasil recebe denúncias de crimes online e tem um canal de ajuda e orientação (Helpline), gratuito e sigiloso.', 'Se a vítima for criança ou adolescente, o Disque 100 recebe denúncias de violações de direitos humanos.', 'Peça a retirada das imagens divulgadas diretamente à plataforma, pelas ferramentas de denúncia.')),
       ('imagens', 'Remover imagens', P('Denuncie à plataforma as imagens divulgadas. Nunca envie dinheiro para evitar a divulgação: em geral só traz mais exigências.'))],
      [('Devo pagar?', 'Não. Pagar normalmente não resolve e traz novas exigências.'),
       ('Devo denunciar?', 'Sim, vale a pena. Guarde antes as provas.'),
       ('Onde encontro ajuda?', 'Na Delegacia Virtual ou numa delegacia, na Helpline da SaferNet Brasil e, para crianças e adolescentes, no Disque 100. Se houver perigo imediato, ligue para o 190.'),
       ('A Unbanz pode ajudar?', 'Ajudamos a denunciar a conta pelas ferramentas oficiais. Registre antes o B.O. e guarde as provas.')],
      ['har', 'fake', 'scams'], HELP_REP, svc='ban',
      desc='Está sendo chantageado com imagens íntimas no Instagram? Não pague, guarde as provas, bloqueie e denuncie a conta e procure a polícia.')

    g('support', 'Como falar com o Instagram ou a Meta no Brasil', 'Falar com o Instagram ou a Meta',
      'Como falar com o Instagram ou a Meta no Brasil.',
      'O Instagram e a Meta não têm telefone de atendimento para usuários comuns. Você chega até eles pela Central de Ajuda, pela opção de informar um problema no app e pelos formulários oficiais. Os números que circulam na internet são quase sempre falsos.',
      [('vias', 'Os caminhos oficiais', UL('A Central de Ajuda do Instagram e do Facebook.', 'No app: Configurações, Ajuda, Informar um problema.', 'Formulários oficiais de contestação, invasão e personificação.', 'Somente para quem tem o Meta Verified: o suporte incluído.')),
       ('falsos', 'Telefones de suporte falsos', P('Se você pesquisar um telefone do Instagram e encontrar um, é quase certo que seja golpe. Veja <a href="@@scams@@">golpes na recuperação de contas</a>.')),
       ('br', 'Se houve crime', P('Se você foi vítima de golpe ou de um crime online, veja <a href="@@rights@@">onde denunciar golpes e crimes online no Brasil</a>.'))],
      [('Como ligo para o Instagram?', 'Não é possível para usuários comuns. Use a Central de Ajuda e a opção de informar um problema no app.'),
       ('Um telefone do Instagram que achei na internet é real?', 'Quase sempre não. Tenha cuidado.'),
       ('A Meta tem um escritório no Brasil?', 'Sim, a Meta tem operação no país, mas o suporte a contas de usuários é feito pelos canais online oficiais.'),
       ('A Unbanz pode ajudar se o caminho oficial travar?', 'Sim, vemos com sinceridade o que é possível. Não temos vínculo com a Meta.')],
      ['rights', 'scams', 'ig-disabled', 'ig'], HELP_IG,
      desc='Como falar com o Instagram ou a Meta no Brasil? Não há telefone, mas há caminhos oficiais. E como reconhecer telefones de suporte falsos.')

    g('rights', 'Onde denunciar golpes e crimes online no Brasil', 'Onde denunciar no Brasil',
      'Onde denunciar golpes e crimes online no Brasil.',
      'Golpe, invasão de conta, ameaça ou extorsão online é crime e pode ser denunciado. Registre um boletim de ocorrência na Delegacia Virtual do seu estado, peça orientação à SaferNet Brasil e, se houve transferência por Pix, fale logo com o seu banco.',
      [('bo', 'Boletim de ocorrência', UL('A maioria dos estados tem uma Delegacia Virtual da Polícia Civil, onde você registra o B.O. pela internet.', 'Guarde prints, links, nomes de usuário, comprovantes de pagamento e datas antes de registrar.', 'Em perigo imediato, ligue para o 190.')),
       ('safernet', 'SaferNet Brasil', P('A SaferNet Brasil é uma organização que recebe denúncias de crimes e violações de direitos humanos na internet e oferece orientação gratuita e sigilosa por meio da Helpline.')),
       ('pix', 'Se você pagou por Pix', UL('Fale logo com o seu banco e peça a contestação pelo MED (Mecanismo Especial de Devolução).', 'Guarde o comprovante e o registro do B.O.', 'O resultado depende da situação; nenhum canal pode prometer devolução.')),
       ('ca', 'Crianças e adolescentes', P('O Disque 100 recebe denúncias de violações de direitos de crianças e adolescentes.')),
       ('ojo', 'Importante', P('Isto é um guia geral e não é orientação jurídica. A plataforma decide sobre a sua conta, e a polícia e a Justiça tratam do crime.'))],
      [('Onde registro um boletim de ocorrência de golpe online?', 'Na Delegacia Virtual da Polícia Civil do seu estado, quando houver, ou numa delegacia.'),
       ('O que é a SaferNet Brasil?', 'Uma organização que recebe denúncias de crimes na internet e oferece orientação gratuita e sigilosa.'),
       ('Perdi dinheiro por Pix. O que faço?', 'Fale com seu banco imediatamente e peça a contestação pelo MED; registre também o B.O.'),
       ('A Unbanz pode registrar o B.O. por mim?', 'Não. O B.O. é pessoal. Podemos ajudar a denunciar a conta pelas ferramentas oficiais da plataforma.')],
      ['scams', 'sextortion', 'support', 'appeal-denied'], HELP_IG,
      desc='Golpe ou crime online no Instagram ou Facebook? Veja onde denunciar no Brasil: Delegacia Virtual, SaferNet Brasil, banco (Pix MED) e Disque 100.')
