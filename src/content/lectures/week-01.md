---
title: final_FINAL_revised2
description:
  Why humans version so badly even when they are smart — and why the
  filename, not the file, has been doing the work all along
week: 1
date: 2027-02-22
teachers:
  - marisol-quaye
slides: /decks/week-01/
related:
  - sessions/01-naming-as-versioning
---

`final_FINAL_revised2.docx` was not written by someone who doesn't understand
version control. It was very likely written by someone who understands the
problem perfectly well and has no tool at hand that solves it.

## The filename is standing in for something else

A filename is one string. Whoever named this document was trying to encode,
in that one string, several things at once: that it supersedes an earlier
file called `final.docx`, that a second round of changes happened after that,
and that — as of this moment — this is the one to use. None of that is
metadata the filesystem tracks. So it goes in the name, because the name is
the only field everyone involved can see, edit, and agree to trust.

This is not a failure of discipline. It's a workaround, built by hand, for a
missing feature: a reliable, shared, visible answer to "which one is current."
Given a folder, an email thread, and no shared tool for tracking revisions,
this is roughly the best available solution. It's also a bad one — `final`
is a claim, not a guarantee, and nothing stops a second `final_FINAL.docx`
from appearing next week.

## Versioning is older than version control

Treat "versioning" and "version control" as different things. Versioning —
keeping track of which state of a work is current, and what changed to get
there — is a practice as old as revision itself: monks correcting a
manuscript, an editor marking up a manuscript in red pen, a filing cabinet
with folders labelled "drafts" and "final." Version *control* — software that
does this automatically, with a shared and enforced record — is barely sixty
years old, and most people writing documents today have never opened it.
Week 5 covers what came before it. This week is about what people do in its
absence.

## Where this goes

Next week asks a question this one keeps dodging: what a file actually *is*,
underneath the name someone gave it. Once you can say precisely what makes
two files the same or different, you can ask why anyone would ever need to
write `revised2` to say so.
