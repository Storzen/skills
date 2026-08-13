# FORMAT — principle entry template

Copy this block for each new principle in a `PRINCIPLES-*.md` file. Every field
below is required unless marked optional; an entry missing one is incomplete.

An entry has two zones. The **design face** carries what changes a decision on a
screen — a designing or auditing agent reads it and stops there. The
**provenance block** carries what defends the claim — an editor verifying or
updating a citation reads it. Keep each fact in its own zone: an entry that
argues its sources in the design face is unreadable at the moment it is used.

```
## UX-Pxx — <canonical name>

**Cue.** The screen situation that should make an agent reach for this lever.

**Principle.** One sentence: the actionable rule, not the theory.

**Mechanism.** Why the mind reacts this way — one or two sentences. No authors,
years, or links: they live in the provenance block.

**Applies / doesn't.**
- ✅ Contexts where the lever genuinely serves the user.
- ❌ Contexts where it is off-topic, ineffective, or tips into a dark pattern.

**Ethical guard.** The line between serving the user and manipulating them; or,
where the lever has no realistic abuse vector, the exact phrase `No meaningful
abuse vector` followed by a one-sentence reason. `SKILL.md` states how far the
rule binds.

**Detection.** Absent: what the screen looks like when the lever is missing
where it belongs. Weakened: what it looks like when applied but half-applied.

**Collides with.** (optional) `UX-Pyy` — which of the two the evidence favours
for this job.

**Example.** One concrete, generic screen — no product-specific detail.

**Provenance.**
`standing:` <value>
`guard-basis:` <value>
`origin:` <citation>
`warrant:` <citation>
```

## Design face

- **Cue** — one line, authored here and nowhere else. `SKILL.md`'s index is
  regenerated from these lines, so editing the index by hand is a defect.
- **Mechanism** — the mechanism only. Moving the citation apparatus out is what
  keeps the design face readable at 40 entries.
- **Detection** — two clauses, one each for *absent* and *weakened*. The third
  case, *crossing its own guard*, belongs to the ethical guard: repeating it
  here produces a second guard field on every entry.
- **Collides with** — present only where two entries claim the same underlying
  effect and following one undercuts the other. Two entries that merely share a
  source do not collide; that relationship lives in their `origin:` lines.

## Provenance block

Two entry-level keys, then one line per citation. A key may repeat; the roles
`origin` and `warrant` are required.

### `standing:` — what the evidence is worth

Describes the evidence cited under `warrant:`, never the principle's fame. A
practitioner heuristic backed by solid independent research takes the standing
of that research, once that research is cited.

| Value | Means |
| --- | --- |
| `replicated` | Holds up under direct replication. |
| `mixed` | A direct replication failed under an otherwise supported phenomenon. |
| `qualified` | Real, but smaller or more conditional than the entry's fame suggests. |
| `reversed` | Later evidence runs the other way. |
| `reinterpreted` | The effect is real but means something other than the popular reading. |
| `unevidenced` | A heuristic or practitioner claim with no study behind it. |

Where the value applies to one component of the claim rather than all of it,
scope it in parentheses: `mixed (end component)`.

### `guard-basis:` — whose claim the ethical guard is

| Value | Means |
| --- | --- |
| `supported by source` | The cited evidence warrants the guard. |
| `stricter than source` | The source licenses what the guard forbids. |
| `independent of source` | The source is silent on ethics; the guard is ours. |
| `contradicts source` | The literature argues against the line we draw. |

A prescription of ours living outside the guard — in the principle, a ✅/❌
bullet, or the example — is marked inline as *(our stance)*. Where a published
argument already makes that case, cite it: an uncredited restatement is a
citation defect, not an editorial stance.

### Citation lines

```
`<role>:` <author(s)> <year> — <work> — <type> — <link> — <note>
```

| Role | Carries |
| --- | --- |
| `origin:` | Where the effect comes from. Exactly one per entry. |
| `warrant:` | The evidence for the claim as we state it. At least one. |
| `contra:` | Evidence against it — the failed replication, the meta-analysis that shrinks it. |
| `current:` | What a reader should consult today, when that is not the origin. |
| `mis-citation:` | A widely circulated wrong attribution, recorded so it is never re-imported. |
| `figure:` | The source of one number, quoted: `figure: "r = 0.12" — Lynn 1991`. |

Every number in an entry carries a `figure:` line. A quantity with no citation
is how an invented threshold reaches a public catalog.

**Type** — one of `peer-reviewed`, `book (academic)`, `book chapter`,
`monograph`, `conference paper`, `trade book`, `essay`, `practitioner article`,
`corporate technical report`, `unpublished dissertation`. It qualifies the
document, so it sits on the citation line: one entry routinely cites documents
of different kinds.

**Link** — a DOI where one exists, otherwise a stable URL, otherwise the
archive's catalogue number.

Two suffixes, each used only where it applies:

- `read: <edition>` — the text actually consulted, when it differs from the work
  cited: a translation, a scan, a republication. Perception's worst distortion
  entered through an untranslated original nobody had read.
- `accessed: <YYYY-MM-DD>` — for a living document or a bare URL. A DOI is
  stable by construction and takes no access date.

## Conventions

- **ID**: `UX-P` plus a two-digit number, in order of addition. Never renumbered,
  never reused. File placement is not a property of the ID.
- **Name**: the canonical term, in English, with the common alias in parentheses
  if useful ("Endowed progress (never start at zero)"). Reusing the established
  name recruits what the reader already knows.
- **Tone**: imperative and concrete — describe what happens on screen, not a
  psychology lecture.
- **Generic examples only.** Entries are shared across projects; keep examples
  free of any one product's domain.

## Deprecated entries

A principle that no longer earns its place keeps its ID and collapses to a stub
at the end of its family file, under a `## Deprecated` heading:

```
## UX-Pxx — <name> — DEPRECATED

Superseded by `UX-Pyy`. <One sentence: why.>

**Ethical guard.** <unchanged — the rule admits no exception>
```

It leaves the `SKILL.md` index, which lists reachable levers. The ID stays
citable, so a design note that already references it still resolves.

## What the checker enforces

Mechanically, on every entry: the ethical guard is present; `origin:` appears
exactly once and `warrant:` at least once; every value of `standing:`,
`guard-basis:` and *type* is in its vocabulary above; every number has a
`figure:` line; `accessed:` never sits on a DOI; and the `SKILL.md` index
matches the `Cue.` lines it is generated from.
