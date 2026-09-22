# Dispatch routing — changelog

## 4.3 — proposed, not yet shipped
- Callout offer timeout back to 90s (was cut to 60s in 4.2).
- A missed offer is no longer scored the same as an active decline —
  new, smaller `TIMEOUT_PENALTY`.
- Recent-acceptance score now decays back toward neutral over time for
  anyone sitting below it, whether they're getting offered anything or
  not (`history.decay_all()`, run weekly). Only ever pulls a low score
  up; never pulls a high score down.
- Added `RECOVERY_FLOOR` — an available responder's score can't sit
  below this indefinitely.
- Proximity/recent-acceptance weights from 4.2 are unchanged. That
  rebalance was a real, requested fix and isn't part of what this
  patch addresses.
- Fixes the trap where a responder who fell behind in ranking had no
  way to recover, since the only way the score improved was by being
  offered something — and a low score was exactly what stopped that.
  Confirmed against `callout-history.csv` (Farlight, Meteor Mite, The
  Undertow, Vesper) and a routing simulation built to test the fix
  before shipping it.

## 4.2 — 12 Aug 2026
- Rebalanced ranking weights: proximity up, recent acceptance down.
- Callout offer timeout 90s -> 60s.
- Console filter persistence (not in this service).

## 4.1 — 16 Jun 2026
- Proximity now uses a travel-time estimate instead of straight-line
  distance.
- Bulk callout.
- Mobile push reliability.

## 4.0 — 7 Apr 2026
- Console navigation.
- Responder profile redesign.
- Routing override audit log.
