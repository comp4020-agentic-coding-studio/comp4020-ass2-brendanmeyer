---
title: Reconstruct the Graph
description:
  Take a real chain of "Save As" filenames and draw the branch-and-merge
  graph it's actually implying, then check it against the content
week: 4
date: 2027-03-15
teachers:
  - idris-fenn
spec:
  - a real set of at least three related filenames from a "Save As" chain (drafts, an email thread, shared-drive versions)
  - a graph, hand-drawn or written, of which file actually branched from which, based on reading the content
  - one place where the filenames imply a different history than the content does
---

## Before the session

Find a chain of files that grew by repeated "Save As" — draft essays, a
group assignment passed between collaborators, a document with a folder
full of `_v2`, `_final`, `_edits` variants. You need at least three files
with a plausible shared ancestor.

Read enough of each to answer, for every pair: does one contain the other's
changes, do they diverge independently from a common point, or is one simply
a dead end nobody built on.

## In the session

Draw the graph: nodes for files, edges for "this one came from that one."
Compare it to what the filenames alone would have implied. Chains rarely
match perfectly — a file named `_v2` sometimes turns out to be a dead-end
branch nobody merged, while an unremarkable name turns out to be the one
everyone actually built on.

## Afterwards

Keep the graph. It's the same kind of object a version-control system would
have produced automatically, from the same underlying edits. Next week asks
how people did this reconstruction before that automation existed at all.
