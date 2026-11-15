"""Build assets/mail-pick.<hash>.js (email topic picker v3) from main.js + strings.js + picker.css.
Run from the repo root: python3 scripts/nov15_picker/build.py  -> prints the new path.
Then point pages at it: python3 scripts/nov15_picker/swap.py mail-pick.<hash>.js (edit its root path) and update
MAIL in scripts/apply_visitor_contact.py. Never delete old hashed files."""
import hashlib, json, re, pathlib
D = pathlib.Path(__file__).resolve().parent
ROOT = D.parent.parent
js = (D / 'main.js').read_text()
css = re.sub(r'\n', '', (D / 'picker.css').read_text())
js = js.replace('/*STRINGS*/', (D / 'strings.js').read_text().rstrip('\n'))
js = js.replace("'/*CSS*/'", json.dumps(css, ensure_ascii=False))
h = hashlib.sha256(js.encode()).hexdigest()[:12]
out = ROOT / 'assets' / ('mail-pick.%s.js' % h)
out.write_text(js, encoding='utf-8')
print(out)
