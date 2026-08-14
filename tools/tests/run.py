#!/usr/bin/env python3
"""Test the catalog checker against its fixtures. Python 3 stdlib only.

    python3 tools/tests/run.py

`valid/` must pass clean, `invalid/` must fire every rule it breaks, and
`drifted/` must converge under `--fix`. The invalid case asserts the *exact* set
of rules — a check that silently stops firing fails here rather than in review.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TESTS = Path(__file__).resolve().parent
CHECKER = TESTS.parent / "check-ux-psychology.py"

EXPECTED_INVALID = {
    "accessed",
    "citation",
    "cue",
    "figure",
    "guard",
    "id",
    "origin",
    "provenance",
    "vocabulary",
    "warrant",
}


def run(directory: Path, *flags: str) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, str(CHECKER), "--dir", str(directory), *flags],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout


def rules(output: str) -> set[str]:
    return set(re.findall(r"\[([a-z-]+)\]", output))


def main() -> int:
    failures: list[str] = []

    code, out = run(TESTS / "valid")
    if code != 0:
        failures.append(f"valid/ must pass clean, got:\n{out}")

    code, out = run(TESTS / "invalid")
    fired = rules(out)
    if code != 1:
        failures.append("invalid/ must exit 1")
    if fired != EXPECTED_INVALID:
        missing = EXPECTED_INVALID - fired
        extra = fired - EXPECTED_INVALID
        failures.append(f"invalid/ rules missing={sorted(missing)} unexpected={sorted(extra)}")

    code, out = run(TESTS / "drifted")
    if code != 1 or "index" not in rules(out):
        failures.append(f"drifted/ must report an index defect, got:\n{out}")

    with tempfile.TemporaryDirectory() as tmp:
        scratch = Path(tmp) / "drifted"
        shutil.copytree(TESTS / "drifted", scratch)
        run(scratch, "--fix")
        code, out = run(scratch)
        if code != 0:
            failures.append(f"drifted/ must be clean after --fix, got:\n{out}")

    for failure in failures:
        print(f"FAIL: {failure}")
    print(f"\n{len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
