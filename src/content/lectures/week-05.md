---
title: Before Git
description:
  Version control as an old problem, not a new tool — scribal copying,
  carbon paper, redlined contracts, and what RCS actually automated
week: 5
date: 2027-03-22
teachers:
  - marisol-quaye
slides: /decks/week-05/
related:
  - sessions/05-a-pre-vcs-artifact
---

Git is about sixty years younger than the problem it solves. People have
been keeping track of which version of a work is current, and reconstructing
what changed between two versions, for as long as works have been copied by
hand. The tools looked nothing like a repository. The problem was identical.

## Four mechanisms, one problem

- **Scribal copying.** Every hand-copied manuscript introduces small errors.
  Textual critics reconstruct a lost original by comparing surviving copies
  and inferring which differences are copying mistakes and which are
  deliberate edits — the same operation as diffing branches to find a common
  ancestor, done on parchment, sometimes centuries after the fact.
- **Carbon paper.** A duplicate made at the moment of writing, not after —
  the copy and the original diverge from zero, not from a later save. This
  is the mechanical ancestor of a commit: one write event, two identical
  records, guaranteed to match because they were made by the same stroke of
  the pen.
- **Redlining and Track Changes.** An explicit diff bolted onto a single
  document: every insertion and deletion marked, attributed to whoever made
  it, visible without needing a second copy to compare against. This is a
  diff format, authored by hand, decades before software formalized one.
- **RCS and SCCS**, from the 1970s and 80s, were the first software to do
  all of this automatically: store a base version, record each change as a
  delta, tag deltas with an author and a timestamp. Nothing here is a new
  idea. It's the first time a computer did the bookkeeping instead of a
  person.

## What actually changed

Git and its predecessors didn't invent tracking versions, comparing them, or
attributing changes to people. They made all three fast, reliable, and free,
for anyone, on anything, without a copyist's patience or a lawyer's
redlining conventions. The problem — competing near-duplicates, disputed
authority, lost provenance — is exactly the one from week 1's filename and
week 4's Save As chain. Only the cost of solving it properly dropped.

Note what did not change. Every one of these mechanisms records that a change
happened and who made it. Not one of them decides whether the change was an
improvement, which of two variant readings the author intended, or which
surviving copy a reader should treat as the text. Textual critics still argue
about that after the comparison is complete, and so does everyone else. The
bookkeeping was automated. The adjudication was not, and week 8 is about who
does it instead.

## Where this goes

Everything since week 1 — the naming schemes, the copy-or-derivative
judgement calls, the manual branch-and-merge — is still what happens
whenever the automatic version isn't being used, which is most non-code
writing, most of the time. Now that there's a formal record of changes, the
next question is mechanical: how does a machine actually compare two
versions and produce something a person can read?
