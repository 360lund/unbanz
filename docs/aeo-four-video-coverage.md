# Four-video AEO coverage — what was implemented

Sources are the four transcripts in the 6 Nov pack. Tactics that are only in the Ahrefs course roadmap, not taught in the intro, are not described as if those modules were viewed. Speaker statistics are not used as Unbanz facts.

## Video 1 — Ross Simmonds, HubSpot, GEO seven steps

| Tactic | Where in the transcript | What the site does | How it was checked | Not done |
| --- | --- | --- | --- | --- |
| Same brands repeat across “best X” prompts | 00:00:00–00:00:31 | Existing comparison URLs stay (`/best-instagram-recovery-service/`, `/best-username-claim-service-{usa,canada,uk,france,netherlands}/`, `/compare/`). No new “we are number one” claim was added. | Canonicals and H1s match `main`. | No private-browser prompt screenshots. |
| Audit money keywords as customer questions; note who AI cites | 00:01:35 | Prompt list for a human to run, not a fake score. See the tracker section below. | The questions are the live page H1s and FAQ questions, not invented queries. | No Profound/Ahrefs Brand Radar pull. No weekly screenshots. |
| Answer first, then why, then detail | 00:02:53 | Username hub and services hub open with a short answer (`data-aeo="2026-11-06"`). Guide `/guides/instagram-account-suspended-appeal/` already starts “Short answer:”. Country fees state the price before the conditions. | Rendered username, services, and guide pages. | Not every one of the 1,200+ URLs was rewritten into a 50-word lede. |
| Bottom-of-funnel “best / top” pages | 00:02:53 | Those comparison URLs were already published. This pass did not add geo doorway “best” pages. | `test_country_cta_policy.py` still finds the USA/UK/France/Netherlands/Canada username comparison URLs with WhatsApp and email. | No new listicles. |
| FAQ schema that matches the visible FAQ | 00:04:57 and 00:07:04 | Country fee questions in the visible section match the FAQ/Offer JSON. Contact answers on those pages no longer tell people to open WhatsApp. | JSON parse on the Saudi and Brazil pages; `test_country_cta_policy.py`. | Rich Results Test was not run in Google’s tool. |
| Do not invent an author | 00:04:57 | About page says pages are published by Unbanz and there is no named individual author. Organization schema stays. No Person schema was added. | About H1 and canonical unchanged. | No author page with credentials, because no named author exists. |
| External reviews, Reddit, journalists, original surveys | 00:04:57 and 00:11:05 | Not done. Existing client videos stay on `/reviews/`. | No new review markup. | Requires the owner. No posts were made. |
| Speed, mobile, clean URLs, freshness | 00:07:04 | URLs and canonicals unchanged. Editorial CSS keeps one H1, labeled controls, and stops mobile page-level overflow from tables and the testimonial row. | Rendered 390px pass, overflow 0 on the checked set. | No lab speed score. The static host has no build step. |
| GEO template: query title, short answer, early facts, sources, FAQ, updated date | 00:08:19 | Username hub has the short answer, a fact list, and primary-source links (Instagram Help, hacked-account page, USPTO, CIPO, UK IPO, INPI, BOIP). The five buyer-country username comparisons link the local IP office. Many guides already show “Updated … 2026”. | Source check for `data-aeo="2026-11-06"` on those six URLs. | A chart in the first 200 words was not added. There is no new dataset to chart. |
| Weekly 20-prompt log and prioritization matrix | 00:10:06 | The prompt list below is the queue. It is not a filled scoreboard. | n/a | Nobody has run the prompts in private mode yet. |
| Contrarian “why switch”, latest-update blocks, off-site republishing, Wikipedia | 00:11:05 | Not done off-site. On-site “Updated” lines that already existed were left in place. | n/a | Needs the owner. Wikipedia was not edited. |
| Submit the sitemap | 00:12:15 | Sitemap file unchanged at 1,008 URLs. It was not resubmitted. | Byte compare with `main`. | Search Console and Bing are not connected. |

## Video 2 — CrowdReply walkthrough

| Tactic | Timestamp | Implemented | Tested | Not done |
| --- | --- | --- | --- | --- |
| Visibility score baseline | 00:00:43 | No score was invented. | n/a | No CrowdReply account. |
| Track many prompts, not a handful | 00:00:43–00:02:57 | 28 buyer questions are listed below for USA, Canada, UK, France, and the Netherlands. | They map to live URLs. | Not run across models. |
| Study citations and comparison pages; copy the format, not the words | 00:01:46–00:02:57 | Existing compare and “best service” pages kept. Fee pages now separate Instagram recovery, Facebook Marketplace, Facebook profiles, and Instagram ad restrictions. | Fee strings in HTML and Offer JSON. | No competitor page was copied. |
| Buy backlinks or brand placements | 00:04:38 | Not done. | n/a | Not authorized as a purchase. |

## Video 3 — Ahrefs, Sam Oh, course introduction only

The file is the course intro, about six minutes. Query fan-out, Brand Radar filters, and the later modules are named as upcoming lessons at 00:04:49–00:06:14. They were not taught in this transcript and were not implemented from it.

| What the intro actually says | Timestamp | What we did | What we did not do |
| --- | --- | --- | --- |
| SEO is the foundation of AEO | 00:00:00 | Kept canonicals, sitemap, robots, and indexable URLs. | Did not chase a new SEO rewrite of every page. |
| AI Overviews cut the #1 click rate; Ahrefs signup share | 00:00:24 | Not printed on the site. | Those figures are the speaker’s, not Unbanz measurements. |
| AEO means being mentioned in the answer, including GEO/LLMO | 00:01:19–00:02:05 | Pages answer the question in the H1 and the opening. `llms.txt` only lists indexable canonical URLs. | No claim that Unbanz is already cited. |
| AI search can grow beside Google | 00:03:07 | Google SEO was not removed. AI bots stay allowed in `robots.txt`. | n/a |
| Mentions can come from ordinary useful pages | 00:04:03 | Useful guides and the fee/answer blocks stay on the existing URLs. | The “7,470 mentions” line is Ahrefs’ number, not ours. |
| Roadmap: mechanics, mentions, content, technical, measurement | 00:04:49–00:06:14 | Used only as a label for the on-site work above. | Module lessons after the intro were not in the pack. |

## Video 4 — Ethan Smith, Lenny’s Podcast

| Tactic | Timestamp in the pack | Implemented | Tested | Not done |
| --- | --- | --- | --- | --- |
| Mentions matter more than one blue link | 00:00:00–00:00:20 | No single-URL “rank #1” claim. Comparison and service hubs stay. | Existing URLs still canonical. | Off-site mention campaign. |
| Early mentions on Reddit, YouTube, blogs | 00:00:27–00:00:32 | Not posted. | n/a | Needs the owner. |
| Head prompts vs long specific questions | 00:10:46–00:14:31 | Hubs answer the short question and link the longer country and situation pages. | Username hub links to USA, Canada, UK, France, Netherlands. | n/a |
| On-site long-tail; off-site video and affiliates | 00:15:38–00:16:32 | Long-tail guides were kept. No new affiliate program. | URL set unchanged. | Off-site. |
| Reddit without bots, with disclosure | 00:16:43–00:18:54 | Not posted. | n/a | Needs the owner. |
| Optimize for retrieval, not training-data spam | 00:20:20–00:21:24 | No doorway pages. Noindex geos stay noindex and out of `llms.txt`. | llms no longer contains `/instagram-username-claim-australia/`. | n/a |
| Topics that answer several questions; avoid rewrite loops | 00:21:45–00:27:59 | Fee and answer blocks were added to existing URLs. Bodies of guides were not mass-rewritten. | Title/H1/canonical/robots diff vs `main` is empty. | n/a |
| Seven-step operating system and share of voice | 00:29:02–00:36:01 | The prompt queue is the tracker. It has no filled scores. | n/a | No control experiment. |
| “How did you hear about us?”, including an AI assistant | 00:38:35–00:40:00 | Optional control on the existing WhatsApp and email pickers. The line is added only to the message the visitor sends. Country pages with no picker do not get one. | Rendered contact and username-hub flows. | Not a new backend field. |
| Allow index bots; do not block all of GPTBot | 00:42:10–00:42:56 | `robots.txt` unchanged. GPTBot, OAI-SearchBot, Perplexity, Claude, Google-Extended stay allowed. | Byte compare with `main`. | n/a |
| Pure AI pages fail; assisted pages need a human edit | 00:51:45–00:55:01 | Fee sentences name the service, the limit, and the non-guarantee. No bulk city pages. | Copy review of the fee strings. | n/a |
| Help center on the same host, linked from hubs | 01:00:49–01:03:15 | `/guides/` stays on unbanz.com. Services hub links the appeal directory and the recovery hubs. | Rendered `/services/`. | n/a |

## Prompt queue (not a score)

Run in a private window. Record the date, the tool, whether Unbanz is named, and which domains are cited. Do not treat a single run as a ranking.

1. Who can help with a disabled Instagram account in the United States?
2. How do I appeal a suspended Instagram account?
3. My Facebook profile is disabled. What are the official steps?
4. What is a fair fee to recover one disabled Instagram account?
5. Is Facebook Marketplace the same service as an Instagram account recovery?
6. How much does a Facebook Marketplace recovery cost compared with a Facebook profile?
7. What does an Instagram ad-account restriction cost to appeal?
8. Is a Business Portfolio restriction the same fee as one Instagram ad account?
9. How do I claim an inactive Instagram username, and what does it cost?
10. Can someone guarantee an Instagram username?
11. Best Instagram username claim service in the United States.
12. Best Instagram username claim service in Canada.
13. Best Instagram username claim service in the UK.
14. Best Instagram username claim service in France.
15. Best Instagram username claim service in the Netherlands.
16. How do I contact Meta about a disabled account if I am in Brazil?
17. Where do I report an online scam in Brazil?
18. Does a white-label recovery partner publish one flat fee?
19. Instagram account disabled in Saudi Arabia. What are the official steps?
20. Facebook account disabled in Saudi Arabia.
21. Meta ad account disabled in Saudi Arabia.
22. Is Unbanz affiliated with Meta?
23. What should I send for an Instagram appeal, and should I include my password?
24. Instagram suspended: how to appeal before the deadline.
25. Disabled Instagram account for someone in Canada.
26. Disabled Facebook account for someone in the UK.
27. Disabled Instagram account for someone in France.
28. Disabled Instagram account for someone in the Netherlands.

## Buyer-country paths these questions point at

- `/instagram-username-claim/`, `/username/`, `/services/`, `/contact/`
- `/best-username-claim-service-usa/` and the Canada, UK, France, and Netherlands twins
- `/guides/instagram-account-suspended-appeal/`
- `/instagram-account-recovery-saudi-arabia/`, `/facebook-account-recovery-saudi-arabia/`, `/meta-ad-account-disabled-saudi-arabia/`
- `/white-label-agency-brazil/`, `/pt-br/white-label-agencias-brasil/`, `/pt-br/falar-com-o-instagram-ou-a-meta-no-brasil/`, `/pt-br/onde-denunciar-golpes-e-crimes-online-no-brasil/`
