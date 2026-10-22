// Vercel Routing Middleware (no framework, Web API only).
// Blocks visitors whose edge-geolocated country is in BLOCKED_COUNTRIES
// with a small self-contained 403 page. Every other request (including
// requests with no country header) passes through untouched, so static
// files, vercel.json headers, redirects and the 404 page behave as before.

const BLOCKED_COUNTRIES = new Set(['IN', 'BD', 'NP', 'NG', 'PK']);
// The owner is in Pakistan: the private /users dashboard and its data API stay reachable from PK only.
const OWNER_COUNTRY = 'PK';
const OWNER_PATHS = /^\/(?:users\/?|api\/users\/.*|assets\/.*)$/i;

const BLOCK_PAGE = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Unavailable in your region | Unbanz</title><style>html,body{margin:0;height:100%}body{display:flex;align-items:center;justify-content:center;padding:24px;box-sizing:border-box;background:#f7fafc;color:#25415d;font-family:'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased;text-align:center}main{max-width:420px}.w{font-size:28px;font-weight:700;letter-spacing:-.04em;margin:0 0 20px}h1{font-size:22px;font-weight:400;letter-spacing:-.02em;line-height:1.3;margin:0}</style></head><body><main><p class="w">unbanz.</p><h1>unbanz.com isn’t available in your region.</h1></main></body></html>`;

export const config = {
  // Run on every path, including /assets/*, so nothing is served to blocked regions.
  matcher: '/(.*)',
};

export default function middleware(request) {
  const country = (request.headers.get('x-vercel-ip-country') || '').toUpperCase();
  if (!country || !BLOCKED_COUNTRIES.has(country)) {
    return; // continue to the static site unchanged
  }
  if (country === OWNER_COUNTRY && OWNER_PATHS.test(new URL(request.url).pathname)) return;
  return new Response(BLOCK_PAGE, {
    status: 403,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'private, no-store',
      'X-Robots-Tag': 'noindex',
      'X-Content-Type-Options': 'nosniff',
      'Referrer-Policy': 'strict-origin-when-cross-origin',
    },
  });
}
