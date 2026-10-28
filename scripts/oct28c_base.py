# -*- coding: utf-8 -*-
"""Shared helpers for the 2026-10-28 country pages (rendered by build_oct28c_pages.py)."""
import oct27_content as o
from oct27_content import A, sec, ul, ol, PAGES, IG_REL, FB_REL, PASSWORD_IG, PASSWORD_FB, CONTACT_FAQ, CAN_FAQ, ig_hf, fb_hf
from oct27b_content_a import ACE
DATE = '2026-10-28'
del PAGES[:]  # importing the earlier content modules registered their pages; keep only the new ones

def igp(slug, cc, place, desc, hero, answer, first, local_h, local, extra, who_items, faq, relq):
    o.country('instagram-account-recovery-' + slug, cc, 'Instagram',
      'Instagram Account Recovery in %s | Unbanz' % place, desc,
      'Instagram account recovery in %s.' % place, 'Instagram account recovery %s' % place.replace('the ', ''),
      hero, answer, first, local_h, local, extra, who_items, faq, IG_REL, relq)

def fbp(slug, cc, place, desc, hero, answer, first, local_h, local, extra, who_items, faq, relq):
    o.country('facebook-account-recovery-' + slug, cc, 'Facebook',
      'Facebook Account Recovery in %s | Unbanz' % place, desc,
      'Facebook account recovery in %s.' % place, 'Facebook account recovery %s' % place.replace('the ', ''),
      hero, answer, first, local_h, local, extra, who_items, faq, FB_REL, relq)

def ig_ans(place, tail):
    return ('Instagram account recovery in %s starts with Instagram’s own routes: request a review on a disabled notice, or use instagram.com/hacked if someone took over the account. %s Unbanz helps you appeal through Meta’s official process; Meta makes the final decision.' % (place, tail))
def fb_ans(place, tail):
    return ('Facebook account recovery in %s follows Facebook’s own routes: disagree with the decision on a suspension notice within the time shown, or use facebook.com/hacked for a hijacked account. %s Unbanz helps you appeal through Meta’s official process; Meta makes the final decision.' % (place, tail))

DSA = lambda coord, extra_sentence='': ('<h2 id="eu">Your rights as an EU user</h2><p>Under the Digital Services Act, Instagram and Facebook must offer an internal complaint route against many account decisions and tell users about out-of-court dispute bodies. %s Appeals Centre Europe is one certified body that accepts some content and account decisions from EU users. It does not cover hacked accounts or decisions based on how an account behaved, and it does not replace the in-app review. Use the in-app route first.%s</p>' % (coord, extra_sentence))
