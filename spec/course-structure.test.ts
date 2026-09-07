import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

interface ApiNode {
  id: string;
  type: string;
  title: string;
  related?: string[];
  meta?: Record<string, unknown>;
}

interface CourseApi {
  nodes: ApiNode[];
}

const api = JSON.parse(readFileSync(resolve("dist/api/index.json"), "utf8")) as CourseApi;
const byType = (type: string) => api.nodes.filter((node) => node.type === type);
const weekOf = (node: ApiNode) => Number(node.meta?.week);

// This site's own promise (CLAUDE.md §5, §9), not just the brief's minimum
// ("at least one lecture carries a real deck"): every week gets a lecture,
// a lab, and a deck, and the lecture links to its deck.
describe("every week has a lecture, a lab, and a deck", () => {
  const lectures = byType("lectures");
  const sessions = byType("sessions");

  it("has exactly twelve lectures, one per week 1-12", () => {
    expect(lectures).toHaveLength(12);
    expect(lectures.map(weekOf).sort((a, b) => a - b)).toEqual(
      Array.from({ length: 12 }, (_, i) => i + 1),
    );
  });

  it("has exactly twelve labs, one per week 1-12", () => {
    expect(sessions).toHaveLength(12);
    expect(sessions.map(weekOf).sort((a, b) => a - b)).toEqual(
      Array.from({ length: 12 }, (_, i) => i + 1),
    );
  });

  it("links every lecture to a deck that actually exists on disk", () => {
    for (const lecture of lectures) {
      const slides = lecture.meta?.slides;
      expect(slides, `${lecture.id} has no slides field`).toMatch(
        /^\/decks\/[a-z0-9-]+\/$/,
      );
      const deckSlug = String(slides).replace(/^\/decks\/|\/$/g, "");
      const deckPath = resolve("src/decks", `${deckSlug}.deck.mdx`);
      expect(existsSync(deckPath), `${lecture.id} points at a missing deck (${deckPath})`).toBe(
        true,
      );
    }
  });

  it("cross-links every lecture with its same-week lab, not merging them", () => {
    const sessionByWeek = new Map(sessions.map((session) => [weekOf(session), session]));
    for (const lecture of lectures) {
      const session = sessionByWeek.get(weekOf(lecture));
      expect(session, `no lab found for week ${weekOf(lecture)}`).toBeDefined();
      expect(lecture.related ?? [], `${lecture.id} does not link to its lab`).toContain(
        session!.id,
      );
      expect(session!.related ?? [], `${session!.id} does not link back to its lecture`).toContain(
        lecture.id,
      );
    }
  });
});

describe("assessments", () => {
  const assessments = byType("assessments");

  it("weight up to exactly 100%", () => {
    const total = assessments.reduce((sum, a) => sum + Number(a.meta?.weight ?? 0), 0);
    expect(total).toBe(100);
  });

  it("each links back to the week it draws its content from", () => {
    for (const assessment of assessments) {
      const lectureRefs = (assessment.related ?? []).filter((ref) => ref.startsWith("lectures/"));
      expect(lectureRefs.length, `${assessment.id} does not link to a lecture`).toBeGreaterThan(0);
    }
  });
});

describe("syllabus schedule agrees with the actual lecture pages", () => {
  const html = readFileSync(resolve("dist/syllabus/index.html"), "utf8");
  const rows = [...html.matchAll(/<td[^>]*>(\d+)<\/td><td[^>]*><a[^>]*>([^<]+)<\/a><\/td>/g)];
  const lectures = byType("lectures");
  const byWeek = new Map(lectures.map((lecture) => [weekOf(lecture), lecture]));

  it("lists exactly the twelve weeks the lectures collection has", () => {
    expect(rows).toHaveLength(12);
  });

  it("agrees on title and order for every week", () => {
    for (const [, weekText, titleHtml] of rows) {
      const week = Number(weekText);
      const lecture = byWeek.get(week);
      expect(lecture, `syllabus lists week ${week}, which has no lecture`).toBeDefined();
      // Decode the handful of HTML entities Astro escapes in this table.
      const title = titleHtml
        .replace(/&amp;/g, "&")
        .replace(/&#39;/g, "'")
        .replace(/&quot;/g, '"');
      expect(title, `syllabus title for week ${week} disagrees with its lecture`).toBe(
        lecture!.title,
      );
    }
  });
});

describe("the three widgets are embedded where the bible says, not orphaned", () => {
  const cases: [string, string][] = [
    ["sessions/06-reading-the-difference", "diff-viewer"],
    ["sessions/06-reading-the-difference", "wfic"],
    ["sessions/07-resolving-by-hand", "mcr"],
  ];

  it.each(cases)("%s renders the %s widget", (id, marker) => {
    const html = readFileSync(resolve("dist", id, "index.html"), "utf8");
    expect(html).toContain(`class="${marker}"`);
  });
});
