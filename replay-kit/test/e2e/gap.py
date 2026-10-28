import re
from playwright.sync_api import sync_playwright
from common import *
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_context(viewport={"width":1360,"height":860},user_agent=UA_D).new_page()
    pg.goto(BASE+"/users/#replays",wait_until="domcontentloaded"); pg.fill("#luser","harness-user"); pg.click("#lform button"); pg.wait_for_selector(".rp-row")
    pg.locator(".rp-row",has_text="0:12").nth(0).click(); pg.wait_for_selector(".rp-ov"); pg.wait_for_timeout(800)
    pg.wait_for_function("document.querySelector('.rp-load').hidden")
    def info(): 
        t=pg.evaluate("document.querySelector('.rp-ov').innerText"); m=re.search(r'(\d+):(\d+)\s*/\s*(\d+):(\d+)',t); return int(m[1])*60+int(m[2]), int(m[3])*60+int(m[4])
    print("gaps", pg.locator(".rp-gap").count(), "dur", info())
    pg.wait_for_timeout(1500)
    log=[]
    for i in range(10):
        pg.wait_for_timeout(700); log.append((info()[0], pg.evaluate("document.querySelector('.rp-skip').classList.contains('on')")))
    print(log)
    b.close()
