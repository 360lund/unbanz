import json, time, urllib.request
BASE = "http://127.0.0.1:8099"
UA_D = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
UA_M = "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
def login(base=BASE):
    r = urllib.request.Request(base + "/api/users/auth/login/", data=json.dumps({"username": "harness-user"}).encode(), headers={"Content-Type": "application/json", "Origin": base})
    return json.load(urllib.request.urlopen(r))["token"]
def get(path, tok, base=BASE):
    r = urllib.request.Request(base + path, headers={"X-Users-Token": tok})
    return urllib.request.urlopen(r).read()
