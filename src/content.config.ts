import { defineCollection, reference } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";
import { courseNodeSchema } from "astro-course-university/schemas";

const weekSchema = z.coerce.number().int().min(1).max(12);
const courseNodeLoader = (dir: string) =>
  glob({ pattern: ["**/*.{md,mdx}", "!**/CLAUDE.md"], base: `src/content/${dir}` });
const teacherRefs = z.array(reference("people")).min(1);

// Version stamp for the VersionHeader component. A course arguing that history
// belongs where the work happens cannot keep its own page versions in a lookup
// table off to one side, so they are declared per entry. Entries written once
// need nothing: the default is the true answer for them.
const versionNumber = z.string().regex(/^\d+\.\d+$/);
const versionOrder = (version: string) => {
  const [major, minor] = version.split(".").map(Number);
  return major * 1000 + minor;
};

const versionFields = {
  version: versionNumber.default("1.0"),
  revisions: z
    .array(z.object({ version: versionNumber, note: z.string().trim().min(1) }))
    .nonempty()
    .optional(),
};

// A version header that can drift is worse than none — it asserts a currency
// nobody checked. These two rules make the stamp self-policing.
const checkVersions = (
  node: { version: string; revisions?: { version: string; note: string }[] },
  ctx: z.RefinementCtx,
) => {
  if (!node.revisions) return;
  const current = versionOrder(node.version);
  node.revisions.forEach((revision, index) => {
    if (versionOrder(revision.version) >= current) {
      ctx.addIssue({
        code: "custom",
        path: ["revisions", index, "version"],
        message: `superseded v${revision.version} is not below the current v${node.version}`,
      });
    }
    const next = node.revisions?.[index + 1];
    if (next && versionOrder(next.version) >= versionOrder(revision.version)) {
      ctx.addIssue({
        code: "custom",
        path: ["revisions", index + 1, "version"],
        message: "list revisions newest first",
      });
    }
  });
};

const weightedMarking = z
  .object({
    mode: z.literal("weighted"),
    criteria: z
      .array(z.object({ name: z.string().trim().min(1), weight: z.number().positive() }))
      .min(1),
  })
  .superRefine((marking, ctx) => {
    const total = marking.criteria.reduce((sum, criterion) => sum + criterion.weight, 0);
    if (total !== 100) {
      ctx.addIssue({
        code: "custom",
        path: ["criteria"],
        message: `criterion weights sum to ${total}, not 100`,
      });
    }
  });

const holisticMarking = z.object({
  mode: z.literal("holistic"),
  description: z.string().trim().min(40),
});

export const collections = {
  sessions: defineCollection({
    loader: courseNodeLoader("sessions"),
    schema: courseNodeSchema
      .extend({
        week: weekSchema,
        date: z.coerce.date(),
        teachers: teacherRefs.optional(),
        ...versionFields,
      })
      .loose()
      .superRefine(checkVersions),
  }),

  assessments: defineCollection({
    loader: courseNodeLoader("assessments"),
    schema: courseNodeSchema
      .extend({
        week: weekSchema,
        due: z.coerce.date(),
        weight: z.coerce.number().positive().max(100),
        marking: z.discriminatedUnion("mode", [weightedMarking, holisticMarking]).optional(),
        ...versionFields,
      })
      .loose()
      .superRefine(checkVersions),
  }),

  lectures: defineCollection({
    loader: courseNodeLoader("lectures"),
    schema: courseNodeSchema
      .extend({
        week: weekSchema,
        date: z.coerce.date(),
        teachers: teacherRefs.optional(),
        slides: z
          .string()
          .regex(/^\/decks\/[a-z0-9-]+\/$/)
          .optional(),
        ...versionFields,
      })
      .loose()
      .superRefine(checkVersions),
  }),

  people: defineCollection({
    loader: courseNodeLoader("people"),
    schema: ({ image }) =>
      z
        .object({
          title: z.string().trim().min(1),
          description: z.string().trim().min(40),
          role: z.string().trim().min(1),
          contact: z.string().trim().min(1).optional(),
          affiliation: z.string().trim().min(1).optional(),
          email: z.email().optional(),
          url: z.url().optional(),
          photo: image().optional(),
          photoAlt: z.string().trim().optional(),
          published: z.coerce.boolean().default(true),
        })
        .superRefine((person, ctx) => {
          if (person.photo && !person.photoAlt) {
            ctx.addIssue({
              code: "custom",
              path: ["photoAlt"],
              message: "describe the photo when one is supplied",
            });
          }
        }),
  }),
};
