# Reference verification — cognition family (UX-P01, P06, P07, P08, P13, P14, P15, P16, P17)

Resolves [#9](https://github.com/Storzen/skills/issues/9). Re-slice of [#4](https://github.com/Storzen/skills/issues/4), cognition family only — 9 entries.

**Method.** Every DOI below was resolved against the Crossref metadata API
(`api.crossref.org/works/<doi>`) and its author list, year, journal, volume and
pages checked against the citation as written in `PRINCIPLES-cognition.md`. Two
non-DOI sources (Tesler's law, Occam's razor) were read at the primary page
itself. Lawsofux, NN/g, Wikipedia and Medium were used as leads only; none is
recorded as a citation.

**Headline.** No attribution in this family is *fabricated* — every named
author/year pair that exists is real and correctly paired. The damage is
elsewhere: **3 of 9 entries name no source at all**, and **7 of 9 state a claim
the cited source does not support as written** — either the mechanism named is
not the one the literature settled on, the effect is far more contested than the
entry admits, or the entry's own examples belong to a different phenomenon than
the paper it cites.

---

## Verdict table

| ID | Cited as | Verdict | Corrected / supplied attribution | Canonical link | Reword? |
|---|---|---|---|---|---|
| `UX-P01` | Samuelson & Zeckhauser, 1988; Johnson & Goldstein, 2003 | **CORRECT** (attribution) | — | [10.1007/BF00055564](https://doi.org/10.1007/BF00055564) · [10.1126/science.1091721](https://doi.org/10.1126/science.1091721) | **Yes** — mechanism over-attributed to status-quo bias; defaults are multi-causal |
| `UX-P06` | Tversky & Kahneman, 1974 | **IMPRECISE** | Effect: Tversky & Kahneman 1974. Mechanism for *provided* anchors: Strack & Mussweiler 1997 / Mussweiler & Strack 1999 | [10.1126/science.185.4157.1124](https://doi.org/10.1126/science.185.4157.1124) | **Yes** — "anchoring and adjustment" is the wrong mechanism for the UI case |
| `UX-P07` | "Hick–Hyman law" — no author, no year | **MISSING** | Hick 1952; Hyman 1953 | [10.1080/17470215208416600](https://doi.org/10.1080/17470215208416600) · [10.1037/h0056940](https://doi.org/10.1037/h0056940) | **Yes** — law does not cover "complexity" of choices, nor menu reading |
| `UX-P08` | Miller, 1956; refined by Cowan, 2001 | **CORRECT** (attribution) | — | [10.1037/h0043158](https://doi.org/10.1037/h0043158) · [10.1017/S0140525X01003922](https://doi.org/10.1017/S0140525X01003922) | **Yes** — "Miller's law" is a UX coinage; the nav-length application is unsupported |
| `UX-P13` | "Tesler's law" — no author, no year | **NOT-ACADEMIC** + **MISSING** | Larry Tesler, ca. 1984 (Xerox PARC); popularized by Saffer 2006 | [nomodes.com — Complexity Law](http://www.nomodes.com/larry-tesler-consulting/complexity-law) | **Yes** — "default to the system" is our stance, not Tesler's |
| `UX-P14` | Iyengar & Lepper, 2000 | **IMPRECISE** (origin correct, claim contested) | Origin correct; must carry Scheibehenne et al. 2010 and Chernev et al. 2015 | [10.1037/0022-3514.79.6.995](https://doi.org/10.1037/0022-3514.79.6.995) | **Yes** — strongest rewrite in the family; effect is conditional, not general |
| `UX-P15` | "Occam's razor" — no author, no year | **NOT-ACADEMIC** + **MISSING** | William of Ockham, c. 1287–1347; the canonical Latin formulation is *not* his | [SEP — William of Ockham §4.1](https://plato.stanford.edu/entries/ockham/) | **Yes** — a metaphysical parsimony principle, not a finding about attention |
| `UX-P16` | Huber, Payne & Puto, 1982 | **CORRECT** (attribution) | — | [10.1086/208899](https://doi.org/10.1086/208899) | **Yes** — robustness contested; the *Economist* case is Ariely 2008, not the paper |
| `UX-P17` | Tversky & Kahneman, 1981 | **IMPRECISE** | Correct for risky-choice framing; the entry's examples are *attribute* framing (Levin, Schneider & Gaeth 1998) | [10.1126/science.7455683](https://doi.org/10.1126/science.7455683) · [10.1006/obhd.1998.2804](https://doi.org/10.1006/obhd.1998.2804) | **Yes** — cite/example mismatch |

Verdict key: `CORRECT` — author, year and work introduced the effect.
`IMPRECISE` — real source, but the entry's claim outruns or misnames it.
`MISSING` — no attribution given. `NOT-ACADEMIC` — a heuristic or aphorism, no
empirical origin. No entry in this family scored `WRONG`.

---

## Evidence

### UX-P01 — Smart defaults

**Verified.** Samuelson, W. & Zeckhauser, R. (1988), "Status quo bias in
decision making", *Journal of Risk and Uncertainty* 1(1): 7–59 —
[10.1007/BF00055564](https://doi.org/10.1007/BF00055564). Johnson, E. J. &
Goldstein, D. (2003), "Do Defaults Save Lives?", *Science* 302(5649): 1338–1339
— [10.1126/science.1091721](https://doi.org/10.1126/science.1091721). Both pairs
correct: authors, years, journals, volumes and pages all match.

**Drift.** The entry states one mechanism — status-quo bias — as *the* reason
defaults stick. The meta-analytic literature does not support a single cause.
Jachimowicz, Duncan, Weber & Johnson (2019), "When and why defaults influence
decisions: a meta-analysis of default effects", *Behavioural Public Policy*
3(2): 159–186 — [10.1017/bpp.2018.43](https://doi.org/10.1017/bpp.2018.43) —
finds a robust default effect overall, moderated by three distinct pathways:
effort (the default is the cheapest option), implied endorsement (the default
reads as the recommended choice), and reference-point/endowment effects. Only
the third is status-quo bias proper. The entry's own advice depends on which
pathway is at work: "trivially changeable" defuses the effort pathway but not
implied endorsement, which is precisely how a pre-checked opt-in does its damage.

**Second drift, worth knowing.** Johnson & Goldstein 2003 measured *registration
as a donor*, not organs transplanted. Arshad, Anderson & Sharif (2019),
"Comparison of organ donation and transplantation rates between opt-out and
opt-in systems", *Kidney International* 95(6): 1453–1460 —
[10.1016/j.kint.2019.01.036](https://doi.org/10.1016/j.kint.2019.01.036) —
found opt-out countries have higher deceased-donor rates but *lower* living-donor
rates, with the net effect far smaller than the registration figures suggest. The
entry doesn't invoke organ donation, so this is not a defect in the text — but it
should stop the rewrite from reaching for the famous 99%-vs-12% chart as
illustration.

### UX-P06 — Anchoring / contrast

**Verified.** Tversky, A. & Kahneman, D. (1974), "Judgment under Uncertainty:
Heuristics and Biases", *Science* 185(4157): 1124–1131 —
[10.1126/science.185.4157.1124](https://doi.org/10.1126/science.185.4157.1124).
The paper does introduce anchoring, and does name "anchoring and adjustment" as
the process. So the entry is quoting the source faithfully — the problem is that
the source was superseded on this exact point.

**Drift.** Insufficient adjustment from an anchor is now understood to apply to
*self-generated* anchors — Epley, N. & Gilovich, T. (2006), "The
Anchoring-and-Adjustment Heuristic: Why the Adjustments Are Insufficient",
*Psychological Science* 17(4): 311–318 —
[10.1111/j.1467-9280.2006.01704.x](https://doi.org/10.1111/j.1467-9280.2006.01704.x).
Anchors *provided externally* — which is every case a UI cares about: the price
you show first, the plan you list first — are better explained by selective
accessibility: the anchor primes anchor-consistent knowledge, which then dominates
the judgment. See Strack, F. & Mussweiler, T. (1997), "Explaining the enigmatic
anchoring effect: Mechanisms of selective accessibility", *JPSP* 73(3): 437–446
— [10.1037/0022-3514.73.3.437](https://doi.org/10.1037/0022-3514.73.3.437), and
Mussweiler, T. & Strack, F. (1999), *JESP* 35(2): 136–164 —
[10.1006/jesp.1998.1364](https://doi.org/10.1006/jesp.1998.1364).

**Robustness: good.** Anchoring is one of the effects that survived the
replication crisis intact — replicated in Many Labs 1 (Klein et al. 2014,
*Social Psychology* 45(3): 142–152 —
[10.1027/1864-9335/a000178](https://doi.org/10.1027/1864-9335/a000178)). This
entry can be stated with more confidence than most in the family; it just needs
the right mechanism name.

### UX-P07 — Hick's law

**Missing attribution.** The entry names "Hick–Hyman law" with neither author nor
year — a defect under the ticket's own rule. Supplied: Hick, W. E. (1952), "On
the Rate of Gain of Information", *Quarterly Journal of Experimental Psychology*
4(1): 11–26 — [10.1080/17470215208416600](https://doi.org/10.1080/17470215208416600);
Hyman, R. (1953), "Stimulus information as a determinant of reaction time",
*Journal of Experimental Psychology* 45(3): 188–196 —
[10.1037/h0056940](https://doi.org/10.1037/h0056940). The law rests on **both**:
Hick established the logarithmic form, Hyman generalized it to the information
content of the stimulus set (unequal probabilities, sequential dependencies), which
is why the pairing is the standard name.

**Drift — two of them, both material.**

1. *"and complexity of choices"* is not in the law. Hick and Hyman measured
   reaction time against the **information content** of the alternative set — a
   function of their number and probability distribution — with simple, practiced,
   arbitrary stimulus→response mappings. Per-option complexity is outside the
   model.
2. The law describes **choice reaction**, not visual search or reading. Applying
   it to a menu of unfamiliar text labels — the entry's headline use — is an
   extension, not an application: scanning unfamiliar labels is closer to linear
   search. The defensible UI evidence for the menu case is Landauer, T. K. &
   Nachbar, D. W. (1985), "Selection from alphabetic and numeric menu trees using
   a touch screen", *CHI '85*: 73–78 —
   [10.1145/317456.317470](https://doi.org/10.1145/317456.317470), which found
   log-form selection times for *ordered* (alphabetic/numeric) menus — i.e. where
   the user can binary-search rather than read every item. Seow, S. C. (2005),
   "Information Theoretic Models of HCI: A Comparison of the Hick-Hyman Law and
   Fitts' Law", *Human-Computer Interaction* 20(3): 315–352 —
   [10.1207/s15327051hci2003_3](https://doi.org/10.1207/s15327051hci2003_3) — is
   the right source for the boundary conditions.

The entry's *advice* (split long forms into steps, segment options) survives all
of this. The mechanism sentence does not.

### UX-P08 — Miller's law

**Verified.** Miller, G. A. (1956), "The magical number seven, plus or minus two:
Some limits on our capacity for processing information", *Psychological Review*
63(2): 81–97 — [10.1037/h0043158](https://doi.org/10.1037/h0043158). Cowan, N.
(2001), "The magical number 4 in short-term memory: A reconsideration of mental
storage capacity", *Behavioral and Brain Sciences* 24(1): 87–114 —
[10.1017/S0140525X01003922](https://doi.org/10.1017/S0140525X01003922). Both
correct, and the entry's hedge — ~4, "the popular 7±2 overstates it" — is the
literature's actual position. This is the best-calibrated claim in the family.

**Drift — the name, and one application.**

1. **"Miller's law" is a UX coinage, not Miller's.** Miller's paper is two
   findings stitched together: the channel capacity of *absolute judgment* on a
   unidimensional stimulus (~7 categories) and the span of *immediate memory* (~7
   chunks) — and Miller's own point was that the two are governed by different
   things and that the recurrence of the number is a coincidence he treats
   ironically ("persecution by an integer"). He proposed no law. The entry should
   either drop the possessive framing or state plainly that the name is the UX
   community's, not the author's.
2. **"limiting nav length" has no support from either source.** Both papers concern
   items held *in memory*; navigation items are on screen and re-readable, so
   working-memory capacity is not the binding constraint. Chunking a phone or card
   number — the entry's other example — is exactly right and is squarely what
   Miller's chunking argument supports. Cut the nav claim or move it to `UX-P07`,
   where the argument is decision cost rather than memory.

**Also.** This entry still carries no `Ethical guard` — one of the 12 known
non-compliant entries recorded in [#8](https://github.com/Storzen/skills/issues/8).
Not this ticket's business, noted so the rewrite doesn't lose it.

### UX-P13 — Tesler's law

**Not academic, and unattributed in the entry.** The law of conservation of
complexity is Larry Tesler's, formulated ca. 1984 while he was at Xerox PARC. The
primary source is Tesler's own page, which gives the original formulation
verbatim: *"Every application has an inherent amount of irreducible complexity.
The only question is: Who will have to deal with it — the user, the application
developer, or the platform developer?"* —
[nomodes.com/larry-tesler-consulting/complexity-law](http://www.nomodes.com/larry-tesler-consulting/complexity-law).
(The old `nomodes.com/Larry_Tesler_Consulting/Complexity_Law.html` URL 301s to
this one — link the current one.) Its wider circulation in design comes from Dan
Saffer's interview with Tesler, reprinted in *Designing for Interaction* (2006);
that is a popularization and should be cited as such if cited at all.

**Drift, mild but real.** Tesler names **three** parties — user, application
developer, platform developer — and asks *who* absorbs the complexity. The entry
compresses this to two ("the system or the user") and adds a prescription
("default to the system") that Tesler does not make. The compression is a
reasonable design stance and worth keeping; it must be marked as ours rather than
attributed to the law.

### UX-P14 — Choice overload

**Verified as origin.** Iyengar, S. S. & Lepper, M. R. (2000), "When choice is
demotivating: Can one desire too much of a good thing?", *JPSP* 79(6): 995–1006
— [10.1037/0022-3514.79.6.995](https://doi.org/10.1037/0022-3514.79.6.995). The
jam study. Attribution correct.

**Drift — the largest in the family.** The entry states choice overload as a
general effect. It is not.

- Scheibehenne, B., Greifeneder, R. & Todd, P. M. (2010), "Can There Ever Be Too
  Many Options? A Meta-Analytic Review of Choice Overload", *Journal of Consumer
  Research* 37(3): 409–425 —
  [10.1086/651235](https://doi.org/10.1086/651235) — pooled 50 experiments and
  found a **mean effect indistinguishable from zero**, with large variance across
  studies and no reliable moderator identified at the time.
- Chernev, A., Böckenholt, U. & Goodman, J. (2015), "Choice overload: A conceptual
  review and meta-analysis", *Journal of Consumer Psychology* 25(2): 333–358 —
  [10.1016/j.jcps.2014.08.002](https://doi.org/10.1016/j.jcps.2014.08.002) —
  recovered the effect **conditionally**, on four moderators: choice-set
  complexity, decision-task difficulty, preference uncertainty, and decision goal.
  With those absent, more options do not depress choice.

So the honest statement is: choice overload appears when the user has no
pre-formed preference, the options are hard to compare, and the task offers no
easy way out — which is a *description of a badly-built picker*, and makes the
entry's advice stronger, not weaker.

**"Paradox of choice" is not a source.** It is the title of Schwartz, B. (2004),
*The Paradox of Choice: Why More Is Less* (Ecco/HarperCollins) — a trade book
popularizing Iyengar & Lepper. The entry currently uses the phrase as if it named
a finding. Either drop it or mark it as the popular name.

### UX-P15 — Occam's razor

**Not academic, and unattributed in the entry.** William of Ockham, c. 1287–1347.
Two facts the rewrite needs, both from the Stanford Encyclopedia of Philosophy,
"William of Ockham" §4.1 —
[plato.stanford.edu/entries/ockham](https://plato.stanford.edu/entries/ockham/):

1. The canonical Latin formulation is **not Ockham's**. SEP, verbatim: *"Although
   the sentiment is certainly Ockham's, this particular formulation is nowhere to
   be found in his texts."* (The wording is usually traced to the 17th-century
   Scotist John Punch.) Do not put Latin in the entry as a quotation from Ockham.
2. The razor is a principle of **ontological parsimony** — do not posit more
   entities than needed to explain something — deployed in metaphysics. It is a
   methodological maxim, not an empirical finding, and says nothing about
   attention, screens, or effort.

**Consequence for the entry.** The mechanism sentence — *"each added element costs
attention and maintenance"* — is a real and defensible claim, but it is **not
Occam's razor**; it is a cognitive-load claim, and its support sits in `UX-P07`
(decision cost) and `UX-P08` (chunking) or in visual-search literature. The entry
currently borrows the razor's authority for a claim the razor does not make. Two
honest options: keep the name as an explicitly-labelled design aphorism and
support the attention claim by cross-reference, or fold the entry into `UX-P07`.
Whichever, `UX-P15` keeps its number (append-only IDs) and would be marked
DEPRECATED rather than reused.

### UX-P16 — Decoy effect

**Verified.** Huber, J., Payne, J. W. & Puto, C. (1982), "Adding Asymmetrically
Dominated Alternatives: Violations of Regularity and the Similarity Hypothesis",
*Journal of Consumer Research* 9(1): 90–98 —
[10.1086/208899](https://doi.org/10.1086/208899). Correct origin, correct year,
and "asymmetric dominance" is the paper's own term.

**Drift — robustness.** The effect is contested in exactly the conditions a
product team would deploy it:

- Frederick, S., Lee, L. & Baskin, E. (2014), "The Limits of Attraction",
  *Journal of Marketing Research* 51(4): 487–507 —
  [10.1509/jmr.12.0061](https://doi.org/10.1509/jmr.12.0061) — across many
  studies, found the effect essentially absent once options are described by
  images or realistic descriptions rather than numeric attribute lists.
- Yang, S. & Lynn, M. (2014), "More Evidence Challenging the Robustness and
  Usefulness of the Attraction Effect", *JMR* 51(4): 508–513 —
  [10.1509/jmr.14.0020](https://doi.org/10.1509/jmr.14.0020) — same direction,
  with real purchase contexts.
- Huber, J., Payne, J. W. & Puto, C. (2014), "Let's Be Honest About the Attraction
  Effect", *JMR* 51(4): 520–525 —
  [10.1509/jmr.14.0208](https://doi.org/10.1509/jmr.14.0208) — the original
  authors' reply, conceding the boundary conditions while defending the effect
  within them.

**The *Economist* example is not from the paper.** It is Dan Ariely's classroom
demonstration, published in *Predictably Irrational* (2008), based on a single
observed pricing page and an in-class replication with ~100 MIT students. Calling
it "the classic" in the entry lends it evidentiary weight it does not have. It is
usable as an *illustration* — clearly labelled — but not as evidence.

**Where this leaves the entry.** Favourably. `UX-P16` already tells the reader to
use the effect to *detect and remove* accidental decoys rather than to deploy one,
and the weak robustness record is an additional argument for exactly that stance:
a tactic that unreliably moves choice but reliably reads as manipulation when
noticed is a bad trade. Say so.

### UX-P17 — Framing effect

**Verified.** Tversky, A. & Kahneman, D. (1981), "The Framing of Decisions and the
Psychology of Choice", *Science* 211(4481): 453–458 —
[10.1126/science.7455683](https://doi.org/10.1126/science.7455683). Correct.
Robustness good: the Asian-disease framing item replicated in Many Labs 1 (Klein
et al. 2014) and Many Labs 2 (Klein et al. 2018, *AMPPS* 1(4): 443–490 —
[10.1177/2515245918810225](https://doi.org/10.1177/2515245918810225)).

**Drift — citation/example mismatch.** Tversky & Kahneman 1981 is **risky-choice
framing**: the same outcome distribution described as lives saved vs lives lost,
flipping risk preference via the prospect-theory value function. The entry's
examples — *"90% fat-free" vs "10% fat"*, *"save 3 hours" vs "lose 3 hours"* — are
**attribute framing** and **goal framing**, distinct phenomena with different
mechanisms and different effect sizes. The typology and its evidence are Levin,
I. P., Schneider, S. L. & Gaeth, G. J. (1998), "All Frames Are Not Created Equal:
A Typology and Critical Analysis of Framing Effects", *Organizational Behavior and
Human Decision Processes* 76(2): 149–188 —
[10.1006/obhd.1998.2804](https://doi.org/10.1006/obhd.1998.2804) — where the
"fat-free" case is the textbook attribute-framing example.

Since almost every UI framing decision is attribute or goal framing rather than
risky choice, Levin et al. 1998 is arguably the *primary* citation this entry
needs, with Tversky & Kahneman 1981 as the origin of the wider effect.

---

## IDs whose claim text needs rewording

All nine, in descending order of how wrong the current text is:

1. **`UX-P14`** — remove the unconditional claim; state the effect as conditional
   on the four Chernev moderators; label "paradox of choice" as Schwartz's
   popularization, not a finding.
2. **`UX-P15`** — stop attributing a cognitive-load claim to a metaphysical
   principle; either relabel as a design aphorism with the attention claim
   cross-referenced, or fold into `UX-P07` and mark `UX-P15` DEPRECATED (number
   retained).
3. **`UX-P07`** — supply Hick 1952 + Hyman 1953; drop "complexity of choices" from
   the mechanism; state the boundary (practiced choice reaction, ordered sets) and
   cite Landauer & Nachbar 1985 for the menu case.
4. **`UX-P16`** — add the failed-replication record (Frederick et al. 2014, Yang &
   Lynn 2014, and the authors' 2014 reply); demote the *Economist* case to a
   labelled illustration sourced to Ariely 2008.
5. **`UX-P17`** — add Levin et al. 1998 and name the frame type the examples
   actually are; keep Tversky & Kahneman 1981 as the origin.
6. **`UX-P06`** — replace "anchoring and adjustment" with selective accessibility
   for externally-provided anchors (Strack & Mussweiler 1997), keeping Tversky &
   Kahneman 1974 as the origin.
7. **`UX-P08`** — mark "Miller's law" as a UX coinage; cut or relocate the
   nav-length application; keep the chunking example and the ~4 hedge as they are.
   (Ethical guard still owed — see [#8](https://github.com/Storzen/skills/issues/8).)
8. **`UX-P01`** — name the three default pathways rather than status-quo bias
   alone; note that "trivially changeable" only defuses the effort pathway.
9. **`UX-P13`** — supply Tesler ca. 1984 with the primary link; restore the third
   party (platform developer); mark "default to the system" as our stance.

## Notes for the v2 entry template

Three things this audit wanted a field for and could not find:

- **A source's standing**, separate from its identity — `replicated` /
  `contested` / `not-academic` / `popularization`. Six of nine entries needed one
  and had nowhere to put it.
- **A separation between the origin citation and the mechanism citation.** Four
  entries (`UX-P06`, `UX-P07`, `UX-P15`, `UX-P17`) cite the paper that named the
  effect while describing a mechanism from a different literature.
- **A marker for the entry's own editorial stance**, so a prescription we add
  (`UX-P13`'s "default to the system") is not read as part of the cited law.
