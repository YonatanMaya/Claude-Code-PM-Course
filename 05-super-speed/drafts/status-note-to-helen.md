Subject: Quiet-responder fix — where we are, before we build anything

Helen —

Quick status, ahead of the artifact you asked for.

**What we're confident about:** four responders (Farlight, Meteor Mite, The Undertow, Vesper) got shut out of rotation the same week, all with clean pre-4.2 track records — this isn't the system correctly deprioritizing unreliable people. The code has a real gap: once a responder's standing drops, there's no way for it to recover except getting offered something, and a low standing is exactly what stops that. That part checks out against the actual code.

**What we're not yet certain about, and I don't want to skip past:** we haven't confirmed this against real production routing data — only against this dataset, the code, and a toy model I built to sanity-check it. I want Wen to confirm the mechanism against actual logs before this ships, not after. Separately, the code stores each responder's standing in memory with no visible database — if that's real, "recovers gradually over time" doesn't work as designed until that's sorted, so I need that confirmed too.

**What I'm proposing** (not a revert — a small patch on top of 4.2): let a low standing drift back up on its own over time, treat a missed offer more gently than an actual decline, put the timeout back to 90 seconds, and add a floor so nobody gets stuck at zero. None of it touches the proximity change people asked for, and none of it exposes a number or a manual switch to anyone.

**Before we touch code:** I'm putting together the click-through you asked for, from Kip and Meteor Mite's side, not a settings screen. Will have it to you shortly. Wen's confirmation on the mechanism and the storage question are the two things I want closed before we actually ship, not before we look at what we'd build.

— [You]
