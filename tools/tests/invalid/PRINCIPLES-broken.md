# Broken — fixture family

Every entry below breaks a rule on purpose. `run.py` asserts which rules fire,
so a check that silently stops firing is itself a test failure.

- `UX-P90` — Missing guard and cue
- `UX-P91` — Bad vocabularies
- `UX-P92` — Bad citations
- `UX-P93` — Uncited number

---

## UX-P90 — Missing guard and cue

**Principle.** No cue, no ethical guard, no provenance at all.

**Example.** A generic screen.

---

## UX-P91 — Bad vocabularies

**Cue.** a fixture entry uses values outside the closed vocabularies

**Principle.** One sentence.

**Ethical guard.** A guard, so only the vocabulary rules fire here.

**Provenance.**
`standing:` mostly-true
`guard-basis:` invented by us
`vibes:` not a provenance key
`origin:` Fixture 1900 — On Fixtures — book (academic) — https://example.org/fixture
`warrant:` Fixture 1950 — Fixtures Replicated — peer-reviewed — https://example.org/w

---

## UX-P92 — Bad citations

**Cue.** a fixture entry cites two origins, no warrant, and dates a DOI

**Principle.** One sentence.

**Ethical guard.** A guard, so only the citation rules fire here.

**Provenance.**
`standing:` replicated
`guard-basis:` supported by source
`origin:` Fixture 1900 — On Fixtures — pamphlet — https://example.org/fixture
`origin:` Fixture 1901 — On Fixtures Again — essay — https://example.org/again
`contra:` Fixture 1960 — Against Fixtures
`current:` Fixture 2020 — Today — peer-reviewed — https://doi.org/10.1000/x — accessed: 2026-08-14

---

## UX-P93 — Uncited number

**Cue.** a fixture entry states a quantity nothing backs

**Principle.** One sentence, stating no quantity of its own.

**Applies / doesn't.**
- ✅ Where a response arrives in under 400 ms — the only quantity in this entry,
  so the figure rule fires here or it does not fire at all.
- ❌ Where a fake "only 2 left" counter is quoted screen copy, not a claim.

**Ethical guard.** A guard, so only the figure rule fires here.

**Provenance.**
`standing:` replicated
`guard-basis:` supported by source
`origin:` Fixture 1900 — On Fixtures — book (academic) — https://example.org/fixture
`warrant:` Fixture 1950 — Fixtures Replicated — peer-reviewed — https://example.org/w

---

## UX-P9 — Malformed id

**Cue.** a fixture entry carries an ID that is not two digits

**Principle.** One sentence.

**Ethical guard.** A guard, so only the id rule fires here.

**Provenance.**
`standing:` replicated
`guard-basis:` supported by source
`origin:` Fixture 1900 — On Fixtures — book (academic) — https://example.org/fixture
`warrant:` Fixture 1950 — Fixtures Replicated — peer-reviewed — https://example.org/w
