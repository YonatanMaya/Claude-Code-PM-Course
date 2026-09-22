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

I'm the new PM for Rook Dispatch, starting September 2026, taking over from
Priya Raghunathan.

### The company

Rook Industries builds coordination and provisioning software for
independently-operating masked responders and the handlers/quartermasters
who support them. Founded 2014, HQ at Site Aleph, ~241 employees. Two
products, both priced per active responder, shipping on a monthly release
train (4.x numbering):

- **Rook Dispatch** (mine) — responder coordination: availability,
  proximity, callout routing, acceptance. Used by handlers (web console)
  and responders (mobile).
- **Rook Supply** — gear provisioning: requisitions, maintenance, failure
  reports. Used by handlers and quartermasters.

Responder cover identities are never stored — we hold capability tags,
availability, and callout history only, never a legal identity. Don't
design anything that assumes we can map one to the other.

### How Dispatch works

Incident comes in → Dispatch ranks available responders → top-ranked
responder gets a callout offer on mobile → they accept or decline (or the
offer times out) → it moves to the next responder → acceptance closes the
loop.

**Routing priority** ranks responders on proximity (travel-time estimate),
current availability, capability match, and recent acceptance history.
Declining/timing out lowers a responder's recent-acceptance component,
which lowers their routing priority until it recovers. Routing config
ships with the release — it's not a runtime setting handlers can touch.

**Key metrics:** acceptance rate (headline metric — share of offers
accepted vs. declined/timed out), time-to-accept (median seconds to
accept), coverage gap (incidents where no available responder had the
required capability tags).

**Where Supply touches Dispatch:** Dispatch writes the Responder
Availability Record; Supply reads it (read-only) to schedule gear
maintenance into low-callout-load windows.

### Vocabulary

- **Responder** — not a Rook employee, independently operating.
- **Handler** — manages a responder or small group: availability, gear,
  readiness. Usually the one actually in the product.
- **Quartermaster** — owns equipment stock/approvals (Supply side).
- **Callout** — a request for a responder to attend an incident.
- **Callout offer** — one callout presented to one responder, awaiting
  accept/decline.
- **Decline** vs **timeout** — distinct in the data, both send the callout
  onward.
- **Capability tags** — flight, structural-entry, hazmat-tolerant,
  cold-weather, aquatic, crowd-management, de-escalation.
- **Mutual aid** — responders across regions covering for each other; not
  built yet, on the Q4 exploration list.

### Where things stand (as of early September 2026)

**4.2 shipped 12 August** — the big change was "who gets pinged": proximity
weighted more heavily relative to recent acceptance history (a
long-requested fix for responders in wide geographies). Also cut the ping
timeout from 90s to 60s, and added console filter persistence.

Since then, acceptance is down and callout-related tickets are running
~3x normal, split roughly 2:1 between "phone never rings" and "offer's
gone before I can answer" (the second is explained by the timeout cut; the
first isn't, yet). Priya's read: mostly seasonal (August is always soft)
plus two changes landing at once — she deliberately did not want this to
become a "revert 4.2" conversation, since the routing change was a
genuine, long-standing ask. Marcus and the team agreed to hold off on
conclusions until I'd had a week to look myself; the real regroup on the
4.2 picture is still pending. Ravi Menon (Data) has weekly acceptance
numbers; Nadia Hoffmann (Support) has the ticket breakdown.

**Open threads inherited from Priya:**
- No written documentation of how routing/"who gets pinged" actually
  works — it lives in Wen Li's head. On my list to write.
- A few Q3 roadmap items got squeezed out of 4.2's compressed timeline;
  need to check with Helen which are still committed.
- Console filter persistence (4.2) will generate some cosmetic-only
  tickets — noise, not worth chasing.

**Q3 roadmap (Dispatch items):** Change to who gets pinged, Availability
Confidence (surfacing a confidence score next to stated availability —
driven by support escalations), and ping timeout tuning are all shipped in
4.2 and committed/locked. Shared cover between responders is Q4,
exploring. (Supply: requisition approval chains committed for 4.3;
handler phone app is Q4/exploring.)

### People (Dispatch team, primarily Chicago + Berlin)

- **Helen Achebe** — Director of Product (Dispatch & Supply), Chicago. My
  manager. Owns roadmap/commitments.
- **Marcus Oyelaran** — Engineering Manager, Dispatch, Chicago. First stop
  for anything uncertain; can pull numbers.
- **Wen Li** — Staff Engineer, Dispatch, Berlin. Built routing — the person
  to talk to (not a doc) to understand how ranking actually works.
- **Sofia Marino** — Product Designer, Dispatch, Chicago. Console and
  phone app.
- **Nadia Hoffmann** — Support Lead, Dispatch & Supply, Berlin. Sees
  complaint volume first; worth a standing check-in.
- **Ravi Menon** — Data Analyst, Dispatch & Supply, Singapore. Weekly
  acceptance-rate reporting; requests go through #data.
- **Priya Raghunathan** — my predecessor, departed 21 August after 14
  months as sole PM on Dispatch. Left a handover doc.

### 4.2 investigation — findings so far (early September 2026)

Dug into the actual evidence (`00-rook/code/dispatch-routing/`,
`00-rook/data/callout-history.csv`, `00-rook/feedback/`), not just the
narrative in the handover doc and Slack thread. Key findings, in case
Priya's "mostly seasonal" read comes back up:

- **The aggregate acceptance-rate "recovery" is an artifact, not good
  news.** Per-responder data shows offer volume didn't shrink
  system-wide — it *redistributed*. 4 of 16 sampled responders collapsed
  to near-zero offers/week (Farlight, Meteor Mite, The Undertow, Vesper),
  while 5 others gained 25–50% more. The blended average looks like it's
  recovering only because the excluded group is shrinking to a smaller
  share of total offers. Pure seasonality doesn't explain a redistribution
  like this — it would shrink everyone's volume together, not split the
  population into winners and losers.
- **Leading mechanism (not yet confirmed against production logs):** the
  4.2 weight rebalance (proximity 0.45→0.60, recent-acceptance 0.40→0.25)
  made ranking stickier, and `offer.py` stops at the first acceptance —
  so responders who rank slightly lower get offered work far less often
  in practice, "eligible" or not. Combined with the shorter 60s timeout
  (more recorded declines) and an asymmetric scoring model in
  `history.py` (decline penalty 0.12 > acceptance credit 0.08, no
  decay-to-neutral), this looks like a self-reinforcing feedback loop:
  fall behind once, get fewer chances to recover, fall further behind.
  Ticket and interview evidence fits this closely (Kip's two responders,
  same week, one dead quiet one nonstop; several tickets describe a
  responder's first offer in weeks being immediately lost to timeout).
- **Before acting on this:** need per-incident routing-priority logs
  (not weekly aggregates) for the affected responders from Wen, to
  confirm the mechanism rather than just the correlation. Ravi should
  start cutting acceptance rate per-responder, not just in aggregate —
  the current metric structurally can't see this failure mode.
- Also surfaced in Sofia's console interviews but *unrelated* to this
  investigation, for the backlog: dark mode (Kip), requisition approval
  queue speed and catalog search (Halloran, Supply-side), filter
  persistence occasionally resetting silently (Ambrose).

### 4.2 — code walkthrough, ticket-silence gap, and the actual fix (mid-September 2026)

Went through `dispatch-routing/` line by line and cross-checked it against
the ticket/interview evidence and a toy simulation. What's new since the
last update:

- **The exact scoring mechanism, confirmed in code:** `history.py` has
  exactly one way down (`record_declined`, -0.12, fires identically for a
  real decline *and* a timeout — no distinction) and exactly one way up
  (`record_accepted`, +0.08, only fires if they're actually offered
  something). No decay back toward neutral exists anywhere. So a
  responder who stops getting offered anything has no way to recover —
  the only door back in is an offer, and a low score is what's blocking
  the offer. This is a pre-existing design gap (Wen's own 2019 TODO comment
  flags it) that 4.2 didn't create but made severe, by shortening the
  timeout (more penalty events) and making rank stickier (fewer chances
  once you fall behind).
- **Bigger-than-expected gap in how we'd have caught this without the
  CSV:** of the four collapsed responders, two (Meteor Mite, Vesper)
  generated *zero* support tickets from anyone — we only know about them
  because Sofia happened to interview their handlers for an unrelated
  console-redesign project. Farlight has exactly one ticket, filed by her
  handler three weeks in, reluctantly. Only The Undertow used the ticket
  system as intended. Takeaway: people who go quiet on the product also
  go quiet on the feedback channel, so tickets can't be trusted as a
  backstop for exactly this failure mode — need the per-responder metric
  instrumentation regardless of ticket volume.
- **Toy simulation (not real data, but useful):** rebuilt the actual
  scoring formula with synthetic responders/regions. Directionally
  confirms the 4.2 weight/timeout combination trends toward permanent
  exclusion for a subset, more so than the pre-4.2 config did — supports
  treating this as a property of the formula, not just a coincidence in
  the August numbers. Still not a substitute for Wen confirming against
  real per-incident logs.
- **No console repo exists.** Checked GitHub — only 3 repos total on the
  account, none besides this one relate to Rook. The console/mobile
  front-end and incident intake aren't in any codebase I have access to;
  `dispatch-routing` is the only real application code that exists for
  Dispatch.
- **Recommended fix, scoped as a 4.3 patch on top of 4.2, not a
  revert:** (1) add decay back toward neutral in `history.py`, but
  *one-directional only* — pull below-neutral scores up, leave
  above-neutral scores alone, so responders who earned a good score
  fairly (Nightwell, The Gale, Vantage, Stormwrack) don't get quietly
  punished by a fix meant for the excluded group; (2) split the timeout
  penalty from the active-decline penalty (timeout should cost less,
  since we don't actually know they'd have said no); (3) put
  `OFFER_TIMEOUT_SECONDS` back to 90; (4) leave the proximity/
  recent-acceptance weights alone — that change was legitimately
  requested and isn't confirmed as the root cause independent of the
  scoring gap; (5) add a hard floor so nobody's score sits near zero
  indefinitely; (6) stage the rollout and alert on per-responder volume
  drops, not just the aggregate rate, this time.
- **Open question for Wen/Marcus before finalizing:** `history.py`
  stores scores in a plain in-memory dict in this code, with no visible
  persistence layer. Need to confirm whether that's just this repo being
  simplified for teaching purposes or an actual gap — either way, "don't
  reset anyone's score on deploy" needs a real place to keep that score
  first.

### 4.3 — the fix actually shipped as code (mid/late September 2026)

Built Helen's requested one-pager and click-through for the quiet-responder
fix, then went further and wrote the actual patch. All of this is on
`claude/rook-dispatch-pm-onboarding-z8u4vy`, tracked by PR #1.

- **For Helen:** `05-super-speed/one-pager.md` + a clickable mock
  (`quiet-responder-mock.html`, then a corrected `prototype.html`)
  told from Kip and Meteor Mite's side — who it's for, what changes,
  what it deliberately doesn't do (not a setting, not instant, no
  exposed score). `05-super-speed/brief.md` is the short status email
  version — confirmed vs. still-needs-Wen's-sign-off, kept separate
  from the click-through itself.
- **Self-review caught real gaps before this went anywhere near
  Marcus:** walking through Kip/Meteor Mite's actual week-by-week
  experience surfaced that the first mock's "with fix" recovery curve
  was unrealistically smooth, and that it showed The Gale's load
  artificially easing down — which contradicts the fix's own logic
  (above-neutral scores are never touched). Corrected in
  `prototype.html`.
- **Built `05-super-speed/routing-fix-simulator.html`** — not an
  illustrative mock, an actual re-implementation of the real scoring
  formulas from `config.py`/`history.py` in JS, running current (4.2)
  vs. proposed (4.3) side by side across all 16 responders against
  identical shared random rolls, so any gap shown is caused by the
  rule, not luck. Has live sliders for decay rate / floor / timeout
  penalty. Published as an Artifact; supports being edited via inline
  comments on the page, not just chat (already used once — a
  hover-effect request came in as an artifact comment and was
  resolved that way).
- **Hit and fixed a real calibration bug in the simulator**: initial
  proximity gap between a "marked" (quiet-prone) responder and their
  regionmates was mathematically impossible for any decay/floor value
  to overcome, and the dominant regionmate absorbed nearly every
  incident before it could cascade down — so Meteor Mite stayed frozen
  at zero in both scenarios, which looked like the fix didn't work.
  Narrowed the proximity spread and widened jitter/incident volume to
  fix it. Worth remembering if the simulator ever looks "stuck" again
  — check calibration before assuming the fix logic is wrong.
- **The 4.3 patch is now real code**, not just a proposal, in
  `00-rook/code/dispatch-routing/`:
  - `config.py`: `OFFER_TIMEOUT_SECONDS` back to 90; added
    `TIMEOUT_PENALTY` (0.04, vs. 0.12 for an active decline),
    `DECAY_RATE` (0.08), `RECOVERY_FLOOR` (0.20). Proximity/
    recent-acceptance weights deliberately untouched.
  - `history.py`: split `record_timed_out()` from `record_declined()`;
    added `decay_all()` — one-directional (only pulls a below-neutral
    score up, never pulls a high one down) and floor-enforcing, meant
    to run on a weekly schedule. This directly answers Wen's 2019 TODO
    comment that had sat unresolved.
  - `offer.py`: `dispatch()` now calls the right history function
    depending on timeout vs. explicit decline.
  - `CHANGELOG.md` and `README.md` updated to document all of this
    under a new "4.3 — proposed, not yet shipped" entry.
  - **Still open before this can actually ship:** `decay_all()` needs
    something to actually call it on a schedule — nothing in this repo
    wires that up yet. And the persistence-layer question from the
    investigation above still isn't resolved. Both need Wen/Marcus
    before this goes beyond a proposal in a PR.
