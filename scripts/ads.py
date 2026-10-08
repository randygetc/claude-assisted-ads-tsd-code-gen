#!/usr/bin/env python3
"""ADS toolchain: the "compiler and test suite" for the document.

  python3 scripts/ads.py check [--final]   validate phase files and registers
  python3 scripts/ads.py build             assemble ADS.md from merged phases
  python3 scripts/ads.py status            one-line-per-phase progress

Standard library only. Final-mode checks switch on automatically once the
phase 10 file exists.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ADS_DIR = ROOT / "ads"
REG_DIR = ROOT / "registers"
OUT = ROOT / "ADS.md"

SECTIONS = {
    0: "Outcome Statement Test",
    1: "Executive Summary", 2: "Business Context", 3: "Business Outcomes",
    4: "Success Measures", 5: "Scope and Autonomy Boundary",
    6: "Stakeholders and Actors", 7: "Business Process and Decision Model",
    8: "Authority, Truth, and Temporal Validity", 9: "Business Requirements",
    10: "Business Acceptance Criteria", 11: "Architectural Responsibilities",
    12: "Architectural Concerns", 13: "Constraints, Assumptions, and Preferences",
    14: "Threat and Failure Model", 15: "Quality Attributes",
    16: "Architecture Drivers", 17: "Architecture Patterns",
    18: "Human Authority and Review Model", 19: "Data and Privacy Architecture",
    20: "Logical Architecture", 21: "Architecture Views",
    22: "Evaluation and Autonomy Plan", 23: "Architecture Acceptance",
    24: "Architecture Decisions / ADR Register",
    25: "Architecture Traceability Matrix", 26: "Decision Log",
    27: "Rejected Alternatives", 28: "Open Questions and Risks",
    29: "Architecture Governance", 30: "Production Evidence and Learning",
    31: "Definition of Architecture Success",
}

# phase -> (file name, ADS sections that file must contain)
PHASES = {
    0: ("00-intake.md", [0]),
    1: ("01-business-context.md", [2, 3, 4]),
    2: ("02-scope-process.md", [5, 6, 7]),
    3: ("03-authority-requirements.md", [8, 9, 10]),
    4: ("04-responsibilities-risks.md", [11, 12, 13, 14, 15]),
    5: ("05-drivers-patterns.md", [16, 17]),
    6: ("06-human-review-privacy.md", [18, 19]),
    7: ("07-logical-architecture.md", [20, 21]),
    8: ("08-evaluation-acceptance.md", [22, 23]),
    9: ("09-decisions.md", [24, 26, 27]),
    10: ("10-traceability-closeout.md", [1, 25, 28, 29, 30, 31]),
}
FINAL_PHASE = 10

ID_RE = re.compile(
    r"\b(?:BO-\d{3}|SM-G\d{2}|SM-\d{3}|BR-\d{3}|BAC-\d{3}-\d{2}|AR-[A-Z]{2,5}"
    r"|D-\d{3}|AD-\d{3}|PAT-\d{3}|AAC-\d{3}|ADR-\d{4}|DEC-\d{3}|ALT-\d{3}"
    r"|OQ-\d{3}|ASM-\d{3}|QAS-\d{3}|THR-\d{3}|FS-\d{3}|CON-\d{3})\b"
)
# A definition is an ID that starts a heading, or a **bold** ID that starts
# a list item or a table row. Every other occurrence is a reference.
DEF_RE = re.compile(
    r"^(?:#{1,6}\s+(?:\*\*)?|\s*(?:[-*]\s+)?(?:\|\s*)?\*\*)(?P<id>" + ID_RE.pattern + r")"
)
SHORTHAND_RE = re.compile(r"(?:" + ID_RE.pattern + r")/\d")
H1_RE = re.compile(r"^# (.+)$")
SECTION_H1_RE = re.compile(r"^# (\d+)\. (.+?)\s*$")
INCLUDE_RE = re.compile(r"^<!--\s*include:\s*(\S+)\s*-->\s*$")
TBD_RE = re.compile(r"\bTBD\b")
OQ_RE = re.compile(r"\bOQ-\d{3}\b")
OUTCOME_RE = re.compile(r"^\|\s*\*\*DEC-\d{3}\*\*\s*\|\s*Outcome statement:", re.M)
# Every defined ID of these kinds must appear in the section 25 matrix.
TRACED = ("BO-", "BR-", "AD-", "PAT-", "AAC-")


def rel(path):
    return str(path.relative_to(ROOT))


def split_front_matter(text):
    """Return (dict, body, number of lines consumed by the front matter)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text, 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            meta = {}
            for raw in lines[1:i]:
                if ":" in raw:
                    key, value = raw.split(":", 1)
                    meta[key.strip()] = value.strip()
            return meta, "\n".join(lines[i + 1:]), i + 1
    return {}, text, 0


def iter_lines(body):
    """Yield (index, line, inside_code_fence)."""
    fenced = False
    for i, line in enumerate(body.split("\n")):
        if line.lstrip().startswith("```"):
            yield i, line, True
            fenced = not fenced
            continue
        yield i, line, fenced


def phase_sections(body):
    """Split a phase body into {section number: text}, plus the preamble."""
    found, order, current, buf, preamble = {}, [], None, [], []
    for _, line, fenced in iter_lines(body):
        m = None if fenced else SECTION_H1_RE.match(line)
        if m:
            if current is not None:
                found[current] = "\n".join(buf).rstrip() + "\n"
            current, buf = int(m.group(1)), [line]
            order.append(current)
        elif current is None:
            preamble.append(line)
        else:
            buf.append(line)
    if current is not None:
        found[current] = "\n".join(buf).rstrip() + "\n"
    return found, order, "\n".join(preamble)


def scan_files():
    files = []
    if ADS_DIR.exists():
        files += sorted(p for p in ADS_DIR.rglob("*.md"))
    if REG_DIR.exists():
        files += sorted(REG_DIR.glob("*.md"))
    return files


def check(final=False):
    errors, warnings = [], []
    defs, refs = {}, []          # id -> (file, line) ; (id, file, line)
    seen_sections = {}           # section number -> file
    section_text = {}

    def err(path, line, msg):
        errors.append(f"{rel(path)}:{line}: {msg}")

    present = [n for n, (name, _) in PHASES.items() if (ADS_DIR / name).exists()]
    final = final or FINAL_PHASE in present
    for n in present:
        for lower in range(n):
            if lower not in present:
                errors.append(f"ads/{PHASES[n][0]}: phase {n} exists but phase {lower} is missing")
    if final:
        for n, (name, _) in PHASES.items():
            if n not in present:
                errors.append(f"ads/{name}: missing (required for the final check)")

    if present:
        log = REG_DIR / "decisions.md"
        rows = log.read_text(encoding="utf-8") if log.exists() else ""
        if not OUTCOME_RE.search(rows):
            errors.append("registers/decisions.md: no passed outcome statement recorded; "
                          "run /outcome before any phase (KICKOFF step 1)")

    known = {name: n for n, (name, _) in PHASES.items()}
    for path in scan_files():
        text = path.read_text(encoding="utf-8")
        meta, body, offset = split_front_matter(text)
        is_phase = path.parent == ADS_DIR and path.name in known
        in_ads_root = path.parent == ADS_DIR

        if in_ads_root and not is_phase and not path.name.startswith("_"):
            err(path, 1, "unexpected file in ads/ (phase files are fixed; see docs/plan.md)")

        if is_phase:
            n = known[path.name]
            expected = PHASES[n][1]
            if meta.get("phase") != str(n):
                err(path, 1, f"front matter must contain 'phase: {n}'")
            if meta.get("status") not in ("draft", "approved"):
                err(path, 1, "front matter 'status' must be draft or approved")
            found, order, preamble = phase_sections(body)
            if "## Reviewer brief" not in preamble:
                err(path, 1, "missing '## Reviewer brief' before the first numbered section")
            if order != expected:
                err(path, 1, f"sections must be exactly {expected} in that order, found {order}")
            for num, chunk in found.items():
                title = SECTION_H1_RE.match(chunk.split("\n", 1)[0]).group(2)
                if num not in SECTIONS:
                    err(path, 1, f"section {num} is not in the locked section list")
                elif title != SECTIONS[num]:
                    err(path, 1, f"section {num} must be titled '{SECTIONS[num]}', found '{title}'")
                if num in seen_sections:
                    err(path, 1, f"section {num} already defined in {seen_sections[num]}")
                seen_sections[num] = rel(path)
                section_text[num] = chunk

        for i, line, fenced in iter_lines(body):
            lineno = i + 1 + offset
            if is_phase and not fenced and H1_RE.match(line) and not SECTION_H1_RE.match(line):
                err(path, lineno, "H1 is reserved for numbered ADS sections ('# 12. Title')")
            m_inc = INCLUDE_RE.match(line)
            if m_inc and not (ROOT / m_inc.group(1)).is_file():
                err(path, lineno, f"include target not found: {m_inc.group(1)}")
            if SHORTHAND_RE.search(line):
                err(path, lineno, "ID shorthand (e.g. BR-003/004) is not allowed; write each ID in full")
            if not fenced and TBD_RE.search(line) and not OQ_RE.search(line):
                err(path, lineno, "TBD without an OQ-nnn on the same line")
            m_def = None if fenced else DEF_RE.match(line)
            def_start = m_def.start("id") if m_def else -1
            for m in ID_RE.finditer(line):
                if m.start() == def_start:
                    if m.group(0) in defs:
                        prev = defs[m.group(0)]
                        err(path, lineno, f"{m.group(0)} already defined at {rel(prev[0])}:{prev[1]}")
                    else:
                        defs[m.group(0)] = (path, lineno)
                else:
                    refs.append((m.group(0), path, lineno))

    for ident, path, lineno in refs:
        if ident not in defs:
            err(path, lineno, f"{ident} is referenced but never defined")

    referenced = {r[0] for r in refs}
    for ident, (path, lineno) in sorted(defs.items()):
        if ident not in referenced and not ident.startswith(("ADR-", "DEC-", "ALT-", "OQ-", "ASM-")):
            warnings.append(f"{rel(path)}:{lineno}: {ident} is defined but nothing references it yet")

    brs = sorted(i for i in defs if i.startswith("BR-"))
    bac_parents = {"BR-" + i.split("-")[1] for i in defs if i.startswith("BAC-")}
    if 10 in seen_sections:
        for br in brs:
            if br not in bac_parents:
                msg = f"{br} has no acceptance criterion (expected BAC-{br[3:]}-nn)"
                (errors if final else warnings).append(msg)

    if final:
        for num in SECTIONS:
            if num not in seen_sections:
                errors.append(f"section {num} ({SECTIONS[num]}) is missing")
        matrix = section_text.get(25, "")
        in_matrix = set(ID_RE.findall(matrix))
        for ident in sorted(defs):
            if ident.startswith(TRACED) and ident not in in_matrix:
                errors.append(f"{ident} does not appear in the section 25 traceability matrix")
        if not errors:
            built = build_text()
            if not OUT.exists():
                errors.append("ADS.md is missing; run: python3 scripts/ads.py build")
            elif OUT.read_text(encoding="utf-8") != built:
                errors.append("ADS.md is out of date; run: python3 scripts/ads.py build")

    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"ERROR {e}")
    mode = "final" if final else "phase"
    print(f"\n{mode} check: {len(defs)} IDs defined, {len(refs)} references, "
          f"{len(seen_sections)}/{len(SECTIONS)} sections, "
          f"{len(warnings)} warnings, {len(errors)} errors")
    return 1 if errors else 0


def expand_includes(text):
    out = []
    for line in text.split("\n"):
        m = INCLUDE_RE.match(line)
        if not m:
            out.append(line)
            continue
        _, body, _ = split_front_matter((ROOT / m.group(1)).read_text(encoding="utf-8"))
        kept = [l for l in body.strip("\n").split("\n") if not H1_RE.match(l)]
        out.append("\n".join(kept).strip("\n"))
    return "\n".join(out)


def build_text():
    sections = {}
    for name, _ in PHASES.values():
        path = ADS_DIR / name
        if path.exists():
            _, body, _ = split_front_matter(path.read_text(encoding="utf-8"))
            sections.update(phase_sections(body)[0])
    parts = []
    header = ADS_DIR / "_header.md"
    if header.exists():
        parts.append(header.read_text(encoding="utf-8").strip() + "\n")
    for num in sorted(sections):
        parts.append(expand_includes(sections[num]).rstrip() + "\n")
    return "\n---\n\n".join(parts)


def build():
    OUT.write_text(build_text(), encoding="utf-8")
    print(f"wrote {rel(OUT)}")
    return 0


def status():
    for n, (name, secs) in PHASES.items():
        path = ADS_DIR / name
        if not path.exists():
            print(f"phase {n:>2}  not started   {name}")
            continue
        text = path.read_text(encoding="utf-8")
        meta, _, _ = split_front_matter(text)
        print(f"phase {n:>2}  {meta.get('status', '?'):<12}  {name}  "
              f"sections {secs}  TBD lines: {sum(1 for l in text.split(chr(10)) if TBD_RE.search(l))}")
    oq = REG_DIR / "open-questions.md"
    if oq.exists():
        rows = [l for l in oq.read_text(encoding="utf-8").split("\n") if l.startswith("| **OQ-")]
        still_open = sum(1 for l in rows if re.search(r"\|\s*open\s*\|", l, re.I))
        print(f"\nopen questions: {still_open} open of {len(rows)}")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        sys.exit(check(final="--final" in sys.argv))
    if cmd == "build":
        sys.exit(build())
    if cmd == "status":
        sys.exit(status())
    print(__doc__)
    sys.exit(2)
