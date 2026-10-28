// Replays for the /users dashboard (same auth as the rest of /users): list, ?ids=1, ?sid=<id> (chunks), DELETE ?sid=<id>.
import replay from "../_lib/replay.mjs";
export default (req, res) => replay.replays(req, res);
