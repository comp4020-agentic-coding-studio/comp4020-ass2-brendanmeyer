---
title: Copies & Clones
description:
  Duplication vs. derivation — when a copy stops being a copy and becomes its
  own thing, and why no technical test can tell you the moment it happened
week: 3
date: 2027-03-08
teachers:
  - marisol-quaye
slides: /decks/week-03/
related:
  - sessions/03-when-did-it-diverge
---

Last week ended on a gap: two files can pass every identity test at the
moment one is copied from the other, and still become different works the
instant someone starts editing one of them. This week is about that instant,
and why it resists a clean definition.

## Duplication is an operation. Derivation is a claim.

Copying a file is mechanical: read the bytes, write them somewhere else,
done. Nothing about the operation itself creates a new work — a copy sitting
untouched next to its original is not a derivative of anything, it's clutter.

Derivation is different. It's the claim that a copy has acquired its own
purpose, its own audience, its own errors — that it is now being maintained
on its own terms rather than as a stand-in for the original. Nothing in the
filesystem marks this transition. There is no flag that flips from "copy" to
"derivative work." The file itself looks the same the instant before and the
instant after someone opens it, changes one number, and sends it to someone
who has never seen the original.

## Where people actually draw the line

Ask five people when a copy becomes a new work and you'll get five different
thresholds: one edit, a meaningful edit, independent circulation, a different
audience, enough divergence that reconciling the two would take real effort.
None of these is wrong. None of them is a property of the file. They're all
judgements about intent and use, applied after the fact to something that, at
the byte level, just accumulated changes the way any file does.

This matters because the judgement has consequences that a hash can't settle:
who owns the result, which version a reader should trust, whether the two
files should ever be reconciled into one again, or left alone as separate
things that happen to share an ancestor.

## Where this goes

The moment a copy diverges, someone eventually has to decide what to do about
the fact that there are now two of them, related but not identical, both
still changing. Next week looks at how people handle exactly that — usually
without ever using the word for what they're doing.
