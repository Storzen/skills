# Structural audit — `ux-psychology`

Resolves #3. Two passes, both structural: against the discipline of writing for
agents, and against the rules the skill sets on itself. No test-drive (that is
#5), no fixes applied.

Scope: `SKILL.md`, `FORMAT.md`, and all 40 entries across the five family files,
read in full.

---

## What is already good — do not break it in the rewrite

Stated first, because the defect list below is long and a rewrite that discards
these would be a net loss.

1. **The ethical guards that exist are genuinely excellent** — specific,
   actionable, and naming the dark pattern by its real name. `UX-P16` (decoy),
   `UX-P28` (variable reward, invoking Eyal's own Manipulation Matrix as a test),
   `UX-P32` (scarcity), `UX-P38` ("roach motel"), `UX-P33` (confirmshaming). These
   are the catalog's differentiator. Most UX principle lists have nothing
   comparable.
2. **`UX-P08` actively debunks the popular framing it inherits** — "~4; the
   popular 7±2 overstates it" with Cowan as the refinement. This is the standard
   the other 39 entries should be held to.
3. **Examples are disciplined** — concrete, single-screen, and genuinely free of
   product-specific detail, exactly as the rules demand. No entry violates this.
4. **The persuasion family header** states the dual-use warning once, at the top,
   so it governs all six entries. The best piece of structural writing in the
   skill.
5. **Cross-references are real and load-bearing** where present — `UX-P25`
   explicitly distinguishes itself from `UX-P02`, `UX-P40` from `UX-P19`,
   `UX-P15` from `UX-P13`. The catalog knows where it overlaps itself.

---

## Pass 1 — against the skill's own rules

### D1 (blocking) — `SKILL.md` and `FORMAT.md` state two different, incompatible rules for the ethical guard

`SKILL.md` under "Catalog rules":

> **Ethical guard is mandatory.** [...] **Every principle** states the line
> between serving the user and manipulating them.

`FORMAT.md` in the entry template:

> **Ethical guard.** [...] **Required whenever the lever can be misused**

These are not the same rule. One is universal, the other conditional. An agent
adding a principle can comply with either and violate the other, and an agent
auditing the catalog cannot tell whether a missing guard is a defect or a
correct application of the conditional rule.

**This is the single most consequential defect**, because it is the rule the
skill's entire ethical posture rests on, and it is ambiguous at the source.

Empirically the conditional rule was followed and the universal one was not:
**15 of 40 entries carry no ethical guard.**

| Family | Entries with no guard |
| --- | --- |
| perception | `UX-P10`, `UX-P19`, `UX-P20`, `UX-P21`, `UX-P22`, `UX-P23`, `UX-P24` |
| cognition | `UX-P07`, `UX-P08`, `UX-P15` |
| trust | `UX-P12`, `UX-P35`, `UX-P37`, `UX-P39`, `UX-P40` |
| motivation | — none |
| persuasion | — none |

**Fix:** the two documents must be reconciled into one rule before the depth
pass, and the decision belongs to #7. If the universal rule wins, 15 entries
need a guard written. If the conditional rule wins, `SKILL.md` must stop
claiming every principle has one — a claim an agent may rely on.

### D2 (high) — three of the guard-less entries are genuinely misusable, so the omission is substantive, not just formal

Independent of how D1 resolves, these three levers can be turned against the
user and the catalog currently says nothing about it:

- **`UX-P12` Peak-end rule.** The most misusable entry in the trust family.
  Engineering the emotional peak and the ending is precisely how a cancellation
  flow is built to feel bad at the exit, and how a dark-patterned upsell lands on
  a high note. The entry is silent.
- **`UX-P07` Hick's law.** Its own ❌ bullet says "when collapsing options hides a
  consequential choice the user needs to see" — that *is* a dark pattern
  (hiding the cheaper plan, burying the decline), and it is filed as an
  applicability note rather than an ethical line.
- **`UX-P10` Von Restorff.** Making one option visually dominant is the mechanism
  behind a de-emphasised "decline" button. `UX-P09` covers the tap-target version
  of this abuse but `UX-P10` covers the visual version and omits it.

The remaining 12 omissions are defensible on the conditional rule (`UX-P21`–
`UX-P24` Gestalt grouping, `UX-P35`, `UX-P40`) or borderline (`UX-P08`,
`UX-P15`, `UX-P19`, `UX-P20`, `UX-P37`, `UX-P39`).

### D3 (high) — ~25 of 40 mechanisms violate the mandatory attribution rule

`FORMAT.md`: "Give the canonical name and the author(s)/year — it makes the entry
citable and verifiable."

Entries with **no author at all**: `UX-P09` (Fitts's law), `UX-P13` (Tesler),
`UX-P15` (Occam), `UX-P21`–`UX-P24` (all four Gestalt principles), `UX-P27` (sunk
cost), `UX-P29` (Parkinson), `UX-P37` (Doherty threshold), `UX-P39` (curse of
knowledge).

Entries with an **author but no year**: `UX-P04`, `UX-P07` (Hick–Hyman named as a
law, no attribution), `UX-P12` (Kahneman), `UX-P19` (Nielsen), `UX-P20`
(Ebbinghaus — Murdock has a year, Ebbinghaus does not), `UX-P26`, `UX-P28`
(Skinner, Eyal), `UX-P30`, `UX-P31`, `UX-P32`, `UX-P33`, `UX-P35`, `UX-P36`,
`UX-P38`, `UX-P40`.

Complete and correct in form: `UX-P01`, `UX-P02`, `UX-P03`, `UX-P05`, `UX-P06`,
`UX-P08`, `UX-P11`, `UX-P14`, `UX-P16`, `UX-P17`, `UX-P18`, `UX-P25`, `UX-P34`.

Note the pattern: **the five Cialdini entries and the five Nielsen-heuristic
entries are uniformly year-less**, which reads as a deliberate house style rather
than an oversight — but it is still the stated rule being broken, and in a public
repo a bare "(Cialdini)" is not verifiable. Whether each attribution is
*factually* right is #4's job; this finding is only that the required field is
incomplete.

### D4 (medium) — three entries dodge the mandatory application context with a dash

`SKILL.md`: "**Application context is mandatory.** [...] Every principle says
where it applies and where it does not."

- `UX-P09`: "❌ — a general constraint, rarely inapplicable."
- `UX-P21`: "❌ — foundational; the risk is under-using whitespace, not over-."
- `UX-P12`: "❌ — applies to almost any multi-moment journey."

Each is an assertion that the field does not apply, which is the field's own
negation. All three are also wrong on the merits: Fitts's law genuinely conflicts
with deliberate friction on destructive actions; proximity genuinely conflicts
with common region (`UX-P23` says so, `UX-P21` does not); and peak-end is
inapplicable to single-moment interactions.

### D5 (medium) — `FORMAT.md` points at a file that does not exist

> Copy this block for each new principle in `PRINCIPLES.md`.

There is no `PRINCIPLES.md`. The catalog was split into five family files and the
template was never updated. An agent following `FORMAT.md` literally has nowhere
to write. It also fails to say how to choose the family, which is the actual
decision when adding a principle — `SKILL.md` covers that, `FORMAT.md` does not
point to it.

### D6 (low) — the ID convention has an undocumented ceiling

`FORMAT.md`: "`UX-P` plus a two-digit number". At `UX-P40`, sixty slots remain
before the format breaks. Worth deciding now what `UX-P100` looks like, since IDs
are append-only and third parties will cite them once published.

---

## Pass 2 — against writing for agents

### D7 (high) — the skill never states what the agent should produce

`SKILL.md` has a three-step "How to apply": name the job, open the family, take
the principles, clear the guard. It says what to *think about* and never what to
*hand back*. No output contract, no worked example of a good response, no
distinction between the artefacts a design task and an audit task should yield.

The `description` promises three different jobs — designing a screen, improving
conversion, and auditing for dark patterns — and the body offers one undifferentiated
procedure for all three. This is the gap most likely to show up in the dogfood run
(#5), and it is the substance of #6.

### D8 (high) — the family routing table assumes one job per screen; real screens have several

The table maps a single "screen job" to a single family file. But a checkout is
transactional (trust) *and* choice-heavy (cognition) *and* laid out (perception),
and the catalog knows it: `UX-P17` in cognition pairs with `UX-P03` in motivation,
`UX-P40` in trust complements `UX-P19` in perception, `UX-P02` in motivation
combines with `UX-P11` in the same family.

The agent is told to "open the matching family file(s)" — the parenthetical "(s)"
is the only hint that more than one may apply, and no rule says when. On a
payment form the difference between loading trust alone and loading trust +
cognition is the difference between a partial answer and a complete one.

### D9 (medium) — the ethical guard is a property of entries, not a step in the procedure

Step 3 of "How to apply" says "then clear each one's **ethical guard** before
shipping". For an agent that skims — the normal case — the guard is an attribute
attached to text it may or may not have loaded, not a gate it must pass. Given
that the guard is the skill's stated differentiator and that 15 entries lack one
(D1), an agent can complete the whole procedure without the guard ever changing
an output.

### D10 (medium) — eager load is ~3.3 KB, on-demand is ~34 KB, and the routing decision is made blind

`SKILL.md` (3.3 KB) is what always loads; the five family files total ~34 KB. The
proportion is right in principle — this is correct progressive disclosure. The
problem is that the routing table carries only a one-line description per family,
so the agent picks which 6–8 KB file to open with no view of what is inside. The
per-family ID indexes exist but live *inside* the files, behind the decision they
would inform.

### D11 (low) — the frontmatter description is a strong trigger but claims a mode the body does not implement

The description is well-built for matching: it enumerates screen types (form,
onboarding, funnel, pricing, transactional) and goals (conversion, completion,
clarity, trust). Its last clause — "or when auditing an interface for dark
patterns" — promises an audit capability that has no procedure behind it (D7).
Either the body gains the mode or the description stops promising it.

### D12 (low) — some entries drift from imperative into description

The house voice is imperative and lands well in most entries ("never show an
empty field", "make primary actions large and near"). `UX-P18`, `UX-P24` and
`UX-P39` open by describing a phenomenon rather than issuing an instruction, and
`UX-P13` states a law before it states an action. Minor, but the rules ask for
"imperative and concrete — describe what happens on screen, not a psychology
lecture".

---

## Content observations that belong to later tickets

Not defects against a stated rule, recorded here so they are not lost:

- **Five entries are not psychology findings**: `UX-P13` (Tesler), `UX-P15`
  (Occam), `UX-P19` (Jakob), `UX-P29` (Parkinson) and arguably `UX-P37`
  (Doherty, an industrial study) are heuristics, aphorisms or industry coinages.
  The skill's premise is principles "grounded in human psychology" with "an
  academic reference". Either the premise widens to admit design heuristics
  explicitly, or these five are marked as such. Input to #4 and #7.
- **`UX-P29` Parkinson's law is the weakest entry.** Its actual content — time
  limits must be real and system-enforced — overlaps `UX-P32` (scarcity) and
  `UX-P03` (loss aversion), and its stated mechanism (work expands to fill
  time) barely connects to its own example (an inventory hold). Candidate for
  rewrite or deprecation, which the append-only rule permits.
- **Entry length is uniform regardless of stakes.** `UX-P28` (variable reward,
  flagged "highest risk") gets the same envelope as `UX-P22` (similarity). If
  the template gains fields (#7), consider whether high-risk entries earn more
  space rather than every entry growing equally.

---

## Summary

| Severity | Count | IDs |
| --- | --- | --- |
| Blocking | 1 | D1 |
| High | 4 | D2, D3, D7, D8 |
| Medium | 4 | D4, D5, D9, D10 |
| Low | 3 | D6, D11, D12 |

The three most consequential:

1. **D1** — the two governing documents disagree on whether the ethical guard is
   universal or conditional, leaving the skill's core promise ambiguous and 15
   entries in an undecidable state.
2. **D7** — the skill never says what the agent should produce, and promises an
   audit mode with no procedure behind it.
3. **D3** — around 25 of 40 mechanisms are missing the author or year the rules
   require, which is a credibility problem the moment the repo is public.
