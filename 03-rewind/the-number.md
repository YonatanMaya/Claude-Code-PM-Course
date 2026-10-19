# The number I'd put in front of Helen

Module 3 · Rewind · Yonatan Maya, PM, Rook Dispatch
Source: `00-rook/data/callout-history.csv` (one row per responder per
week, 29 Jun – 31 Aug, 160 rows)

---

## The number

> **Four of sixteen responders went from about 12 pings a week to about
> 2 within three weeks of Release 4.2, while total pings across the
> pool fell only 6%.**

The four are Farlight, Meteor Mite, The Undertow and Vesper. They weren't
declining more beforehand: their acceptance rates over the six weeks
before 4.2 were 69–82%, the same range as everyone else.

## The rows it came from

Pings sent / pings taken, per week. 4.2 shipped on Wednesday 12 Aug,
inside the week of 10 Aug.

| Week of | Farlight | Meteor Mite | The Undertow | Vesper |
|---|---|---|---|---|
| 29 Jun | 12 / 9 | 11 / 7 | 12 / 9 | 14 / 11 |
| 6 Jul | 12 / 9 | 12 / 9 | 11 / 9 | 13 / 10 |
| 13 Jul | 11 / 8 | 10 / 6 | 12 / 9 | 15 / 13 |
| 20 Jul | 12 / 9 | 11 / 7 | 13 / 10 | 14 / 11 |
| 27 Jul | 13 / 10 | 12 / 9 | 12 / 10 | 13 / 11 |
| 3 Aug | 12 / 8 | 11 / 8 | 12 / 9 | 14 / 12 |
| **10 Aug** | 10 / **4** | 10 / **4** | 11 / **4** | 12 / **6** |
| **17 Aug** | **3** / 0 | **4** / 1 | **4** / 1 | **5** / 1 |
| 24 Aug | 1 / 0 | 2 / 0 | 1 / 0 | 2 / 0 |
| 31 Aug | 0 / 0 | 1 / 0 | 1 / 0 | 1 / 0 |

CSV line numbers (header is line 1): Farlight 5, 21, 37 … 149 · Meteor
Mite 8, 24, 40 … 152 · The Undertow 16, 32, 48 … 160 · Vesper 17, 33,
49 … 161 (every 16th line).

**The sequence, in two steps.** In release week, pings *sent* barely
moved, but pings *taken* fell by half or more for all four. The week after, pings
sent fell off a cliff, by 6 to 7 for each of them in a single week. In
the six weeks before that, no responder in the file moved by more than
2 in a week.

## Worked out a second way

**Way 1: each responder against their own baseline.** I compared each
responder's average over the six full weeks before 4.2 with the three
full weeks after, and flagged anyone who fell below half. Exactly four
responders cross that line: Farlight −89%, The Undertow −83%, Vesper
−81%, Meteor Mite −79%. The next worst is Corporal Ashgrove at −27%.

**Way 2: their share of everything.** Before 4.2, the four received
294 of 1,034 pings (28.4%). After, they received 25 of 485 (5.2%).

The two methods agree. The pings didn't disappear, they moved. Ten of
the other twelve responders gained, The Gale most (+49%), from 13 to
19 pings a week.

## Why nobody saw it

The headline metric, pool-wide acceptance rate, ran at 75–78% before
4.2, dropped to **54.2%** in release week, then climbed back to 65.8%,
66.7% and **72.7%** by the week of 31 Aug. On a dashboard that looks
like a recovery. It's actually the four shrinking to such a small share
of pings that their 0% stops pulling the average down.

## What these rows can't tell me

- **Why.** These are weekly totals per responder: no per-incident ranks,
  no locations, no capability tags. The mechanism comes from the code
  (see `04-x-ray-vision/what-the-code-does.md`), and Wen Li's
  per-incident logs are needed to confirm it.
- **Whether the tickets are right.** For 17 of the 21 tickets that
  report silence, this file shows normal or rising volume that same
  week (see `02-super-hearing/feedback-read.md`). This file and the
  tickets can't both be right about those weeks.
- **Seasonality.** The file starts on 29 June, so there's no August last
  year to compare against. The pool-wide −6% could be seasonal. A drop
  of 79–89% concentrated in four people can't be.
