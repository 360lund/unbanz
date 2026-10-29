// Returns the visitor's country code from Vercel's IP geo header. Used only by the human-only CTA note.
export default function handler(req, res) {
  const c = String(req.headers["x-vercel-ip-country"] || "").slice(0, 2).toUpperCase();
  res.setHeader("Cache-Control", "private, no-store");
  res.setHeader("X-Robots-Tag", "noindex");
  res.status(200).json({ c });
}
