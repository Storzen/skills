#!/usr/bin/env python3
"""Check the ux-psychology catalog against FORMAT.md, and regenerate its indexes.

FORMAT.md is the source of truth for the rules below; this script is what makes
them mechanically checkable rather than merely stated. Python 3 stdlib only, on
purpose: a public prose repo that needs an install step to be verified stops
being verified.

    python3 tools/check-ux-psychology.py              # check everything
    python3 tools/check-ux-psychology.py --family persuasion
    python3 tools/check-ux-psychology.py --fix        # regenerate the indexes

Exit code 0 when clean, 1 when any defect is reported.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1] / "skills" / "ux-psychology"

STANDING = {
    "replicated",
    "mixed",
    "qualified",
    "reversed",
    "reinterpreted",
    "unevidenced",
}

GUARD_BASIS = {
    "supported by source",
    "stricter than source",
    "independent of source",
    "contradicts source",
}

CITATION_TYPES = {
    "peer-reviewed",
    "book (academic)",
    "book chapter",
    "monograph",
    "conference paper",
    "trade book",
    "essay",
    "practitioner article",
    "corporate technical report",
    "unpublished dissertation",
}

CITATION_ROLES = {"origin", "warrant", "contra", "current", "mis-citation", "figure"}
ENTRY_KEYS = {"standing", "guard-basis"}

# Deliberately loose: a malformed ID must be *seen* and reported, not skipped
# silently as a non-entry heading.
ENTRY_RE = re.compile(r"^##\s+(\S+)\s+—\s+(.+?)\s*$")
ID_RE = re.compile(r"^UX-P\d{2}$")
# The apostrophe is load-bearing: without it `**Applies / doesn't.**` is not a
# field, and the whole ✅/❌ block — the likeliest home for a conditional
# threshold — falls out of every check, the `figure:` rule included.
FIELD_RE = re.compile(r"^\*\*([A-Za-z][A-Za-z /'’]*)\.\*\*\s*(.*)$")
KEY_RE = re.compile(r"^`([a-z-]+):`\s*(.*)$")
DOI_RE = re.compile(r"doi\.org/|\b10\.\d{4,}/")
# A bare quantity: the years, thresholds, effect sizes and counts an entry may
# only state on the authority of a `figure:` line.
NUMBER_RE = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*")
# Screen copy quoted in an entry ("only 2 left") illustrates a lever; it makes no
# claim about the world and owes no citation. Nor do IDs and reference numbers.
QUOTED_RE = re.compile(r'"[^"]*"|“[^”]*”')
NOT_A_QUANTITY_RE = re.compile(r"UX-P\d{2}|#\d+")


class Defect:
    def __init__(self, path: Path, line: int, rule: str, message: str) -> None:
        self.path, self.line, self.rule, self.message = path, line, rule, message

    def render(self, root: Path) -> str:
        where = self.path.relative_to(root)
        return f"{where}:{self.line}: [{self.rule}] {self.message}"


class Entry:
    def __init__(self, path: Path, ident: str, name: str, line: int) -> None:
        self.path = path
        self.id = ident
        self.line = line
        self.deprecated = name.endswith("— DEPRECATED")
        self.name = re.sub(r"\s*—\s*DEPRECATED$", "", name).strip()
        self.body: list[tuple[int, str]] = []  # (1-based line number, text)

    @property
    def fields(self) -> dict[str, tuple[int, str]]:
        """Design-face fields, keyed by their bold label (`Cue`, `Ethical guard`…)."""
        found: dict[str, tuple[int, str]] = {}
        label = None
        for lineno, text in self.design_face:
            match = FIELD_RE.match(text)
            if match:
                label = match.group(1).strip()
                found.setdefault(label, (lineno, match.group(2).strip()))
            elif label and text.strip():
                lineno0, value = found[label]
                found[label] = (lineno0, f"{value} {text.strip()}".strip())
            elif not text.strip():
                label = None
        return found

    @property
    def design_face(self) -> list[tuple[int, str]]:
        out = []
        for lineno, text in self.body:
            if text.startswith("**Provenance.**") or KEY_RE.match(text):
                break
            out.append((lineno, text))
        return out

    @property
    def provenance(self) -> list[tuple[int, str, str]]:
        """(line number, key, value) for every `key:` line in the entry."""
        out = []
        for lineno, text in self.body:
            match = KEY_RE.match(text)
            if match:
                out.append((lineno, match.group(1), match.group(2).strip()))
        return out

    def cue(self) -> str | None:
        field = self.fields.get("Cue")
        if not field or not field[1]:
            return None
        return field[1].rstrip(".").strip()


def parse_family(path: Path) -> list[Entry]:
    entries: list[Entry] = []
    current: Entry | None = None
    for lineno, text in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = ENTRY_RE.match(text)
        if match:
            current = Entry(path, match.group(1), match.group(2), lineno)
            entries.append(current)
        elif text.startswith("## "):
            current = None  # a non-entry heading (`## Deprecated`) ends the entry
        elif current is not None and text.strip() != "---":
            current.body.append((lineno, text))
    return entries


def check_entry(entry: Entry, defects: list[Defect]) -> None:
    def fail(line: int, rule: str, message: str) -> None:
        defects.append(Defect(entry.path, line, rule, f"{entry.id}: {message}"))

    if "Ethical guard" not in entry.fields:
        fail(entry.line, "guard", "no `**Ethical guard.**` — the rule admits no exception")

    if entry.deprecated:
        return  # a stub carries its ID, its supersession and its guard, nothing else

    if entry.cue() is None:
        fail(entry.line, "cue", "no `**Cue.**` — the `SKILL.md` index is generated from it")

    roles: dict[str, int] = {}
    figure_text = ""
    for lineno, key, value in entry.provenance:
        if key in ENTRY_KEYS:
            vocabulary = STANDING if key == "standing" else GUARD_BASIS
            base = re.sub(r"\s*\(.*\)$", "", value).strip()  # `mixed (end component)`
            if base not in vocabulary:
                fail(lineno, "vocabulary", f"`{key}:` value {value!r} is not in FORMAT.md")
            continue

        if key not in CITATION_ROLES:
            fail(lineno, "vocabulary", f"unknown provenance key `{key}:`")
            continue

        roles[key] = roles.get(key, 0) + 1
        if key == "figure":
            figure_text += " " + value
            continue

        parts = [part.strip() for part in value.split("—")]
        if len(parts) < 3:
            fail(lineno, "citation", f"`{key}:` needs author/year — work — type — link")
        elif parts[2] not in CITATION_TYPES:
            fail(lineno, "citation", f"`{key}:` type {parts[2]!r} is not in FORMAT.md")

        if "accessed:" in value and DOI_RE.search(value):
            fail(lineno, "accessed", f"`{key}:` carries `accessed:` on a DOI, which is stable")

    for key in ("standing", "guard-basis"):
        if not any(k == key for _, k, _ in entry.provenance):
            fail(entry.line, "provenance", f"no `{key}:` line")

    if roles.get("origin", 0) != 1:
        fail(entry.line, "origin", f"`origin:` appears {roles.get('origin', 0)}×, must be exactly 1")
    if roles.get("warrant", 0) < 1:
        fail(entry.line, "warrant", "no `warrant:` line — the evidence for the claim as we state it")

    # Scanned per field rather than per line: a quoted string wrapped across two
    # lines is screen copy on both of them.
    figures = re.sub(r"\s+", "", figure_text)
    for label, (lineno, value) in entry.fields.items():
        if label == "Cue":
            continue
        scrubbed = QUOTED_RE.sub("", NOT_A_QUANTITY_RE.sub("", value))
        for number in NUMBER_RE.findall(scrubbed):
            if number not in figures:
                fail(lineno, "figure", f"{number!r} in {label} has no `figure:` line")


def check_ids(entries: list[Entry], defects: list[Defect]) -> None:
    seen: dict[str, Entry] = {}
    for entry in entries:
        if not ID_RE.match(entry.id):
            defects.append(
                Defect(entry.path, entry.line, "id", f"{entry.id} is not a `UX-P` plus two digits")
            )
        if entry.id in seen:
            defects.append(
                Defect(
                    entry.path,
                    entry.line,
                    "id",
                    f"{entry.id} is already defined in {seen[entry.id].path.name} — IDs are never reused",
                )
            )
        else:
            seen[entry.id] = entry


def index_lines(entries: list[Entry]) -> list[str]:
    """The `SKILL.md` bullets for one family: reachable levers only."""
    return [
        f"- `{e.id}` {e.name} — {e.cue()}"
        for e in sorted(entries, key=lambda e: e.id)
        if not e.deprecated
    ]


def family_index_lines(entries: list[Entry]) -> list[str]:
    out = []
    for entry in sorted(entries, key=lambda e: e.id):
        suffix = " — DEPRECATED" if entry.deprecated else ""
        out.append(f"- `{entry.id}` — {entry.name}{suffix}")
    return out


def rebuild_skill_index(text: str, by_family: dict[str, list[Entry]]) -> tuple[str, list[str]]:
    """Return (regenerated SKILL.md, families the index has no heading for)."""
    lines = text.splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("## Index — "))
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )

    reachable = sum(1 for e in sum(by_family.values(), []) if not e.deprecated)
    lines[start] = f"## Index — the {reachable} principles"

    section = lines[start + 1 : end]
    header = re.compile(r"^`(PRINCIPLES-[a-z]+\.md)`")
    bullet = re.compile(r"^- `UX-P\d{2}`")

    out: list[str] = []
    covered: set[str] = set()
    index = 0
    while index < len(section):
        line = section[index]
        match = header.match(line)
        out.append(line)
        index += 1
        if not match:
            continue
        covered.add(match.group(1))
        while index < len(section) and (
            bullet.match(section[index]) or not section[index].strip()
        ):
            if bullet.match(section[index]):
                break
            out.append(section[index])
            index += 1
        while index < len(section) and bullet.match(section[index]):
            index += 1
        out.extend(index_lines(by_family.get(match.group(1), [])))

    missing = sorted(set(by_family) - covered)
    return "\n".join(lines[: start + 1] + out + lines[end:]) + "\n", missing


def rebuild_family_index(text: str, entries: list[Entry]) -> str:
    lines = text.splitlines()
    bullet = re.compile(r"^- `UX-P\d{2}`")
    first = next((i for i, l in enumerate(lines) if bullet.match(l)), None)
    if first is None:
        return text
    last = first
    while last + 1 < len(lines) and bullet.match(lines[last + 1]):
        last += 1
    return "\n".join(lines[:first] + family_index_lines(entries) + lines[last + 1 :]) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--family", help="check one family (e.g. persuasion)")
    parser.add_argument("--fix", action="store_true", help="regenerate the generated indexes")
    parser.add_argument("--dir", type=Path, default=SKILL_DIR, help="catalog directory (tests)")
    args = parser.parse_args()

    skill_dir = args.dir.resolve()
    root = skill_dir.parents[1] if len(skill_dir.parents) > 1 else skill_dir
    pattern = f"PRINCIPLES-{args.family}.md" if args.family else "PRINCIPLES-*.md"
    paths = sorted(skill_dir.glob(pattern))
    if not paths:
        print(f"no family file matching {pattern} in {skill_dir}", file=sys.stderr)
        return 1

    by_family = {path.name: parse_family(path) for path in paths}
    entries = [entry for family in by_family.values() for entry in family]

    defects: list[Defect] = []
    check_ids(entries, defects)
    for entry in entries:
        check_entry(entry, defects)

    skill_path = skill_dir / "SKILL.md"
    uncued = [e for e in entries if not e.deprecated and e.cue() is None]

    if args.fix:
        for path, family in by_family.items():
            full = skill_dir / path
            regenerated = rebuild_family_index(full.read_text(encoding="utf-8"), family)
            if regenerated != full.read_text(encoding="utf-8"):
                full.write_text(regenerated, encoding="utf-8")
                print(f"regenerated the ID index in {path}")
        if args.family:
            print(
                f"skipped the {skill_path.name} index: it regenerates from all families",
                file=sys.stderr,
            )
        elif uncued:
            print(
                f"skipped the {skill_path.name} index: {len(uncued)} entries have no `Cue.` "
                "and it is generated from them",
                file=sys.stderr,
            )
        else:
            current = skill_path.read_text(encoding="utf-8")
            regenerated, missing = rebuild_skill_index(current, by_family)
            for name in missing:
                print(f"{skill_path.name} index has no heading for {name}", file=sys.stderr)
            if regenerated != current:
                skill_path.write_text(regenerated, encoding="utf-8")
                print(f"regenerated the index in {skill_path.name}")

    elif not uncued and not args.family:
        current = skill_path.read_text(encoding="utf-8")
        regenerated, missing = rebuild_skill_index(current, by_family)
        for name in missing:
            defects.append(Defect(skill_path, 1, "index", f"no heading for {name}"))
        if regenerated != current:
            defects.append(
                Defect(skill_path, 1, "index", "does not match the `Cue.` lines — run --fix")
            )

    for defect in sorted(defects, key=lambda d: (str(d.path), d.line)):
        print(defect.render(root))

    reachable = sum(1 for e in entries if not e.deprecated)
    scope = args.family or "all families"
    print(
        f"\n{len(defects)} defect(s) across {reachable} entries "
        f"({len(entries) - reachable} deprecated) — {scope}",
        file=sys.stderr,
    )
    return 1 if defects else 0


if __name__ == "__main__":
    sys.exit(main())
