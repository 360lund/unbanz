// Public ingest for the session recorder (POST). Validated, size-limited and rate-limited per session in replay-kit/server/core.mjs.
import replay from "../_lib/replay.mjs";
export default (req, res) => replay.ingest(req, res);
