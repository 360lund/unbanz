# Pre-release QA — 6 Nov 2026

This pass stays on `cursor/unbanz-editorial-aeo-6199`. It does not merge and it does not promote production.

## Preservation against `main` (`bc3800e0`)

Compared all 1,225 HTML files with `main` for `<title>`, canonical, robots, and the first `<h1>`. **0 differences.**

`sitemap.xml` and `robots.txt` are byte-identical to `main`. The sitemap still has 1,008 `<url>` blocks. AI crawlers stay allowed. Intentional `noindex` was not removed.

`llms.txt` drops 148 noindex URLs and retargets 4 aliases to their canonicals. That matches the corrected 6 Nov audit. A line in `llms.txt` or an HTTP 200 is not an indexed URL. Google Search Console and Bing Webmaster were not connected, so there is no coverage percentage.

## Fee correction

Marketplace is Facebook Marketplace, not an Instagram feature. Visible copy and Offer schema no longer say “Instagram Marketplace”.

| Service | Fee | What it is not |
| --- | --- | --- |
| One disabled, suspended or hacked Instagram account | $800 | Not Marketplace, not a portfolio, not two accounts |
| One Facebook Marketplace case | $800 | Not the Instagram account fee |
| One disabled, suspended or hacked Facebook profile | $900 | Does not include Marketplace |
| One Instagram ad-account restriction | $1,200 | Not a Business Portfolio and not a two-account case |
| Instagram username claim | Priced after the handle is reviewed | Not $800, $900 or $1,200 |

The same menu is on the Saudi ad-account page, the Saudi agency-client page, and the white-label pages for **Brazil (English and Portuguese)** and **Saudi Arabia**. Those white-label pages say the figures are individual service fees, not a white-label retainer.

These Brazil and Saudi pages stay without a product fee because they are not those services: the Brazil “how to contact Meta” guide, the Brazil crime-reporting guide, the Saudi appeal-link directory, and the two Saudi Snapchat pages. Mexico, Afghanistan, Iran, Iraq and Indonesia still have no country landing page.

## Rendered enquiry check

`node scripts/qa_render_cta.mjs` loads the pages in headless Chrome after scripts run.

- All 17 low-priority country pages: no `wa.me` link, no `mailto:` link, no sticky contact bar, in the rendered DOM.
- Contact, the Instagram username hub, Canada Facebook recovery, Italy Instagram recovery, and Services still render both WhatsApp and email.
- Contact → WhatsApp picker topics: Unban my account, Ban an account, Username claim, Ad account, Other, plus Instagram, Facebook, Snapchat. The optional “How did you hear about us?” control is in that dialog.
- Username hub → email picker topics include Username, Instagram disabled, Instagram hacked, Facebook, ad account, Business Portfolio, Snapchat, and Other, plus the same optional source control.
- Saudi recovery does not gain an enquiry link after the page scripts run.

Mobile width 390: no horizontal page overflow after tables and the testimonial row scroll inside their own boxes. Each checked page has one `h1`. Images in those checks had `alt`.

## Build

`package.json` has no site build. `vercel.json` sets framework null, an empty build command, and output directory `.`. The check that stands in for a build is `python3 scripts/test_country_cta_policy.py`, `node --check` on the new scripts, and the rendered Chrome pass above.

## Not done, and not claimed

No Search Console or Bing submission. No IndexNow ping in this pass. No Reddit, YouTube, journalist, or paid-placement work. No weekly prompt screenshots from ChatGPT or Perplexity. No invented reviews, authors, offices, or guarantees. Speaker statistics from the four videos are not printed on the site as Unbanz facts.
