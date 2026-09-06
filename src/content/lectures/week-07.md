---
title: Merge Conflict
description:
  Two true, incompatible histories, and what actually gets decided when a
  system runs out of authority to decide it
week: 7
date: 2027-04-05
teachers:
  - marisol-quaye
slides: /decks/week-07/
version: "1.1"
revisions:
  - version: "1.0"
    note: Minor copyedit; no change to the claims made.
related:
  - sessions/07-resolving-by-hand
---

A merge conflict is not an error. It is a system reporting, accurately, that
it has reached a decision it has no basis to make. Both versions are valid.
Both histories are true. They cannot both be the file.

## What a merge can do without asking

Most of a merge is arithmetic, and it works. Given a common ancestor and two
descendants, a three-way merge asks a narrow question of each region of
text: did one side change it, both sides, or neither? If one side changed a
region and the other left it alone, the change applies: the untouched side
expressed no preference, so there is nothing to weigh. Merges succeed
silently and often, and this is the reason.

The conflict arises in exactly one case: both sides changed the same region,
differently. Now the system has two candidate texts, no ancestor to defer
to and, as week 8 will put it more carefully, no ground on which to
prefer either. So it stops, writes both into the file with markers around
them, and hands the region back:

```text
<<<<<<< HEAD
the committee reviewed the findings
=======
the committee noted the findings
>>>>>>> revision
```

Those markers are the honest part of the operation. The system is declining
to fabricate a decision it cannot support, and saying so in the file where
the problem is.

## What actually gets decided

The technical resolution is trivial: pick lines, delete markers, save. That
is not the decision. The decision is which of two intents survives, and the
two texts above are not stylistic variants: *reviewed* and *noted* make
different claims about what the committee did, and one of them will be what
the record says happened.

Three properties of this decision are worth naming, because the tooling
conceals all three. It is **lossy**: the discarded version does not go
anywhere the reader will find. It is **unattributed**: the resolved file
records who committed the merge, not who was overruled. And it is
**unexplained**: no format has a field for why, so the reason lives in
someone's memory or nowhere. A resolved merge looks exactly like text that
was never contested.

That is what this week's lab is for, and the reason the Merge Conflict, In
Writing assessment asks for prose rather than a file: the artefact a merge
produces has no room in it for the only part that was difficult.

## Where this goes

Someone resolved that conflict, and the file now reads as though there was
never a question. Next week asks what entitled them to decide, and what
anyone's claim to hold the real version actually rests on.
