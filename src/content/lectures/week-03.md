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
version: "2.0"
revisions:
  - version: "1.0"
    note:
      Compressed the five thresholds into a single sentence, and asserted
      that no technical test exists without saying why one cannot.
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

Ask five people when a copy becomes a new work and you get five thresholds,
each defensible:

- **Any edit.** The moment the bytes differ, they are two things. Clean,
  checkable, and it classifies a corrected typo as a new work.
- **A meaningful edit.** Substance, not spelling. Requires someone to rule on
  what counts as substance, which is the original problem restated.
- **Independent circulation.** It became its own work when someone sent it to
  someone without reference to the original. The file may not have changed
  at all.
- **A different audience.** The same text, repurposed — a report becoming a
  board paper. Identical bytes, different work.
- **Irreconcilability.** It is a separate work once pulling the two back
  into one would cost more than maintaining both. This one is measurable,
  and it is measured in effort rather than in content.

None of the five is wrong. None of them is a property of the file, and two
of them can be satisfied while the bytes stay identical.

There is a reason no technical test is available here, and it is not that
nobody has built one. Derivation is a claim about how a file will be used
from now on — who maintains it, who reads it, what it answers for. The bytes
record what has happened to a file, and no property of what has happened can
encode what is about to. A hash can tell you two files diverged. It cannot
tell you that one of them has acquired a separate job.

This matters because the judgement has consequences a hash can't settle: who
owns the result, which version a reader should trust, whether the two files
should ever be reconciled into one again, or left alone as separate things
that happen to share an ancestor.

## Where this goes

The moment a copy diverges, someone eventually has to decide what to do about
the fact that there are now two of them, related but not identical, both
still changing. Next week looks at how people handle exactly that — usually
without ever using the word for what they're doing.
