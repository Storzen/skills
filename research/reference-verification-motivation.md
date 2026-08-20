# Reference verification — motivation family (UX-P02, P03, P05, P11, P25, P26, P27, P28, P29)

Resolves [#10](https://github.com/Storzen/skills/issues/10). Re-slice of [#4](https://github.com/Storzen/skills/issues/4), motivation family only — 9 entries.

**Method.** Every DOI below was resolved against the Crossref metadata API
(`api.crossref.org/works/<doi>`) and its author list, year, journal, volume and
pages checked against the citation as written in `PRINCIPLES-motivation.md`.
Sources that Crossref could **not** settle are flagged inline and were verified
otherwise: Parkinson's 1955 essay (publisher page blocked to automated fetch —
verified against the essay text mirror and the book record); Cialdini's
*Influence* and Eyal's *Hooked* (trade books, no DOI — verified against Open
Library edition records keyed by ISBN); Zeigarnik 1927 (the DOI resolves, but
**Crossref's metadata for it is wrong** — see `UX-P11`). One primary paper,
Nunes & Drèze 2006, was read in full text rather than by abstract, because three
of this audit's findings turn on what is inside it. Lawsofux, NN/g, Wikipedia,
Medium and the loyalty-marketing blogs were used as leads only; none is recorded
as a citation.

**Headline.** This family is in materially worse shape than the cognition
family: **4 of 9 entries name no year, and two of those name no author at all**,
**the two most-used numbers in the family — loss aversion's "about twice" and the
IKEA effect's year — are both wrong as written**, and three entries rest on
sources that are not evidence at all (a satirical magazine essay, a trade
persuasion book, a business book). Worse, this is the family where the primary
sources *license manipulations our own ethical guards forbid* — Nunes & Drèze
found that a **specious** reason for fake progress works as well as a real one,
which is precisely what `UX-P02` prohibits. The guards are good; they are just
not derived from the cited literature, and nothing in the template says so.

---

## Verdict table

| ID | Cited as | Verdict | Corrected / supplied attribution | Canonical link | Reword? |
|---|---|---|---|---|---|
| `UX-P02` | Nunes & Drèze, 2006 | **CORRECT** (attribution) | — ; add the "reason" moderator, and Ghibellini & Meier 2025 against the Zeigarnik leg | [10.1086/500480](https://doi.org/10.1086/500480) | **Yes** — the source is a purchase-loyalty field study, and it endorses *specious* reasons our guard forbids |
| `UX-P03` | Kahneman & Tversky, 1979 | **IMPRECISE** | Origin correct. "About twice" is **not** in the 1979 paper — it is λ = 2.25 from Tversky & Kahneman 1992; riskless loss aversion is Tversky & Kahneman 1991 | [10.2307/1914185](https://doi.org/10.2307/1914185) · [10.1007/BF00122574](https://doi.org/10.1007/BF00122574) | **Yes** — drop or re-source "about twice"; the ratio is contested down to ~1.3 |
| `UX-P05` | Norton, Mochon & Ariely, **2011** | **WRONG** (year) | Norton, Mochon & Ariely (**2012**), *Journal of Consumer Psychology* 22(3): 453–460 — 2011 is the online-first date, not the citation year | [10.1016/j.jcps.2011.08.002](https://doi.org/10.1016/j.jcps.2011.08.002) | **Yes** — fix the year; add the psychological-ownership mechanism and the successful-completion boundary |
| `UX-P11` | Zeigarnik, 1927 | **IMPRECISE** (origin correct, claim does not replicate) | Zeigarnik, B. (1927), *Psychologische Forschung* 9: 1–85. Resumption lineage: Ovsiankina 1928. Must carry Ghibellini & Meier 2025 | [10.1007/BF02409755](https://doi.org/10.1007/BF02409755) · [10.1057/s41599-025-05000-w](https://doi.org/10.1057/s41599-025-05000-w) | **Yes** — the *recall* half of the claim is dead; the *resumption* half survives |
| `UX-P25` | Hull, 1932; Kivetz et al., 2006 | **CORRECT** | — ; spell out Kivetz, Urminsky & Zheng, and mark Hull as animal work | [10.1037/h0072640](https://doi.org/10.1037/h0072640) · [10.1509/jmkr.43.1.39](https://doi.org/10.1509/jmkr.43.1.39) | **Yes** — lightest rewrite in the family; naming and scope only |
| `UX-P26` | "Cialdini" — no year, no work | **MISSING** + **NOT-ACADEMIC** | Origin is Freedman & Fraser 1966 (foot-in-the-door). Cialdini's *Influence* is a trade book that **synthesises** it — current edition Harper Business, 2021 | [10.1037/h0023552](https://doi.org/10.1037/h0023552) · [10.1207/s15327957pspr0304_2](https://doi.org/10.1207/s15327957pspr0304_2) | **Yes** — cite the experiment, demote the trade book, state the effect is small |
| `UX-P27` | *no author, no year at all* | **MISSING** | Arkes & Blumer 1985 (the canonical experimental source); Staw 1976 (escalation of commitment) | [10.1016/0749-5978(85)90049-4](https://doi.org/10.1016/0749-5978\(85\)90049-4) · [10.1016/0030-5073(76)90005-2](https://doi.org/10.1016/0030-5073\(76\)90005-2) | **Yes** — supply the attribution; note it is a *fallacy* the entry proposes to exploit |
| `UX-P28` | "Skinner"; "Eyal" — no years, no works | **MISSING** + **NOT-ACADEMIC** | Ferster & Skinner 1957, *Schedules of Reinforcement*; the extinction-resistance result is Humphreys 1939. Eyal, *Hooked* (Portfolio/Penguin, 2014) is a trade book | [10.1037/10627-000](https://doi.org/10.1037/10627-000) · [10.1037/h0058138](https://doi.org/10.1037/h0058138) | **Yes** — hardest rewrite; the operant literature does not say what the entry says |
| `UX-P29` | "Parkinson's law" — no author, no year | **NOT-ACADEMIC** + **MISSING** | C. Northcote Parkinson, *The Economist*, 19 November 1955 — a satirical essay. Empirical work on the phenomenon: Bryan & Locke 1967; Aronson & Landy 1967 | [economist.com/1955/11/19/parkinsons-law](https://www.economist.com/news/1955/11/19/parkinsons-law) · [10.1016/0030-5073(67)90021-9](https://doi.org/10.1016/0030-5073\(67\)90021-9) | **Yes** — say plainly it is a joke about bureaucracy, not a finding about users |

Verdict key: `CORRECT` — author, year and work introduced the effect.
`WRONG` — the attribution as written does not match the work.
`IMPRECISE` — real source, but the entry's claim outruns or misnames it.
`MISSING` — no attribution given. `NOT-ACADEMIC` — a heuristic, aphorism or
trade book, no empirical origin.

**Ethical guards.** All nine motivation entries carry an `Ethical guard`
section, so none of this family is among the known non-compliant IDs recorded in
[#8](https://github.com/Storzen/skills/issues/8). Flagged only, nothing to fix —
but see the template findings: three of these guards are *stricter than the
source they sit under*, which is a different problem than a missing guard.

---

## Evidence

### UX-P02 — Never start at zero (endowed progress)

**Verified.** Nunes, J. C. & Drèze, X. (2006), "The Endowed Progress Effect: How
Artificial Advancement Increases Effort", *Journal of Consumer Research* 32(4):
504–512 — [10.1086/500480](https://doi.org/10.1086/500480). Crossref confirms
authors, March 2006, volume, issue and pages exactly as the entry has them. This
is the right citation and not a generic progress-bar reference — the lead held.

**Drift — three, and the third is the serious one.**

1. **The Zeigarnik leg is now unsupported.** The entry's mechanism is "endowed
   progress … combined with the Zeigarnik effect". That is faithful to the
   *paper*: Nunes & Drèze rest their first hypothesis on exactly that, writing
   that "Zeigarnik (1927) demonstrated that interrupted or uncompleted actions
   engender a strong motivation to complete the action", and their second on
   Hull's goal gradient. But the Zeigarnik recall effect has since failed to
   replicate (see `UX-P11`). Keeping the Zeigarnik name in `UX-P02` inherits a
   dead citation through a live one. The paper's own data favour the other
   reading anyway: it reports that the effect "appears to depend on perceptions
   of task completion rather than a desire to avoid wasting the endowed
   progress" — i.e. framing plus goal gradient, not tension from interruption.
2. **The evidence is a purchase-frequency loyalty programme, not a UI.** Study 1
   is a field experiment at a professional car wash: 300 randomly distributed
   loyalty cards, 8 stamps required from zero versus 10 required with 2 already
   given. Redemption was **34% versus 19%**, and inter-visit time fell by ~2.9
   days per wash as the card filled. Every step in that design costs the user
   money. A checklist that opens at 2/6 costs the user nothing, so the
   motivational economics are not the same and the entry should not present the
   transfer as settled.
3. **A moderator the entry omits, and which cuts against its own guard.** Study
   3 (240 shoppers, 2 × 4 between-subjects) found that when progress is tallied
   *in purchases* and **no reason is given** for the endowment, the programme is
   rated no better than no endowment at all (M = 4.24 vs 4.06, p = .25) — "a
   reason is necessary to get an effect". And, in the authors' words, "an
   entirely arbitrary reason was shown to work just as well as a reason based on
   purchase history": a **specious** justification performed the same as a real
   one. Our ethical guard — the offered progress "must map to something actually
   done … never an invented number" — is therefore *stricter than the finding*
   and, taken literally, forbids the manipulation the paper actually tested
   (unearned stamps). That is a defensible editorial stance and should be kept,
   but it must be marked as ours, not read as what Nunes & Drèze established.

### UX-P03 — Loss aversion

**Verified as origin.** Kahneman, D. & Tversky, A. (1979), "Prospect Theory: An
Analysis of Decision under Risk", *Econometrica* 47(2): 263–291 —
[10.2307/1914185](https://doi.org/10.2307/1914185). Correct authors, year,
journal, volume, issue, first page. It is the right origin cite for loss
aversion as a construct.

**Drift 1 — "about twice" is not in this paper.** The 1979 paper posits a value
function that is *steeper for losses than for gains*; it supplies no loss-aversion
coefficient. The figure the entry is repeating is **λ = 2.25**, the median
estimate reported thirteen years later in Tversky, A. & Kahneman, D. (1992),
"Advances in prospect theory: Cumulative representation of uncertainty",
*Journal of Risk and Uncertainty* 5(4): 297–323 —
[10.1007/BF00122574](https://doi.org/10.1007/BF00122574). Separately, loss
aversion **in riskless choice** — which is what an unsaved-changes dialog
actually is — was formalised in Tversky, A. & Kahneman, D. (1991), "Loss Aversion
in Riskless Choice: A Reference-Dependent Model", *Quarterly Journal of
Economics* 106(4): 1039–1061 — [10.2307/2937956](https://doi.org/10.2307/2937956).
An entry about UI copy is citing the risky-gamble paper for a riskless-choice
claim and quoting a number from a third paper. All three are real; the pairing
is not.

**Drift 2 — the ratio is contested, downward and hard.**

- Gal, D. & Rucker, D. D. (2018), "The Loss of Loss Aversion: Will It Loom Larger
  Than Its Gain?", *Journal of Consumer Psychology* 28(3): 497–516 —
  [10.1002/jcpy.1047](https://doi.org/10.1002/jcpy.1047) — review concluding
  that "current evidence does not support that losses, on balance, tend to be
  any more impactful than gains", and that its two headline supports (endowment
  effect, status-quo bias) admit alternative explanations.
- Walasek, L., Mullett, T. L. & Stewart, N. (2024), "A meta-analysis of loss
  aversion in risky contexts", *Journal of Economic Psychology* 103: 102740 —
  [10.1016/j.joep.2024.102740](https://doi.org/10.1016/j.joep.2024.102740) —
  re-fitting prospect theory to individual choices across the usable datasets
  yields **λ ≈ 1.31**, not 2.25.
- Yechiam, E. & Zeif, D. (2025), "Loss aversion is not robust: A re-meta-analysis",
  *Journal of Economic Psychology* 107: 102801 —
  [10.1016/j.joep.2025.102801](https://doi.org/10.1016/j.joep.2025.102801).

Note the direction of the error: "about twice" **overstates** the lever, and the
entry uses that overstatement to justify a persuasion technique. Given the
entry's own hard stop around the user's money, the honest number matters.

### UX-P05 — IKEA effect

**Wrong year.** Crossref returns `issued: 2011-09-09` (online-first) but
`published-print: 2012-07`, with the article of record at *Journal of Consumer
Psychology* **22(3): 453–460, 2012**. Full citation: Norton, M. I., Mochon, D. &
Ariely, D. (2012), "The IKEA effect: When labor leads to love" —
[10.1016/j.jcps.2011.08.002](https://doi.org/10.1016/j.jcps.2011.08.002). The
entry's "2011" is the online-first stamp, which is also what the DOI suffix
encodes; it is not the citation year, and the standing convention is 2012. The
lead was correct.

**Drift — mechanism and boundary, both missing.**

- The entry says only "labor raises valuation". The paper is explicit that this
  holds **only for successfully completed** labour: participants who assembled
  and then disassembled their creation, or who failed to complete it, showed no
  premium. An onboarding flow the user abandons half-built produces no IKEA
  effect, which is a live risk for the "configuration onboarding" use the entry
  recommends.
- The mechanism has since been identified as **feelings of competence /
  psychological ownership**, not effort per se: Mochon, D., Norton, M. I. &
  Ariely, D. (2012), "Bolstering and restoring feelings of competence via the
  IKEA effect", *International Journal of Research in Marketing* 29(4): 363–369
  — [10.1016/j.ijresmar.2012.05.001](https://doi.org/10.1016/j.ijresmar.2012.05.001),
  and Sarstedt, M., Neubert, D. & Barth, K. (2017), "The IKEA Effect. A
  Conceptual Replication", *Journal of Marketing Behavior* 2(4): 307–312 —
  [10.1561/107.00000039](https://doi.org/10.1561/107.00000039), which supports
  the original effect and identifies psychological ownership as the mediator.
  This is the one entry in the family whose effect has a **positive** replication
  record; the rewrite may say so.

### UX-P11 — Zeigarnik effect

**Verified, with a Crossref defect that must be recorded.** The canonical source
is Zeigarnik, B. (1927), "Das Behalten erledigter und unerledigter Handlungen"
(item III of Lewin's series *Untersuchungen zur Handlungs- und Affektpsychologie*),
*Psychologische Forschung* 9: 1–85 —
[10.1007/BF02409755](https://doi.org/10.1007/BF02409755). **Crossref's record for
this DOI is wrong**: it returns only the series title and credits `K. Lewin` as
author, with no mention of Zeigarnik (Semantic Scholar mirrors the same bad
metadata). Journal, volume and page range match, and the same series-title
pattern appears across neighbouring records (Ovsiankina 1928 at
[10.1007/BF00410261](https://doi.org/10.1007/BF00410261), *Psychologische
Forschung* 11: 302–379; Karsten 1928 at vol. 10: 142–254), so the DOI is right
and the author field is a cataloguing artefact. Link the DOI, but state the
author from the article, not from the API. Publisher pages for this volume are
behind a bot challenge and could not be fetched directly.

**Drift — the entry's headline claim is the half that failed.** The entry asserts
both that unfinished tasks are "remembered better" *and* that they "create
tension to complete them". A 2025 meta-analysis separates these and kills the
first: Ghibellini, R. & Meier, B. (2025), "Interruption, recall and resumption: a
meta-analysis of the Zeigarnik and Ovsiankina effects", *Humanities and Social
Sciences Communications* 12, article 962 —
[10.1057/s41599-025-05000-w](https://doi.org/10.1057/s41599-025-05000-w).
Pooling 38 publications on recall and 20 on resumption, they report a
recall-ratio of **0.99** (i.e. no memory advantage for interrupted tasks; dz =
0.15 across the 8 studies reporting it; interrupted items were 49.4% of those
recalled), against a **67% resumption rate** for interrupted tasks. Their
sensitivity analysis excluding Zeigarnik's own 1927 data leaves this unchanged
(0.99; 49.2%) — the effect does not survive the removal of its founder's
dataset. The authors' conclusion is that the Zeigarnik effect "lacks universal
validity" while the Ovsiankina resumption tendency is general.

For UX this is unusually clean news, because it is the **resumption** half a
progress checklist relies on, not the memory half. The lineage the rewrite needs
is therefore Ovsiankina, M. (1928), "Die Wiederaufnahme unterbrochener
Handlungen", *Psychologische Forschung* 11: 302–379 —
[10.1007/BF00410261](https://doi.org/10.1007/BF00410261) — not Zeigarnik.
Related and worth a line for anyone tempted to nag: Wendsche, J., Weigelt, M. &
Syrek, C. (2026), "Unfinished work tasks and work-related thoughts during off-job
time: meta-analysis of the Zeigarnik effect in a work-recovery context",
*Anxiety, Stress, & Coping* 39: 385–407 —
[10.1080/10615806.2026.2616302](https://doi.org/10.1080/10615806.2026.2616302) —
the residue of unfinished tasks in the modern literature shows up as rumination,
not as helpful motivation.

### UX-P25 — Goal-gradient effect

**Verified, both links in the chain.** Hull, C. L. (1932), "The goal-gradient
hypothesis and maze learning", *Psychological Review* 39(1): 25–43 —
[10.1037/h0072640](https://doi.org/10.1037/h0072640). Kivetz, R., Urminsky, O. &
Zheng, Y. (2006), "The Goal-Gradient Hypothesis Resurrected: Purchase
Acceleration, Illusionary Goal Progress, and Customer Retention", *Journal of
Marketing Research* 43(1): 39–58 —
[10.1509/jmkr.43.1.39](https://doi.org/10.1509/jmkr.43.1.39). Authors, years,
journals, volumes, issues and pages all check out, and the descent the ticket
asked about is real: Hull is the animal origin (rats accelerating toward food in
a maze), Kivetz et al. is the human demonstration (café card-holders accelerating
purchases as the card fills, plus the "illusionary goal progress" and
post-reward-reset findings). This is the best-sourced entry in the family.

**Drift — minor, three points of hygiene.**

1. `Kivetz et al., 2006` should be spelled out at least once; "et al." on a
   three-author paper in a catalog of nine citations is where the next audit
   loses the thread.
2. Hull 1932 is **rats in a maze**. The entry states the goal gradient as a flat
   fact about people; the human evidence is Kivetz et al. alone, and it is about
   *reward programmes*, not about progress bars in software.
3. Kivetz et al. found the effect **strengthens with each subsequent reward
   cycle** — and Drèze, X. & Nunes, J. C. (2011), "Recurring Goals and Learning:
   The Impact of Successful Reward Attainment on Purchase Behavior", *JMR* 48(2):
   268–281 — [10.1509/jmkr.48.2.268](https://doi.org/10.1509/jmkr.48.2.268) —
   found the boost from a completed goal appears only when the goal was
   *challenging*. The entry's "❌ long or open-ended processes" caveat is
   correct and now has a source.

### UX-P26 — Commitment & consistency

**Not the origin, and no year given.** The entry credits "Cialdini" with no year
and no work — a defect twice over, because the work is a trade book and Cialdini
did not originate the effect. He synthesised it. The lead held.

- **Origin:** Freedman, J. L. & Fraser, S. C. (1966), "Compliance without
  pressure: The foot-in-the-door technique", *Journal of Personality and Social
  Psychology* 4(2): 195–202 —
  [10.1037/h0023552](https://doi.org/10.1037/h0023552). Verified against
  Crossref.
- **The trade book, cited as such:** Cialdini, R. B., *Influence: The Psychology
  of Persuasion*. First published 1984; the current authoritative edition is
  *Influence, New and Expanded: The Psychology of Persuasion*, Harper Business,
  4 May 2021, ISBN 9780062937650 (verified via the Open Library edition record —
  the HarperCollins product page refused automated fetch). **Caveat on the first
  edition:** I could not settle 1984 against a publisher record; Open Library's
  index reports a `first_publish_year` of 1983 across a messy edition history
  (Morrow/Quill trade line versus the Scott, Foresman textbook line *Influence:
  Science and Practice*). Cite the edition actually consulted, with its year, and
  do not assert "1984" without checking the copy in hand.
- Chapter 3's underlying experiments, if the entry wants a source per claim
  rather than per chapter: Deutsch, M. & Gerard, H. B. (1955) —
  [10.1037/h0046408](https://doi.org/10.1037/h0046408) — for the effect of
  *public* commitment, and Moriarty, T. (1975) —
  [10.1037/h0076288](https://doi.org/10.1037/h0076288) — for the beach-theft
  commitment field studies.

**Drift — the effect is small and unreliable, and the entry implies otherwise.**
"People act consistently with a prior small commitment" is stated as a mechanism
that simply works. The meta-analytic record:

- Beaman, A. L., Cole, C. M., Preston, M., Klentz, B. & Steblay, N. M. (1983),
  "Fifteen Years of Foot-in-the-Door Research: A Meta-Analysis", *Personality and
  Social Psychology Bulletin* 9(2): 181–196 —
  [10.1177/0146167283092002](https://doi.org/10.1177/0146167283092002) — pooled
  120 experimental groups and found a significant but **modest** effect, with a
  large share of studies showing null or reversed results.
- Burger, J. M. (1999), "The Foot-in-the-Door Compliance Procedure: A
  Multiple-Process Analysis and Review", *Personality and Social Psychology
  Review* 3(4): 303–325 —
  [10.1207/s15327957pspr0304_2](https://doi.org/10.1207/s15327957pspr0304_2) —
  the standard review: the effect is real under specific conditions and is
  produced by several competing processes (self-perception, commitment,
  consistency, reactance, conformity, attribution), not by "consistency" alone.
  Freedman & Fraser's own effect size has not been reproduced at that magnitude.

So the honest statement names self-perception as at least as likely a mechanism
as consistency, and drops any implication of reliability. The entry's ethical
guard already anticipates the abuse case correctly and should survive intact.

### UX-P27 — Sunk cost

**No attribution at all — the worst case in either family so far.** The entry
names an effect ("the sunk cost fallacy") with neither author nor year nor work.
Supplied, both verified against Crossref:

- Arkes, H. R. & Blumer, C. (1985), "The psychology of sunk cost",
  *Organizational Behavior and Human Decision Processes* 35(1): 124–140 —
  [10.1016/0749-5978(85)90049-4](https://doi.org/10.1016/0749-5978\(85\)90049-4)
  — the canonical experimental source (the ski-trip and theatre-season-ticket
  studies), and the source of the standard definition: a greater tendency to
  continue an endeavour once money, effort or time has been invested.
- Staw, B. M. (1976), "Knee-deep in the big muddy: A study of escalating
  commitment to a chosen course of action", *Organizational Behavior and Human
  Performance* 16(1): 27–44 —
  [10.1016/0030-5073(76)90005-2](https://doi.org/10.1016/0030-5073\(76\)90005-2)
  — escalation of commitment, the organisational sibling; earlier than Arkes &
  Blumer and framed around self-justification rather than waste-avoidance.

Modern estimate of prevalence, useful for calibrating how much weight the entry
should put on the lever: Ronayne, D., Sgroi, D. & Tuckwell, A. (2021),
"Evaluating the sunk cost effect", *Journal of Economic Behavior & Organization*
186: 318–327 —
[10.1016/j.jebo.2021.03.029](https://doi.org/10.1016/j.jebo.2021.03.029) — with
a real-effort task and a dominated-versus-dominant lottery switch, **23%** of
subjects stuck with the dominated option; the endowment effect accounts for only
about a third of that, and cognitive reflection predicts susceptibility. The
effect is real, and it is a minority behaviour.

**Drift — the entry's mechanism sentence and its advice describe different
things.** The mechanism states the *fallacy*: "prior irrecoverable investment
**irrationally** drives continuation". The advice then recommends "reflecting
genuine value the user has built … so they see what leaving would waste".
Genuine accumulated value is **not** a sunk cost — it is a real switching cost,
and acting on it is rational. The entry is using the name of an irrationality to
license a piece of honest disclosure. That is a good practice attached to the
wrong theory, and the rewrite should either rename the principle (switching-cost
transparency) or keep the sunk-cost name while stating plainly that the entry
recommends *not* exploiting the fallacy. Worth noting that Nunes & Drèze
explicitly tested the sunk-cost reading of endowed progress (their study 2,
against Arkes & Blumer) and rejected it in favour of perceived task completion —
so `UX-P02` and `UX-P27` should not be presented as the same machinery.

### UX-P28 — Variable reward

**No years, no works, and the load-bearing source is a business book.** The entry
cites "(Skinner)" and "(Eyal)". Supplied:

- Ferster, C. B. & Skinner, B. F. (1957), *Schedules of Reinforcement*,
  Appleton-Century-Crofts — [10.1037/10627-000](https://doi.org/10.1037/10627-000).
  Crossref resolves this as a `book` (no volume/pages), which is the correct
  primary for reinforcement schedules; Skinner's schedule work begins in *The
  Behavior of Organisms* (1938), but the systematic treatment of variable-ratio
  and variable-interval schedules is the 1957 volume.
- The **resistance-to-extinction** result that UX writing actually means when it
  says "reinforce more strongly" is older and separate: Humphreys, L. G. (1939),
  "The effect of random alternation of reinforcement on the acquisition and
  extinction of conditioned eyelid reactions", *Journal of Experimental
  Psychology* 25(2): 141–158 —
  [10.1037/h0058138](https://doi.org/10.1037/h0058138) — the partial
  reinforcement extinction effect.
- Eyal, N. (2014), *Hooked: How to Build Habit-Forming Products*,
  Portfolio/Penguin, ISBN 9781591847786 (verified via the Open Library edition
  record). A trade book. It is **not evidence**, and the entry currently presents
  the Hook Model as the mechanism's continuation ("the engine of the 'Hooked'
  model").

**Drift — the largest evidential gap in the family.** "Unpredictable rewards
reinforce a behavior more strongly than fixed ones" is not what the operant
literature says, on three counts:

1. Ferster & Skinner's schedules describe **rates and patterns of responding**
   and **resistance to extinction** in pigeons and rats under food deprivation
   with a single, consumed, primary reinforcer. "Reinforce more strongly" is not
   a quantity the work defines; variable-ratio schedules produce high, steady
   response rates and post-reinforcement pauses shorter than fixed-ratio, which
   is a claim about response *topography*, not about motivational strength.
2. The extinction-resistance advantage is a **partial-versus-continuous**
   contrast (Humphreys 1939), not "variable versus fixed". The entry has fused
   two separate findings into one sentence.
3. Nothing in this literature licenses the transfer to app notifications, feeds
   or streaks, where the "reward" is informational, unconsumed, self-paced and
   competing with a hundred other reinforcers. The usual bridge offered is the
   dopamine reward-prediction-error work — Schultz, W., Dayan, P. & Montague,
   P. R. (1997), "A Neural Substrate of Prediction and Reward", *Science*
   275(5306): 1593–1599 —
   [10.1126/science.275.5306.1593](https://doi.org/10.1126/science.275.5306.1593)
   — but that describes a **learning signal**, and citing it for "unpredictability
   makes users come back" is the same over-reach one step deeper.

The entry's ethical guard is the best-written text in the catalog and should not
change. But it currently rests on a mechanism claim the sources do not support,
and it borrows its test (the Manipulation Matrix) from the same trade book it
should be holding at arm's length. Note the awkwardness the rewrite must own:
`UX-P28` cites Eyal's Manipulation Matrix as the ethical check on a technique
Eyal's book exists to teach.

### UX-P29 — Parkinson's law

**Not academic, unattributed, and a joke.** "Work expands so as to fill the time
available for its completion" is the opening line of an unsigned satirical essay
by the naval historian **C. Northcote Parkinson**, published in *The Economist*
on **19 November 1955** —
[economist.com/news/1955/11/19/parkinsons-law](https://www.economist.com/news/1955/11/19/parkinsons-law).
**Could not resolve via Crossref** (no DOI) **and the publisher page refuses
automated fetch**; the date, authorship and opening formulation were checked
against the essay text mirrors and the subsequent book, and the publisher URL is
recorded as the canonical link on the strength of that. The essay was reprinted
with others as *Parkinson's Law: The Pursuit of Progress* (London: John Murray,
1958; US edition *Parkinson's Law and Other Studies in Administration*, Houghton
Mifflin, 1957) — I could not settle the two competing first-edition years against
a publisher record, so the 1955 essay is the citation to use. Its subject is the
growth of civil-service staffing, and its "evidence" is a comic extrapolation
from Admiralty headcount figures.

**Drift — the entry treats a satire about bureaucracies as a finding about
users.** There is nothing in Parkinson to support "a reasonable, honest
constraint helps users complete a task instead of stalling". The closest real
literature is the **excess-time effect**, and it is more interesting than the
aphorism:

- Bryan, J. F. & Locke, E. A. (1967), "Parkinson's Law as a goal-setting
  phenomenon", *Organizational Behavior and Human Performance* 2(3): 258–275 —
  [10.1016/0030-5073(67)90021-9](https://doi.org/10.1016/0030-5073\(67\)90021-9)
  — reframes the observation as goal-setting: people given excess time slow down
  because no goal is set, and the fix is an explicit goal, not a shorter clock.
- Aronson, E. & Landy, D. (1967), "Further steps beyond Parkinson's Law: A
  replication and extension of the excess time effect", *Journal of Experimental
  Social Psychology* 3(3): 274–285 —
  [10.1016/0022-1031(67)90029-7](https://doi.org/10.1016/0022-1031\(67\)90029-7).

That is the honest support for the entry's advice, and it points somewhere
better: the mechanism is a **clear goal**, not a **time limit**. The entry's own
examples (autosave-and-continue, a clearly scoped step) are goal-setting, not
time pressure — and its only genuinely time-bound example, the reservation hold,
is a real-world inventory constraint that would exist with or without Parkinson.

---

## IDs whose claim text needs rewording

All nine, in descending order of how wrong the current text is:

1. **`UX-P28`** — supply Ferster & Skinner 1957 and Humphreys 1939; replace
   "reinforce more strongly than fixed" with what the schedules literature
   actually shows (response rate and resistance to extinction under partial
   reinforcement, in animals); state that the transfer to feeds and
   notifications is an extrapolation with no direct evidence; label *Hooked* as
   a trade book, and flag that its Manipulation Matrix is being used as a guard
   against the technique its own author promotes.
2. **`UX-P03`** — remove "about twice" or re-source it to Tversky & Kahneman 1992
   (λ = 2.25) and immediately qualify it with Walasek et al. 2024 (λ ≈ 1.31),
   Gal & Rucker 2018 and Yechiam & Zeif 2025; cite Tversky & Kahneman 1991 for
   the riskless case the UI examples actually are; keep Kahneman & Tversky 1979
   as the origin.
3. **`UX-P11`** — split the claim: drop the *memory* half outright (Ghibellini &
   Meier 2025: recall ratio 0.99, unchanged when Zeigarnik's own data are
   removed) and keep the *resumption* half, re-sourced to Ovsiankina 1928; note
   the Crossref author-metadata defect on the Zeigarnik DOI so the next reader
   does not "correct" it to Lewin.
4. **`UX-P27`** — supply Arkes & Blumer 1985 and Staw 1976; add Ronayne et al.
   2021 for prevalence (~23%); resolve the contradiction between naming a
   fallacy and recommending honest disclosure of real switching cost — they are
   not the same thing.
5. **`UX-P26`** — cite Freedman & Fraser 1966 as the origin; demote Cialdini to
   an explicitly-labelled trade-book synthesis with a specific edition and year;
   state that the effect is small and multiply-determined (Beaman et al. 1983,
   Burger 1999) rather than a reliable mechanism.
6. **`UX-P29`** — say plainly it is a 1955 satirical essay about civil-service
   staffing, not a finding; re-ground the advice in the excess-time /
   goal-setting literature (Bryan & Locke 1967, Aronson & Landy 1967) and shift
   the recommendation from "time limit" to "explicit goal".
7. **`UX-P02`** — keep Nunes & Drèze 2006; drop or qualify the Zeigarnik leg
   (inherited dead citation); state the evidence base honestly (a paid loyalty
   programme, 34% vs 19%, not a UI); add the "a reason must be given" moderator;
   and mark the ethical guard as *stricter than the source*, which found a
   specious reason works as well as a real one.
8. **`UX-P05`** — fix the year to 2012; add the successful-completion boundary
   (no premium for abandoned or disassembled work) and the psychological-ownership
   mechanism; note that this is the one entry in the family with a positive
   replication record and may be stated with confidence.
9. **`UX-P25`** — spell out Kivetz, Urminsky & Zheng 2006; mark Hull 1932 as
   animal work and Kivetz et al. as the human evidence, scoped to reward
   programmes; add Drèze & Nunes 2011 to support the existing "long or
   open-ended processes" caveat.

## Findings for the v2 entry template (#7)

The motivation family **confirms all three** fields the cognition audit proposed,
and demands two more.

- **Source standing** (`replicated` / `contested` / `not-academic` /
  `popularization`) — confirmed, and needed more urgently here: `UX-P05` is
  *replicated*, `UX-P03` and `UX-P11` are *contested* to the point of partial
  refutation, and `UX-P26`, `UX-P28`, `UX-P29` are *not-academic* as currently
  cited. Six of nine.
- **Origin citation separated from mechanism citation** — confirmed. `UX-P02`
  (endowed progress vs. Zeigarnik/Hull), `UX-P03` (1979 origin vs. 1991 riskless
  vs. 1992 coefficient), `UX-P05` (2012 effect vs. 2012 IJRM mechanism), `UX-P26`
  (Freedman & Fraser origin vs. Cialdini's consistency framing) and `UX-P28`
  (Ferster & Skinner schedules vs. Humphreys extinction) all need two slots.
  Five of nine — and `UX-P03` needs **three**.
- **A marker for our own editorial stance** — confirmed, and this family shows it
  is not optional. See the new field below, which is the sharp version of it.

Two new fields this family demands:

- **`source type`** — `peer-reviewed` / `book (academic)` / `trade book` /
  `essay` / `none`. The standing field above does not capture this: *Hooked*,
  *Influence* and Parkinson's *Economist* piece are each a different kind of
  non-evidence, and each needs a different disclaimer. A reader must be able to
  see at a glance that `UX-P28`'s mechanism rests on a 1957 animal-behaviour
  monograph and a 2014 business book, and that these are not the same kind of
  thing. This family leans on trade books in a way the cognition family did not:
  three of nine.
- **`guard divergence`** — an explicit flag for *the ethical guard is stricter
  than the cited evidence*. This is the finding I did not expect and the one the
  template most needs. In `UX-P02`, the source found that a **specious**
  justification for fake progress works as well as a real one, and our guard
  forbids exactly that. In `UX-P28`, the operant literature is silent on ethics
  and the guard is entirely ours. In `UX-P25`, the source (Kivetz et al.) reports
  "illusionary goal progress" as an effective tactic, and our guard requires the
  distance shown to be real. Without this flag, a reader can reasonably conclude
  that the guard is part of the finding, and a future editor "correcting the
  entry to match the source" would strip the guard as unsupported. Every entry
  in this family whose lever is near a dark pattern needs it — which, per the
  family's own preamble, is most of them.
