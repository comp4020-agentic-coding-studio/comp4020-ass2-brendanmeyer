---
title: Archive or Delete?
description:
  Retention, digital decay, and what it takes to build a system that tells
  you the truth about which version is current
week: 12
date: 2027-05-10
teachers:
  - idris-fenn
slides: /decks/week-12/
related:
  - sessions/12-a-system-that-does-not-lie
---

Keeping everything is not a retention policy. It is the absence of one, and
it has a specific cost: every version you keep is another candidate for
being mistaken for the current one. Week 1's filename existed because four
files were kept and none of them was marked. Deleting is how a system stops
lying about which version counts — and deleting the wrong thing is how it
starts lying in the other direction.

## Decay does not wait for a decision

Files degrade without anyone touching them. Bit rot on failing media. A
proprietary format whose only reader stops shipping. An external link that
returns a different page than it did when it was cited. A cloud document
that is a pointer, not a file, and resolves to nothing once the account
lapses. Encryption whose key is no longer held. None of these are deletions.
Each produces an artefact that is still listed in the directory, still
opens or appears to, and no longer contains what it did.

The archival response is not storage. It is migration — periodically
re-encoding holdings into currently readable formats, which is week 10's
conversion damage accepted deliberately, at a known cost, because the
alternative is total loss later rather than partial loss now. Retention is
the choice of which losses to take and when.

## What a non-lying system requires

Everything in this course has been a system telling a small untruth about
which version was current. A filename asserting finality it could not
enforce. A timestamp standing in for authority. A sync status standing in
for agreement. A conversion reporting success while dropping content. So the
requirements are the inverse of those failures:

- **Currency is stated, not inferred.** One version is marked current, by
  someone, on a ground they could name. Not the newest by default.
- **History is recorded where the work happens.** Not reconstructible from
  residue later — recorded at the time, as week 11's archivists insisted.
- **Losses are logged.** A conversion, a migration, a deletion each leave a
  record of what was dropped, so week 10's silent gaps become visible ones.
- **Deletion is a decision with an author.** Not a cleanup, not a quota
  eviction, not the disk filling up.

A version-control system does most of this, which is why it works. It also
does not solve the problem, because the problem was never the tooling. The
four files called `final` were produced by people who had access to
version-control software and did not reach for it, because the naming
workaround was cheaper at the moment of the save and the cost arrived later,
distributed across everyone who had to guess.

## Where this leaves you

The course opened by claiming digital work is rarely one file — that it is a
family of near-duplicates competing to become the truth. Twelve weeks later
the claim holds, and the reason is now specific: nothing in the ordinary
handling of files records which one won, or why. Deciding is still human
work. What a well-built system can do is refuse to pretend it has already
happened.
