# -*- coding: utf-8 -*-
"""Shared builders for the money/core pages (home, services, faq, contact, reviews). Texts come from C."""
from lib import *

def services_page(site, C):
    S = site.S
    site.reg('services', 'listing', C['services']['title'], C['services']['desc'], C['services']['nav'])
    def b():
        d = site.pages['services']; site.svc[0] = 'unban'
        c = C['services']
        items = ''.join('<article><span class="service-no">%02d</span><div><h3>%s</h3><p>%s</p></div><div class="service-row-actions">'
                        '<a class="service-chat" href="%s" data-service="%s">%s <span aria-hidden="true">↗︎</span></a><a href="%s">%s ↗︎</a></div></article>'
                        % (i + 1, t, p, site.WA, sv, S['write_us'], site.path(k), S['see_detail']) for i, (t, p, k, sv) in enumerate(c['rows']))
        main = ('<main id="content">' + site.hero(c['h1'], c['lead'], S['crumb_services']) +
                '<div class="expertise-band"><section class="expertise container" id="expertise"><div class="expertise-heading"><div><p class="eyebrow">%s</p><h2>%s</h2></div></div><div class="service-rows">' % (c['eyebrow'], c['h2']) + items + '</div></section></div>' +
                site.faq_section(c['faq'], eyebrow=S['faq_eyebrow2']) + site.proof() + site.related_nav(c['related']) + '</main>')
        return site.page_shell(d, main, c['faq'], [(S['n_home'], BASE + '/%s/' % site.dir), (S['crumb_services'], site.url('services'))])
    site.build['services'] = b

def faq_page(site, C):
    S = site.S; c = C['faq']
    site.reg('faq', 'faq', c['title'], c['desc'], c['nav'])
    def b():
        d = site.pages['faq']; site.svc[0] = 'unban'
        main = ('<main id="content">' + site.hero(c['h1'], c['lead'], c['crumb']) +
                site.faq_section(c['items'], eyebrow=S['faq_eyebrow2'], title=c['faq_h2']) + site.proof() + site.related_nav(c['related']) + '</main>')
        return site.page_shell(d, main, c['items'], [(S['n_home'], BASE + '/%s/' % site.dir), (c['nav'], site.url('faq'))])
    site.build['faq'] = b

def contact_page(site, C):
    S = site.S; c = C['contact']
    site.reg('contact', 'contact', c['title'], c['desc'], c['nav'])
    def b():
        d = site.pages['contact']
        opts = ''.join('<a class="contact-option" href="%s" data-service="%s">%s <span aria-hidden="true">↗︎</span></a>' % (site.wa(t), sv, lab) for lab, t, sv in c['opts'])
        main = ('<main id="content"><section class="contact-intro container"><p class="eyebrow">%s</p><h1>%s</h1>'
                '<p>%s</p><div class="contact-options">' % (c['eyebrow'], c['h1'], c['p1']) + opts + '</div>'
                '<div class="email-option"><h2>%s</h2><a href="%s">team@unbanz.com ↗︎</a><p>%s</p></div>' % (c['mail_h2'], site.MAIL, c['mail_p']) +
                '<div class="email-option"><h2>%s</h2><p>%s</p></div>' % (c['what_h2'], c['what_p']) +
                '<div class="email-option"><h2>%s</h2><p>%s</p></div>' % (c['lang_h2'], c['lang_p']) +
                '<p class="contact-note">%s</p></section></main>' % c['note'])
        return site.page_shell(d, main, [], [(S['n_home'], BASE + '/%s/' % site.dir), (c['nav'], site.url('contact'))])
    site.build['contact'] = b

def reviews_page(site, C):
    S = site.S; c = C['reviews']
    site.reg('reviews', 'avis', c['title'], c['desc'], c['nav'])
    def b():
        d = site.pages['reviews']; site.svc[0] = 'unban'
        rows = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (q, a_) for q, a_ in c['faq'])
        pick = ('<div class="rv-pick" role="group" aria-label="%s"><span>%s</span>' % (c['pick'], c['pick']) +
                ''.join('<a href="%s" data-service="%s">%s</a>' % (site.wa(t), sv, lab) for lab, t, sv in c['pick_opts']) + '</div>')
        main = ('<main id="content" class="rv"><section class="rv-top container"><h1>%s</h1><p>%s</p></section>' % (c['h1'], c['p']) +
                '<section class="vt vt-page container" aria-label="%s"><ul class="vt-track">' % c['video_aria'] + ''.join(site.vt_cards) + '</ul></section>'
                '<section class="rv-cta container" aria-label="Contact"><a class="button button-light" href="%s" data-service="unban">%s <span aria-hidden="true">↗︎</span></a>' % (site.WA, S['mc_wa']) +
                '<a class="rv-mail" href="%s">%s</a>' % (site.MAIL, c['mail']) + pick + '</section>'
                '<section class="rv-faq container" aria-labelledby="rvq"><h2 id="rvq">%s</h2><div class="simple-faq">' % c['q_h2'] + rows + '</div></section></main>')
        return site.page_shell(d, main, c['faq'], [(S['n_home'], BASE + '/%s/' % site.dir), (c['nav'], site.url('reviews'))], vt=True).replace('</head>', AVIS_STYLE + '</head>', 1)
    site.build['reviews'] = b

def home_page(site, C):
    S = site.S; c = C['home']
    site.reg('home', 'hub', c['title'], c['desc'], S['n_home'])
    def b():
        d = site.pages['home']; site.svc[0] = 'unban'
        items = ''.join('<article><span class="service-no">%02d</span><div><h3>%s</h3><p>%s</p></div><div class="service-row-actions">'
                        '<a class="service-chat" href="%s" data-service="%s">%s <span aria-hidden="true">↗︎</span></a><a href="%s">%s ↗︎</a></div></article>'
                        % (i + 1, t, p, site.WA, sv, S['write_us'], site.path(k), S['see_detail']) for i, (t, p, k, sv) in enumerate(c['rows']))
        det = ''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>' % (q, a_) for q, a_ in c['faq'])
        nav, mobile = site.header()
        steps = ''.join('<p><span>%02d</span>%s</p>' % (i + 1, t) for i, t in enumerate(c['steps']))
        body = ('<body><a class="skip-link" href="#expertise">%s</a>' % c['skip'] + SPRITE + '<main><section class="hero" id="home" aria-labelledby="hero-title"><div class="hero-sky" aria-hidden="true"></div>'
            '<header class="site-header container"><a class="wordmark" href="#home" aria-label="%s"><span>unbanz<span class="wordmark-dot">.</span></span></a>' % c['home_aria'] + nav +
            '<a class="header-contact" href="%s">WhatsApp <span aria-hidden="true">↗︎</span></a>' % site.WA +
            '<button class="menu-button" aria-label="%s" aria-expanded="false" aria-controls="mobile-nav"><span></span><span></span><span></span></button></header>' % S['menu_open'] + mobile +
            '<div class="hero-ornaments" aria-hidden="true"><div class="ornament ornament-facebook"><img src="/assets/hero-facebook.c3ca6b00d0.webp" width="360" height="360" alt="" fetchpriority="high" decoding="sync"></div>'
            '<div class="ornament ornament-instagram"><img src="/assets/hero-instagram.fef5a3021b.webp" width="360" height="360" alt="" decoding="sync"></div></div>'
            '<div class="hero-content container"><h1 id="hero-title"><span class="title-line"><span>%s</span></span><span class="title-line"><span>%s</span></span></h1>' % (c['h1a'], c['h1b']) +
            '<p class="hero-description">%s</p>' % c['hero_p'] +
            '<div class="hero-cta"><a class="button button-light hero-button" href="%s" data-service="unban">%s <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="%s">%s ↗︎</a></div></div></section>' % (site.WA, S['cta_quote'], site.MAIL, S['hero_mail']) +
            '<section class="recovery-intro container" data-reveal><p class="eyebrow">%s</p><h2>%s</h2><p>%s</p></section>' % (c['intro_eyebrow'], c['intro_h2'], c['intro_p']) +
            '<div class="expertise-band"><section class="expertise container" id="expertise"><div class="expertise-heading"><div><p class="eyebrow">%s</p><h2>%s</h2></div></div><div class="service-rows">' % (c['exp_eyebrow'], c['exp_h2']) + items + '</div></section></div>'
            '<section class="vt container" id="testimonials" aria-labelledby="vt-title"><div class="vt-head"><div><p class="eyebrow">%s</p><h2 id="vt-title">%s</h2></div></div><ul class="vt-track">' % (c['vt_eyebrow'], c['vt_h2']) + ''.join(site.vt_cards) + '</ul>'
            '<p style="margin-top:14px;font-size:14px">%s <a href="@@reviews@@">%s ↗︎</a></p></section>' % (c['vt_note'], c['vt_all']) +
            '<section class="approach container" id="approach" aria-labelledby="approach-title"><div class="approach-image turnaround-panel"><div class="approach-image-copy"><p class="eyebrow">%s</p><p class="days">0<span>%s</span></p><p class="timing-note">%s</p></div></div>' % (c['pw_eyebrow'], c['pw_zero'], c['pw_note']) +
            '<div class="approach-copy"><p class="eyebrow">%s</p><h2 id="approach-title">%s</h2><div class="simple-steps">%s</div>' % (c['how_eyebrow'], c['how_h2'], steps) +
            '<a class="text-button approach-link" href="@@how@@">%s <span aria-hidden="true">↗︎</span></a></div></section>' % c['how_link'] +
            '<section class="price-section container" id="pricing"><div><p class="eyebrow">%s</p><h2>%s</h2><p>%s</p>' % (c['pr_eyebrow'], c['pr_h2'], c['pr_p']) + site.cta_pair(c['pr_cta']) + '</div>'
            '<div class="price-notes">%s<a href="@@pricing@@">%s ↗︎</a></div></section>' % (''.join('<article><h3>%s</h3><p>%s</p></article>' % x for x in c['pr_notes']), c['pr_link']) +
            '<section class="faq-section" id="questions"><div class="container faq-layout"><div class="faq-intro"><p class="eyebrow">%s</p><h2>%s</h2></div><div class="simple-faq">' % (c['faq_eyebrow'], c['faq_h2']) + det + '</div></div></section>'
            '<section class="closing" id="contact" aria-labelledby="closing-title"><div class="closing-sky" aria-hidden="true"></div><div class="closing-content" data-reveal><p class="eyebrow">%s</p><h2 id="closing-title">%s</h2>' % (c['cl_eyebrow'], c['cl_h2']) +
            '<div class="hero-cta"><a class="button button-light" href="%s" data-service="unban">%s <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="%s">%s ↗︎</a></div><p>%s</p></div></section></main>' % (site.WA, S['mc_wa'], site.MAIL, S['hero_mail'], c['cl_p']))
        full = site.head(d, c['faq'], [(S['n_home'], site.url('home'))], None, vt=True) + '\n' + body + '\n' + site.footer('home') + '\n' + site.mobile_contact + '</body>\n</html>\n'
        return site.res(full)
    site.build['home'] = b
