---
title: Sync Is a Lie
description:
  What a sync service is actually doing when it says two devices are in
  sync, and what the conflict copy in your folder is a record of
week: 9
date: 2027-04-19
teachers:
  - marisol-quaye
slides: /decks/week-09/
related:
  - sessions/09-anatomy-of-a-conflict-copy
---

"In sync" is a status message, not a state. It means: as of the last
successful exchange, no device reported anything the service couldn't
reconcile. It does not mean the devices currently hold the same bytes.
Between those two things sits every conflict copy you have ever found in a
folder and deleted without reading.

## What the service is actually doing

A sync service has one hard constraint: it cannot ask you. It has to decide
which version wins, immediately, using only what it can observe — usually a
modification timestamp and a change counter, on clocks that belong to
different machines and don't agree. Last week's four grounds are not
available to it. Possession is meaningless when every device has a copy.
Position is unknowable — the service has no idea that one of the two editors
is your supervisor. Consensus can't be polled. Recency is the only ground a
sync service can mechanically apply, which is why it applies it, which is
why it is wrong on a predictable schedule.

## The conflict copy is the honest part

When two devices both edited while offline, the service has two versions
neither of which can be discarded without data loss. So it declines to
decide, writes both to disk, and names the loser after the device or the
person it came from:

```text
budget.xlsx
budget (Marisol's conflicted copy 2027-04-14).xlsx
```

That second file is not a malfunction. It is the service correctly reporting
that it hit a decision it has no authority to make, and handing it back to
the only party who does. The failure is downstream: nobody reads it, because
it looks like litter rather than a finding.

## Where this goes

The conflict copy at least preserves both versions intact. Next week looks
at the other kind of loss — the kind where nothing is duplicated, nothing is
overwritten, and the file quietly stops being what it was anyway.
