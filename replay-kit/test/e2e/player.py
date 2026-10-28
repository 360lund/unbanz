import sys, json
from playwright.sync_api import sync_playwright
from common import *
which = sys.argv[1]  # Desktop | Mobile
errs=[]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    ctx = b.new_context(viewport={"width":1360,"height":860}, user_agent=UA_D, timezone_id="Asia/Karachi")
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errs.append("pageerror: "+str(e)))
    pg.on("console", lambda m: m.type=="error" and errs.append("console: "+m.text[:200]))
    pg.goto(BASE+"/users/#replays", wait_until="domcontentloaded")
    pg.fill("#luser","harness-user"); pg.click("#lform button"); pg.wait_for_selector(".rp-row", timeout=10000)
    pg.locator(".rp-row", has_text=which).first.click()
    pg.wait_for_selector(".rp-ov", timeout=5000); pg.wait_for_timeout(2500)
    print("hash", pg.evaluate("location.hash"))
    pg.screenshot(path=f"shots/play_{which}_0.png")
    print("markers", pg.locator(".rp-mk").count(), "gaps", pg.locator(".rp-gap").count(), "evs", pg.locator(".rp-ev").count())
    print("addr", pg.locator(".rp-addr").inner_text()[:80])
    print("frame", pg.evaluate("(()=>{const f=document.querySelector('.rp-frame');return f&&f.className})()"))
    pg.wait_for_timeout(3000)
    pg.screenshot(path=f"shots/play_{which}_1.png")
    # controls
    for sel in [".rp-ov [data-sp='2']", ".rp-ov [data-sp='4']"]:
        if pg.locator(sel).count(): pg.click(sel); pg.wait_for_timeout(500)
    print("buttons", pg.eval_on_selector_all(".rp-ov button", "els=>els.map(e=>e.getAttribute('aria-label')||e.dataset.sp||e.textContent.trim()).slice(0,30)"))
    pg.keyboard.press("Space"); pg.wait_for_timeout(300); pg.screenshot(path=f"shots/play_{which}_paused.png")
    # scrub to 60%
    tr = pg.locator(".rp-track"); bb = tr.bounding_box()
    pg.mouse.click(bb["x"]+bb["width"]*0.6, bb["y"]+bb["height"]/2); pg.wait_for_timeout(1200)
    pg.screenshot(path=f"shots/play_{which}_scrub.png")
    print("time", pg.locator(".rp-time").first.inner_text())
    print(json.dumps(errs))
    b.close()
