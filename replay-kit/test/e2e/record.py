import sys, json, time
from playwright.sync_api import sync_playwright
from common import *
mode = sys.argv[1]  # mobile | desktop
base = sys.argv[2] if len(sys.argv) > 2 else BASE
test = "--test" in sys.argv
mobile = mode == "mobile"
out = {"errors": [], "t": [], "rp": []}
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    ctx = b.new_context(viewport={"width": 390, "height": 844} if mobile else {"width": 1280, "height": 800}, user_agent=UA_M if mobile else UA_D,
                        is_mobile=mobile, has_touch=mobile, device_scale_factor=2 if mobile else 1, locale="en-US", timezone_id="Europe/London")
    ctx.add_init_script("try{localStorage.setItem('ubz_rec_test','1');%s}catch(e){}" % ("localStorage.setItem('ubz_test','1');" if test else ""))
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: out["errors"].append("pageerror: " + str(e)))
    pg.on("console", lambda m: m.type == "error" and out["errors"].append("console: " + m.text[:200]))
    def req(r):
        if "/api/t/" in r.url: out["t"].append(r.post_data and json.loads(r.post_data).get("e"))
        if "/api/users/rp/" in r.url: out["rp"].append(r.url.split("?")[1][:60])
    pg.on("request", req)
    resp = []
    pg.on("response", lambda r: "/api/users/rp/" in r.url and resp.append(r.status))
    pg.goto(base + "/?utm_source=chatgpt.com", wait_until="domcontentloaded")
    pg.wait_for_load_state("load"); pg.wait_for_timeout(2500)
    sid = pg.evaluate("JSON.parse(sessionStorage.getItem('ubz1')).id")
    if mobile:
        # scroll with touch-like wheel, tap
        for y in (300, 700, 1100): pg.mouse.wheel(0, 400); pg.wait_for_timeout(500)
        pg.touchscreen.tap(195, 420); pg.wait_for_timeout(600)
    else:
        for i in range(12): pg.mouse.move(100 + i * 60, 200 + (i % 4) * 40); pg.wait_for_timeout(40)
        for y in range(5): pg.mouse.wheel(0, 350); pg.wait_for_timeout(350)
        pg.mouse.wheel(0, -1500); pg.wait_for_timeout(500)
    # type into any input (privacy) if present later on contact popup
    # open popup: click the first wa.me link (popup intercept)
    link = pg.locator('a[href^="https://wa.me/"]:visible').first
    link.scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    box = link.bounding_box()
    if mobile: pg.touchscreen.tap(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
    else: pg.mouse.move(box["x"] + 10, box["y"] + 10, steps=15); pg.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
    pg.wait_for_timeout(1500)
    out["dialog"] = pg.locator(".cm-dialog").count()
    pg.screenshot(path=f"shots/rec_{mode}_popup.png")
    # type in popup textarea/input if any
    inp = pg.locator(".cm-dialog textarea, .cm-dialog input[type=text]")
    if inp.count():
        inp.first.fill("SECRET-TYPED-VALUE-123"); pg.wait_for_timeout(500)
    # click the WhatsApp continue button in popup (open in new tab -> block it)
    ctx.route("https://wa.me/**", lambda r: r.abort())
    ctx.route("https://api.whatsapp.com/**", lambda r: r.abort())
    wa = pg.locator(".cm-dialog a.cm-wa")
    if wa.count():
        wa.first.evaluate("a => a.removeAttribute('target')") if False else None
        pg.evaluate("document.querySelector('.cm-dialog a.cm-wa').addEventListener('click', e => e.preventDefault())")
        wa.first.click(); pg.wait_for_timeout(800)
    pg.keyboard.press("Escape"); pg.wait_for_timeout(500)
    # navigate to another page (internal link)
    href = pg.evaluate("(() => { const a=[...document.querySelectorAll('a[href^=\"/\"]')].find(a=>/^\\/[a-z0-9-]+\\/$/.test(a.getAttribute('href')) && !a.href.includes('users') ); return a && a.getAttribute('href') })()")
    out["nav"] = href
    if href:
        pg.goto(base + href, wait_until="domcontentloaded"); pg.wait_for_load_state("load"); pg.wait_for_timeout(2500)
        pg.mouse.wheel(0, 500); pg.wait_for_timeout(1500)
    pg.wait_for_timeout(7000)   # let periodic flush happen
    out["sid"] = sid; out["resp"] = resp
    out["sticky"] = pg.evaluate("!!document.querySelector('.mobile-contact')")
    ctx.close(); b.close()
print(json.dumps(out))
