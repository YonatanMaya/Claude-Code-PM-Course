# 4.3 patch: let a quiet responder find their way back

`4.3-routing.patch` is the proposed fix, written against the original
code in `00-rook/code/dispatch-routing/`. The original code is left
untouched; this patch sits beside it so the change can be reviewed
before anyone applies it.

To apply it to a copy of the code: `git apply 05-super-speed/4.3-patch/4.3-routing.patch`

## What it changes, in plain English

| File | Before (4.2) | After (4.3) |
|---|---|---|
| `config.py` | An offer waits 60 seconds | An offer waits 90 seconds again |
| `config.py` | A missed ping costs the same as saying no (−0.12) | A missed ping costs less (−0.04); an active "no" still costs −0.12 |
| `history.py` | A low score only rises when the responder is offered something and takes it | Once a week, any score below neutral (0.5) moves 8% of the way back toward it, whether or not they were offered anything |
| `history.py` | A score can sit at zero forever | Nobody available sits below 0.20 |
| `offer.py` | A timeout is recorded as a decline | A timeout is recorded as a timeout |

## What it deliberately leaves alone

- **The 4.2 proximity weighting (0.60 / 0.25 / 0.15).** Responders working
  wide areas asked for it for three quarters. It is not the bug.
- **Anyone above neutral.** The weekly drift only pulls low scores up.
  It never pulls a good score down, so The Gale, Nightwell and the
  others who gained volume are not penalised for a fix aimed at
  someone else.
- **What handlers and responders see.** No new setting, no visible
  score, no manual override.

## What the simulator does and doesn't show

`05-super-speed/routing-fix-simulator.html` runs these exact scoring
rules on sixteen simulated responders, side by side with 4.2.

- **It reproduces the trap.** Under 4.2 rules, the four responders who
  start a little farther from incidents settle at 0–1 pings a week and
  stay there.
- **It does not show the fix getting them out.** Run headlessly for 12
  weeks, the 4.3 column looks almost the same as the 4.2 column. I
  tried two variants: letting high scores drift down as well, and
  putting everyone at the same distance. Neither changed the result.
  The model gives each responder only 1–3 pings a week, where the real
  export shows about 11, so whoever ranks last in a region is almost
  never reached under any scoring rule. The model is too small to
  answer the question.

So the values above are a reasoned starting point, not a tested
result. That's why the brief carries a decision rule: if the four
aren't back to 6 pings a week within four weeks, add a minimum weekly
share of pings for every available responder.

## Not done yet, before this can ship

1. Something has to call `history.decay_all()` once a week. Nothing in
   this repo schedules it.
2. In this repo `history.py` keeps scores in memory. If production does
   the same, scores reset on every deploy, and the weekly drift has
   nothing to work on. Wen Li needs to confirm where scores are stored.
3. The mechanism is confirmed in the code and in the weekly export,
   not yet in per-incident production logs. Wen confirms that too.
