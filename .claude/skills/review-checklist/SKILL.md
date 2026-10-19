---
name: review-checklist
description: Review a brief, one-pager, proposal or spec before it goes any further, using the same four checks every time — named owner, success measure, scope that stays bounded, problem explained before the fix. Use this whenever someone asks to review, check, vet or sanity-check a brief or one-pager, points at a file or folder of briefs (for example 06-sidekicks/briefs/ or 05-super-speed/brief.md), or asks "is this ready to send", even if they don't name the checklist.
---

# review-checklist

A review habit, written down once so it runs the same way every time,
with or without anyone watching.

## How to run it

- **One brief** (a file path, pasted text, or "the brief we just wrote"):
  read the whole brief first, then run the four checks in order and
  answer in the single-brief format below.
- **A folder of briefs:** run the four checks on every file in it, then
  answer in the folder format below.

Quote or point to the exact place in the brief that decided each
verdict. A verdict nobody can trace back to the text is just an
opinion.

## The four checks

### 1. It names who owns it

Someone has to be accountable for what happens next, or nothing does.

- **Pass:** a named person ("Sofia"), or a team identified by the person
  who leads it ("Marcus's team builds it", "Halloran's team, Supply").
- **Fail:** only a department label ("Product, Dispatch"), "the team",
  "we", or ownership deferred to the future ("flagging this for
  whoever picks it up next quarter").
- **Fail:** an owner slot that was never filled in, such as `[You]`,
  `[Name]`, `TBD`, or a blank signature. A first-person voice ("I'm
  proposing…") isn't enough if the name attached to it is a
  placeholder.

### 2. It says how we'll know it worked

Without a success measure, a brief asks for trust instead of making a
case.

- **Pass:** something someone could check later and answer yes or no:
  a number, a threshold, or something that observably stops happening.
  A measure with an honest "no baseline yet" still passes.
- **Fail:** the brief describes what gets built, logged or shown, but
  never what "it worked" would look like.

### 3. The scope stays bounded

Write down the ask exactly as the brief first states it. Then read
*everything* after that, including the middle, not only the closing
section.

- **Pass:** every later section describes the same-sized thing.
- **Fail:** anything added beyond the first statement of the ask, at
  any point in the document. It still fails even if the closing
  section quietly narrows back down. A reasonable idea that arrived by
  scope creep still gets flagged.

### 4. It explains the problem before it proposes a fix

- **Pass:** the problem (what's wrong, for whom, and how we know)
  appears in the document before the proposed solution.
- **Fail:** the brief opens with what to build, and the problem shows
  up afterwards as justification, or never shows up at all.

Use **PARTIAL** when a check is present but weak, for example an owner
who is named but clearly not accountable. Don't force a PASS or FAIL
onto something that's genuinely in between.

## Output: one brief

```
1. Owner — PASS / FAIL / PARTIAL — [one line, citing the place in the brief]
2. Success measure — PASS / FAIL / PARTIAL — [one line, citing the place]
3. Scope stays bounded — PASS / FAIL / PARTIAL — [first statement of the ask vs. what got added, and where]
4. Problem before fix — PASS / FAIL / PARTIAL — [one line, citing the order]

Overall: [one sentence: ready to go further, or the one thing to fix first]
```

## Output: a folder of briefs

```
review-checklist — run on <folder>
<N> briefs checked, <N> flagged.

<file name>
  owner named ................. yes (<who>) / NO — flagged
  success measure .............. yes / NO — flagged
  scope stays bounded .......... yes / NO — flagged
  problem stated before fix .... yes / NO — flagged
  -> <n> flag(s): <one line on the flag, quoting the brief>
```

## Calibration history

This skill has been run against real briefs and corrected three times.
Each correction is now part of the rules above.

1. A first-person voice passed the owner check even though the
   signature read `— [You]`. Placeholders now fail.
2. "Marcus's team" failed the owner check, but a team named by its lead
   is accountable, and the reference run agrees. It now passes.
3. A brief that grew in the middle (`requisition-approval-chains.txt`)
   could pass a start-versus-end comparison, because its closing section
   narrows back down. The scope check now reads the whole document.
