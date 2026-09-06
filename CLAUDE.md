# Rook Industries — course working file

## Session scope — Product School lab

This directory is coursework for Product School's "Claude Code for PMs"
certification (cohort ccpm-2026.1). Everything in it is a fictional
teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

### The company

Rook Industries builds coordination and provisioning software for the
protective-response sector (independently-operating masked responders,
and the handlers/quartermasters who support them). Founded 2014,
headquartered at Site Aleph with regional offices in Berlin, Singapore,
and Cornwall. 241 employees. Revenue is subscription, priced per active
responder.

Responder cover identities are never stored in production — Rook holds
capability tags, availability windows, and callout history only, never
a mapping to a legal identity. Don't design anything that assumes we
know who a responder really is.

### The two products

- **Rook Dispatch** — responder coordination: availability, proximity,
  callout routing, acceptance. Used by handlers (web console) and
  responders (mobile). This is my product.
- **Rook Supply** — gear provisioning: requisitions, maintenance,
  failure reports. Used by handlers and quartermasters. Reads (but
  never writes) Dispatch's Responder Availability Record for
  maintenance scheduling.

### How Dispatch works

An incident comes in → Dispatch ranks available responders (proximity,
availability, capability match, recent acceptance history) → a callout
offer goes to the top-ranked responder's mobile → they accept or
decline/timeout → on decline/timeout it moves to the next responder →
acceptance closes the loop.

Headline metrics: **callout acceptance rate** (accepted vs.
declined/timed out, reported weekly), **time-to-accept** (median
seconds to accept), **coverage gap** (no responder had the required
capability tag).

Ships monthly on a release train (4.x). Routing config ships with the
release, not adjustable at runtime by handlers.

### Where I am right now

I joined as PM on Dispatch two weeks ago (started the Monday after 28
August), replacing Priya Raghunathan who was the sole Dispatch PM for
14 months and left 21 August with no overlap. **Release 4.2 shipped 12
August**, days before I arrived, with:

- **Routing weight rebalance** — proximity weighted more heavily
  relative to recent acceptance history. A long-standing ask (three
  quarters) from responders working wide geographies, so someone
  nearby wasn't passed over for someone farther away with a better
  acceptance record.
- **Callout offer timeout cut from 90s to 60s.**
- Console filter persistence, plus three minor defect fixes.

Since the release: callout acceptance is down and support tickets are
up roughly 3x normal (as of 18 August), running elevated and flat
since. Tickets split into two distinct themes, roughly two-thirds to
one-third: (1) "my phone never goes off anymore" — unexplained so far,
and (2) "it buzzed but was gone before I could answer" — explained by
the shorter timeout.

Priya's read (in her handoff) was that this is mostly seasonal —
August is soft every year — and that reverting the routing change
would just trade one unhappy group of responders for another, so she
was against reverting it. Support (Nadia Hoffmann) has been tracking
the ticket split but the team was waiting for me to get up to speed
before regrouping properly on "the 4.2 picture."

### Who's who (Dispatch)

- **Helen Achebe** — Director of Product, owns roadmap/commitments.
- **Marcus Oyelaran** — Engineering Manager, Dispatch. Go-to for
  "is this a bad idea" and for pulling numbers.
- **Wen Li** — Staff Engineer, built the routing/ranking logic. The
  only real source on how ranking actually works — no design doc
  exists for it.
- **Sofia Marino** — Product Designer, console + phone app.
- **Nadia Hoffmann** — Support Lead, sees ticket volume first.
- **Ravi Menon** — Data Analyst, weekly numbers on responder
  answer rates, shared across Dispatch & Supply.

### Open threads worth knowing about

- No written explanation of the routing/ranking algorithm exists
  anywhere — it lives in Wen Li's head and the code.
- Some Q3 roadmap items were squeezed out of 4.2 when its timeline
  compressed; which are still committed vs. quietly dropped hasn't
  been revisited with Helen.
- Console filter persistence (shipped in 4.2) is expected to generate
  low-value/cosmetic tickets — not worth spending time on.
- **Working hypothesis on "phone never goes off":** `callout-history.csv`
  shows most responders' acceptance rate dipped mildly after 4.2, but
  four (Farlight, Meteor Mite, The Undertow, Vesper) collapsed hard —
  both far fewer offers sent and a much lower share accepted. Ruled out
  geography as the sole cause (Meteor Mite and The Gale share a handler
  and a city, yet one went quiet and the other stayed busy). Tickets
  for the four show the same pattern twice over: a long silence, then
  losing the one offer that finally arrives almost instantly. Likely
  mechanism: `history.py`'s `DECLINE_PENALTY` applies identically to a
  decline and a timeout, so a responder who misses an offer because
  they weren't expecting one (long silence made them less "primed") is
  scored the same as one who refused outright — which can compound
  into a self-reinforcing spiral. Not yet confirmed against real
  routing internals — needs a conversation with Wen Li, who built the
  ranking logic and is the only real source on how it behaves (no
  design doc exists).
