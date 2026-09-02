---
title: Format Autopsy
description:
  Run one file through a chain of format conversions, keep every stage, and
  argue at what point it stopped being the same file
week: 11
due: 2027-05-07T17:00:00+10:00
weight: 25
marking:
  mode: holistic
  description:
    There is no correct answer to where the file stopped being itself. The
    mark is for the argument — whether the verdict follows from the artefacts
    you produced, whether the losses you claim are ones you can point to, and
    whether you distinguish what the format could not carry from what the
    tool declined to carry. A defended early verdict and a defended late one
    can both score full marks. An undefended one cannot.
spec:
  - a source file of your choosing, with a stated reason it is a useful subject
  - a chain of at least four conversions, with the artefact from every stage submitted
  - an itemised record of what changed at each step, including changes that are not losses
  - a verdict naming the step at which it stopped being the same file, argued from the artefacts
related:
  - lectures/week-10
  - sessions/10-one-step-of-the-chain
---

Set in week 10. Due 5pm Friday of week 11.

## The brief

> Convert one file until it is no longer the same file. Say where that
> happened, and defend it.

Pick a source file with something to lose: comments, tracked changes,
footnotes, a table, embedded fonts, non-Latin characters, transparency,
layers, a colour profile. A plain paragraph of English text survives almost
anything, which makes it a poor subject. Then run it through at least four
conversions — the worked chain is DOCX to Google Docs to PDF to OCR to TXT
to DOCX, but any chain that crosses a format boundary in both directions
will do. Keep every intermediate artefact. They are part of the submission.

The week 10 lab did one step and itemised the losses. This does the chain,
where the interesting behaviour is: losses that compound, a step that cannot
tell an authored character from an artefact the previous step introduced,
and a round trip that returns a file with the original extension, which
opens in the original application, and fails every identity test from week 2
against the file you started with.

Record what changed at every step, and include changes that are not losses —
a file that gets larger, a heading that becomes bold text of the same size, a
straight quote that becomes a curly one. Then answer the question. At what
point did it stop being the same file? Any step is defensible. The mark is
on whether your verdict follows from the artefacts in front of you, and on
whether you separate what the target format could not hold from what the
converter chose not to write.

## What you submit

The artefact from every stage of the chain, named so the order is
unambiguous, plus one document containing the per-step record and the
verdict. State the exact tool and version used for each conversion — two
DOCX-to-PDF converters do not lose the same things, and the record is not
reproducible without knowing which one ran.
