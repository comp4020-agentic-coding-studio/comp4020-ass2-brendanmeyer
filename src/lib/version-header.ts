import { z } from "astro/zod";

// Version stamp for the VersionHeader component. A course arguing that history
// belongs where the work happens cannot keep its own page versions in a lookup
// table off to one side, so they are read per entry, straight from frontmatter.
// `sessions`/`assessments`/`lectures` schemas are fixed and stay passthrough;
// `version`/`revisions` are validated here, in page code, instead.
const versionNumber = z.string().regex(/^\d+\.\d+$/);
const versionOrder = (version: string) => {
  const [major, minor] = version.split(".").map(Number);
  return major * 1000 + minor;
};

// A version header that can drift is worse than none — it asserts a currency
// nobody checked. This schema is self-policing: a superseded version that
// isn't below the current one, or revisions listed oldest-first, fails here.
const versionMetaSchema = z
  .object({
    version: versionNumber.default("1.0"),
    revisions: z
      .array(z.object({ version: versionNumber, note: z.string().trim().min(1) }))
      .nonempty()
      .optional(),
  })
  .superRefine((node, ctx) => {
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
  });

export function parseVersionMeta(data: unknown) {
  return versionMetaSchema.parse(data);
}
