---
title: The Sameness Test
description:
  A small forensic task. Run the four tests from this week's lecture against
  real files and find a pair where they disagree
week: 2
date: 2027-03-01
teachers:
  - idris-fenn
version: "1.1"
revisions:
  - version: "1.0"
    note: Style correction only.
spec:
  - a table comparing at least two files by name, modified time, and SHA-256 hash
  - one pair in that table where two of the three tests disagree
  - one sentence saying which test you'd trust for that pair, and why
---

## Before the session

Find three files on any machine you use that you would, in casual
conversation, call "the same file": a document and its emailed attachment, a
photo and its cloud-synced copy, a script and the version a colleague sent
back. They do not need to be related to this course.

For each pair, record three facts: do the filenames match, do the modified
timestamps match, and does a SHA-256 of the contents match. `sha256sum` on
Linux, `shasum -a 256` on macOS, `Get-FileHash` in PowerShell. Any of them
will do.

## In the session

Short demos of what each person found, then time spent on the pairs where the
three tests didn't all agree. The interesting cases are not the ones where
everything matched. They're the ones where a file you'd have called
identical failed one test, or a file you'd have called different passed one.

## Afterwards

Keep the table. Week 3 asks a related but harder question: not whether two
files are the same, but at what point a copy stops being a copy and starts
being its own thing. This table is the evidence you'll be arguing from.
