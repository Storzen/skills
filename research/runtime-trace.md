# Runtime trace — what `/ux-psychology` actually applies, and what it misses

Evidence for [#5](https://github.com/Storzen/skills/issues/5). Baseline: `c975f21`
(pre-rewrite). Three contrasted screens, each run by following `SKILL.md`'s
"How to apply" literally: name the screen's job → open the family file(s) the
mapping table gives → take the principles whose "applies / doesn't" covers the
job → clear each ethical guard.

**Fidelity caveat.** The runs were executed by the same agent that wrote them up,
in one context. The file-loading decision for each run was fixed from the mapping
table *before* the unmapped families were read, so the "families opened" column is
honest. The "what a practitioner would raise" column is the weakest part of the
evidence and is the part most in need of human judgement.

---

## Run 1 — Payment / checkout form

**Job named**: transactional, high-stakes form.
**Families the mapping opens**: `cognition` (row: "Choices, forms, settings,
pricing"), `trust` (row: "Transactional, high-stakes, feedback, errors, memory,
trust"). **Not opened**: perception, motivation, persuasion.

| ID | Cited | Applied or name-dropped |
| --- | --- | --- |
| `UX-P01` Smart defaults | ✅ | **Applied** — country from locale, quantity 1 |
| `UX-P07` Hick's law | ✅ | **Applied** — split into steps |
| `UX-P08` Miller's law | ✅ | **Applied** — card number grouped 4-4-4-4 |
| `UX-P13` Tesler's law | ✅ | **Applied** — city/region from postal code |
| `UX-P15` Occam's razor | ✅ | **Applied** — company / address line 2 behind a toggle |
| `UX-P35` Recognition over recall | ✅ | **Applied** — saved cards, address carried between steps |
| `UX-P36` Visibility of system status | ✅ | **Applied** — real Processing / Sent / Failed states |
| `UX-P37` Doherty threshold | ✅ | **Applied** — skeletons yes, optimistic confirm no |
| `UX-P38` Error prevention | ✅ | **Applied** — inline validation, cancel always reachable |
| `UX-P39` Curse of knowledge | ✅ | **Applied** — "declined by the bank", not "Gateway error 402" |
| `UX-P12` Peak-end rule | ✅ | **Applied** — warm confirmation screen |
| `UX-P40` Consistency & standards | ✅ | **Name-dropped** — nothing checkout-specific fell out |
| `UX-P06`, `UX-P14`, `UX-P16`, `UX-P17` | ✅ | **Correctly declined** — their "applies / doesn't" excludes a committed transactional screen |

**Did the ethical guard change a recommendation?** Twice, and both times cheaply,
because the entry states the refusal itself: `UX-P01`'s ❌ ("never default a money
movement or a bundled add-on") killed a pre-checked insurance add-on, and
`UX-P37`'s ❌ killed optimistic confirmation of the payment itself.

**Did it refuse conversion levers?** Not as a decision. Scarcity (`UX-P32`), social
proof (`UX-P30`) and reciprocity (`UX-P04`) all live in `persuasion`, which a
checkout job never loads — so the agent never saw the levers it was supposed to
refuse. The refusal is an artifact of file loading, not of judgement. Asked
directly ("can I put *only 2 left* on the checkout?"), nothing in `SKILL.md` tells
the agent to open a family for a lever it is being *asked about* rather than for a
job it is designing.

**What a practitioner would raise and the agent did not**
- Guest checkout vs forced account creation — the largest single driver of checkout
  abandonment. No entry covers it.
- Total-cost transparency; no fees revealed at the last step. Drip pricing is a
  named, regulated dark pattern and is absent from the catalog.
- Accepted payment methods shown before the user commits.
- Never clear the card field on a failed submit. `UX-P38` points the right way but
  does not reach this.
- Session timeouts vs users who need more time (cognitive accessibility). Absent.
- Trust-signal placement — `UX-P31` Authority's own example is *"A payments page
  shows the actual compliance certifications"*, but it is filed in `persuasion`,
  which a payments page never opens.

---

## Run 2 — Onboarding flow

**Job named**: onboarding, multi-step.
**Families the mapping opens**: `motivation` only. Naming the job "onboarding"
matches exactly one row. **Not opened**: perception, cognition, trust, persuasion.

| ID | Cited | Applied or name-dropped |
| --- | --- | --- |
| `UX-P02` Endowed progress | ✅ | **Applied** — checklist opens at 2/6 for two genuinely done items |
| `UX-P11` Zeigarnik | ✅ | **Applied** — persistent "3 of 5 done" |
| `UX-P25` Goal gradient | ✅ | **Applied** — "Last step" emphasis in the tail |
| `UX-P26` Commitment & consistency | ✅ | **Applied** — one small goal before the fuller plan |
| `UX-P05` IKEA effect | ✅ | **Applied** — user picks widgets during setup |
| `UX-P03` Loss aversion | ✅ | **Applied** — "you have unsaved changes" |
| `UX-P29` Parkinson's law | ✅ | **Name-dropped** — "scope the step" produced nothing concrete |
| `UX-P27` Sunk cost | ✅ | **Name-dropped** — nothing is invested yet at onboarding; the entry does not say so |
| `UX-P28` Variable reward | ✅ | **Refused** — guard forbids engagement-for-its-own-sake streaks |

**Did the ethical guard change a recommendation?** Once decisively (`UX-P28`), once
as a constraint on shape (`UX-P02`: the seeded progress must map to something real,
so the 2/6 had to be justified rather than chosen for effect).

**What a practitioner would raise and the agent did not**
- Time-to-value / the aha moment — the organizing idea of onboarding. Absent.
- Progressive disclosure. Absent (`UX-P07` and `UX-P15` gesture at it; not the same).
- Skip or defer without punishment — user autonomy. Absent.
- Empty states as a teaching surface — appears only inside two examples, never as a
  principle.
- Self-determination theory (autonomy / competence / relatedness). Absent — the
  motivation family is a bag of levers with no organizing model behind them.
- Three principles whose own ✅ names onboarding were never loaded: `UX-P39` Curse of
  knowledge (✅ *"Onboarding, empty states, labels, error messages"*, filed in
  `trust`), `UX-P20` Serial position (✅ *"onboarding steps"*, filed in `perception`),
  `UX-P18` Aesthetic-usability (✅ *"First impressions"*, filed in `perception`).

---

## Run 3 — Pricing page

**Job named**: pricing, conversion.
**Families the mapping opens**: `cognition` ("pricing" is named in the row),
`persuasion` ("Acquisition, landing, conversion"). **Not opened**: perception,
motivation, trust.

| ID | Cited | Applied or name-dropped |
| --- | --- | --- |
| `UX-P06` Anchoring | ✅ | **Applied** — premium tier listed first |
| `UX-P14` Choice overload | ✅ | **Applied** — three tiers, one recommended |
| `UX-P17` Framing | ✅ | **Applied** — value-framed tier copy |
| `UX-P07` / `UX-P08` | ✅ | **Applied** — comparison table chunked |
| `UX-P30` Social proof | ✅ | **Applied** — real usage count, "most popular" on the actually popular tier |
| `UX-P31` Authority | ✅ | **Applied** — real certifications, linked |
| `UX-P16` Decoy effect | ✅ | **Refused** — guard says detect and remove, never deploy |
| `UX-P32` Scarcity | ✅ | **Refused** — no genuine limit exists on a pricing page |
| `UX-P33` Liking | ✅ | **Constrained** — decline link reads "No thanks"; no confirmshaming |
| `UX-P04` Reciprocity, `UX-P34` Unity | ✅ | **Name-dropped** — weak fit, no concrete change |

**Did the ethical guard change a recommendation?** This is where it performs best —
three distinct refusals, all traceable to a specific line in a specific entry.

**Where it still leaks**
- The guard is **per-entry and advisory**. There is no screen-level gate: nothing
  makes the agent open with *"this screen touches money, therefore scarcity, decoy
  and confirmshaming are off the table"*. It is discovered entry by entry, so an
  agent that stops after two good levers never reaches the refusal.
- 15 of 40 entries carry no guard at all (`#3`'s blocking defect, observed here in
  the concrete): step 3 of "How to apply" — *clear each one's ethical guard* —
  silently no-ops on those. On this screen `UX-P07` Hick's law has no guard, yet
  "collapse the options" is precisely how a free tier gets buried; the guard against
  that is stranded in `UX-P14`.
- Layout is the pricing page's whole substance and `perception` is never loaded:
  `UX-P10` (one dominant CTA), `UX-P22`, `UX-P23` (plan cards as common regions) are
  all unreachable from the "pricing" job.

---

## Cross-cutting findings

### F1 — The families are filed by mechanism-origin; the mapping promises screen job

`SKILL.md` sells a screen-job → family table, but the five files are grouped by
where the psychology comes from (Cialdini → `persuasion`, Gestalt → `perception`,
Nielsen → `trust`). The two do not line up. Cross-referencing every entry's ✅
contexts against the family it is filed in, **~15 of 40 entries name a screen job
that maps to a different family than their own**. Since the mapping is what loads
files, every run gets a wrong subset. The sharpest cases:

| Entry | Filed in | Its ✅ names | Loaded for that job? |
| --- | --- | --- | --- |
| `UX-P31` Authority | persuasion | payments, finance, security | ❌ |
| `UX-P39` Curse of knowledge | trust | onboarding, empty states | ❌ |
| `UX-P20` Serial position | perception | onboarding steps | ❌ |
| `UX-P21` Proximity | perception | form field grouping | ❌ |
| `UX-P23` Common region | perception | sectioned forms, grouped settings | ❌ |
| `UX-P35` Recognition over recall | trust | autocomplete, form context | ❌ (for a plain form) |
| `UX-P01` Smart defaults | cognition | onboarding | ❌ |
| `UX-P03` Loss aversion | motivation | abandoned form or cart | ❌ |
| `UX-P29` Parkinson's law | motivation | a real checkout hold | ❌ |
| `UX-P33` Liking | persuasion | ❌-side: errors moving money | ❌ |

### F2 — One job, one row: real screens are multi-job and the mapping under-loads

The instruction is to name *the* screen's job and open *the matching* file(s).
Every one of the three runs needed families the mapping did not give it — most
starkly onboarding, which resolves to a single row and a single file. Nothing says
how many families to open, in what order, or what to do when a screen straddles
rows.

### F3 — There is no audit mode

The skill's own `description` claims *"when auditing an interface for dark
patterns"*, but "How to apply" is a design-time path only (name job → open → apply
→ clear guard). There is no procedure for walking an existing screen, and no
per-entry detection signal — nothing that says *what this looks like on a screen
where it has already been done wrong*. The agent has to invert each guard on the
fly, which it does unevenly and only for the entries that have one.

### F4 — The output shape is unspecified, and it showed

Three runs produced three differently shaped artifacts (a prioritised change list,
a flow annotation, a table of tiers) because nothing states what the agent hands
back. `SKILL.md` says to cite IDs "in design notes, tickets, or code comments" but
gives no format for the citation and no template for the deliverable. (`#3` found
this by reading; it reproduces at runtime.)

### F5 — Guard coverage is non-uniform, so protection depends on which entry gets cited

Whether the agent is stopped from doing the wrong thing depends on which of two
adjacent entries it happened to cite. `UX-P07`/`UX-P14` on pricing is the clean
example. This is `#3`'s blocking defect (`SKILL.md` universal vs `FORMAT.md`
conditional) with an observed runtime consequence.

### F6 — Levers are only reachable by job, never by name

A user asking about a specific tactic ("should I add a countdown here?") hits a
skill with no lookup path: there is no global ID→name index, and the only route in
is the job→family table. The five per-file indexes are invisible until the file is
already open.

---

## Candidate gap list (input to #6)

Ordered by how much they distort a run, not by effort:

1. **Re-cut or cross-index the families** so loading by screen job reaches every
   entry that claims that job (F1). Note the constraint: IDs are locked and
   append-only, but *file placement* is not an ID property — an entry can move, or
   be reached by a second index, without renumbering.
2. **Let a screen open several families**, and say how to pick and order them (F2).
3. **Add an audit path** alongside the design path, which likely means a new
   per-entry field: what the misuse looks like on screen (F3).
4. **State the deliverable** — output shape and citation format (F4).
5. **Make the guard uniform and screen-level**, not only per-entry and advisory
   (F5) — resolves against `#8`.
6. **Add a by-name lookup** so a lever can be found without guessing its job (F6).

Content gaps surfaced across the runs, for the breadth pass rather than for #6:
drip pricing / total-cost transparency, guest checkout, progressive disclosure,
time-to-value, autonomy and skippability, cognitive accessibility, empty states as
teaching surface, and an organizing model for motivation (SDT).
