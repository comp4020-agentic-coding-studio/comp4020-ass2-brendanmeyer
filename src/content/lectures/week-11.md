---
title: Provenance & Forensics
description:
  Reconstructing a history from fragments, and how archivists formalised
  that work a century before software did
week: 11
date: 2027-05-03
teachers:
  - naledi-mokoena
slides: /decks/week-11/
version: "2.2"
revisions:
  - version: "2.1"
    note: Updated to name the current teaching staff.
  - version: "2.0"
    note: Text tightened; nothing substantive changed.
  - version: "1.0"
    note:
      Ran the residue signals together in a paragraph, so the evidence a
      reconstruction rests on could not be read one item at a time.
related:
  - sessions/11-chain-of-custody
---

Nothing so far in this course has kept a reliable record of itself. Naming
was a workaround. Save As destroyed the branch structure it created. Sync
reported a timestamp. Conversion dropped things silently. What you are left
with is a folder of artefacts and no log, which is the normal condition,
not a special case, and it is where reconstruction starts.

## Reconstruction from fragments

Reconstruction reads a history out of what the artefacts still carry, on the
assumption that every operation leaves residue somewhere. Not proof.
Residue:

- **A modification time earlier than the creation time.** The file was
  copied to this location, not authored here. The copy operation carried the
  old mtime and stamped a new birth time.
- **An embedded application version string.** Places an edit inside a range
  of years, and sometimes identifies which organisation's software licence
  produced it.
- **Styles flattened into positioned glyphs.** The document passed through a
  fixed-layout format, whatever its current extension claims.
- **A departed colleague's name in a filename.** Establishes who held it,
  and roughly when, from a field nobody thought of as a record.

None of these are records anyone intended to leave, which is exactly what
makes them useful: nobody curated them, so nobody shaped them.

Every one of these signals is also defeasible. A timestamp can be set
deliberately. Metadata can be stripped by a tool that had no opinion about
it. Reconstruction produces an argument with stated confidence, not a
finding of fact, and a reconstruction that does not say which parts it is
unsure of is not a reconstruction. It is a story.

## The same work, formalised in advance

Archivists reached this problem first, and their response was to stop doing
it after the fact. Nineteenth-century archival practice built two principles
that hold whether the records are paper or not.

**Provenance**: records are kept grouped by who created them, not
reorganised by subject. Regrouping a collection by topic destroys the
evidence of who held what, which is often the more useful fact. **Chain of
custody**: every transfer of the records is itself recorded, so a gap in
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
