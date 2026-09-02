---
title: Provenance & Forensics
description:
  Reconstructing a history from fragments, and how archivists formalised
  that work a century before software did
week: 11
date: 2027-05-03
teachers:
  - marisol-quaye
slides: /decks/week-11/
related:
  - sessions/11-chain-of-custody
---

Nothing so far in this course has kept a reliable record of itself. Naming
was a workaround. Save As destroyed the branch structure it created. Sync
reported a timestamp. Conversion dropped things silently. What you are left
with is a folder of artefacts and no log — which is the normal condition,
not a special case, and it is where reconstruction starts.

## Reconstruction from fragments

Reconstruction reads a history out of what the artefacts still carry, on the
assumption that every operation leaves residue somewhere. Not proof —
residue. A modification time that precedes a creation time says the file was
copied, not authored, at that location. An embedded application version
places an edit within a range of years. A style flattened into positioned
glyphs says the document passed through a fixed-layout format even if the
extension no longer admits it. A filename retains the name of a person who
left the project. None of these are records anyone intended to leave, which
is exactly what makes them useful: nobody curated them.

Every one of these signals is also defeasible. A timestamp can be set
deliberately. Metadata can be stripped by a tool that had no opinion about
it. Reconstruction produces an argument with stated confidence, not a
finding of fact, and a reconstruction that does not say which parts it is
unsure of is not a reconstruction — it is a story.

## The same work, formalised in advance

Archivists reached this problem first, and their response was to stop doing
it after the fact. Nineteenth-century archival practice built two principles
that hold whether the records are paper or not.

**Provenance** — records are kept grouped by who created them, not
reorganised by subject. Regrouping a collection by topic destroys the
evidence of who held what, which is often the more useful fact. **Chain of
custody** — every transfer of the records is itself recorded, so a gap in
the custody log is visible as a gap rather than passing as continuity.

Both principles say the same thing: the history of a thing is part of the
thing, and cannot be reconstructed reliably once discarded. Version control
software is a late implementation of exactly this. A commit records an
author, a parent, and a time; a repository refuses to let you rewrite that
without leaving a trace. Git did not invent an approach to provenance. It
mechanised one that had been written down for a century.

## Where this goes

Provenance answers what happened. It does not answer what to keep. Next
week is the last question in the course, and the only one that requires you
to throw something away.
