# Nov 20 2026: add a WhatsApp mode to the email topic picker (same topics, same 2 steps, same design).
# window.unbanzMailPick.open(topic, {wa: "<digits>"}) opens it in WhatsApp mode; the number is passed in at
# runtime by contact-policy.js (from /api/geo/, strict geo + time zone gate) and is never in this file.
import hashlib, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = os.path.join(ROOT, 'assets', sys.argv[1] if len(sys.argv) > 1 else 'mail-pick.b6c609ff4bd8.js')
s = open(src, encoding='utf8').read()

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:80], s.count(old))
    s = s.replace(old, new)

WA = r'''    var WA_T = {
      en: { eyebrow: 'WHATSAPP US', hint: 'Pick one and WhatsApp opens with your details filled in. Takes about a minute.', go: 'Continue on WhatsApp', note: 'Anything else we should know?', nph: 'e.g. disabled yesterday, already appealed once', nk: 'Details', page: 'Page' },
      nl: { eyebrow: 'WHATSAPP ONS', hint: 'Kies er één en WhatsApp opent met je gegevens al ingevuld. Duurt ongeveer een minuut.', go: 'Verder op WhatsApp', note: 'Nog iets dat we moeten weten?', nph: 'bijv. gisteren uitgeschakeld, al één keer bezwaar gemaakt', nk: 'Details', page: 'Pagina' },
      fr: { eyebrow: 'WHATSAPP', hint: 'Choisissez une option : WhatsApp s’ouvre avec vos informations déjà remplies.', go: 'Continuer sur WhatsApp', note: 'Autre chose à savoir ?', nph: 'ex. désactivé hier, déjà fait appel une fois', nk: 'Détails', page: 'Page' },
      es: { eyebrow: 'WHATSAPP', hint: 'Elige una opción y WhatsApp se abre con tus datos ya escritos.', go: 'Continuar en WhatsApp', note: '¿Algo más que debamos saber?', nph: 'p. ej. desactivada ayer, ya apelé una vez', nk: 'Detalles', page: 'Página' },
      pt: { eyebrow: 'WHATSAPP', hint: 'Escolha uma opção e o WhatsApp abre com seus dados já preenchidos.', go: 'Continuar no WhatsApp', note: 'Algo mais que devemos saber?', nph: 'ex.: desativada ontem, já recorri uma vez', nk: 'Detalhes', page: 'Página' },
      de: { eyebrow: 'WHATSAPP', hint: 'Wähle eine Option und WhatsApp öffnet sich mit deinen Angaben.', go: 'Weiter zu WhatsApp', note: 'Sonst noch etwas?', nph: 'z. B. gestern deaktiviert, schon einmal Einspruch eingelegt', nk: 'Details', page: 'Seite' },
      it: { eyebrow: 'WHATSAPP', hint: 'Scegli un’opzione e WhatsApp si apre con i tuoi dati già inseriti.', go: 'Continua su WhatsApp', note: 'Altro che dovremmo sapere?', nph: 'es. disattivato ieri, già fatto ricorso una volta', nk: 'Dettagli', page: 'Pagina' },
      ar: { eyebrow: 'واتساب', hint: 'اختر خيارًا وسيفتح واتساب مع بياناتك جاهزة.', go: 'المتابعة على واتساب', note: 'هل هناك شيء آخر يجب أن نعرفه؟', nph: 'مثلًا: عُطّل أمس، قدّمت طعنًا مرة', nk: 'تفاصيل', page: 'الصفحة' }
    };
    var W = WA_T[lang] || WA_T.en;
    var channel = 'mail', waNum = '', note, txt0 = null;
'''
rep("    var modal, sheet, lastFocus, topic = null, input, hear, go, step = 1, busy = false, scrollY = 0;\n",
    "    var modal, sheet, lastFocus, topic = null, input, hear, go, step = 1, busy = false, scrollY = 0;\n" + WA)

# Message for WhatsApp vs mailto.
rep("""      if (hear && hear.value) body += '\\nHow I heard about Unbanz: ' + hear.value;
      return 'mailto:'""", """      if (hear && hear.value) body += '\\nHow I heard about Unbanz: ' + hear.value;
      if (channel === 'wa') {
        var n = (note && note.value || '').replace(/\\s+/g, ' ').trim().slice(0, 400);
        var m = L.hi + '\\n\\n' + L.f[0] + ': ' + t[3] + '\\n' + L.f[1] + ': ' + (u || '-') + (n ? '\\n' + W.nk + ': ' + n : '') +
          (hear && hear.value ? '\\nHow I heard about Unbanz: ' + hear.value : '') + (window.unbanzViaTag ? '\\n' + String(window.unbanzViaTag).slice(0, 120) : '') + '\\n' + W.page + ': unbanz.com' + location.pathname;
        return 'https://wa.me/' + waNum + '?text=' + encodeURIComponent(m);
      }
      return 'mailto:'""")

# Note field (WhatsApp mode only), after the username input.
rep("""placeholder="' + esc(L.ph) + '">' +""",
    """placeholder="' + esc(L.ph) + '">' +
        '<div class="mp-wa-only"><label class="mp-label" for="mp-note">' + esc(W.note) + ' <span>' + esc(L.opt) + '</span></label>' +
        '<textarea id="mp-note" class="mp-input mp-ta" rows="2" maxlength="400" dir="auto" placeholder="' + esc(W.nph) + '"></textarea></div>' +""")
rep("      go = modal.querySelector('.mp-go');\n",
    "      go = modal.querySelector('.mp-go');\n      note = modal.querySelector('#mp-note');\n      note.addEventListener('input', function () { update(); });\n")

# open(preset, opts): pick channel, swap texts.
rep("""    var open = function (preset) {
      if (!modal) build();
      if (!modal.hidden && modal.classList.contains('is-open')) return;""",
"""    var setChannel = function (opts) {
      var wa = !!(opts && /^[0-9]{8,15}$/.test(String(opts.wa || '')));
      channel = wa ? 'wa' : 'mail'; waNum = wa ? String(opts.wa) : '';
      var eye = modal.querySelector('.mp-eye'), hint = modal.querySelector('.mp-hint');
      if (!txt0) txt0 = [eye.textContent, hint.textContent, go.innerHTML];
      modal.classList.toggle('mp-wa', wa);
      eye.textContent = wa ? W.eyebrow : txt0[0];
      hint.textContent = wa ? W.hint : txt0[1];
      go.innerHTML = wa ? esc(W.go) + ' <span aria-hidden="true">↗︎</span>' : txt0[2];
      if (wa) { go.setAttribute('target', '_blank'); go.setAttribute('rel', 'nofollow noopener'); }
      else { go.removeAttribute('target'); go.removeAttribute('rel'); }
      note.value = '';
    };
    var open = function (preset, opts) {
      if (!modal) build();
      if (!modal.hidden && modal.classList.contains('is-open')) return;
      setChannel(opts);""")

CSS_ADD = ".mp3:not(.mp-wa) .mp-wa-only{display:none}.mp3 .mp-ta{height:auto;min-height:76px;padding:12px 16px;line-height:1.45;resize:vertical}.mp3.mp-wa .mp-go{background:#1f9d55;border-color:#1f9d55;color:#fff}.mp3.mp-wa .mp-go:hover{background:#178a49;border-color:#178a49}.mp3.mp-wa .mp-prog i.on{background:#1f9d55}"
i = s.find('    var CSS = "'); j = s.find('";\n', i)
s = s[:j] + CSS_ADD + s[j:]
rep("    window.unbanzMailPick = { open: open, close: close };", "    window.unbanzMailPick = { open: open, close: close, wa: true };")
rep("// The plain mailto href stays as the no-JS fallback. Email is the only contact channel.",
    "// The plain mailto href stays as the no-JS fallback.\n// Nov 20 2026: WhatsApp mode (open(topic, {wa})) for eligible visitors only; number passed at runtime, never stored here.")
assert '447723' not in s
h = hashlib.sha256(s.encode()).hexdigest()[:12]
out = os.path.join(ROOT, 'assets', 'mail-pick.%s.js' % h)
open(out, 'w', encoding='utf8').write(s)
print(os.path.basename(out))
