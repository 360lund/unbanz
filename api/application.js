import { createHash } from 'node:crypto';

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  const ready = Boolean(process.env.RESEND_API_KEY && process.env.APPLICATION_FROM);
  if (req.method === 'GET') return res.status(200).json({ ready });
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'GET, POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }
  if (!ready) return res.status(503).json({ error: 'Email delivery is not configured' });
  if (!String(req.headers['content-type'] || '').includes('application/json')) {
    return res.status(415).json({ error: 'JSON required' });
  }
  const origin = req.headers.origin;
  if (origin) {
    try {
      if (new URL(origin).host !== req.headers.host) {
        return res.status(403).json({ error: 'Origin rejected' });
      }
    } catch {
      return res.status(403).json({ error: 'Origin rejected' });
    }
  }
  let data;
  try {
    data = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  } catch {
    return res.status(400).json({ error: 'Invalid application' });
  }
  if (!data || typeof data !== 'object' || JSON.stringify(data).length > 5000) {
    return res.status(400).json({ error: 'Invalid application' });
  }
  if (data.company) return res.status(400).json({ error: 'Invalid application' });
  const services = new Set([
    'Instagram unban',
    'Facebook unban',
    'Instagram & Facebook unbans',
    'Ad account unban',
    'Hacked account recovery',
    'Instagram username claim',
    'Ban request — genuine policy violation',
    'Page access & ownership',
    'Impersonation & content reports',
    'Profile & name changes',
    'Something else'
  ]);
  const { service, account, email, details = '', name = '', phone = '' } = data;
  if (typeof name !== 'string' || name.length > 100 || typeof phone !== 'string' || phone.length > 30) {
    return res.status(400).json({ error: 'Invalid contact details' });
  }
  if (
    !services.has(service) ||
    typeof account !== 'string' ||
    account.trim().length < 2 ||
    account.length > 240 ||
    typeof email !== 'string' ||
    email.length > 254 ||
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ||
    /[\r\n]/.test(email) ||
    typeof details !== 'string' ||
    details.length > 1200
  ) {
    return res.status(400).json({ error: 'Check your application details' });
  }
  const text = `Service: ${service}\nAccount: ${account.trim()}\nReply email: ${email}\nName: ${name}\nPhone: ${phone}\n\n${details.trim()}`;
  // Stable retries within one hour avoid duplicate deliveries. This is not a rate limiter.
  const key = createHash('sha256').update(text + Math.floor(Date.now() / 3600000)).digest('hex');
  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
        'Idempotency-Key': key
      },
      body: JSON.stringify({
        from: process.env.APPLICATION_FROM,
        to: ['team@unbanz.com'],
        reply_to: email,
        subject: `Unbanz application — ${service}`,
        text
      }),
      signal: AbortSignal.timeout(10000)
    });
    const result = await response.json();
    if (!response.ok || !result.id) return res.status(502).json({ error: 'Delivery could not be confirmed' });
    return res.status(200).json({ accepted: true });
  } catch {
    return res.status(502).json({ error: 'Delivery could not be confirmed' });
  }
}
