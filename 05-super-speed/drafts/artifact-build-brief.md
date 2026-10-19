# Build brief: the quiet-responder artifact

For handoff to another AI session with artifact-building capabilities.
Paste this whole document as the prompt.

---

## Executive summary

Build a single, self-contained, clickable HTML prototype that shows
Helen Achebe (Director of Product, Rook Dispatch) what we'd build
instead of quietly changing a number in the routing code — a proposed
fix that lets a responder who's gone quiet since Release 4.2 recover
on their own, without a manual override or a visible score. The
artifact must be understandable in under two minutes with no verbal
walkthrough, told entirely from the point of view of two real people:
Kip, a handler running two responders on one screen, and Meteor Mite,
a responder who dropped from ~11 callout offers a week to 1, and has
heard nothing since 31 August. A first-pass version of this exists
already (`quiet-responder-mock.html` in this repo) — this brief asks
for a fuller, more complete version: more screens, a real week-by-week
walkthrough instead of a two-state toggle, an explicit plain-English
explainer of the mechanism, and a closing screen that states clearly
what the fix does not do. Every number either comes from real data or
is explicitly labeled as a projection — nothing is presented as
measured that isn't.

---

## 1. Background — what actually happened (ground truth, use verbatim where noted)

Rook Dispatch shipped Release 4.2 on 12 August 2026. Two changes
landed together: routing weights rebalanced (proximity weight
0.45→0.60, recent-acceptance weight 0.40→0.25), and the callout offer
timeout cut from 90 seconds to 60. Both were real, requested changes —
particularly the proximity rebalance, asked for by responders working
wide geographies who were losing callouts to farther-but-more-reliable
responders.

What nobody caught before shipping: the scoring system that ranks
responders has exactly one way a responder's standing goes down
(`record_declined`, in `history.py` — fires identically whether they
actively declined an offer or simply ran out of time to answer, docking
0.12) and exactly one way it goes up (`record_accepted`, +0.08, and
only fires if they're offered something in the first place). There is
no decay back toward neutral over time. Once a responder's standing
falls low enough that they stop being offered callouts, they have no
way to earn it back — the only door back in is an offer, and a low
score is what's keeping the offer from reaching them. This gap
predates 4.2 (an engineer, Wen Li, flagged it in a code comment back
in 2019 and nobody returned to it) — 4.2 made it severe by shortening
the timeout (more penalty events) and making rank stickier.

Four of Rook Dispatch's sixteen responders fell into this trap:
**Farlight**, **Meteor Mite**, **The Undertow**, and **Vesper**. All
four had normal, healthy acceptance rates before 4.2 (68–82%) — this
wasn't the system correctly deprioritizing unreliable people. All four
collapsed in the same single week, the week of 17 August, from a
steady 10–14 offers/week down to 0–5, and kept falling. Two of the
four (Meteor Mite, Vesper) generated zero support tickets from anyone
— they were only discovered because a product designer happened to
interview their handlers for an unrelated console-redesign project.

**Kip** is the handler for two responders: Meteor Mite (one of the
four affected) and The Gale (one of the responders who *gained*
volume in the same period). His quote to the designer, verbatim, worth
using directly in the artifact:

> "Meteor Mite's been texting me all week asking if something's broken
> because it's so quiet. Nothing coming in, phone just sitting there.
> And The Gale hasn't stopped, like, at all, same week, same city. I
> don't know what to tell either of them. Mite thinks Mite's been
> forgotten. Gale's exhausted. I'm looking at two cards on the same
> screen that might as well be two different products."

## 2. The ask, from Helen (verbatim, this is who the artifact is for)

> "Before anyone touches the code, I want to see what we'd actually
> build instead — from the point of view of the person it happens to.
> Not a setting. Something a handler like Kip would notice, and
> something a responder who's gone quiet would feel differently
> about... It doesn't need to be polished — I'd rather see something
> real than a tidy slide. And if you can get me something I can
> actually click through, even better."

Read that closely — three hard requirements, not preferences:
1. Told from the point of view of the person it happens to, not as a technical description of a config change.
2. Not a setting — no dial, no manual per-responder override, nothing that reads as a human flipping a switch on Meteor Mite specifically.
3. Clickable, not a static slide.

## 3. The proposed fix (what the artifact needs to make legible, without ever showing code or a config screen)

Ship as a follow-up release on top of 4.2 (not a revert):
1. Add decay back toward neutral in the scoring, but **one-directional only** — pull a below-neutral standing back up over time even with no offers; leave an above-neutral standing alone, so responders who earned a good record fairly (like The Gale) aren't quietly punished by a fix meant for someone else.
2. Split the penalty for a missed/timed-out offer from the penalty for an active decline — missing it should cost less, since we don't actually know they'd have said no.
3. Put the offer timeout back to 90 seconds.
4. Leave the proximity/recent-acceptance weight balance alone — that change was legitimately requested and isn't itself the bug.
5. Add a hard floor so nobody's standing sits near zero indefinitely.
6. This time, watch per-responder offer volume on rollout, not just the aggregate acceptance rate — that's what let this go undetected for three weeks.

None of this is ever exposed as a number to anyone. What changes is
outcome — Meteor Mite starts getting offered callouts again, gradually,
over the following weeks. Nothing about the interface changes for
Kip or for Meteor Mite; what they experience is the product starting
to behave the way it used to.

## 4. What exists already — build on this, don't start from zero conceptually

Two files already exist in this repo, in `05-super-speed/`:

- **`one-pager.md`** — the written version: who this is for, what
  changes for them, what this deliberately doesn't do. Use this as
  your source of truth for copy and tone. Don't contradict it.
- **`quiet-responder-mock.html`** — a first-pass clickable mock. It
  has: a two-state toggle ("Without the fix" / "With the fix"), a dark
  console card view for Kip showing Meteor Mite and The Gale with
  sparklines, and a light phone-frame view of Meteor Mite's
  notification history. Real weekly numbers through 31 August, clearly
  labeled illustrative numbers after that.

**What's missing that this fuller version should add:**
- A real week-by-week walkthrough (a scrubber/stepper across actual
  weeks), not just a binary before/after toggle — Helen and Marcus
  should be able to watch the gap open in August and, in the "with
  fix" path, watch it close gradually, week by week, not jump between
  two end states.
- An explicit, plain-English "how this works" panel or screen — no
  code, no formulas, using the ride-the-line-in-order metaphor
  established elsewhere in this project (saying no or missing your
  turn pushes you back a lot, saying yes moves you up only a little,
  and right now there's no way to move up except by getting a turn at
  all) — positioned so Helen can hand this artifact to someone else
  and it explains itself.
- A closing screen or section that states the three hard constraints
  from the one-pager as clearly as the opening states the problem: not
  a setting, not instant, no exposed score.
- Consider showing the pattern isn't unique to one lucky case — a
  secondary, lighter-weight view of at least one more affected pair
  (e.g. Farlight/Linda Pruitt) so it doesn't read as a single
  anecdote.
- Annotate what's the *same* screen as today vs. what's different —
  Helen needs to see that Kip's console and Meteor Mite's phone don't
  gain new UI; only the data behind them changes over time.

## 5. Audience and tone

Primary reader: **Helen Achebe**, Director of Product. Product-literate,
not an engineer — she should never need code explained to understand
this. Secondary readers, if she forwards it: **Marcus Oyelaran**
(Engineering Manager) and **Wen Li** (Staff Engineer, owns the routing
code) — both should recognize the mechanism described without feeling
it's been oversimplified or gotten wrong.

Tone: plain, concrete, grounded in real names and real numbers — not
a pitch deck. Helen explicitly said she doesn't want "a tidy slide."
Avoid marketing language, avoid vague reassurance ("this will fix
everything"), avoid hiding uncertainty (projected data must be labeled
as such, every time it appears, not just once in a footnote).

## 6. Required content — data and quotes to embed

Use real data. Do not invent numbers where real ones exist.

**Meteor Mite, weekly pings_sent (from `callout-history.csv`):**
`6/29:11, 7/06:12, 7/13:10, 7/20:11, 7/27:12, 8/03:11, 8/10:10, 8/17:4, 8/24:2, 8/31:1`

**The Gale, weekly pings_sent (same source):**
`6/29:13, 7/06:12, 7/13:13, 7/20:14, 7/27:13, 8/03:13, 8/10:15, 8/17:17, 8/24:20, 8/31:21`

Weeks after 31 August don't exist yet — any data shown there is a
projection and must say so, on-screen, not just in a footnote. Suggested
projected shape: "without the fix" stays flat near 0–1 indefinitely;
"with the fix" climbs gradually back toward Meteor Mite's ~11/week
baseline over roughly 5–6 weeks, while The Gale eases back down from
21 toward a more normal load rather than staying pinned at the top —
both responders' patterns should normalize, not just the quiet one.

**Kip's quote** (section 1, above) — use verbatim, attributed to Kip,
handler for Meteor Mite and The Gale.

**Optional second pair, if building the secondary view (section 4):**
Farlight, handled by Linda Pruitt, capability tag crowd-management,
collapsed from ~12/week to 0 by 31 August — the only visibility Rook
had into her situation was one ticket her handler filed reluctantly,
three weeks in: *"Farlight has gone almost two weeks now without a
single callout, which given her crowd-management tag surprises me...
Raising this because she's started asking me directly, which she
doesn't usually do, and I'd like something more to tell her than 'I
don't know.'"*

## 7. Design direction

- Two device-style views, styled as real product screens, not generic
  cards: a dark console/dashboard view (Kip explicitly wants dark mode
  — lean into that) and a light mobile-notification view (typical
  phone OS conventions) for Meteor Mite.
- Palette should read as an operations/dispatch tool, not a generic
  SaaS landing page — avoid cliché AI-generated defaults (no warm
  cream + serif + terracotta, no purple-to-blue gradient hero, no
  Inter/Space Grotesk as the default face). A cool, technical neutral
  with one deliberate accent color works well; semantic color
  (amber/warn for "quiet," green/good for "back in rotation") should
  be distinct from the accent hue.
- Typography: a technical sans for interface text, a monospace face
  for data — timestamps, counts, sparkline labels — to reinforce that
  this is a real product screen, not a mockup drawn in a generic
  design tool.
- Charts (the sparklines/timelines) must be drawn to scale, with the
  actual reached values labeled, not decorative squiggles.
- Must render legibly at phone width (~400px) and work in both light
  and dark viewer themes for the surrounding page chrome (the
  device-mock panels themselves can keep their fixed internal
  palette, same as the existing draft, since they represent real
  product screens rather than the artifact's own chrome).

## 8. Interaction requirements

- Must be genuinely clickable — Helen said this explicitly. At
  minimum: a way to scrub or step through weeks (not just a two-state
  toggle) and see both Kip's console and Meteor Mite's phone update in
  sync; a way to compare "without the fix" vs. "with the fix" for the
  same week.
- No page reload, no external navigation — single self-contained
  experience.
- Should be understandable via clicking alone, without reading a
  separate document — but can and should carry the same explanatory
  copy as `one-pager.md` where useful, adapted to fit the screen
  rather than pasted as a wall of text.
- Keyboard-operable controls, visible focus states — this may be
  reviewed by more than one person, not everyone will use a mouse.

## 9. Hard constraints — do not violate these

1. **Never show a visible "score" or numeric standing to Kip or Meteor
   Mite anywhere in the mock.** Only show what a real product screen
   would show today: offer counts, status words ("quiet," "back in
   rotation"), timestamps. The scoring mechanism is explained in prose
   in a separate explainer panel, never rendered as a live UI number.
2. **Never depict a manual toggle, dial, or override control aimed at
   a specific responder.** The fix is systemic and automatic. If the
   UI has a toggle, it must be clearly a *viewer* control for exploring
   the scenario ("Without the fix" / "With the fix," or a week
   scrubber) — never something that reads as Kip or anyone at Rook
   flipping a switch on Meteor Mite.
3. **Never imply the fix is instant.** Any "with the fix" recovery
   must visibly take multiple weeks, matching the projection in
   section 6 — no jump-cut from 1 offer/week to 11 in one step.
4. **Label every projected/future data point as a projection**, in the
   UI itself, not only in a footnote — e.g., a "projected" tag or
   visually distinct treatment on weeks after 31 August.
5. **Don't touch or reference reverting the proximity/recent-acceptance
   weight change.** That's explicitly out of scope for this fix and
   for this artifact.
6. **Use real names and terms exactly as they appear in Rook's own
   documents** — Rook Dispatch, callout, callout offer, capability
   tag, handler, responder, recent-acceptance (never invent new
   in-universe terminology).

## 10. Success criteria

- Helen can open the artifact cold, with no verbal explanation, and
  in under two minutes understand: what's broken, who it's happening
  to, what we'd build instead, and what that fix deliberately doesn't
  do.
- Kip, if he ever saw it, would recognize his own console.
- Nobody reviewing it mistakes the fix for a manual, case-by-case
  intervention or an instant reset.
- Every number on screen is either traceable to `callout-history.csv`
  or clearly marked as a projection.

## 11. Deliverable

A single self-contained HTML file (inline CSS/JS, no build step, no
external dependencies beyond a Google Fonts stylesheet link if needed)
that can be opened directly or published as a clickable artifact. If
the receiving tool has its own artifact platform constraints (CDN
allowlist, no file downloads, sandboxed forms, light/dark theme
tokens, etc.), follow that platform's own rules over anything
implied-but-not-stated here — this brief describes the content and
experience, not a specific runtime's technical contract.
