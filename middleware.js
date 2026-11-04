// Vercel Routing Middleware (no framework, Web API only).
// GEO-BLOCK DISABLED. Previously blocked visitors from a country list
// with a small self-contained 403 page. Every other request (including
// requests with no country header) passes through untouched, so static
// files, vercel.json headers, redirects and the 404 page behave as before.

// The owner is in Pakistan: the private /users dashboard and its data API stay reachable from PK only.
const OWNER_COUNTRY = 'PK';
const OWNER_PATHS = /^\/(?:users\/?|api\/users\/.*|assets\/.*)$/i;

const BLOCK_PAGE = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Unavailable in your region | Unbanz</title><style>html,body{margin:0;height:100%}body{display:flex;align-items:center;justify-content:center;padding:24px;box-sizing:border-box;background:#f7fafc;color:#25415d;font-family:'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased;text-align:center}main{max-width:420px}.w{font-size:28px;font-weight:700;letter-spacing:-.04em;margin:0 0 20px}h1{font-size:22px;font-weight:400;letter-spacing:-.02em;line-height:1.3;margin:0}</style></head><body><main><p class="w">unbanz.</p><h1>unbanz.com isn’t available in your region.</h1></main></body></html>`;

export const config = {
  // Run on every path, including /assets/*, so nothing is served to blocked regions.
  matcher: '/(.*)',
};

// Known AI assistants and search crawlers: their fetchers can sit in (or be geolocated to)
// blocked regions, so they are never geo-blocked. Human visitors are unaffected.
const BOT_UA = /(ChatGPT-User|OAI-SearchBot|GPTBot|PerplexityBot|Perplexity-User|ClaudeBot|Claude-User|Claude-SearchBot|anthropic-ai|Google-Extended|Googlebot|Google-InspectionTool|GoogleOther|Storebot-Google|bingbot|BingPreview|msnbot|adidxbot|Applebot|DuckDuckBot|DuckAssistBot|YandexBot|Amazonbot|meta-externalagent|meta-externalfetcher|facebookexternalhit|MistralAI-User|cohere-ai|YouBot|PhindBot|xAI|Grok|Bravebot|CCBot|Diffbot)/i;
const SHORT = { '/testimonials': '/reviews/', '/review': '/reviews/' };

const NAMES = ['OAI-SearchBot','ChatGPT-User','GPTBot','Claude-SearchBot','Claude-User','ClaudeBot','anthropic-ai','Perplexity-User','PerplexityBot','Google-Extended','Google-InspectionTool','GoogleOther','Googlebot','BingPreview','Applebot-Extended','Applebot','DuckAssistBot','DuckDuckBot','Amazonbot','meta-externalfetcher','meta-externalagent','facebookexternalhit','MistralAI-User','cohere-ai','YouBot','PhindBot','xAI-Bot','Grok','Bravebot','CCBot','YandexBot'];
const ASSET = /^\/(assets\/|api\/|users)|\.(css|js|png|jpe?g|webp|svg|ico|woff2?|mp4|webmanifest)$/i;
function botName(ua) {
  if (!BOT_UA.test(ua)) return null;
  const l = ua.toLowerCase();
  for (const n of NAMES) if (l.includes(n.toLowerCase())) return n;
  return /bingbot|msnbot|adidxbot/i.test(ua) ? 'Bingbot' : null;
}

export default function middleware(request, context) {
  const url = new URL(request.url);
  const path = url.pathname.replace(/\/+$/, '') || '/';
  // Log AI and search crawler page fetches after the response (waitUntil), so pages are not delayed.
  try {
    const bot = botName(request.headers.get('user-agent') || '');
    if (bot && !ASSET.test(url.pathname) && context && typeof context.waitUntil === 'function') {
      context.waitUntil(fetch(new URL('/api/crawl/', url.origin), { method: 'POST', headers: { 'content-type': 'application/json', 'x-ubz-mw': '1' }, body: JSON.stringify({ bot, path: url.pathname, country: request.headers.get('x-vercel-ip-country') || '', test: url.searchParams.get('ubz_test') === '1' }) }).catch(() => {}));
    }
  } catch (e) {}
  // Never serve installed packages or manifests as static files (outputDirectory is the repo root).
  if (/^\/(node_modules(\/|$)|package(-lock)?\.json$)/i.test(url.pathname)) return new Response('Not found', { status: 404, headers: { 'X-Robots-Tag': 'noindex' } });
  if (SHORT[path]) {
    return new Response(null, { status: 301, headers: { Location: new URL(SHORT[path], request.url).toString(), 'Cache-Control': 'public, max-age=3600' } });
  }
  // Geo-block disabled 2026-10-23: all countries and paths pass through.
  return;
}
