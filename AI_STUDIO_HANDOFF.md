# Unbanz — Firebase handoff

Preserve the current page layouts, typography, local images, colors, rounded surfaces, animation timing and mobile behavior. Do not regenerate the design. The frontend is in dist/. The routes are /, /unban/, /username/, /ban/, /apply/ and /admin/.

The application at /apply/ should submit on this website. It collects service, account, context, name, email and optional phone. Replace the endpoint /api/application with a validated Firebase callable function or server endpoint. Store leads in Firestore with a server timestamp and status New, and send an email notification to team@unbanz.com server-side if configured. Never store API secrets in frontend code. Preserve data in the form on errors and only show success after persistence succeeds.

/admin is a design-only preview with password preview and fictional example.com records. Replace this with Firebase Authentication and an admin role check. Enforce permissions with backend rules, not route visibility or a hardcoded browser password. Unauthenticated visitors must not read any leads. Do not replace demo data with real leads until those controls are tested.

Keep search, filters, lead detail panel, status updates and private notes. Wire them to authenticated database operations. Use App Check and suitable rate limits for the public application endpoint. Review the README. Keep a backup branch and compare mobile/desktop rendering before and after integration.

The newest application has its own apply.css and apply.js. Keep the desktop two-column form and mobile two-step layout. Main app.js only handles site navigation, accordions and information dialogs now.
