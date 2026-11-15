import re, sys
BTN = {
 "'Message us on WhatsApp'": "'Email us'",
 "'Écrivez-nous sur WhatsApp'": "'Écrivez-nous par e-mail'",
 "'Stuur ons een bericht op WhatsApp'": "'Mail ons'",
 "'Escríbenos por WhatsApp'": "'Escríbenos por correo'",
 "'Mande uma mensagem no WhatsApp'": "'Envie um e-mail'",
}
def cut_block(t, marker, repl=''):
    i = t.find(marker)
    if i < 0: return t, False
    # start at beginning of line
    i = t.rfind('\n', 0, i) + 1
    j = t.find('\n})();', i)
    if j < 0: return t, False
    j += len('\n})();')
    if j < len(t) and t[j] == '\n': j += 1
    return t[:i] + repl + t[j:], True
def patch(t):
    t, a = cut_block(t, '// Mobile primary CTA:', '// Mobile WhatsApp CTA removed (Nov 15 2026): contact is email only.\n')
    t, b = cut_block(t, '// Contact modal:', '// WhatsApp contact modal removed (Nov 15 2026): contact is email only.\nwindow.unbanzContact = { open() {}, close() {} };\n')
    t = t.replace("const WA = 'https://wa.me/19342012490';", "const WA = 'mailto:team@unbanz.com';")
    t = t.replace("a.href = `${WA}?text=${encodeURIComponent(", "a.href = `${WA}?subject=Account%20help&body=${encodeURIComponent(")
    t = t.replace("a.href = `https://wa.me/${CFG.wa}?text=${encodeURIComponent(", "a.href = `mailto:${CFG.email}?subject=${encodeURIComponent(CFG.Name)}&body=${encodeURIComponent(")
    t = t.replace("a.append('Message us on WhatsApp ');", "a.append('Email us ');")
    t = t.replace('"wa": "19342012490", ', '')
    t = re.sub(r'const PRIORITY = new Set\(\[[^\]]*\]\);', 'const PRIORITY = new Set([]); // Nov 15 2026: WhatsApp contact removed for every country; email only.', t)
    for k, v in BTN.items():
        t = t.replace("btn: " + k, "btn: " + v)
    t = t.replace("team@kx.com", "team@unbanz.com")
    return t
if __name__ == '__main__':
    for p in sys.argv[1:]:
        o = open(p, encoding='utf-8').read(); n = patch(o)
        open(p, 'w', encoding='utf-8').write(n)
        print(p, 'changed' if n != o else 'same', 'left:', len(re.findall(r'19342012490|wa\.me/\$\{|Continue on WhatsApp', n)))
