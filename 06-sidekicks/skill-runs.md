# review-checklist: written once, run twice, then scheduled

Module 6 · Sidekicks · Yonatan Maya, PM, Rook Dispatch
Skill: `.claude/skills/review-checklist/SKILL.md`. It lives inside this
repo, so it respects the session-scope rule in `CLAUDE.md`, and Claude
Code loads it for anyone who opens the folder.

---

## Run 1: my own Module 5 brief, until it was right

| Version | Owner | Success measure | Scope | Problem first | What happened next |
|---|---|---|---|---|---|
| `drafts/status-note-to-helen.md` | ~~PASS~~ → **FAIL**: signed "— [You]" | **FAIL**: no way to check it later | PASS | PASS | The skill passed the owner check on the first-person voice alone. **Fixed the skill:** placeholders now fail. |
| `drafts/one-pager-v1.md` | **PARTIAL**: "For Helen", but nobody owns the outcome | **FAIL**: describes the change, never what "worked" means | PASS | PASS | **Fixed the brief:** named owner, three checkable measures. |
| `brief.md`, first pass | PASS | PASS | **PARTIAL**: "contact the four directly" appears mid-brief, beyond the ask as first stated | PASS | **Fixed the brief:** stated both parts of the ask at the top. |
| `brief.md`, final | **PASS**: "Owner: Yonatan Maya, PM, Rook Dispatch" | **PASS**: three thresholds plus a decision rule | **PASS**: the ask at the top matches the scope section at the end | **PASS**: "The problem" comes before "What changes" | Ready to go further. |

## Run 2: four briefs I'd never seen (`06-sidekicks/briefs/`)

```
review-checklist — run on 06-sidekicks/briefs/
4 briefs checked, 4 flagged.

bulk-callout.txt
  owner named ................. NO — flagged
  success measure .............. yes
  scope stays bounded .......... yes
  problem stated before fix .... yes
  -> 1 flag: no owner named. Header says only "Product, Dispatch", and
     it ends "flagging this for whoever picks it up next quarter ...
     nobody's picked it up yet."

handler-phone-app.txt
  owner named ................... yes (Sofia)
  success measure .............. yes
  scope stays bounded .......... yes
  problem stated before fix .... NO — flagged
  -> 1 flag: solution before problem. Opens with "We should build a
     phone app for handlers"; the problem (Aunt Dot) arrives in the
     second section, "What this solves".

requisition-approval-chains.txt
  owner named ................... yes (Halloran's team, Supply)
  success measure ............... yes
  scope stays bounded ........... NO — flagged
  problem stated before fix .... yes
  -> 1 flag: scope grows mid-document. "That's the whole ask." is
     followed straight away by "And while we're building the approval
     step, we should also ..." plus a routing-around rule, a cross-site
     dashboard, handler visibility and a spreadsheet replacement.

routing-override-audit-log.txt
  owner named ................... yes (Marcus's team)
  success measure .............. NO — flagged
  scope stays bounded .......... yes
  problem stated before fix .... yes
  -> 1 flag: no success measure. Says what gets logged and where it
     shows up; never how anyone would know it's working.
```

**Against the reference run (`scheduled-run-output.txt`): 4 of 4
match.** Same flag on the same brief, and no extra flags. Getting
there took two fixes to the skill:

- "Marcus's team" originally **failed** my owner rule ("a team doesn't
  count"). A team named by its lead is accountable, so the rule now
  accepts it.
- My scope rule compared the opening with the closing section. On the
  requisition brief, the closing success measure narrows back down to
  the $2,000 sign-off, so a start-versus-end comparison would have
  **passed** it. The rule now reads the whole document.

**One thing the checklist doesn't catch.** `handler-phone-app.txt` says
Aunt Dot "described finding out her responder had declined a callout
only when she happened to glance at the console later that evening."
Her interview (`00-rook/feedback/interviews/aunt-dot.txt`) says
something else: she hears the phone buzz, shouts upstairs, and he
loses the offer before he can answer. The brief passes all four
checks with evidence that doesn't match its source. That's a possible
fifth check: does the brief's evidence say what the source says?

## Run 3: on a schedule

Set to run every Monday morning on `06-sidekicks/briefs/` and
`05-super-speed/brief.md`, and to report what it finds. Nothing needs
to be ready for it to fire. The habit is set; I don't have to watch it.
