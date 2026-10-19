# When a responder goes quiet, give them a way back

Brief · Rook Dispatch · September 2026
**Owner:** Yonatan Maya, PM, Rook Dispatch
**Decides:** Helen Achebe · **Builds:** Marcus Oyelaran's team, with Wen Li
Answers Helen's note in `director-request.txt`. Clickable version: `prototype.html`.

**The ask:** let a responder whose standing has fallen recover on their
own, and in the meantime talk directly to the four people this has
already happened to.

---

## The problem

Since Release 4.2, four of Dispatch's sixteen responders (Farlight,
Meteor Mite, The Undertow and Vesper) have gone from about 12 pings a
week to 0–1. They weren't turning work down: before 4.2 each of them
accepted 69–82% of what they were offered, like everyone else
(`03-rewind/the-number.md`).

Here is how it happens (`04-x-ray-vision/what-the-code-does.md`). A
missed ping counts the same as saying no, and since 4.2 a ping only
waits 60 seconds, so more people who would have said yes simply run out
of time. A responder's standing only goes back up when they're offered
something and take it. A low standing is exactly what stops the offers
from reaching them. **Once they fall far enough, nothing in Dispatch
gives them a way back.**

It stayed hidden for three weeks because the pool-wide acceptance rate
"recovered" to 73%, and two of the four never filed a ticket.

## Who it's for

**Meteor Mite**, who went from 10–12 pings a week to 2, then 1, and has
no way to know whether he's still in the system. He filed nothing.

**Kip**, his handler, who also runs The Gale in the same city. In the
week Meteor Mite got one ping, The Gale got 21. *"I'm looking at two
cards on the same screen that might as well be two different
products."*

The same story applies to Farlight (Linda Pruitt), The Undertow
(Desmond Okafor) and Vesper (Aunt Dot).

## What changes for them

- **For Meteor Mite:** his standing drifts back toward normal a little
  every week, whether or not he's offered anything. A missed ping costs
  less than an actual "no", and pings wait 90 seconds again. He doesn't
  have to do anything differently, and he doesn't need to know anything
  changed. Over the following weeks, he starts hearing from Dispatch
  again.
- **For Kip:** nothing new to learn or check. Meteor Mite's card on the
  coverage view fills back in, the way it did before August, and he
  stops being the one explaining a silence he can't see into.
- **This week, before any code ships:** someone from Rook contacts the
  four directly. So far only their handlers have spoken for them.

The patch itself is in `4.3-patch/`, written against the original
routing code.

## What it deliberately doesn't do

- **It isn't a setting.** No dial for handlers, no manual override on a
  person. The system corrects itself the same way for everyone.
- **It doesn't undo 4.2's proximity change.** Responders who work wide
  areas asked for it, and a closer responder still ranks first.
- **It doesn't pull anyone down.** The weekly drift only lifts scores
  below neutral. The Gale and others with a good record keep what they
  earned.
- **It doesn't promise equal volume.** Some responders will still get
  more pings than others.
- **It doesn't show anyone a score.**
- **It doesn't happen overnight.** Recovery takes weeks, by design.

## How we'll know it worked

Measured per responder in the weekly export, not in tickets: the
tickets contradicted the export in 17 of 21 "silence" reports, and two
of the four never filed one (`02-super-hearing/feedback-read.md`).

1. Within four weeks of the patch, Farlight, Meteor Mite, The Undertow
   and Vesper are each back to **at least 6 pings a week**, half their
   pre-4.2 average.
2. **No available responder** spends two weeks in a row under 2 pings a
   week while someone else in their region is above their own baseline.
3. Pool-wide acceptance stays at or above its pre-4.2 level (75–78%).

**If (1) misses at four weeks,** recovering the score isn't enough on
its own, and the next step is a minimum weekly share of pings for every
available responder. Our simulator (`routing-fix-simulator.html`) is an
early warning that this may happen: it reproduces the trap, but it's
too small to show whether the fix alone gets them out.

## Before it ships

Wen Li confirms the mechanism in per-incident routing logs, and
confirms where scores are stored (in this code they live only in
memory, so a deploy would reset them). Something also has to run the
weekly drift on a schedule.

## Scope

The two parts of the ask above, and nothing more: a way back in the
product, and a direct conversation with the four until it ships. Not
in scope: the tickets-versus-export contradiction (an open question for
Wen and Ravi Menon), the console requests from the interviews (dark
mode, larger status text), or Supply's requisition queue.
