---
title: The Canonical Version
description:
  Authority — who gets to say which copy is real, and on what grounds, once
  a hash or a timestamp can no longer settle the question
week: 8
date: 2027-04-12
teachers:
  - idris-fenn
slides: /decks/week-08/
related:
  - sessions/08-name-the-ground
---

Somewhere between "these two files differ" and "someone acts on one of
them," a decision gets made about which one counts. That decision isn't a
technical fact. It's a claim about authority, and it has to be grounded in
something.

## Four grounds people actually use

- **Possession.** Whoever holds the master copy — the signed contract in
  legal's filing system, the "source of truth" spreadsheet on one person's
  laptop. Authority by custody, regardless of who else has a copy.
- **Position.** Whoever's role entitles them to decide — an editor, a
  maintainer, a manager with sign-off. Authority by standing, independent of
  who actually touched the file most recently.
- **Recency.** Whoever edited last. The most commonly used ground, and the
  weakest: "latest" is a timestamp, not a judgement, and a timestamp can't
  tell you whether the last person to touch the file had any standing to.
- **Consensus.** Whoever most people currently defer to. This can shift
  without the file changing at all — a version becomes canonical because
  enough people started treating it that way, not because of anything that
  happened to its bytes.

## Why they conflict

These four grounds don't agree by default, and the disagreements are where
this gets consequential. The most recent edit isn't automatically
authoritative if the editor lacked standing to make it. The copy in
possession of one department can lose to a court's reading of a different
copy. A team can build consensus around a draft that the person with formal
position never approved. None of this is settled by comparing bytes —
by week 2's tests, all four copies could hash identically or differently and
it would tell you nothing about which one anyone should trust.

## Where this goes

Every one of these grounds is something a human applies with judgement,
case by case. Next week looks at what happens when a machine has to make
this same decision automatically, in real time, with no human available to
ask — because that is exactly what a file-sync service does, constantly,
and mostly gets away with.
