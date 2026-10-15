import express from 'express';
import { createServer as createViteServer } from 'vite';
import path from 'path';
import { fileURLToPath } from 'url';
import crypto from 'crypto';
import dotenv from 'dotenv';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json({ limit: '1mb' }));

// In-memory demo lead database synced with admin desk
export interface Lead {
  id: number;
  name: string;
  handle: string;
  email: string;
  phone: string;
  service: string;
  status: 'New' | 'In progress' | 'Closed';
  date: string;
  message: string;
  note?: string;
}

const initialSeedLeads: Lead[] = [
  { id: 1, name: 'Alex Morgan', handle: '@alex.example', email: 'alex@example.com', phone: '+1 415 555 0192', service: 'Instagram unban', status: 'New', date: 'Today', message: 'Account was disabled 48 hours ago for alleged community guidelines violation. Over 85k followers, verified business email attached.' },
  { id: 2, name: 'Maya Chen', handle: '@studio.design', email: 'maya@studio.com', phone: '+1 310 555 0144', service: 'Instagram username claim', status: 'New', date: 'Today', message: 'Looking to claim inactive username @studio. Trademark registration number US-882910.' },
  { id: 3, name: 'Omar Ali', handle: 'Apex Brand Ad Account #9281', email: 'omar@apex.co', phone: '+44 20 7946 0912', service: 'Ad account unban', status: 'In progress', date: 'Yesterday', message: 'E-commerce Meta Business Manager disabled right before product launch. High monthly spend history.' },
  { id: 4, name: 'Sofia Reed', handle: '@sofia.reed', email: 'sofia@reedmedia.com', phone: '+1 212 555 0188', service: 'Facebook unban', status: 'In progress', date: 'Yesterday', message: 'Personal Facebook profile disabled which restricts admin access to client business pages.' },
  { id: 5, name: 'Noah Park', handle: '@noahpark.official', email: 'noah@parkholdings.com', phone: '+1 650 555 0177', service: 'Ban request — genuine policy violation', status: 'New', date: 'Yesterday', message: 'Malicious impersonator created duplicate account scamming clients via direct messages.' },
  { id: 6, name: 'Amira Khan', handle: '@amira.k', email: 'amira@example.com', phone: '+971 4 555 0122', service: 'Instagram username claim', status: 'Closed', date: '2 days ago', message: 'Secured dormant 6-letter first-name handle after trademark documentation submission.' },
  { id: 7, name: 'Ethan Cole', handle: 'Cole & Sons Fine Art', email: 'ethan@colesons.com', phone: '+1 312 555 0165', service: 'Page access & ownership', status: 'In progress', date: '2 days ago', message: 'Former marketing contractor left agency without releasing Page Ownership admin permissions.' },
  { id: 8, name: 'Leila Hassan', handle: '@leila_h', email: 'leila@atelier.fr', phone: '+33 1 42 68 55 00', service: 'Instagram unban', status: 'Closed', date: '3 days ago', message: 'Successfully restored creator profile after false positive AI automated ban.' }
];

let leads: Lead[] = JSON.parse(JSON.stringify(initialSeedLeads));
let nextLeadId = 9;

// Application API routes
const validServices = new Set([
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

// Check readiness
app.get('/api/application', (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  const ready = Boolean(process.env.RESEND_API_KEY && process.env.APPLICATION_FROM);
  res.status(200).json({ ready });
});

// Submit application
app.post('/api/application', async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  const ready = Boolean(process.env.RESEND_API_KEY && process.env.APPLICATION_FROM);

  const data = req.body;
  if (!data || typeof data !== 'object' || JSON.stringify(data).length > 5000) {
    return res.status(400).json({ error: 'Invalid application' });
  }

  // Honeypot check
  if (data.company) {
    return res.status(400).json({ error: 'Invalid application' });
  }

  const { service, account, email, details = '', name = '', phone = '' } = data;

  if (typeof name !== 'string' || name.length > 100 || typeof phone !== 'string' || phone.length > 30) {
    return res.status(400).json({ error: 'Invalid contact details' });
  }

  if (
    !validServices.has(service) ||
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

  // Record in lead desk
  const newLead: Lead = {
    id: nextLeadId++,
    name: name.trim() || account.trim(),
    handle: account.trim(),
    email: email.trim(),
    phone: phone.trim() || 'Not provided',
    service,
    status: 'New',
    date: 'Just now',
    message: details.trim() || 'Case submission from website form.'
  };
  leads.unshift(newLead);

  // If email provider is configured, send email via Resend
  if (ready) {
    const text = `Service: ${service}\nAccount: ${account.trim()}\nReply email: ${email}\nName: ${name}\nPhone: ${phone}\n\n${details.trim()}`;
    const key = crypto.createHash('sha256').update(text + Math.floor(Date.now() / 3600000)).digest('hex');

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

      const result = (await response.json()) as { id?: string; error?: unknown };
      if (!response.ok || !result.id) {
        return res.status(502).json({ error: 'Delivery could not be confirmed' });
      }

      return res.status(200).json({ accepted: true, leadId: newLead.id });
    } catch {
      return res.status(502).json({ error: 'Delivery could not be confirmed' });
    }
  }

  // Local/preview mode fallback: accepted and logged to Lead Desk
  return res.status(200).json({
    accepted: true,
    simulated: true,
    leadId: newLead.id,
    message: 'Application received and recorded in Unbanz Lead Desk.'
  });
});

// Lead desk management APIs
app.get('/api/leads', (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  res.json({ leads });
});

app.patch('/api/leads/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const lead = leads.find((l) => l.id === id);
  if (!lead) return res.status(404).json({ error: 'Lead not found' });

  const { status, note } = req.body;
  if (status && ['New', 'In progress', 'Closed'].includes(status)) {
    lead.status = status;
  }
  if (typeof note === 'string') {
    lead.note = note;
  }
  res.json({ success: true, lead });
});

app.post('/api/leads/reset', (req, res) => {
  leads = JSON.parse(JSON.stringify(initialSeedLeads));
  res.json({ success: true, leads });
});

async function startServer() {
  const isProd = process.env.NODE_ENV === 'production';

  if (!isProd) {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: 'spa'
    });
    app.use(vite.middlewares);
  } else {
    app.use(express.static(path.resolve(__dirname, 'dist')));
    app.get('*', (req, res) => {
      res.sendFile(path.resolve(__dirname, 'dist', 'index.html'));
    });
  }

  app.listen(PORT, () => {
    console.log(`Unbanz server running at http://localhost:${PORT}`);
  });
}

startServer();
