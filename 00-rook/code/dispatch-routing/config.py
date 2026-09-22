"""Tuning values for callout routing.

Everything in here changes who gets asked to take a job, so don't
change anything in here without telling Marcus.
"""

# How long a callout offer stays on a responder's phone before we give
# up on them and move to the next person on the list.
OFFER_TIMEOUT_SECONDS = 90           # was 60 in 4.2, 90 before that and again from 4.3

# How much each input counts when we rank who to ask first. These are
# relative to each other; they don't need to add up to anything.
# Not touched in 4.3 — the 4.2 rebalance toward proximity was a real,
# requested change and isn't what 4.3 is fixing.
WEIGHT_PROXIMITY = 0.60              # was 0.45 until 4.2
WEIGHT_RECENT_ACCEPTANCE = 0.25      # was 0.40 until 4.2
WEIGHT_CAPABILITY_MATCH = 0.15       # unchanged since 4.0

# Points on and off the recent-acceptance score.
ACCEPTANCE_CREDIT = 0.08
DECLINE_PENALTY = 0.12               # an active decline — they answered "no"

# 4.3: a missed offer isn't the same as a "no". We don't know they'd
# have declined, so it costs less than an active decline.
TIMEOUT_PENALTY = 0.04

# 4.3: how much of the gap back to NEUTRAL_SCORE closes each week for
# a responder sitting below it, whether or not they got offered
# anything. Only ever pulls a low score up — never pulls a high score
# down. Answers the TODO Wen left on this in 2019.
DECAY_RATE = 0.08

# 4.3: an available responder's score is never allowed to sit below
# this indefinitely, regardless of how it got there.
RECOVERY_FLOOR = 0.20

# The score never goes outside these.
SCORE_FLOOR = 0.0
SCORE_CEILING = 1.0

# Anyone further out than this scores zero on proximity.
PROXIMITY_HORIZON_MINUTES = 45
