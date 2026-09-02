---
title: What Is a File?
description:
  Identity, metadata, hashes — what actually makes two files "the same," and
  why the filesystem, the operating system, and the user each answer that
  question differently
week: 2
date: 2027-03-01
teachers:
  - idris-fenn
slides: /decks/week-02/
related:
  - sessions/02-file-identity
---

A file's identity is not a property of the file. It is a claim made by
whichever system last had to check, and different systems check differently.

## Four tests, four answers

- **Name.** Two files are "the same" if they're called the same thing. This
  is the test everyone actually uses day to day, and the one worth trusting
  least — nothing stops two unrelated files sharing a name, or one file
  existing under four.
- **Metadata.** Size, modified time, permissions, owner. This is what most
  file browsers show you when they imply "this is the same file." None of it
  survives a copy unchanged, and all of it can be rewritten with a single
  command.
- **Content.** A hash of the bytes — MD5, SHA-256, whichever. This is the
  strongest available claim: identical hash means identical content, full
  stop. It says nothing about name, location, history, or who put it there.
- **Reference.** The inode a name resolves to, or the object a symlink
  points at. Two names can share one identity; one name can, over its
  lifetime, point at several different identities in turn. This is the test
  the filesystem itself uses, and it is invisible to almost every tool that
  isn't the filesystem.

## Where they disagree

A renamed file keeps its hash and its reference but fails the name test. A
copied file keeps its hash but fails every other test. An edited-then-reverted
file can pass its own hash test against an old snapshot while its metadata
trail shows the edit happened. Pick the wrong test for the situation and you
either merge two things that were never one, or split one thing into two you
can no longer reconcile.

Every later week in this course — copies, branches, diffs, merges, canonical
versions — is really an argument about which of these four tests should
decide a particular dispute. Get the test wrong here and the dispute doesn't
resolve. It just relocates to next week.

Next week: two files can pass all four tests above at the moment they're
created, and still become — the instant someone starts editing one of them —
two different works by any reasonable account. Sameness of bytes turns out to
say nothing about sameness of intent. That's the copy-versus-derivation
problem, and it has no hash-based answer.
