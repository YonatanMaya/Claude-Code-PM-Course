# Rook Industries — course working file

## Session scope — Product School lab

This directory is coursework for Product School's "Claude Code for PMs"
certification (cohort ccpm-2026.1). Everything in it is a fictional
teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

I'm the new PM for Rook Dispatch, starting September 2026, taking over from
Priya Raghunathan.

### The company

Rook Industries builds coordination and provisioning software for
independently-operating masked responders and the handlers/quartermasters
who support them. Founded 2014, HQ at Site Aleph, ~241 employees. Two
products, both priced per active responder, shipping on a monthly release
train (4.x numbering):

- **Rook Dispatch** (mine) — responder coordination: availability,
  proximity, callout routing, acceptance. Used by handlers (web console)
  and responders (mobile).
- **Rook Supply** — gear provisioning: requisitions, maintenance, failure
  reports. Used by handlers and quartermasters.

Responder cover identities are never stored — we hold capability tags,
availability, and callout history only, never a legal identity. Don't
design anything that assumes we can map one to the other.

### How Dispatch works

Incident comes in → Dispatch ranks available responders → top-ranked
responder gets a callout offer on mobile → they accept or decline (or the
offer times out) → it moves to the next responder → acceptance closes the
loop.

**Routing priority** ranks responders on proximity (travel-time estimate),
current availability, capability match, and recent acceptance history.
Declining/timing out lowers a responder's recent-acceptance component,
which lowers their routing priority until it recovers. Routing config
ships with the release — it's not a runtime setting handlers can touch.

**Key metrics:** acceptance rate (headline metric — share of offers
accepted vs. declined/timed out), time-to-accept (median seconds to
accept), coverage gap (incidents where no available responder had the
required capability tags).

**Where Supply touches Dispatch:** Dispatch writes the Responder
Availability Record; Supply reads it (read-only) to schedule gear
maintenance into low-callout-load windows.

### Vocabulary

- **Responder** — not a Rook employee, independently operating.
- **Handler** — manages a responder or small group: availability, gear,
  readiness. Usually the one actually in the product.
- **Quartermaster** — owns equipment stock/approvals (Supply side).
- **Callout** — a request for a responder to attend an incident.
- **Callout offer** — one callout presented to one responder, awaiting
  accept/decline.
- **Decline** vs **timeout** — distinct in the data, both send the callout
  onward.
- **Capability tags** — flight, structural-entry, hazmat-tolerant,
  cold-weather, aquatic, crowd-management, de-escalation.
- **Mutual aid** — responders across regions covering for each other; not
  built yet, on the Q4 exploration list.

### Where things stand (as of early September 2026)

**4.2 shipped 12 August** — the big change was "who gets pinged": proximity
weighted more heavily relative to recent acceptance history (a
long-requested fix for responders in wide geographies). Also cut the ping
timeout from 90s to 60s, and added console filter persistence.

Since then, acceptance is down and callout-related tickets are running
~3x normal, split roughly 2:1 between "phone never rings" and "offer's
gone before I can answer" (the second is explained by the timeout cut; the
first isn't, yet). Priya's read: mostly seasonal (August is always soft)
plus two changes landing at once — she deliberately did not want this to
become a "revert 4.2" conversation, since the routing change was a
genuine, long-standing ask. Marcus and the team agreed to hold off on
conclusions until I'd had a week to look myself; the real regroup on the
4.2 picture is still pending. Ravi Menon (Data) has weekly acceptance
numbers; Nadia Hoffmann (Support) has the ticket breakdown.

**Open threads inherited from Priya:**
- No written documentation of how routing/"who gets pinged" actually
  works — it lives in Wen Li's head. On my list to write.
- A few Q3 roadmap items got squeezed out of 4.2's compressed timeline;
  need to check with Helen which are still committed.
- Console filter persistence (4.2) will generate some cosmetic-only
  tickets — noise, not worth chasing.

**Q3 roadmap (Dispatch items):** Change to who gets pinged, Availability
Confidence (surfacing a confidence score next to stated availability —
driven by support escalations), and ping timeout tuning are all shipped in
4.2 and committed/locked. Shared cover between responders is Q4,
exploring. (Supply: requisition approval chains committed for 4.3;
handler phone app is Q4/exploring.)

### People (Dispatch team, primarily Chicago + Berlin)

- **Helen Achebe** — Director of Product (Dispatch & Supply), Chicago. My
  manager. Owns roadmap/commitments.
- **Marcus Oyelaran** — Engineering Manager, Dispatch, Chicago. First stop
  for anything uncertain; can pull numbers.
- **Wen Li** — Staff Engineer, Dispatch, Berlin. Built routing — the person
  to talk to (not a doc) to understand how ranking actually works.
- **Sofia Marino** — Product Designer, Dispatch, Chicago. Console and
  phone app.
- **Nadia Hoffmann** — Support Lead, Dispatch & Supply, Berlin. Sees
  complaint volume first; worth a standing check-in.
- **Ravi Menon** — Data Analyst, Dispatch & Supply, Singapore. Weekly
  acceptance-rate reporting; requests go through #data.
- **Priya Raghunathan** — my predecessor, departed 21 August after 14
  months as sole PM on Dispatch. Left a handover doc.
