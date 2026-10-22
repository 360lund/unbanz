// Neon Postgres over its HTTP SQL endpoint (no npm dependencies). DATABASE_URL comes from the Vercel Neon integration.
export async function sql(query, params = []) {
  const cs = process.env.DATABASE_URL;
  if (!cs) throw new Error("DATABASE_URL missing");
  const r = await fetch(`https://${new URL(cs).hostname}/sql`, {
    method: "POST",
    headers: { "Neon-Connection-String": cs, "Content-Type": "application/json" },
    body: JSON.stringify({ query, params }),
  });
  const j = await r.json();
  if (!r.ok) throw new Error(j.message || "db error");
  return j.rows;
}
