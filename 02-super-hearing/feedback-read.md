# Two piles of feedback, read together

Module 2 · Super-Hearing · Yonatan Maya, PM, Rook Dispatch

Sources: the four interviews in `00-rook/feedback/interviews/` (Sofia
Marino's console-redesign calls, 2–5 Sep) and the 25 tickets in
`00-rook/feedback/tickets/` (13 Aug – 5 Sep). Every count below can be
checked against those files. Each quote is word for word.

---

## The interviews: what the four handlers are unhappy about

| Group | How many of 4 | One line |
|---|---|---|
| The offer is gone before the responder can answer | **3** (Ambrose, Aunt Dot, Halloran) | "by the time he's actually got a thumb on the screen — it's gone." (Aunt Dot) |
| Long stretches where the phone never goes off | **2** (Aunt Dot, Kip) | "Meteor Mite's been texting me all week asking if something's broken because it's so quiet." (Kip) |
| Status text too small to read at a glance | 2 (Ambrose, Aunt Dot) | "Larger text on the status badge." (Ambrose) |
| Alerts are hard to tell apart, or don't reach the handler | 2 (Aunt Dot, Kip) | "something that tells me too, not just him" (Aunt Dot) |
| No dark mode | 1 (Kip) | "dark mode. I am begging." |
| Saved filter resets without warning | 1 (Ambrose) | "Twice now it's reverted to the default view" |
| Supply: requisitions stuck in one queue | 1 (Halloran) | "One queue, everything in it, doesn't matter if it's laces or plate." |

**Said by only one person, and the most useful line in the pile.**
Kip runs two responders in the same city and watched them go opposite
ways in the same week: *"Mite thinks Mite's been forgotten. Gale's
exhausted. I'm looking at two cards on the same screen that might as
well be two different products."* With one handler behind both cards,
the handler can't be the cause.

None of the four calls was about 4.2. Every problem above surfaced as
an aside in a console-redesign interview.

**My read after the interviews:** the trouble with 4.2 is that offers
disappear before responders can answer them.

---

## The tickets: same treatment

| Group | How many of 25 | One line |
|---|---|---|
| The phone never goes off | **16** | "is my account broken. nothing in like 10 days" (T-009, Nightwell) |
| Silence, then the one rare offer is lost before they can answer | **5** | "first one in weeks and it vanished before i could even swipe. of course" (T-023, The Drift) |
| The offer is gone before they can answer | **4** | "literally had my thumb on the screen and it switched to someone else" (T-015, Cindermark) |

So **21 of 25** tickets talk about silence, and only 9 talk about losing
an offer they saw.

**Who filed them.** 15 were filed by handlers and 10 by responders. Twelve
responders are named across the 25 tickets. Nightwell, Ironvale and The
Undertow have three tickets each. **Four responders appear in no ticket at
all:** Meteor Mite, Vesper, The Gale and Sgt. Bulwark.

**What changed after 12 August.** All 25 tickets are dated after the
release (the earliest is 13 Aug), so this folder has no "before" to
compare against. The change shows up *inside* the period instead:

| Week of | Lost before answering | Silence | Silence, then lost |
|---|---|---|---|
| 10 Aug (release week) | 1 | 1 | 0 |
| 17 Aug | 2 | 6 | 0 |
| 24 Aug | 1 | 6 | 1 |
| 31 Aug | 0 | 3 | 4 |

The first complaints are about offers vanishing. By the last week the
most common ticket is a responder who waited weeks for anything and
then lost it.

---

## Where the two piles disagree

**Loud in the interviews, rare in the tickets.** Losing an offer while
reaching for the phone came up in 3 of 4 interviews but only 9 of 25
tickets. People notice it because it happens in front of them.

**All over the tickets, barely in the interviews.** Silence is in 21 of
25 tickets but only 2 of 4 interviews, and there only as an aside. A
missing ping doesn't happen in front of anyone. You notice it later,
or not at all.

**How can both piles be right?** They describe two different failures.
A ping that vanishes before you can answer is the timeout. A ping that
never arrives at all is about who gets asked. 4.2 changed both: the
60-second timeout and the ranking weights.

## Then I checked the tickets against the numbers

Before trusting the silence tickets, I lined each one up against
`00-rook/data/callout-history.csv` for the week it was filed (full
table: `03-rewind/the-number.md`). **Only 4 of the 21 silence tickets
match the data.** All four are about responders whose pings really did
collapse: The Undertow (T-005, T-013, T-019) and Farlight (T-018).

**The other 17 contradict the data.** Some examples:

| Ticket | What it says | Same week in the export |
|---|---|---|
| T-009, 22 Aug, Nightwell | "nothing in like 10 days" | 18 sent, 14 taken |
| T-014, 27 Aug, Stormwrack's handler | "the quietest I've seen him since he joined" | 18 sent, 13 taken |
| T-025, 5 Sep, Ironvale's handler | "first one in almost a month" | 12 sent, 9 taken |
| T-020, 1 Sep, Cindermark's handler | "only one callout" in ten days | 12 sent, 9 taken |

A responder who took 14 callouts in a week was not sitting in silence,
so a "pings weren't delivered" explanation doesn't cover these. Two
open questions for Wen Li and Ravi Menon: does the export attribute
pings to the right responder, and what exactly does it count? Until
that's settled, I use the export for volume and the tickets as a
signal of distress, not as a measurement.

**The four responders whose numbers actually collapsed** are Farlight,
Meteor Mite, The Undertow and Vesper. Two of them, **Meteor Mite and
Vesper, never appear in a ticket.** The only trace of them in the
feedback is two unprompted asides in interviews about something else.

---

**My read after both piles:** the trouble with 4.2 is two problems, not
one. Offers vanish before people can answer them, which everyone
notices. And four responders quietly stopped being asked at all, which
only the numbers show, and half of them never complained.

**What I believed after the first pile and stopped believing after the
second:** that the timeout was the whole story, and that the ticket
queue was where I'd find the people it hurt most.
