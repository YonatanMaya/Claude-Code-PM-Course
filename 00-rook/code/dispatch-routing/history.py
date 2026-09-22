"""Recent acceptance — a running score of how often somebody has been
taking the callouts we send them.

One of the three inputs to ranking. Sits between 0 and 1. Everyone
starts at NEUTRAL_SCORE when we take them on.
"""

from config import (
    ACCEPTANCE_CREDIT,
    DECLINE_PENALTY,
    TIMEOUT_PENALTY,
    DECAY_RATE,
    RECOVERY_FLOOR,
    SCORE_FLOOR,
    SCORE_CEILING,
)

NEUTRAL_SCORE = 0.5

_scores = {}


def recent_acceptance(responder):
    """This responder's score right now. Read by routing.score()."""
    return _scores.get(responder.id, NEUTRAL_SCORE)


def record_accepted(responder):
    """They took the callout. Score goes up."""
    _set(responder, recent_acceptance(responder) + ACCEPTANCE_CREDIT)


def record_declined(responder):
    """They actively turned it down. Score goes down."""
    _set(responder, recent_acceptance(responder) - DECLINE_PENALTY)


def record_timed_out(responder):
    """We ran out of time waiting on them. Score goes down, but less
    than an active decline — we don't actually know they'd have said
    no.

    4.3. Used to be scored identically to record_declined(); splitting
    it out is part of what makes the offer timeout safe to keep short.
    """
    _set(responder, recent_acceptance(responder) - TIMEOUT_PENALTY)


def decay_all():
    """Ease every below-neutral score back toward NEUTRAL_SCORE, and
    enforce the recovery floor. Run this on a schedule (weekly),
    independent of whether anyone got offered anything.

    4.3. Answers the TODO Wen left here in 2019: a responder who's
    stopped getting offered work has, until now, had no way for their
    score to recover on its own — the only way up was an offer, and a
    low score is exactly what was keeping the offer from reaching
    them. This only ever pulls a low score up; a score already at or
    above neutral is never touched, so nobody's standing erodes
    because of this.
    """
    for responder_id, value in list(_scores.items()):
        if value < RECOVERY_FLOOR:
            value = RECOVERY_FLOOR
        if value < NEUTRAL_SCORE:
            value += (NEUTRAL_SCORE - value) * DECAY_RATE
        _scores[responder_id] = max(SCORE_FLOOR, min(SCORE_CEILING, value))


def _set(responder, value):
    _scores[responder.id] = max(SCORE_FLOOR, min(SCORE_CEILING, value))
