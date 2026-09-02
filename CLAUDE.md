# CLAUDE.md — Almost the Same File

You are building the course website for **Almost the Same File**, a SlopU course.
The full content spec — thesis, syllabus, assessments, widget specs, voice
guide — lives in `COURSE_BIBLE.md`. Read it in full before writing any page.
This file is the harness: what you're allowed to touch, how to work, and how
to keep 20-odd pages from drifting apart.

## 0. Before you do anything

1. Read `README.md` (starter repo docs — defines what's fixed vs. yours).
2. Read `COURSE_BIBLE.md` in full (this project's content spec — not skimmed).
3. Inspect the existing content model / collections in the starter. Do not
   redesign the content model. Work within it. If the course genuinely needs
   a field the model doesn't have, say so and propose the smallest possible
   addition — don't silently restructure.
4. Inspect the starter's components/design tokens before building new UI.
   Reuse before you invent.

## 1. What's fixed, what's yours

**Fixed (do not touch):** SlopU brand identity/design tokens, the content
collections/schema, the generated API the programs-and-courses page ingests,
the data-integrity check. If a task seems to require breaking one of these,
stop and flag it instead of working around it silently.

**Yours:** every page, every word, the nav, the slide decks, any interactive
widgets, the visual treatment within the brand system, the information
architecture.

## 2. The thesis is the spec

> Digital work is rarely one file. It is a family of near-duplicates
> competing to become the truth.

Every page you write should be checkable against this sentence. If a page
could be dropped into a generic "intro to Git" or "intro to file management"
course without editing, it's off-thesis — rewrite it so it couldn't be.

Before finalizing any content page, ask: *does this page argue the thesis,
or just mention the topic?* Topic-mentioning is the failure mode to watch
for — a week on "sync" that's really just a feature comparison of Dropbox
vs. Drive has failed even if it's accurate and well-written.

## 3. Voice — enforced, not vibes

Register: **dry, forensic, bureaucratic, plain.** Model: an incident report,
a chain-of-custody log, an audit finding. Never: enthusiastic, exclamatory,
"exciting journey," "unlock," "dive in," "in today's digital world," rhetorical
questions used as filler ("Have you ever wondered...?").

Concrete rules:
- No exclamation points anywhere in course copy, including nav labels and
  error states.
- No sentence that could open a generic university course description
  ("In this course, students will explore..."). Every course-description
  sentence should be specific to *this* course or it gets cut.
- Prefer short declarative sentences stacked in sequence over long
  compound ones. See the target register in `COURSE_BIBLE.md` § Voice.
- Never use the word "seamless," "leverage," "journey," "unlock,"
  "empower," "robust," or "cutting-edge." These are slop markers — if one
  appears, rewrite the sentence, don't just swap the word.
- Humor comes from specificity and deadpan understatement, not jokes,
  puns, or winking asides. If a line is trying to be funny, cut the
  effort and let the fact be funny on its own.
- Write every piece of content — syllabus, assignment prompts, widget
  copy, nav microcopy, 404 page, footer — in this same voice. Voice
  consistency across the whole site is itself a coherence signal graders
  will check for.

After drafting each page, do a pass specifically checking it against this
section before moving on. Don't defer voice-checking to the end.

## 4. Diegesis — use sparingly, on purpose

The site is allowed to gesture at its own subject matter (a version-history
header component, a couple of staged "which file is real" moments) but
**the site's actual navigation and information architecture must work
normally.** Do not make real navigation confusing as a bit. See
`COURSE_BIBLE.md` § Diegetic Design for exactly which moments are load-bearing
and which would be over-reach.

The **version header component** goes on every content page (syllabus,
weekly pages, assessment pages). It is not decorative — treat it as a real
piece of UI you design once and reuse everywhere. Spec is in the bible.

## 5. Build order

Work in this order so early decisions (voice, components) are locked before
they get replicated across 12 weeks of content:

1. Homepage / course landing page (this sets the voice and the version-header
   pattern for everything downstream — get this right before anything else).
2. Syllabus / course overview page.
3. One full week, built as the template for the other 11 — don't write all
   12 weeks until this one is approved-quality. **Structure is settled: every
   week has three pieces, using both fixed collections as the platform nav
   already implies — a `lectures` entry (states and argues the week's core
   question; carries the week's `slides:` link), a `sessions` entry (relabeled
   "Labs" via `sessionLabels` — a small hands-on forensic task illustrating
   the same question, not a discussion prompt), and a deck in `src/decks/`
   for the lecture. The lecture and lab pages are cross-linked, not merged
   into one.**
4. Remaining weeks (2–12): lecture page, lab page, deck, for each.
5. Assessment pages 1–4 (Duplicate Audit, Which One Is Real?, Merge Conflict
   In Writing, Format Autopsy) — full specs in the bible. **Each is its own
   standalone page, cross-linked with (not nested inside) its lecture and lab
   pages.**
6. Interactive widgets 1–3 (Which File Is Current?, Diff Viewer, Merge
   Conflict Resolver) — full specs in the bible. **Each is embedded inline in
   its supporting week's lab page (weeks 6 and 7), not a standalone page —
   and for those two weeks the widget is the lab; don't also write a
   separate generic lab task.**
7. Closing page — The Version History (ungraded synthesis page, after week
   12; see bible). Build this after the four assessments exist, since it
   references them.
8. Nav, footer, 404, any remaining connective pages.
9. Coherence pass (§6) — for this build, explicitly check: does every week
   have a lecture page, a lab page, and a deck that agree on title and
   order, and does each lecture page link to its deck; does every
   assessment page link back to its week and vice versa; are widgets
   actually embedded (not orphaned standalone pages); does the closing
   page's reflection prompt accurately describe all four assessments as
   built, not as originally specced.

## 6. Coherence pass — do this explicitly, at the end

Before considering the site done, re-read it as a single document, in order,
and check:

- Do the syllabus week list, the actual lecture/lab pages, and any homepage
  preview of the schedule all agree on titles, order, and count?
- Does every week have a lecture page, a lab page, and a deck, and does the
  lecture page link to its deck?
- Does every assessment page's due-week claim match where that content
  actually lands in the weekly sequence?
- Is any term introduced in week 6 used casually in week 3 without
  being defined yet?
- Does the voice hold across pages written at different times in the build
  (a common failure mode — later pages drift back toward generic LMS copy)?
- Do the three widgets actually get referenced/linked from the weeks and
  assessments they support, or are they orphaned pages?

Fix what you find. This pass is not optional and not skippable because the
site "looks done" — 20 pages that individually work but disagree with each
other is the specific failure mode this course is graded against.

## 7. What not to do

- Don't invent additional assessments or widgets beyond the four assessments
  and three widgets specified in the bible. Scope is fixed — depth over
  breadth.
- Don't pad weekly pages with generic "further reading" filler to hit a
  length target. Short and specific beats long and generic.
- Don't restructure the fixed content model to make your life easier.
- Don't write marketing copy. This is not a landing page trying to convert
  a visitor — it's a course site a enrolled, slightly overwhelmed student is
  actually using.