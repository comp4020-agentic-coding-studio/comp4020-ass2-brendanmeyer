---
title: Conversion Damage
description:
  What a format conversion actually discards, and why a chain of lossy
  steps ends somewhere no single step would have taken you
week: 10
date: 2027-04-26
teachers:
  - idris-fenn
slides: /decks/week-10/
related:
  - sessions/10-one-step-of-the-chain
---

Last week's loss was visible: two files, one of them named as the loser.
This week's loss leaves one file, correctly named, opening without error,
and missing things nobody recorded the absence of.

## Conversion is re-encoding into a format that can't hold everything

A DOCX carries a comment thread, tracked changes with attribution, a style
hierarchy, and text as characters. Follow it through four steps and watch
what each format is capable of holding:

```text
                  comments  revisions  styles  layout  characters
DOCX                 yes       yes      yes     flow     authored
PDF                   no        no    glyphs    fixed    authored
PDF + OCR             no        no       no      no      guessed
TXT                   no        no       no      no      guessed
```

Print to PDF and the comments are gone, the revision history is gone, the
styles have been flattened into positioned glyphs. Run OCR over that PDF and
the glyphs become characters again — but guessed characters, with an error
rate, and now with no layout. Export to TXT and the last of the structure
goes. Read down any column and it only ever degrades. No step in the chain
restores something an earlier step gave up, and no step is required to
mention that it gave it up.

At no point does anything report a failure. Each step produced a valid file
in a valid format. The question the format autopsy asks — at what point did
it stop being the same file? — has no mechanical answer, because no step
recorded what it dropped.

## The chain is worse than its steps

Each conversion is lossy in its own direction, and the losses do not cancel.
DOCX to PDF discards structure and fixes layout. PDF to OCR discards layout
and guesses at characters. Together they discard structure *and* corrupt
characters, and the second step can no longer tell the difference between a
character the author typed and an artefact the first step introduced.

Round-tripping is the specific trap. Convert DOCX to PDF to OCR and back to
DOCX and you have a file with the original extension, which opens in the
original application, and which any of week 2's identity tests will report
as a different file from the one you started with. It is the same document
by name and by intent, and by content it is a reconstruction.

## Where this goes

You now have a document whose history is real but unrecorded — losses that
happened, at identifiable steps, with no log of them anywhere. Next week is
about doing that work backwards: reconstructing what happened to a thing
from what the thing still carries.
