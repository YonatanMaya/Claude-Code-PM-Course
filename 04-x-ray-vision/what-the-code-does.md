# What the routing code does, and what it doesn't

Module 4 · X-Ray Vision · Yonatan Maya, PM, Rook Dispatch
Source: `00-rook/code/dispatch-routing/` (five files, read as-is)

---

## What it does, from "something's wrong" to a phone buzzing

| Step | In plain English | File |
|---|---|---|
| 1 | Someone logs an incident in the console. This happens outside this folder; no code for it exists in the repo. | none |
| 2 | Find everyone marked available in that region, and how many minutes each would take to get there. | `availability.py` |
| 3 | Give each available responder one score: closeness × 0.60, recent yes-rate × 0.25, right skills × 0.15. | `routing.py`, weights in `config.py` |
| 4 | Sort everyone by that score, best first. | `routing.py` |
| 5 | Ping the top person and wait **60 seconds**. | `offer.py`, timer in `config.py` |
| 6 | If they say yes, done. If they say no **or the timer runs out**, move to the next person. | `offer.py` |
| 7 | Remember the outcome: a yes adds **+0.08** to their recent yes-rate. A no, or a missed ping, takes **−0.12** off. | `history.py`, points in `config.py` |

Step 7 feeds back into step 3 for every future incident.

## What it doesn't do

These don't appear in any release note, because none of them changed
in 4.2. They were already in the code.

1. **It doesn't tell a missed ping from a "no".** `offer.py` says it
   outright: *"Everything downstream treats the last two the same way."*
   Since 4.2 cut the timer from 90 to 60 seconds, more responders who
   would have said yes now run out of time, and each miss is scored as
   if they'd turned the job down. (Rook's own glossary says a decline
   and a timeout are *distinct in the data*. The scoring ignores that.)
2. **It doesn't let a score recover on its own.** The only way up is
   `record_accepted`: being offered something and taking it. Nothing
   eases a low score back over time. Wen Li asked exactly this in a 2019
   comment (*"should this ease back toward NEUTRAL_SCORE on its own
   after a while?"*), and nobody came back to it. Once you fall low
   enough to stop being reached, you have no way back.
3. **It doesn't decide *whether* someone gets asked, but in practice it
   does.** The README promises *"Everyone available is on the list."*
   True, but `offer.py` stops at the first yes. Someone ranked last in a
   busy region is on the list and still never reached.
4. **It doesn't treat recovery fairly.** One missed ping costs 0.12; one
   accepted job earns 0.08. Each miss takes one and a half accepted
   jobs to undo, and only if the jobs keep coming.
5. **It doesn't keep a record.** Scores live in a plain in-memory list
   (`_scores = {}` in `history.py`) and no rank is ever logged. That's
   why nobody could answer "why did Farlight stop getting pinged" from
   the system itself.

## The answer to Marcus's question

On 14 Aug, two days after release, Marcus asked in `#dispatch-team`:

> *"was that meant to apply to responders who've been turning jobs down
> too, or only everyone else? the config doesn't distinguish between
> them as far as i can tell … just want to know if it was a decision or
> if it just fell out that way"*

**It fell out that way.** Marcus is right that the config doesn't
distinguish them. There is one formula for every responder, with no
special case for people who decline a lot. It's actually broader than
he asked: because a missed ping counts as a decline, someone who was
simply slower to reach their phone is treated *as if* they'd been
turning jobs down. The four responders whose pings collapsed
(`03-rewind/the-number.md`) all accepted 69–82% of their offers before
4.2. They weren't decliners. The scoring treated them like decliners.

## What it would take to get out

For a responder who's gone quiet, the code offers exactly one way back:
**be offered something, and take it.** And a low score is precisely what
stops the offer from reaching them. The fix (`05-super-speed/`) starts
there.
