"""Strip our own WhatsApp contact (wa.me links, +1 934 201 2490, WhatsApp-contact copy) from built static HTML/TXT.
Idempotent. Usage: python3 run_all.py <site_root> [...]. Keeps WhatsApp-as-a-service mentions.
Added Nov 15 2026 after the user's WhatsApp was restricted: contact is email only (team@unbanz.com)."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
for s in ['strip_anchors.py', 'strip_jsonld.py', 'strip_text.py', 'strip_copy.py', 'strip_copy2.py', 'strip_copy3.py', 'strip_copy4.py']:
    subprocess.check_call([sys.executable, os.path.join(HERE, s)] + sys.argv[1:])
