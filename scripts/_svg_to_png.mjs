// Reads an SVG string from stdin, rasterizes it with sharp (already a
// project dependency for Astro's own image pipeline), and writes a PNG to
// the path given as argv[2]. Used by build-assessment-packages.py to build
// the "screenshot" artefact for the Which One Is Real? file package.
import sharp from "sharp";

const outPath = process.argv[2];
if (!outPath) {
  console.error("usage: node _svg_to_png.mjs <out.png> < in.svg");
  process.exit(1);
}

const chunks = [];
for await (const chunk of process.stdin) chunks.push(chunk);
const svg = Buffer.concat(chunks);

await sharp(svg).png().toFile(outPath);
