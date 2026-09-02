# COURSE_BIBLE.md — Almost the Same File

Single source of truth for course content. `CLAUDE.md` is the ruleset;
this is the material. If something in a generated page contradicts this
file, this file wins.

---

## Thesis

> Digital work is rarely one file. It is a family of near-duplicates
> competing to become the truth.

The course is not about filenames. It's about how humans and systems decide
which version counts, and what's lost in the deciding.

Recurring questions the course should keep returning to, in different forms,
across the semester:

- When are two files "the same"?
- When does a copy become a new work?
- Who gets to decide which version is authoritative?
- What gets lost when software merges, syncs, compresses, converts, or
  overwrites?
- Why do humans create duplicate files instead of maintaining one canonical
  source, even when they know better?
- What happens when different people remember different versions as "the
  real one"?
- Can provenance be designed, or only reconstructed after the fact?

## Course title

**Almost the Same File**
Subtitle: *Versioning, Copies, and Digital Truth*

## Opening/landing copy (use as-is or as the model for tone)

> There is no such thing as "the file."
>
> There is the attachment you emailed. The copy in Downloads. The one you
> renamed. The autosave. The version your collaborator edited. The PDF you
> exported. The PDF they annotated. The copy stored in Drive. The copy Drive
> created when syncing failed.
>
> This course studies what happens next.

---

## Voice guide

Register: dry, forensic, bureaucratic. Model: an incident report, a
chain-of-custody log, an audit finding — not a lecture, not marketing.

Reference example (this is the target, calibrate everything to this):

> You have seven copies of the document. Three are called final. None are
> identical. The person who created them has left the organisation. Your
> first task is to determine what happened.

What that example is doing, mechanically, so it can be reproduced elsewhere:
short declarative sentences, no adjectives doing emotional work, the joke
is entirely in the accumulation of true facts, and it ends on a task, not
a punchline. Use this pattern for assignment prompts, week intros, and
error states throughout.

---

## Syllabus — 12 weeks

| Wk | Title | Core question |
|---|---|---|
| 1 | `final_FINAL_revised2` | Why do humans version so badly, even when they're smart? |
| 2 | What Is a File? | Identity, metadata, hashes — what actually makes two files "the same"? |
| 3 | Copies & Clones | Duplication vs. derivation — when does a copy become a new work? |
| 4 | Save As | Branching, performed by people who've never used the word "branch." |
| 5 | Before Git | Scribal copying, RCS, carbon paper, Track Changes — version control as an old problem, not a new tool. |
| 6 | The Diff | How machines compare versions; why diffs are legible and merges aren't. |
| 7 | Merge Conflict | Two true, incompatible histories — what actually gets decided when they collide. |
| 8 | The Canonical Version | Authority — who gets to say which copy is real, and on what grounds. |
| 9 | Sync Is a Lie | Dropbox, Drive, iCloud, conflict copies — distributed systems for civilians. |
| 10 | Conversion Damage | DOCX → PDF → OCR → TXT — at what point did it stop being the same file? |
| 11 | Provenance & Forensics | Reconstructing a history from fragments, and how archivists formalized that work a century before software did. |
| 12 | Archive or Delete? | Retention, digital decay, and designing a system that doesn't lie to you. |

Note: Week 11 merges what were previously two separate weeks (Forensic
Versioning; Provenance & Archives). They're kept together deliberately —
forensic reconstruction is what provenance work looks like done after the
fact; archival provenance practice is that same work formalized in advance.
This week should cover both halves without treating them as two topics
bolted together — open on reconstruction-from-fragments, then pivot to how
archivists turned that into a discipline.

Each week has two pages, not one: a lecture page and a lab page (the site's
`sessions` collection, labelled "Labs"). The lecture states the week's core
question up top, holds to one idea (resist covering three loosely-related
things), and ends pointing at the next week's question, so the sequence
reads as an argument, not a list. The lab is not a discussion prompt or a
reading-response form — it's a small hands-on forensic task that makes the
same week's question concrete (inspect these files, spot the fake metadata,
reconstruct this timeline). Weeks 6 and 7 already have this covered: their
lab *is* Widget 2 and Widget 3 respectively — don't also write a separate
generic lab task for those two weeks.

Every week also gets a slide deck, built from the lecture page's content
rather than duplicating it wholesale — the deck is the lecture compressed to
slide form, not a second draft of the same argument.

Final synthesis / capstone name: **The Version History** — see the Closing
Page section below for the full spec; it is in scope, not optional.

---

## Assessments (build exactly these four, in this order of appearance)

**Site structure:** each assessment is its own standalone page (own URL,
own version-header component per the usual pattern), not content embedded
inside a weekly page. Each assessment page links back to the week it
belongs to, and the relevant weekly page links forward to the assessment —
the relationship is cross-referenced, not nested. This mirrors the
week/widget relationship (widgets are embedded inline in their week;
assessments are not).

### 1. The Duplicate Audit
**Lands:** ~week 3–4.
**Task:** Student inspects a folder of their own real files and documents
one "file family" — every related copy, export, screenshot, backup, and
renamed version of a single piece of work they actually made.
**Deliverable:** A visual genealogy (a diagram or annotated list) showing how
the files relate — which is the ancestor, which are exports, which are dead
ends.
**Why it's here:** Low-stakes, establishes vocabulary (copy, export, fork,
snapshot) before the course needs it technically.

### 2. Which One Is Real?
**Lands:** ~week 6–7 (after "The Diff," before/alongside "Merge Conflict").
**Task:** Student is given a deliberately chaotic package of near-duplicate
files (`proposal.docx`, `proposal_final.docx`, `proposal_final2.docx`,
`proposal_FIXED.docx`, `proposal.pdf`, `proposal_old.pdf`, autosave
artifacts, a screenshot, an email attachment) and must reconstruct the most
likely edit history and identify the authoritative version.
**Deliverable:** A reconstructed timeline plus a stated, justified answer
for which file is authoritative and why.
**Site note:** This assessment's source package should be presented using
the same interaction pattern as Widget 1 (Which File Is Current?) — the
widget is effectively the practice version of this assessment. Link them.

### 3. Merge Conflict, In Writing
**Lands:** week 7, alongside the Merge Conflict topic.
**Task:** Two students (or one student handling both sides) receive
diverging versions of the same real document, each containing legitimate,
non-overlapping edits. The task is not just to combine them.
**Deliverable:** A merged document **plus a written rationale** explaining
what survived, what was cut, and on what grounds. The rationale is the
actual deliverable being assessed — a mechanically correct merge with no
justification doesn't meet the brief.

### 4. Format Autopsy
**Lands:** week 10, with Conversion Damage.
**Task:** Student repeatedly converts a document or media file through a
chain of formats (e.g. DOCX → Google Docs → PDF → OCR → TXT → DOCX) and
records what changes at each step.
**Deliverable:** The artifact at each stage of the chain, plus a short
written verdict on the question: *at what point did it stop being the
same file?* There's no single correct answer expected — the grading is on
the quality of the argument.

---

## Closing page — The Version History

**Status:** ungraded. This is not a 5th assessment and should not be
presented or worded like one — no rubric, no due date framed as a
submission deadline.

**Lands:** after week 12, as the site's final content page.

**Function:** A look-back page, not a new task. It prompts the student to
revisit their own four assessment artifacts (the Duplicate Audit, the
reconstructed timeline from Which One Is Real?, the merge rationale, the
Format Autopsy verdict) and write a short closing reflection: *across your
own semester's evidence, what actually decided which version counted —
and was it ever really the file itself?*

**Why it exists:** It closes the thesis rather than leaving the site to end
on a technical exercise. The four assessments produced real evidence over
the semester; this page is where that evidence gets read back against the
course's opening claim ("there is no such thing as 'the file'"). Keep the
prompt short — this page should feel like the last entry in a case file,
not a fifth assignment brief. One or two sentences of framing, then the
prompt, in the same forensic voice as everything else.

**Site structure note:** standalone page, linked from the syllabus/nav as
the final entry after Week 12 — not folded into Week 12 itself.

---

## Interactive widgets (build exactly these three)

### Widget 1 — Which File Is Current?
**Function:** Presents a set of files with plausible-looking but
conflicting metadata (filenames, timestamps, sizes, a fake "last modified
by") and asks the user to pick the current/authoritative one, then reveals
the actual answer and the reasoning.
**Role on the site:** Doubles as the practice/teaching tool for Assessment 2
— link explicitly. Should feel like a real forensic exercise, not a quiz.
**Tone:** Same forensic voice as everywhere else — present it as an
inspection, not a game.

### Widget 2 — Diff Viewer
**Function:** Toggle between two versions of a real piece of course content
(e.g. two drafts of a week's notes, or the syllabus itself at two points)
and see additions/deletions highlighted.
**Role on the site:** Supports Week 6 (The Diff) directly — embed it in that
week's page rather than only linking to a standalone tool.
**Scope note:** Line-level diffing on real text content is enough. Don't
build a general-purpose diff tool — build one instance that diffs specific,
real course content, so it doubles as content and demo.

### Widget 3 — Merge Conflict Resolver
**Function:** User is shown two conflicting paragraph-level edits to the
same source text and manually resolves the conflict, choosing/combining
lines, with the interaction structured to require (or at least prompt for)
a stated reason for each resolution.
**Role on the site:** Supports Week 7 and is the direct practice version of
Assessment 3 — link explicitly, same relationship as Widget 1 to
Assessment 2.

**Pattern across all three widgets:** each one is the "practice" instance of
a real assessment, not a decorative add-on. Build them to be linked from,
and referenced by, the specific week and assessment they support. An
orphaned widget with no inbound links from the content is a coherence
failure — check for this explicitly (see `CLAUDE.md` §6).

---

## Diegetic design — exactly what's in scope

Use the site's own subject matter as material for the site's design, but
narrowly:

**Do:**
- A version-header component (`Version 6.3 · Supersedes v6.2 · Status:
  CURRENT`) on every content page — real, reused, consistent.
- The homepage opening on the "there is no such thing as 'the file'" copy
  block before resolving into normal navigation.
- One or two other staged moments where the site briefly performs its own
  thesis (e.g. the syllabus page showing its own honest revision history).

**Don't:**
- Make real navigation confusing, broken, or multi-path as a bit.
- Use misleading filenames/URLs for pages a student actually needs to find
  reliably (assessment pages, the syllabus, due dates).
- Let the conceit outrank usability anywhere a real student would get
  legitimately lost or miss a deadline because of it.

The rule of thumb: diegesis is seasoning on a site that works normally, not
the site's actual structure.