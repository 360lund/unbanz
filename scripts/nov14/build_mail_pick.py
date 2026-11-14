# Nov 14: mail-pick v2 = previous mail-pick + Facebook Page / TikTok / YouTube / WhatsApp topics,
# path inference for those, and an optional data-topic on the clicked mailto link (used by the
# "How can we help?" options). Everything else is byte-identical to the previous version.
import hashlib, pathlib, sys
SRC = pathlib.Path('assets/mail-pick.b0ade601709f.js')
s = SRC.read_text(encoding='utf-8')
ADD = {
 'en': [("page","Facebook Page","Facebook Page - help","Facebook Page disabled or restricted","Facebook"),
        ("tiktok","TikTok","TikTok account - help","TikTok account banned or suspended","TikTok"),
        ("youtube","YouTube channel","YouTube channel - help","YouTube channel terminated or hacked","YouTube"),
        ("whatsapp","WhatsApp number","WhatsApp number - help","WhatsApp number banned","WhatsApp")],
 'fr': [("page","Page Facebook","Page Facebook - aide","Page Facebook désactivée ou restreinte","Facebook"),
        ("tiktok","TikTok","Compte TikTok - aide","Compte TikTok banni ou suspendu","TikTok"),
        ("youtube","Chaîne YouTube","Chaîne YouTube - aide","Chaîne YouTube résiliée ou piratée","YouTube"),
        ("whatsapp","Numéro WhatsApp","Numéro WhatsApp - aide","Numéro WhatsApp banni","WhatsApp")],
 'nl': [("page","Facebookpagina","Facebookpagina - hulp","Facebookpagina uitgeschakeld of beperkt","Facebook"),
        ("tiktok","TikTok","TikTok-account - hulp","TikTok-account verbannen of geschorst","TikTok"),
        ("youtube","YouTube-kanaal","YouTube-kanaal - hulp","YouTube-kanaal beëindigd of gehackt","YouTube"),
        ("whatsapp","WhatsApp-nummer","WhatsApp-nummer - hulp","WhatsApp-nummer verbannen","WhatsApp")],
}
def q(x): return "'" + x.replace("\\","\\\\").replace("'","\\'") + "'"
for lang, rows in ADD.items():
    i = s.find(f"      {lang}: {{"); assert i >= 0, lang
    j = s.find("          ['other'", i); assert j > i
    ins = ''.join("          [" + ', '.join(q(v) for v in r) + "],\n" for r in rows)
    s = s[:j] + ins + s[j:]
old_inf = "      if (/snapchat/.test(s)) return 'snap';\n"
assert old_inf in s
s = s.replace(old_inf, old_inf +
  "      if (/tiktok/.test(s)) return 'tiktok';\n"
  "      if (/youtube/.test(s)) return 'youtube';\n"
  "      if (/whatsapp/.test(s)) return 'whatsapp';\n", 1)
old_fb = "      if (/facebook/.test(s)) return 'fb';\n"
assert old_fb in s
s = s.replace(old_fb, "      if (/facebook/.test(s)) return /facebook-page|page-recovery|-page-|pagina-facebook|page-facebook|facebookpagina/.test(s) ? 'page' : 'fb';\n", 1)
old_open = "    var open = function () {\n      if (!modal) build();\n      topic = infer();"
assert old_open in s
s = s.replace(old_open, "    var open = function (preset) {\n      if (!modal) build();\n      topic = (preset && find(preset)) ? preset : infer();", 1)
old_click = "      e.preventDefault();\n      open();\n    });"
assert old_click in s
s = s.replace(old_click, "      e.preventDefault();\n      open(a.getAttribute('data-topic'));\n    });", 1)
s = s.replace("// Email topic picker:", "// Email topic picker (v2, Nov 14: + Page/TikTok/YouTube/WhatsApp topics and data-topic preset):", 1)
h = hashlib.sha256(s.encode()).hexdigest()[:12]
out = pathlib.Path(f'assets/mail-pick.{h}.js'); out.write_text(s, encoding='utf-8')
print(h)
