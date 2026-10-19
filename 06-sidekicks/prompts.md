# 06 · Sidekicks — prompts

**Context:** You joined Rook two weeks ago as PM on Dispatch.
Release 4.2 shipped on 12 August, just before you arrived, and
landed badly. You've spent five sessions on it: finding out what
went wrong, then building the fix nobody had — a working prototype,
by hand, in one sitting, for one room.

At the end of the session, ask Claude Code to save the prompts you
wrote yourself below — not the starter prompt. The closing slide has
the exact prompt to paste. By Module 6 this file is a prompt library
built from your own questions.

---

### 1.

What is the brief?

### 2.

Why my partner had this:

Bulk Callout — one-pager
Product, Dispatch
12 January 2026

Problem
When something big happens — a building evacuation, a multi-block
search, anything that needs more than one responder — a handler right
now sends callouts the same way they'd send one: pick a responder,
wait, pick the next. Halloran mentioned it too, on the Supply side,
when a shift needs several people kitted out at once. For a handler
managing more than one responder, or covering for another handler
who's out, that's slow exactly when speed matters most.

Proposal
Let a handler select several responders from the console and send them
all the same callout in a single action. Each responder still gets
their own accept/decline, on their own phone, same as today — this
isn't a group message, it's the existing callout flow sent to more
than one person at once.

Success measure
Fewer support tickets mentioning a handler who "just started calling
people directly" during a multi-responder incident. Time-to-full-
coverage on a multi-responder callout should drop, though we don't
have a clean baseline for it yet — worth getting one before this
ships.

Scope
Only the existing callout flow, sent to more than one responder. No
group chat between responders, no bulk requisitions, no change to how
any individual responder's callout is scored or ranked. If a table
needs to send different jobs to different people, that's still one
callout at a time — this is only for "the same job, several people."

Open questions
Flagging this for whoever picks it up next quarter. Console changes
will need Sofia's input on the multi-select interaction, and
engineering will need to scope the actual send logic — noting it here
so it isn't lost, but nobody's picked it up yet.

### 3.

Why we had to is difference - short and straight forward answer

---

### The prompt that generated `final-report.html`

The lines from my message that asked for the final report:

אני פשוט רוצה להגיש הכל ולסיים עם זה ולהגיש בצורה טובה
אם אתה צריך לשנות משהו אז כמובן שתשנה או תוסיף..
