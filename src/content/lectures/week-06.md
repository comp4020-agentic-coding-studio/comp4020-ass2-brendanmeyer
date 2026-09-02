---
title: The Diff
description:
  How a machine compares two versions, why the comparison is legible, and
  why the same algorithm cannot tell you what to do about it
week: 6
date: 2027-03-29
teachers:
  - idris-fenn
slides: /decks/week-06/
---

A machine cannot see that you rewrote a paragraph. It sees that some lines
are present in one file and absent in the other. Everything a diff shows you
is built from that, and the gap between "these lines differ" and "this is
what changed" is where the rest of this course lives.

## What the algorithm actually computes

A line diff finds the longest sequence of lines the two versions have in
common, in order. Whatever is left over on the left is reported as a
deletion; whatever is left over on the right is reported as an addition.
There is no third category. A modified line is a deletion and an addition
that happen to sit next to each other, and the tool describes it that way
because the tool has no concept of modification.

This is why diffs behave the way they do in practice:

- **Moved text reads as deleted and re-added.** The algorithm preserves
  order, so a paragraph relocated is a paragraph destroyed and a different
  one created.
- **Reflowing a paragraph changes every line in it.** Nothing was edited;
  the line boundaries moved, and line boundaries are what the algorithm
  compares.
- **A one-character fix and a full rewrite look identical at line level.**
  Both are one deletion and one addition.
- **The result is not unique.** More than one common subsequence can be
  longest. Different tools pick different ones and produce different,
  equally correct diffs of the same two files.

## Legible, and still not an answer

A diff is legible because it is mechanical. It reports what it observed with
no interpretation, which is exactly what makes it trustworthy and exactly
what makes it insufficient. It cannot tell you which side is right, because
neither side is wrong in any sense available to it. It cannot tell you which
change matters, because significance is not a property of a line. It cannot
tell you why either edit was made, because intent was never in the file. And
it cannot combine them, because combining requires deciding, and deciding
requires all four of the things it does not have.

That last one is not a limitation to be engineered away. It is structural.
The diff is complete as a report and empty as a judgement.

## Where this goes

Two people each hand you a version. The diff shows you precisely what
differs, and precisely nothing about what to keep. Next week is what happens
at that point, when a system tries to resolve it anyway and has to stop.
