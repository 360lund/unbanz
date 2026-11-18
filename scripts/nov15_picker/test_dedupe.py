#!/usr/bin/env python3
"""Local check: first onboarding submit opens mailto once (intercepted, not sent) and
shows the success state; a second submit within 6 hours does not open mailto again."""
import subprocess, time, sys
from playwright.sync_api import sync_playwright

PORT = 8933
BASE = 'http://127.0.0.1:%d' % PORT
OK = "Got it. We'll email you shortly, usually within the hour. Check your inbox and spam."
srv = subprocess.Popen(
    ['python3', '-m', 'http.server', str(PORT), '--bind', '127.0.0.1', '--directory', '/workspace/site'],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
)
time.sleep(0.6)
problems = []
try:
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        c = br.new_context(viewport={'width': 1280, 'height': 900})
        pg = c.new_page()
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.route('**/api/geo/**', lambda r: r.fulfill(status=200, body='{}', headers={'content-type': 'application/json'}))
        pg.add_init_script("""
          window.__hrefs = [];
          window.__whop = [];
          window.whop = new Proxy({}, {
            get: function (t, p) {
              if (p === 'track') return function (n) { window.__whop.push(n); };
              return function () { return window.whop; };
            }
          });
          document.addEventListener('click', function (e) {
            var a = e.target && e.target.closest && e.target.closest('a.mp-go');
            if (!a) return;
            var href = a.getAttribute('href') || '';
            if (/^mailto:/i.test(href)) {
              window.__hrefs.push(href);
              e.preventDefault();
            }
          }, true);
        """)
        pg.goto(BASE + '/', wait_until='load')
        pg.wait_for_timeout(400)
        # confirm new asset is on the page
        src = pg.evaluate("() => [...document.scripts].map(s => s.src).filter(s => /mail-pick/.test(s))")
        if not any('mail-pick.884976c7b592.js' in s for s in src):
            problems.append('homepage is not on the new mail-pick asset: %s' % src)

        pg.locator('main a[href^="mailto:team@unbanz.com"] >> visible=true').first.click()
        pg.wait_for_timeout(700)
        if not pg.evaluate("() => { const m=document.querySelector('.mp3'); return m && !m.hidden && m.classList.contains('is-open'); }"):
            problems.append('modal did not open')
        else:
            if pg.evaluate("document.querySelector('.mp-sheet').dataset.step") != '2':
                pg.click('.mp-card[data-value="ig_hacked"]')
                pg.wait_for_timeout(700)
            pg.fill('#mp-user', '@TestDedupe')
            pg.evaluate("() => { window.__hrefs = []; window.__whop = []; }")
            pg.click('.mp-go')
            pg.wait_for_timeout(500)
            hrefs = pg.evaluate('window.__hrefs')
            whop = pg.evaluate('window.__whop')
            st = pg.evaluate("""() => {
              const s = document.querySelector('.mp-sheet');
              const ok = s && s.querySelector('.mp-done');
              const ls = localStorage.getItem('unbanz_lead_submit_v1');
              return {
                step: s && s.dataset.step,
                okHidden: !ok || ok.hidden,
                okText: ok && (ok.innerText || '').replace(/\\s+/g,' ').trim(),
                goDis: s && s.querySelector('.mp-go').getAttribute('aria-disabled'),
                goOff: s && s.querySelector('.mp-go').classList.contains('mp-off'),
                open: !document.querySelector('.mp3').hidden,
                store: ls && JSON.parse(ls)
              };
            }""")
            if not hrefs or not any(h.startswith('mailto:team@unbanz.com') for h in hrefs):
                problems.append('first submit did not open mailto (intercepted): %s' % hrefs)
            else:
                body = hrefs[-1]
                if 'TestDedupe' not in body and 'testdedupe' not in body.lower() and '%40TestDedupe' not in body and '@testdedupe' not in body.lower() and 'TestDedupe' not in __import__('urllib.parse').unquote(body):
                    # decoded check below
                    pass
                from urllib.parse import unquote
                if 'testdedupe' not in unquote(body).lower():
                    problems.append('mailto body missing username: %s' % unquote(body)[:300])
            if 'submit_application' not in whop or 'schedule' not in whop:
                problems.append('Whop events missing on first submit: %s' % whop)
            if not st['open'] or st['step'] != 'ok' or st['okHidden']:
                problems.append('success state not shown after first submit: %s' % st)
            if st['okText'] != OK:
                problems.append('success copy mismatch: %r' % st['okText'])
            if st['goDis'] != 'true' or not st['goOff']:
                problems.append('submit button not disabled after first submit')
            store = st['store'] or {}
            if not store.get('at'):
                problems.append('localStorage missing timestamp: %s' % store)
            users = store.get('users') or {}
            if 'testdedupe' not in users:
                problems.append('localStorage missing normalized username: %s' % store)

            # close and try again — must not open mailto or fire Whop submit events
            pg.locator('.mp3 .cm-close').click()
            pg.wait_for_function("() => { const m = document.querySelector('.mp3'); return m && m.hidden; }", timeout=5000)
            pg.evaluate("() => { window.__hrefs = []; window.__whop = []; }")
            pg.locator('main a[href^="mailto:team@unbanz.com"] >> visible=true').first.click()
            pg.wait_for_timeout(700)
            st2 = pg.evaluate("""() => {
              const s = document.querySelector('.mp-sheet');
              const ok = s && s.querySelector('.mp-done');
              return {
                open: !document.querySelector('.mp3').hidden && document.querySelector('.mp3').classList.contains('is-open'),
                step: s && s.dataset.step,
                okHidden: !ok || ok.hidden,
                okText: ok && (ok.innerText || '').replace(/\\s+/g,' ').trim(),
                hrefs: window.__hrefs,
                whop: window.__whop
              };
            }""")
            if not st2['open'] or st2['step'] != 'ok' or st2['okHidden'] or st2['okText'] != OK:
                problems.append('second open did not show success only: %s' % st2)
            # CTA click is a page mailto that we intercept in init, then preventDefault + open().
            # Those page mailto hrefs are not a second lead send. Only .mp-go mailto is a send.
            go_mail = [h for h in st2['hrefs'] if 'mp-go' in h]  # hrefs don't include class
            # Filter: a successful second send would be another mailto with subject/body after clicking Write the email.
            # The CTA is typically mailto:team@unbanz.com with no body or a short subject.
            # Safer: count mp-go clicks via a flag.
            if 'submit_application' in st2['whop'] or 'schedule' in st2['whop']:
                problems.append('Whop submit events fired on blocked resubmit: %s' % st2['whop'])
            # Explicitly try clicking the hidden/disabled go button if present
            pg.evaluate("() => { window.__hrefs = []; window.__whop = []; }")
            pg.evaluate("""() => { const g = document.querySelector('a.mp-go'); if (g) g.click(); }""")
            pg.wait_for_timeout(300)
            after = pg.evaluate('({hrefs: window.__hrefs, whop: window.__whop})')
            if after['hrefs']:
                problems.append('disabled go still opened mailto: %s' % after['hrefs'])
            if after['whop']:
                problems.append('disabled go still fired Whop: %s' % after['whop'])

        ee = [e for e in errs if 'favicon' not in e]
        if ee:
            problems.append('page errors: %s' % ee[:3])
        c.close()
        br.close()
finally:
    srv.terminate()

for x in problems:
    print('FAIL:', x)
print('problems', len(problems))
sys.exit(1 if problems else 0)
