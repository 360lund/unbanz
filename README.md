# Unbanz — React Application

Unbanz is a high-performance React application for Instagram and Facebook account recovery, Meta Business ad account unbans, trademark and username claim acquisitions, and genuine policy violation ban requests.

## Architecture & Features

- **React SPA with TypeScript & Vite**: Fast modular components, typed client-side routing, responsive layouts.
- **Express Backend Server (`server.ts`)**:
  - Handles `/api/application` case submissions with strict validation and idempotency.
  - Optional production integration with Resend API for automated email notifications.
  - Interactive simulated demo mode when API keys are omitted.
  - Full Lead Desk backend API (`/api/leads`, `/api/leads/:id`, `/api/leads/reset`).
- **Pages & Routes**:
  - `/` (Home): Overview of services, consultation process, trust metrics, and FAQs.
  - `/unban`: Dedicated landing page for Instagram and Facebook account recovery, Terms of Service appeals, and Ad account unbans.
  - `/username`: Instagram username claim acquisition requirements, dormant handle criteria, and trademark priority.
  - `/ban`: Genuine policy violation ban requests, impersonation takedowns, and copyright abuse enforcement.
  - `/apply`: Interactive case review intake form with validation, character limits, honeypot protection, and case reference generation.
  - `/admin`: Interactive Lead Desk with preview authentication (`preview`), filtering (All, New, In progress, Closed), live search, status updates, and specialist notes.
- **Styling**: Tailwind CSS with custom brand palette (`#18334a` navy, `#599fe0` brand blue, `#f5f9fc` sky background).

## Development & Build

```bash
# Run full-stack dev server (port 3000)
npm run dev

# Run test suite
npm test

# Build for production
npm run build

# Start production server
npm start
```
