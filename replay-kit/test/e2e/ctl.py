import re, json
from playwright.sync_api import sync_playwright
from common import *
errs=[]
def secs(pg):
    t=pg.locator(".rp-time").first.inner_text() if False else pg.evaluate("document.querySelector('.rp-ov .rp-ctl, .rp-ov .rp-bar').innerText")
    m=re.search(r'(\d+):(\d+)\s*/\s*(\d+):(\d+)',t); return int(m[1])*60+int(m[2]), int(m[3])*60+int(m[4])
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_context(viewport={"width":1360,"height":860},user_agent=UA_D).new_page()
    pg.on("pageerror",lambda e:errs.append(str(e))); pg.on("console",lambda m:m.type=="error" and errs.append(m.text[:150]))
    pg.goto(BASE+"/users/#replays",wait_until="domcontentloaded"); pg.fill("#luser","harness-user"); pg.click("#lform button"); pg.wait_for_selector(".rp-row")
    pg.locator(".rp-row",has_text="Mobile").first.click(); pg.wait_for_selector(".rp-ov"); pg.wait_for_timeout(1500)
    print("loaded, dur", secs(pg))
    pg.click('.rp-ov [data-a=skip]')  # toggle skip off
    print("skip pressed:", pg.get_attribute('.rp-ov [data-a=skip]','aria-pressed'))
    pg.click('.rp-ov [data-a=skip]')
    # pause test
    pg.keyboard.press("Space"); pg.wait_for_timeout(300); a=secs(pg)[0]; pg.wait_for_timeout(1200); print("paused holds:", a==secs(pg)[0], pg.get_attribute(".rp-play","aria-label"))
    pg.keyboard.press("Space"); pg.wait_for_timeout(300)
    for sp in ("1","2","4"):
        pg.click(f'.rp-ov [data-s="{sp}"]'); pg.locator(".rp-track").bounding_box()
        tr=pg.locator(".rp-track").bounding_box(); pg.mouse.click(tr["x"]+4,tr["y"]+tr["height"]/2); pg.wait_for_timeout(300)
        t0=pg.evaluate("performance.now()"); s0=secs(pg)[0]
        pg.wait_for_timeout(2600); s1=secs(pg)[0]
        print(f"speed {sp}x pressed={pg.get_attribute(f'.rp-ov [data-s=\"{sp}\"]','aria-pressed')} progressed {s1-s0}s in ~2.6s")
        pg.screenshot(path=f"shots/ctl_{sp}x.png")
    # play to end -> finished state
    pg.wait_for_timeout(6000); print("end:", secs(pg), pg.get_attribute(".rp-play","aria-label"), "ended-icon-redo:", "path" in pg.inner_html(".rp-play"))
    pg.screenshot(path="shots/ctl_end.png")
    pg.keyboard.press("ArrowLeft"); pg.wait_for_timeout(300); print("left key ->", secs(pg))
    # click marker in events list
    pg.locator(".rp-ev").nth(2).click(); pg.wait_for_timeout(600); print("event click ->", secs(pg), "toast/addr:", pg.locator(".rp-addr").inner_text().replace("\n"," "))
    # newer/older
    pg.click('[aria-label="Older session"]'); pg.wait_for_timeout(2500); print("older opened:", pg.evaluate("location.hash"))
    print("errors",errs); b.close()
