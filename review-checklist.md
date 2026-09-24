# Review checklist

A habit, written down so it's the same every time. Point Claude at this
file alongside any brief — "run review-checklist.md against this" — and
expect the same four checks, in this order, before anything else gets
said about the brief.

## How to use this

Give Claude the brief (a file path, pasted text, or "the brief we just
wrote") and this file together. Don't re-explain the criteria — they're
below. Expect the output in the format at the bottom, not a paragraph
of general impressions.

## The four checks

### 1. It names who owns it

A brief without a named owner is a brief nobody's actually accountable
for shipping or deciding on. "The team" or "we" doesn't count — a
brief passes this check only if a specific person (or a specific,
singular role if the person isn't known yet) is identifiable as the
one who owns the outcome, not just the one who wrote the document.

**Look for:** a named owner in the header, byline, or opening — or,
failing that, someone the body of the brief clearly identifies as
accountable for what happens next ("Helen decides," "I'm proposing,
Marcus signs off").

**Fails when:** ownership is implied but never stated, or diffused
across a group with nobody actually holding it.

### 2. It says how we'll know it worked

A brief that proposes something without stating what success looks
like is asking for trust, not making a case. This doesn't need to be
a formal metric — "Kip stops filing this kind of ticket" is a
legitimate success criterion — but it has to be something someone
could actually check later and say yes or no to.

**Look for:** an explicit statement, anywhere in the brief, of what
changes, what gets measured, or what observably stops happening if
this works.

**Fails when:** the brief describes the fix in detail but never says
what "it worked" would actually look like from outside.

### 3. The scope at the end matches the scope at the start

Briefs drift. They open narrowly ("fix X for this one case") and close
broadly ("...and also we should reconsider Y and Z"), or the reverse —
open with a big claim and quietly narrow to something much smaller by
the recommendations. Either direction is a real problem: the reader
approved the opening framing, not whatever scope showed up by the end.

**Look for:** re-read the opening statement of the problem/ask, then
the closing recommendations, side by side. They should be describing
the same-sized thing.

**Fails when:** the close introduces asks, fixes, or claims that
weren't part of what the opening framed — even reasonable ones. A
reasonable idea that showed up via scope creep still needs to be
flagged, not smuggled in.

### 4. It explains the problem before it proposes a fix

A brief that leads with the solution is asking the reader to trust the
diagnosis without ever seeing it. The problem — what's actually wrong,
for whom, and how we know — has to be established and justified before
any fix, patch, or recommendation appears.

**Look for:** problem statement, with evidence or reasoning behind it,
positioned structurally before the proposed solution — not just
mentioned in passing on the way to the fix.

**Fails when:** the brief opens with (or leads with) what to build/do,
and the problem is backfilled afterward as justification, or is never
really established at all — just asserted.

## Output format

Always respond with exactly this structure, one line of verdict per
check, each citing the specific place in the brief that decided it —
not a vague summary:

```
1. Owner — PASS / FAIL / PARTIAL — [one line, citing the specific place in the brief]
2. Success criteria — PASS / FAIL / PARTIAL — [one line, citing the specific place]
3. Scope consistency — PASS / FAIL / PARTIAL — [one line, citing opening vs. closing]
4. Problem before fix — PASS / FAIL / PARTIAL — [one line, citing structure/order]

Overall: [one sentence — is this ready to go further as-is, or what's the one thing to fix first]
```

Use PARTIAL when a check is present but weak (e.g., an owner is named
but not clearly accountable; success criteria exist but are vague) —
don't force PASS/FAIL on something that's genuinely in between.
