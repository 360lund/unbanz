import subprocess, time, json, sys, urllib.parse
from playwright.sync_api import sync_playwright
L = json.load(open('/workspace/nowa/picker/langs.json'))
BASE = next((a for a in sys.argv[1:] if a.startswith('http')), None)
SHOTS = '--shots' in sys.argv
srv = None
if not BASE:
    srv = subprocess.Popen(['python3', '-m', 'http.server', '8932', '--bind', '127.0.0.1', '--directory', '/workspace/site'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(.8)
    BASE = 'http://127.0.0.1:8932'
PAGES = [('/', 'en'), ('/fr/', 'fr'), ('/nl/', 'nl'), ('/es/contacto/', 'es'), ('/pt-br/', 'pt'), ('/de/', 'de'), ('/it/', 'it'), ('/tr/', 'tr'), ('/ar/', 'ar'), ('/zh-hk/white-label-agency/', 'zh'), ('/instagram-hacked-uk-what-to-do/', 'en'), ('/faq/', 'en')]
if '--quick' in sys.argv: PAGES = [('/', 'en'), ('/ar/', 'ar'), ('/fr/', 'fr'), ('/instagram-hacked-uk-what-to-do/', 'en')]
O = '/workspace/cta_nov15/picker/'
def expected(lang, topic, user, hear):
    d = L[lang]; t = [x for x in d['t'] if x[0] == topic][0]
    body = d['hi'] + '\n\n' + d['f'][0] + ': ' + t[3] + '\n' + d['f'][1] + ': ' + user + '\n' + d['f'][2] + ': \n' + d['f'][3] + ': \n' + d['f'][4] + ': \n\n' + d['bye']
    if hear: body += '\nHow I heard about Unbanz: ' + hear
    return t[2], body, t[4]
def parse(href):
    q = href.split('?', 1)[1]; out = {}
    for kv in q.split('&'):
        k, v = kv.split('=', 1); out[k] = urllib.parse.unquote(v)
    return href.split('?')[0], out
problems = []; n = 0
with sync_playwright() as p:
    br = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    for vp, (w, h) in (('mobile', (390, 844)), ('desktop', (1280, 900))):
        for path, lang in PAGES:
            c = br.new_context(viewport={'width': w, 'height': h}, is_mobile=vp == 'mobile', has_touch=vp == 'mobile', device_scale_factor=2 if vp == 'mobile' else 1)
            pg = c.new_page(); errs = []; beacons = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e: errs.append('PAGEERROR ' + str(e)))
            pg.route('**/api/t/**', lambda r: (beacons.append(r.request.post_data), r.fulfill(status=204)))
            pg.route('**/api/geo/**', lambda r: r.fulfill(status=200, body='{}', headers={'content-type': 'application/json'}))
            pg.add_init_script("document.addEventListener('click', e => { const a = e.target.closest && e.target.closest('a.mp-go'); if (a) { window.__href = a.href; window.__svc = a.dataset.service; window.__pl = a.dataset.platform; e.preventDefault(); } });")
            pg.goto(BASE + path, wait_until='load'); pg.wait_for_timeout(500)
            tag = '%s %s' % (vp, path); pr = []
            pg.locator('main a[href^="mailto:team@unbanz.com"] >> visible=true').first.click()
            pg.wait_for_timeout(700)
            st = pg.evaluate("""() => { const m = document.querySelector('.mp3'), s = m && m.querySelector('.mp-sheet'); if (!m) return null; const r = s.getBoundingClientRect();
               return {open: !m.hidden && m.classList.contains('is-open'), step: s.dataset.step, top: r.top, bottom: r.bottom, left: r.left, right: r.right, ov: document.documentElement.scrollWidth - innerWidth, sov: s.scrollWidth - s.clientWidth,
                 dir: getComputedStyle(s).direction, cards: s.querySelectorAll('.mp-card').length, small: [...s.querySelectorAll('.mp-card, .mp-x, button.mp-back')].filter(b => b.offsetParent && (b.getBoundingClientRect().height < 44 || b.getBoundingClientRect().width < 44)).length,
                 lock: document.documentElement.classList.contains('cm-lock'), hearDup: document.querySelectorAll('#ubz-hear-mail').length, focusIn: s.contains(document.activeElement) } }""")
            if not st or not st['open']: problems.append((tag, 'did not open', st)); c.close(); continue
            preset = pg.evaluate("(() => { const a = [...document.querySelectorAll('main a[href^=\"mailto:team@unbanz.com\"]')].find(x => x.offsetParent); return a && a.getAttribute('data-topic'); })()")
            exp_step = '2' if preset and preset != 'other' else '1'
            if st['step'] != exp_step: pr.append('step %s (preset %s)' % (st['step'], preset))
            if st['ov'] > 0 or st['sov'] > 0: pr.append('overflow %s/%s' % (st['ov'], st['sov']))
            if st['bottom'] > h + 1 or st['top'] < 0 or st['left'] < 0 or st['right'] > w + 1: pr.append('sheet outside viewport %s' % st)
            if st['small']: pr.append('small targets %d' % st['small'])
            if not st['lock'] or not st['focusIn']: pr.append('lock/focus %s' % st)
            if lang == 'ar' and st['dir'] != 'rtl': pr.append('not rtl')
            if SHOTS and path in ('/', '/ar/'):
                pg.screenshot(path=O + 'after_%s_step1%s.png' % (vp, '' if path == '/' else '_ar'))
            # Esc closes, reopen
            pg.keyboard.press('Escape'); pg.wait_for_timeout(450)
            if pg.evaluate("!document.querySelector('.mp3').hidden || document.documentElement.classList.contains('cm-lock')"): pr.append('esc did not close/unlock')
            pg.locator('main a[href^="mailto:team@unbanz.com"] >> visible=true').first.click(); pg.wait_for_timeout(600)
            # tab trap: 40 tabs stay inside
            for _ in range(40): pg.keyboard.press('Tab')
            if not pg.evaluate("document.querySelector('.mp-sheet').contains(document.activeElement)"): pr.append('focus escaped')
            if pg.evaluate("document.querySelector('.mp-sheet').dataset.step") == '2':
                pg.click('.mp-back'); pg.wait_for_timeout(600)
            pg.click('.mp-card[data-value="ig_hacked"]'); pg.wait_for_timeout(800)
            s2 = pg.evaluate("""() => { const s = document.querySelector('.mp-sheet'), g = s.querySelector('.mp-go'), r = g.getBoundingClientRect(), sr = s.getBoundingClientRect();
               return {step: s.dataset.step, focus: document.activeElement && document.activeElement.id, goVis: r.bottom <= innerHeight + 1 && r.top >= sr.top && r.height >= 44, dis: g.getAttribute('aria-disabled'), op: getComputedStyle(g).opacity, ov: document.documentElement.scrollWidth - innerWidth, sov: s.scrollWidth - s.clientWidth, s1hidden: s.querySelector('.mp-s1').hidden, bottom: sr.bottom} }""")
            if s2['step'] != '2' or not s2['s1hidden']: pr.append('no step2 %s' % s2)
            if s2['focus'] != 'mp-user': pr.append('input not focused (%s)' % s2['focus'])
            if not s2['goVis'] or s2['dis'] != 'false' or float(s2['op']) < 1: pr.append('CTA %s' % s2)
            if s2['ov'] > 0 or s2['sov'] > 0: pr.append('overflow step2')
            if s2['bottom'] > h + 1: pr.append('sheet bottom off-screen step2')
            # back button -> step1 -> pick again
            pg.click('.mp-back'); pg.wait_for_timeout(600)
            if pg.evaluate("document.querySelector('.mp-sheet').dataset.step") != '1': pr.append('back failed')
            pg.click('.mp-card[data-value="ig_hacked"]'); pg.wait_for_timeout(800)
            pg.keyboard.type('@testuser')
            pg.select_option('#ubz-hear-mail', index=2)
            if SHOTS and path in ('/', '/ar/'):
                pg.screenshot(path=O + 'after_%s_step2%s.png' % (vp, '' if path == '/' else '_ar'))
            beacons.clear()
            pg.click('.mp-go'); pg.wait_for_timeout(700)
            href = pg.evaluate('window.__href')
            subj, body, plat = expected(lang, 'ig_hacked', '@testuser', 'Google or another search engine')
            if not href: pr.append('no href captured')
            else:
                base, q = parse(href)
                if base != 'mailto:team@unbanz.com': pr.append('base ' + base)
                if q.get('subject') != subj: pr.append('subject %r != %r' % (q.get('subject'), subj))
                if q.get('body') != body: pr.append('body mismatch %r' % q.get('body'))
                if '+' in href.split('body=')[1] and '+' not in body: pr.append('plus-encoding')
            if pg.evaluate('window.__svc') != 'ig_hacked' or pg.evaluate('window.__pl') != plat: pr.append('data-service/platform')
            if not any(b and '"sv":"ig_hacked"' in b and '"k":"email"' in b for b in beacons): pr.append('tracker beacon missing %s' % beacons)
            if pg.evaluate("!document.querySelector('.mp3').hidden"): pr.append('did not close after send')
            # backdrop close
            pg.locator('main a[href^="mailto:team@unbanz.com"] >> visible=true').first.click(); pg.wait_for_timeout(600)
            pg.mouse.click(5, 5); pg.wait_for_timeout(450)
            if pg.evaluate("!document.querySelector('.mp3').hidden"): pr.append('backdrop close failed')
            ee = [e for e in errs if 'favicon' not in e and 'Failed to load resource' not in e]
            if ee: pr.append('console: %s' % ee[:3])
            n += 1
            if pr: problems.append((tag, pr))
            c.close()
    br.close()
if srv: srv.terminate()
for x in problems: print(x)
print('runs', n, 'problems', len(problems))
