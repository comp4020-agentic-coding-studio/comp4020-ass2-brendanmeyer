#!/usr/bin/env python3
"""Builds the real, downloadable file packages for the assessments that need
one: "Which One Is Real?" and "Merge Conflict, In Writing". Deliberately a
*different* fictional scenario from either practice widget (WhichFileIsCurrent,
MergeConflictResolver) so the widgets stay practice rather than an answer key
for the graded assessment.

Every file is built from scratch (minimal OOXML .docx, hand-written .pdf, a
placeholder Word lock file) using only the standard library, with both the
document's own internal metadata and its filesystem mtime set to match the
intended timeline. Run with: python scripts/build-assessment-packages.py
"""

from __future__ import annotations

import os
import subprocess
import sys
import zipfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

REPO_ROOT = Path(__file__).resolve().parent.parent
PUBLIC_ASSESSMENTS = REPO_ROOT / "public" / "assessments"


# --------------------------------------------------------------------------
# DOCX
# --------------------------------------------------------------------------

_CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
</Types>
"""

_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
</Relationships>
"""


def _document_xml(paragraphs: list[str]) -> str:
    body = "\n".join(
        f'    <w:p><w:r><w:t xml:space="preserve">{escape(p)}</w:t></w:r></w:p>' for p in paragraphs
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
{body}
    <w:sectPr/>
  </w:body>
</w:document>
"""


def _core_xml(creator: str, created: datetime, modified: datetime, title: str) -> str:
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties
    xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:dcterms="http://purl.org/dc/terms/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>{escape(title)}</dc:title>
  <dc:creator>{escape(creator)}</dc:creator>
  <cp:lastModifiedBy>{escape(creator)}</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{created.strftime(fmt)}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{modified.strftime(fmt)}</dcterms:modified>
</cp:coreProperties>
"""


def make_docx(paragraphs: list[str], creator: str, created: datetime, modified: datetime, title: str) -> bytes:
    import io

    buf = io.BytesIO()
    dt = (modified.year, modified.month, modified.day, modified.hour, modified.minute, modified.second)
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, content in (
            ("[Content_Types].xml", _CONTENT_TYPES_XML),
            ("_rels/.rels", _RELS_XML),
            ("word/document.xml", _document_xml(paragraphs)),
            ("docProps/core.xml", _core_xml(creator, created, modified, title)),
        ):
            info = zipfile.ZipInfo(name, date_time=dt)
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, content)
    return buf.getvalue()


# --------------------------------------------------------------------------
# PDF (hand-written, minimal, single page, Helvetica)
# --------------------------------------------------------------------------


def make_pdf(lines: list[str], creator: str, created: datetime, modified: datetime, title: str) -> bytes:
    def pdf_date(dt: datetime) -> str:
        return f"D:{dt.strftime('%Y%m%d%H%M%S')}"

    content_lines = []
    y = 740
    for line in lines:
        escaped = line.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")
        content_lines.append(f"BT /F1 11 Tf 72 {y} Td ({escaped}) Tj ET")
        y -= 18
    content_stream = "\n".join(content_lines).encode("latin-1", "replace")

    objects: list[bytes] = []
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    objects.append(
        b"<< /Type /Page /Parent 2 0 R /Resources << /Font << /F1 4 0 R >> >> "
        b"/MediaBox [0 0 612 792] /Contents 5 0 R >>"
    )
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    objects.append(
        b"<< /Length " + str(len(content_stream)).encode() + b" >>\nstream\n"
        + content_stream + b"\nendstream"
    )
    info_dict = (
        f"<< /Title ({title}) /Author ({creator}) "
        f"/CreationDate ({pdf_date(created)}) /ModDate ({pdf_date(modified)}) >>"
    ).encode("latin-1")
    objects.append(info_dict)

    out = bytearray()
    out += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + obj + b"\nendobj\n"

    xref_offset = len(out)
    n = len(objects) + 1
    out += f"xref\n0 {n}\n".encode()
    out += b"0000000000 65535 f \n"
    for off in offsets[1:]:
        out += f"{off:010d} 00000 n \n".encode()
    out += (
        f"trailer\n<< /Size {n} /Root 1 0 R /Info {n - 1} 0 R >>\n"
        f"startxref\n{xref_offset}\n%%EOF"
    ).encode()
    return bytes(out)


# --------------------------------------------------------------------------
# Word lock file (~$<name>): a small placeholder in the real naming
# convention. Real lock files carry the editing user's name near the start
# of the file; that's the only part worth reproducing here.
# --------------------------------------------------------------------------


def make_lock_file(editor_name: str) -> bytes:
    return bytes([0x01, 0x00]) + editor_name.encode("utf-16-le") + bytes(32)


# --------------------------------------------------------------------------
# Packaging
# --------------------------------------------------------------------------


@dataclass
class PackageFile:
    name: str
    content: bytes
    modified: datetime


@dataclass
class Package:
    slug: str
    files: list[PackageFile] = field(default_factory=list)


def write_package(pkg: Package) -> Path:
    out_dir = PUBLIC_ASSESSMENTS / pkg.slug
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / "package.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in pkg.files:
            m = f.modified
            info = zipfile.ZipInfo(f.name, date_time=(m.year, m.month, m.day, m.hour, m.minute, m.second))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, f.content)
    return zip_path


def build_screenshot(out_path: Path, window_title: str, lines: list[str]) -> bytes:
    """Rasterizes an SVG mockup of a word-processor window to PNG via sharp
    (already a project dependency for Astro's own image pipeline)."""
    svg_lines = "\n".join(
        f'<text x="32" y="{92 + i * 22}" font-family="Georgia, serif" font-size="15" fill="#1a1a1a">{escape(line)}</text>'
        for i, line in enumerate(lines)
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520">
  <rect width="900" height="520" fill="#e8e8ea"/>
  <rect x="0" y="0" width="900" height="40" fill="#2b2b30"/>
  <text x="16" y="26" font-family="Segoe UI, sans-serif" font-size="14" fill="#f0f0f0">{escape(window_title)}</text>
  <rect x="16" y="56" width="868" height="448" fill="#ffffff" stroke="#c7c7cc"/>
{svg_lines}
</svg>"""
    script = REPO_ROOT / "scripts" / "_svg_to_png.mjs"
    result = subprocess.run(
        ["node", str(script), str(out_path)],
        input=svg.encode("utf-8"),
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"screenshot rasterization failed: {result.stderr.decode()}")
    return out_path.read_bytes()


def set_mtime(path: Path, when: datetime) -> None:
    ts = when.timestamp()
    os.utime(path, (ts, ts))


# --------------------------------------------------------------------------
# "Which One Is Real?" — the Incident Report package
# --------------------------------------------------------------------------


def build_which_one_is_real() -> None:
    solberg = "M. Solberg"
    ilic = "K. Ilic"

    v1_paragraphs = [
        "Incident Report: Bandsaw Guard Failure, Workshop 2",
        "On 10 August 2027 at approximately 14:20, the guard interlock on Bandsaw 2 "
        "in Workshop 2 failed to engage during routine use.",
        "No injury was reported. The machine was taken out of service immediately by "
        "the workshop supervisor.",
        "A preliminary inspection found the interlock switch had accumulated sawdust "
        "residue, preventing full engagement.",
        "Recommendation: schedule interlock cleaning as part of the weekly "
        "maintenance checklist.",
    ]

    v2_paragraphs = [
        "Incident Report: Bandsaw Guard Failure, Workshop 2",
        "On 10 August 2027 at approximately 14:20, the guard interlock on Bandsaw 2 "
        "in Workshop 2 failed to engage during routine use by a second-year student "
        "under supervision.",
        "No injury was reported. The machine was taken out of service immediately by "
        "the workshop supervisor.",
        "A preliminary inspection found the interlock switch had accumulated sawdust "
        "residue, and a hairline crack in the switch housing, preventing full "
        "engagement.",
        "Recommendation: replace the switch housing and schedule interlock cleaning "
        "as part of the weekly maintenance checklist.",
    ]

    v2_final_paragraphs = [
        "Incident Report: Bandsaw Guard Failure, Workshop 2",
        "On 10 August 2027 at 14:22, confirmed against the workshop's swipe-access "
        "log, the guard interlock on Bandsaw 2 in Workshop 2 failed to engage during "
        "routine use by a second-year student under supervision.",
        "No injury was reported. The machine was taken out of service immediately by "
        "the workshop supervisor.",
        "A preliminary inspection found the interlock switch had accumulated sawdust "
        "residue, and a hairline crack in the switch housing, preventing full "
        "engagement.",
        "Recommendation: replace the switch housing and schedule interlock cleaning "
        "as part of the weekly maintenance checklist.",
    ]

    autosave_paragraphs = [
        "Incident Report: Bandsaw Guard Failure, Workshop 2",
        "On 10 August 2027 at approximately 14:20 [check against swipe log], the "
        "guard interlock on Bandsaw 2 in Workshop 2 failed to engage during routine "
        "use by a second-year student under supervision.",
        "No injury was reported. The machine was taken out of service immediately by "
        "the workshop supervisor.",
        "A preliminary inspection found the interlock switch had accumulated sawdust "
        "residue, and a hairline crack in the switch housing, preventing full "
        "engagement.",
        "Recommendation: replace the switch housing and schedule interlock cleaning "
        "as part of the weekly maintenance checklist.",
    ]

    updated_paragraphs = [
        "Incident Report: Bandsaw Guard Failure, Workshop 2",
        "On 10 August 2027 at approximately 14:20, the guard interlock on Bandsaw 2 "
        "in Workshop 2 failed to engage during routine use by a second-year student "
        "under supervision.",
        "No injury was reported. The machine was taken out of service immediately by "
        "the workshop supervisor.",
        "A preliminary inspection found the interlock switch had accumulated sawdust "
        "residue, and a hairline crack in the switch housing, preventing full "
        "engagement.",
        "Recommendation: replace the switch housing and schedule interlock cleaning "
        "as part of the weekly maintenance checklist.",
        "Follow-up: interlock switch housing replaced 15 August 2027. Bandsaw "
        "returned to service.",
    ]

    draft0_lines = [
        "Incident Report - Draft",
        "Equipment: Bandsaw 2, Workshop 2",
        "10 Aug 2027, ~14:20 - guard interlock failed during use. No injury.",
        "Machine withdrawn from service. Investigation ongoing.",
    ]

    pkg = Package(slug="which-one-is-real")

    pkg.files.append(
        PackageFile(
            "incident-report.docx",
            make_docx(v1_paragraphs, solberg, datetime(2027, 8, 13, 9, 5), datetime(2027, 8, 13, 9, 5), "Incident Report"),
            datetime(2027, 8, 13, 9, 5),
        )
    )
    pkg.files.append(
        PackageFile(
            "incident-report_v2.docx",
            make_docx(v2_paragraphs, solberg, datetime(2027, 8, 13, 9, 5), datetime(2027, 8, 14, 14, 30), "Incident Report"),
            datetime(2027, 8, 14, 14, 30),
        )
    )
    pkg.files.append(
        PackageFile(
            "incident-report (Autosaved).docx",
            make_docx(autosave_paragraphs, solberg, datetime(2027, 8, 13, 9, 5), datetime(2027, 8, 14, 14, 28), "Incident Report"),
            datetime(2027, 8, 14, 14, 28),
        )
    )
    pkg.files.append(
        PackageFile(
            "incident-report_v2_final.docx",
            make_docx(v2_final_paragraphs, solberg, datetime(2027, 8, 13, 9, 5), datetime(2027, 8, 14, 14, 31), "Incident Report"),
            datetime(2027, 8, 14, 14, 31),
        )
    )
    pkg.files.append(
        PackageFile(
            "incident-report.pdf",
            make_pdf(
                [v2_final_paragraphs[0], "", v2_final_paragraphs[1]],
                solberg,
                datetime(2027, 8, 14, 14, 40),
                datetime(2027, 8, 14, 14, 40),
                "Incident Report",
            ),
            datetime(2027, 8, 14, 14, 40),
        )
    )
    pkg.files.append(
        PackageFile(
            "incident-report_draft0.pdf",
            make_pdf(draft0_lines, solberg, datetime(2027, 8, 12, 17, 50), datetime(2027, 8, 12, 17, 50), "Incident Report Draft"),
            datetime(2027, 8, 12, 17, 50),
        )
    )
    pkg.files.append(
        PackageFile(
            "~$cident-report.docx",
            make_lock_file(ilic),
            datetime(2027, 8, 15, 8, 50),
        )
    )
    pkg.files.append(
        PackageFile(
            "incident-report_UPDATED.docx",
            make_docx(updated_paragraphs, ilic, datetime(2027, 8, 15, 8, 40), datetime(2027, 8, 15, 10, 12), "Incident Report"),
            datetime(2027, 8, 15, 10, 12),
        )
    )
    pkg.files.append(
        PackageFile(
            "Incident report (forwarded).docx",
            make_docx(v2_paragraphs, solberg, datetime(2027, 8, 13, 9, 5), datetime(2027, 8, 14, 14, 30), "Incident Report"),
            datetime(2027, 8, 15, 8, 15),
        )
    )

    shot_path = PUBLIC_ASSESSMENTS / pkg.slug / "_screenshot.png"
    screenshot_bytes = build_screenshot(
        shot_path,
        "incident-report_v2_final.docx - Document1",
        [
            "Incident Report: Bandsaw Guard Failure, Workshop 2",
            "",
            "On 10 August 2027 at 14:22, confirmed against the",
            "workshop's swipe-access log, the guard interlock on",
            "Bandsaw 2 in Workshop 2 failed to engage during",
            "routine use by a second-year student under supervision.",
        ],
    )
    pkg.files.append(
        PackageFile("incident-report-screenshot.png", screenshot_bytes, datetime(2027, 8, 14, 14, 36))
    )
    shot_path.unlink(missing_ok=True)

    zip_path = write_package(pkg)
    set_mtime(zip_path, datetime(2027, 8, 15, 10, 12))
    print(f"wrote {zip_path} ({zip_path.stat().st_size} bytes, {len(pkg.files)} files)")


# --------------------------------------------------------------------------
# "Merge Conflict, In Writing" — the Lab Safety Policy package
# --------------------------------------------------------------------------


def build_merge_conflict() -> None:
    coordinator = "Workshop Coordinator"
    chen = "R. Chen"
    devereux = "A. Devereux"
    title = "Workshop Lab Safety Policy"

    source_paragraphs = [
        "Workshop Lab Safety Policy",
        "This policy applies to all use of Workshop 1 and Workshop 2 equipment by "
        "students, staff and visitors.",
        "Closed-toe footwear and safety glasses are required at all times when "
        "equipment is in operation.",
        "Each piece of powered equipment requires a supervisor sign-off before "
        "first use by a student.",
        "This policy takes effect at the start of the next teaching period.",
        "Any equipment fault or near-miss must be reported to the workshop "
        "supervisor within 24 hours.",
        "Exception: postgraduate researchers with prior certification from an "
        "equivalent facility may be exempted from the sign-off requirement, at "
        "the discretion of the workshop supervisor.",
        "Questions about this policy should be directed to the Workshop "
        "Coordinator.",
    ]

    chen_paragraphs = [
        "Workshop Lab Safety Policy",
        "This policy applies to all use of Workshop 1 and Workshop 2 equipment by "
        "students, staff and visitors.",
        "Closed-toe footwear and safety glasses are required at all times when "
        "equipment is in operation.",
        # Conflict 1 (mechanical): compatible addition, same sentence as Devereux's.
        "Each piece of powered equipment requires a supervisor sign-off before "
        "first use by a student, recorded in the workshop logbook.",
        # Conflict 2 (substantive): incompatible with Devereux's effective date.
        "This policy takes effect immediately.",
        "Any equipment fault or near-miss must be reported to the workshop "
        "supervisor within 24 hours, using the incident report form.",
        # Conflict 3 (defensible either way): Chen cuts the exception for brevity.
        "Questions about this policy should be directed to the Workshop "
        "Coordinator.",
    ]

    devereux_paragraphs = [
        "Workshop Lab Safety Policy",
        "This policy applies to all use of Workshop 1 and Workshop 2 equipment, "
        "including short-course and community-education enrolments, by students, "
        "staff and visitors.",
        "Closed-toe footwear and safety glasses are required at all times when "
        "equipment is in operation.",
        # Conflict 1 (mechanical): compatible addition, same sentence as Chen's.
        "Each piece of powered equipment requires a supervisor sign-off before "
        "first use by a student, valid for the current semester only.",
        # Conflict 2 (substantive): incompatible with Chen's effective date.
        "This policy takes effect from the start of Semester 2, 2027.",
        "Any equipment fault or near-miss must be reported to the workshop "
        "supervisor within 24 hours.",
        # Conflict 3 (defensible either way): Devereux keeps the exception.
        "Exception: postgraduate researchers with prior certification from an "
        "equivalent facility may be exempted from the sign-off requirement, at "
        "the discretion of the workshop supervisor.",
        "Questions about this policy should be directed to the Workshop "
        "Coordinator, workshop-coordinator@example.edu.",
    ]

    pkg = Package(slug="merge-conflict-in-writing")
    pkg.files.append(
        PackageFile(
            "policy-source.docx",
            make_docx(source_paragraphs, coordinator, datetime(2027, 3, 1, 10, 0), datetime(2027, 3, 1, 10, 0), title),
            datetime(2027, 3, 1, 10, 0),
        )
    )
    pkg.files.append(
        PackageFile(
            "policy-revision-chen.docx",
            make_docx(chen_paragraphs, chen, datetime(2027, 3, 1, 10, 0), datetime(2027, 3, 4, 11, 15), title),
            datetime(2027, 3, 4, 11, 15),
        )
    )
    pkg.files.append(
        PackageFile(
            "policy-revision-devereux.docx",
            make_docx(devereux_paragraphs, devereux, datetime(2027, 3, 1, 10, 0), datetime(2027, 3, 4, 16, 40), title),
            datetime(2027, 3, 4, 16, 40),
        )
    )

    zip_path = write_package(pkg)
    set_mtime(zip_path, datetime(2027, 3, 4, 16, 40))
    print(f"wrote {zip_path} ({zip_path.stat().st_size} bytes, {len(pkg.files)} files)")


def main() -> None:
    build_which_one_is_real()
    build_merge_conflict()


if __name__ == "__main__":
    main()
