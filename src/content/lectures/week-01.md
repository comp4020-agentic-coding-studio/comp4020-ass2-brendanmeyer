---
title: final_FINAL_revised2
description:
  Why humans version so badly even when they are smart, and why the
  filename, not the file, has been doing the work all along
week: 1
date: 2027-02-22
teachers:
  - naledi-mokoena
slides: /decks/week-01/
version: "2.2"
revisions:
  - version: "2.1"
    note: Teaching staff reassigned; the material is unchanged.
  - version: "2.0"
    note: Copyedited for house style.
  - version: "1.0"
    note:
      Asserted that the filename was standing in for a missing field without
      showing the folder, listing the claims the name carries, or accounting
      for why the strings only ever grow.
related:
  - sessions/01-naming-as-versioning
---

`final_FINAL_revised2.docx` was not written by someone who doesn't understand
version control. It was very likely written by someone who understands the
problem perfectly well and has no tool at hand that solves it.

## The filename is standing in for something else

Here is the folder it lives in:

```text
report.docx
report_v2.docx
final.docx
final_FINAL.docx
final_FINAL_revised2.docx
```

A filename is one string, and by the last entry that string is carrying four
separate assertions at once:

- **Supersession**: this replaces `final.docx`, which replaced something
  before it.
- **Sequence**: `revised2` says a second round happened, and implies a first
  one you are expected to already know about.
- **Currency**: as of now, this is the one to use.
- **Finality**: `final`, twice, asserting that no further version is coming.

None of the four is metadata the filesystem tracks. There is no *supersedes*
field, no *current* flag, no *round* counter. So all four go into the name,
because the name is the only field in the entire arrangement that everyone
involved can see, write to, and agree to read.

That is the whole mechanism, and it explains the shape of the result. The
name has no schema, so a claim cannot be corrected, only appended to, which
is why these strings grow rightward and never shrink. It has no authority
behind it, so `final` is a claim and not a guarantee. And it is not
exclusive, so anyone can file a competing claim in the same field.
`final_FINAL.docx` is that happening once. `final_FINAL_revised2.docx` is it
happening twice.

This is not a failure of discipline. Given a folder, an email thread, and no
shared tool for tracking revisions, it is roughly the best available
solution. It is also a bad one, and the badness is structural rather than
personal.

## Versioning is older than version control

Treat "versioning" and "version control" as different things. Versioning is
the practice of keeping track of which state of a work is current, and what
changed to get there. It is as old as revision itself: monks correcting a
manuscript, an editor marking up a typescript in red pen, a filing cabinet
with folders labelled "drafts" and "final." Version *control*, software that
does this automatically with a shared and enforced record, is barely sixty
years old, and most people writing documents today have never opened it.
Week 5 covers what came before it. This week is about what people do in its
absence.

## Where this goes

Next week asks a question this one keeps dodging: what a file actually *is*,
underneath the name someone gave it. Once you can say precisely what makes
two files the same or different, you can ask why anyone would ever need to
write `revised2` to say so.
