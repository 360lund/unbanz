# Indexing inventory — 6 Nov 2026

Built from the files in this commit. Google Search Console and Bing Webmaster were not available, so this is not a coverage percentage and not proof of indexing.

| Check | Result |
| --- | --- |
| Sitemap `<url>` blocks | 1008 |
| Sitemap `<loc>` values | 1008 |
| HTML paths with `noindex` | 212 |
| Self-canonical indexable HTML paths | 1008 |
| Indexable alias paths (canonical points elsewhere) | 4 |
| Self-canonical indexable paths absent from sitemap `<loc>` | 0 |

The live audit on 6 Nov 2026 counted 1008 primary page locs and found no hard 1000 cap. This commit does not rebuild or truncate the sitemap. Intentional `noindex` is unchanged.

An HTTP 200 response, an IndexNow submission, or a line in `llms.txt` is not an indexed URL. Confirm indexing in Search Console URL Inspection or Bing Webmaster when those accounts are connected.

## Alias paths

- `/guides/ad-account-circumventing-systems/` → `/ad-account-disabled-circumventing-systems-help/`
- `/guides/ad-account-unacceptable-business-practices/` → `/ad-account-disabled-unacceptable-business-practices-help/`
- `/guides/instagram-account-disabled-for-no-reason/` → `/instagram-disabled-no-reason-given/`
- `/white-label-vs-in-house-account-recovery/` → `/white-label-vs-referral-vs-in-house-recovery/`

## Self-canonical indexable paths not listed as a sitemap loc

None. No sitemap rewrite was required.

## Country pages with no enquiry buttons

- `agency-client-account-banned-saudi-arabia/index.html` — Saudi Arabia — menu
- `facebook-account-disabled-saudi-arabia-what-to-do/index.html` — Saudi Arabia — fb
- `facebook-account-recovery-saudi-arabia/index.html` — Saudi Arabia — fb
- `instagram-account-recovery-saudi-arabia/index.html` — Saudi Arabia — ig
- `instagram-disabled-saudi-arabia-what-to-do/index.html` — Saudi Arabia — ig
- `instagram-hacked-saudi-arabia-what-to-do/index.html` — Saudi Arabia — ig
- `instagram-suspended-appeal-saudi-arabia/index.html` — Saudi Arabia — ig
- `instagram-username-claim-saudi-arabia/index.html` — Saudi Arabia — username
- `meta-ad-account-disabled-saudi-arabia/index.html` — Saudi Arabia — ad
- `meta-appeal-links-saudi-arabia/index.html` — Saudi Arabia — info
- `pt-br/falar-com-o-instagram-ou-a-meta-no-brasil/index.html` — Brazil — info
- `pt-br/onde-denunciar-golpes-e-crimes-online-no-brasil/index.html` — Brazil — info
- `pt-br/white-label-agencias-brasil/index.html` — Brazil — agency
- `snapchat-account-locked-saudi-arabia/index.html` — Saudi Arabia — snap
- `snapchat-hacked-saudi-arabia-what-to-do/index.html` — Saudi Arabia — snap
- `white-label-agency-brazil/index.html` — Brazil — agency
- `white-label-agency-saudi-arabia/index.html` — Saudi Arabia — agency

No public landing page was found for Mexico, Afghanistan, Iran, Iraq or Indonesia. Nothing was invented for those countries.
