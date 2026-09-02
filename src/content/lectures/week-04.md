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
version: "2.0"
revisions:
  - version: "1.0"
    note:
      Called the filename chain a commit graph without drawing it, and read
      the chain as a record of what happened rather than a set of claims
      about what happened.
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

A version-control system gives a branch four things. The naming scheme
substitutes something for each, and the substitute is always a person:

- **A recorded divergence point.** In a repository, the exact commit the
  branch left from. In the folder, whatever someone remembers about which
  file John was sent.
- **An identity distinct from the name.** A branch can be renamed without
  losing track of what it is. Here the name *is* the identity, so renaming
  the file destroys the record.
- **A mechanical diff against the origin.** Here, reading both documents
  side by side and hoping to notice.
- **A merge operation.** Here, retyping one person's changes into the other
  person's file by hand.

Three of the four substitutes are memory, and memory is not shared storage.
It is held per-person, it degrades, and it does not travel with the file.

## Filenames as an ad hoc commit graph

Read the chain above as a graph and it states something precise:

```text
essay_draft.docx
        │
essay_draft_v2.docx
        ├──────────────► essay_draft_v2_JOHN_EDITS.docx
        │                              │
        └──────── merge ───────────────┘
                     │
   essay_draft_v2_JOHN_EDITS_MARISOL_MERGED.docx
```

One file, two people editing separately, one merge event. That is exactly the
shape of a real branch-and-merge, and the filenames encode it well enough
that you could reconstruct the diagram from the folder listing alone.

What the listing cannot tell you is whether the diagram is true. The
filenames record that a merge was claimed, not that one was performed —
`MARISOL_MERGED` is a person's assertion about what they did, and if
Marisol worked from the wrong copy the name says nothing about it. The graph
also stops being accurate the moment someone forgets which file was the merge
target, edits the wrong one, or forwards the chain to a third person who was
not there for any of it. A commit graph is recorded by the system that
performed the operations. This one is recorded by the participants,
afterwards, in a field that has room for a claim and no room for evidence.

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
