---
title: Save As
description:
  What "Save As," repeated, actually is — branching performed by people who
  have never used the word, without a graph, a diff, or a merge tool
week: 4
date: 2027-03-15
teachers:
  - idris-fenn
slides: /decks/week-04/
related:
  - sessions/04-reconstruct-the-graph
---

`essay_draft.docx`, then `essay_draft_v2.docx`, then
`essay_draft_v2_JOHN_EDITS.docx`, then
`essay_draft_v2_JOHN_EDITS_MARISOL_MERGED.docx`. Nobody involved would call
this branching. It is branching — diverging from a shared point, working on
each line independently, then reconciling them back into one — with every
piece of machinery that makes branching survivable removed.

## What branching actually requires

A version-control system gives a branch four things: a record of exactly
where it diverged, an identity distinct from the file's name, a mechanical
diff against its point of origin, and a merge operation that can (mostly)
reconcile two branches automatically. None of these come from naming a file
`_v2`. The divergence point is whatever someone remembers. The diff is
reading both documents side by side. The merge is retyping one person's
changes into the other person's file by hand, hoping nothing gets dropped.

## Filenames as an ad hoc commit graph

Read the chain of filenames above as a graph and it says something precise:
one file, two people editing separately, one merge event. That's exactly the
shape of a real branch-and-merge. The difference is that this graph exists
nowhere except in whoever remembers the story, and it stops being accurate
the moment someone forgets which file was the merge target, or edits the
wrong one, or the chain gets forwarded to a third person who wasn't there for
any of it.

This is why "merge conflict" as a lived experience predates the term. It's
just two people's changes to the same paragraph, discovered only when someone
compares the files by eye and finds they disagree — with no tool telling them
where, and no record of who touched what first.

## Where this goes

None of this — filenames as commits, memory as a merge log, eyeballing as a
diff tool — is new. People have been managing divergent copies of documents
for centuries without any of it running on a computer. Next week looks at
what they actually did, and how much of it survives, unacknowledged, in the
software that eventually replaced it.
