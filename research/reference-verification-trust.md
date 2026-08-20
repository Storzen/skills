# Reference verification — trust family (UX-P12, P35, P36, P37, P38, P39, P40)

Resolves [#13](https://github.com/Storzen/skills/issues/13). Re-slice of [#4](https://github.com/Storzen/skills/issues/4), trust family only — 7 entries.

**Method.** Every DOI below was resolved against the Crossref metadata API
(`api.crossref.org/works/<doi>`) and its author list, year, journal, volume and
pages checked against the citation as written in `PRINCIPLES-trust.md`. Three
sources were read primary because the family's verdicts turn on their exact
words. **Camerer, Loewenstein & Weber 1989 was read in full from George
Loewenstein's own PDF at CMU** — the footnote crediting the coinage and the
abstract quoted below come from that copy. **Newton's 1990 Stanford dissertation
was read in full from the ProQuest scan**, and this report's tapping numbers are
taken from its own Table 1 rather than from the popular retelling, which
disagrees with it.
**Doherty & Thadhani 1982 was read in full** from the
text IBM authorised Jim Elliott to republish (`© Copyright IBM Corporation 1982,
1997. All rights reserved. Published here with permission.`) — IBM's own hosted
copy at `vm.ibm.com/devpages/jelliott/evrrt1.html` now redirects to an IBM 404
and is **dead**, which is recorded here because that document is the only warrant
the entry has. Abstracts blocked at the publisher were read verbatim from PubMed
(Kemp, Burt & Furneaux 2008, PMID 18323069; Redelmeier, Katz & Kahneman 2003,
PMID 12855328) or from Crossref's deposited abstract (Kahneman et al. 1993; Sels
et al. 2019). **One source resisted entirely: Alaybek et al. 2022 is closed at
Elsevier (ScienceDirect returns 403), Crossref carries no abstract, and Semantic
Scholar was unreachable** — its results are reported here from secondary
summaries and are **marked as second-hand** wherever used.
Lawsofux, Wikipedia
and Medium were used as leads only; none is recorded as a citation. **NN/g is the
honest exception in four of these seven entries**, on the same pattern the
perception audit applied to `UX-P19`: Nielsen's own publication of Nielsen's own
heuristics is the primary source *for the heuristic*, and those entries are
marked `NOT-ACADEMIC` accordingly. `deceptive.design` is recorded as primary
once, for a pattern name Brignull coined himself.

**Headline.** **Five of the seven entries are not findings at all.** Four are
Jakob Nielsen's usability heuristics (`UX-P35` #6, `UX-P36` #1, `UX-P38` #5/#3,
`UX-P40` #4) and the fifth (`UX-P37`) is an IBM sales brief; the file states all
of them in the same declarative voice it uses for an experiment, and **six of the
seven carry no year and no work**. That is the structural defect, and it is
milder than persuasion's — nothing here is attributed to the wrong person.
The
sharp defect is a single number. **`UX-P37`'s "~400 ms" does not appear in the
document it is credited to.** The 1982 Doherty & Thadhani brief was read end to
end: the string 400 occurs exactly once and refers to the number of simultaneous
NIH terminal users; the word "millisecond" occurs zero times; the document's own
argument is for **sub-second** response, and its one hard curve runs 3.0 s → 0.3
s. The brief is also **not** in the *IBM Systems Journal*, as lawsofux and every
blog downstream of it assert — the Computer History Museum catalogues it as a
12-page IBM technical report. The 400 ms is a practitioner number with no primary
warrant this audit could find. Second in severity, `UX-P12` states the peak-end
rule in its strongest form — "not its average" — which is the one clause its own
meta-analytic literature does not support, and generalises from a body of
evidence that is overwhelmingly about **pain**. On guards the news is mixed, and
one trap needs flagging: three of seven comply **on `main`**, and this branch's
copy of the file is stale.

---

## Verdict table

| ID | Cited as | Verdict | Corrected / supplied attribution | Canonical link | Reword? |
|---|---|---|---|---|---|
| `UX-P12` | "Peak-end rule (Kahneman)" — no year, no work | **IMPRECISE** + **MISSING** | Demonstration: Fredrickson, B. L. & Kahneman, D. (1993), *JPSP* 65(1): 45–55. Choice result: Kahneman, Fredrickson, Schreiber & Redelmeier (1993), *Psych. Science* 4(6): 401–405. Clinical: Redelmeier & Kahneman (1996), *Pain* 66(1): 3–8. **RCT: Redelmeier, Katz & Kahneman (2003), *Pain* 104(1): 187–194** | [10.1111/j.1467-9280.1993.tb00589.x](https://doi.org/10.1111/j.1467-9280.1993.tb00589.x) · [10.1016/S0304-3959(03)00003-4](https://doi.org/10.1016/S0304-3959\(03\)00003-4) | **Yes** — the evidence is about **aversive** episodes; "not its average" is the clause Alaybek et al. 2022 reportedly does not support; the *end* half failed in Sels et al. 2019 and the rule underperformed over week-long vacations (Kemp et al. 2008) |
| `UX-P35` | "Nielsen heuristic #6" — no year, no work | **NOT-ACADEMIC** + **MISSING** | Nielsen, J. & Molich, R. (1990), CHI '90: 249–256 — where it is "**Minimize user memory load**", one of nine. The wording "recognition rather than recall" and the numbering are Nielsen, J. (1994), CHI '94: 152–158. Underlying finding, uncited: Shepard 1967; Standing 1973; Anderson & Bower 1972 | [10.1145/97243.97281](https://doi.org/10.1145/97243.97281) · [10.1145/191666.191729](https://doi.org/10.1145/191666.191729) · [nngroup.com/articles/ten-usability-heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) | **Yes** — say it is a heuristic, and cite the recognition-memory literature that makes it true |
| `UX-P36` | "Nielsen heuristic #1" — no year, no work | **NOT-ACADEMIC** + **MISSING** | Same two Nielsen sources; in 1990 the heuristic is "**Provide feedback**". The numbers a designer needs are Miller, R. B. (1968), AFIPS FJCC: 267–277 (0.1 s / 1 s / 10 s); Card, Robertson & Mackinlay (1991), CHI '91: 181–186; Myers, B. A. (1985), CHI '85: 11–17 | [10.1145/1476589.1476628](https://doi.org/10.1145/1476589.1476628) · [10.1145/317456.317459](https://doi.org/10.1145/317456.317459) | **Light** — claim is sound; supply the heuristic's work and the response-time bands |
| `UX-P37` | "Doherty threshold" — no author, no year, no work, **and a number** | **NOT-ACADEMIC** + **MISSING** + **IMPRECISE** | Doherty, W. J. & Thadhani, A. J. (1982), *The Economic Value of Rapid Response Time*, IBM technical report, form GE20-0752-0, November 1982, 12 pp. Peer-reviewed antecedents: Doherty & Kelisky (1979), *IBM Sys. J.* 18(1): 143–163; Thadhani (1981), *IBM Sys. J.* 20(4): 407–423 | [CHM 102751398](https://www.computerhistory.org/collections/catalog/102751398) · [10.1147/sj.181.0143](https://doi.org/10.1147/sj.181.0143) · [10.1147/sj.204.0407](https://doi.org/10.1147/sj.204.0407) | **Yes** — hardest in the family. **The document says "sub-second", never 400 ms**; it is not in the *IBM Systems Journal*; and Barber & Lucas 1983 finds errors rise at *both* extremes |
| `UX-P38` | "Nielsen heuristics #5, #3" — no year, no work | **NOT-ACADEMIC** + **MISSING** | Same two Nielsen sources; the entry's phrase "clearly marked exits" **is the 1990 wording verbatim**, so cite 1990. Academic substrate: Norman, D. A. (1981), *Psych. Review* 88(1): 1–15; Norman, D. A. (1983), *CACM* 26(4): 254–258; Reason, J. (1990), *Human Error* (CUP). "Roach motel" is Brignull's own 2010 coinage, retired in his taxonomy in favour of "Hard to Cancel" | [10.1145/2163.358092](https://doi.org/10.1145/2163.358092) · [deceptive.design/types/hard-to-cancel](https://www.deceptive.design/types/hard-to-cancel) | **Yes** — moderate. Supply Norman for "prevent the slip, don't message it", and note the pattern's current name |
| `UX-P39` | *nothing* — no author, no year, no work | **MISSING** | Term and origin: Camerer, C., Loewenstein, G. & Weber, M. (1989), *JPE* 97(5): 1232–1254 — term "suggested by Robin Hogarth" (their footnote 1). **But the entry's actual claim is a different finding**: Hinds, P. J. (1999), *JEP: Applied* 5(2): 205–221; review: Nickerson, R. S. (1999), *Psych. Bulletin* 125(6): 737–759; tappers/listeners: Newton, E. L. (1990), PhD dissertation, Stanford (**unpublished**) | [10.1086/261651](https://doi.org/10.1086/261651) · [10.1037/1076-898X.5.2.205](https://doi.org/10.1037/1076-898X.5.2.205) · [10.1037/0033-2909.125.6.737](https://doi.org/10.1037/0033-2909.125.6.737) | **Yes** — the only entry naming nobody, and its named origin is about **markets**, not expertise. Hinds 1999 is the entry's claim, tested |
| `UX-P40` | "Nielsen heuristic #4" — no year, no work | **NOT-ACADEMIC** + **MISSING** | Same two Nielsen sources; in 1990 "**Be consistent**". The entry's own ❌ caveat is a published position, not just ours: Grudin, J. (1989), *CACM* 32(10): 1164–1173, "The case against user interface consistency". Measurement: Ozok & Salvendy (2000), *Ergonomics* 43(4): 443–460 | [10.1145/67933.67934](https://doi.org/10.1145/67933.67934) · [10.1080/001401300184332](https://doi.org/10.1080/001401300184332) | **Yes** — light-to-moderate. Supply the heuristic's work, and cite Grudin for the caveat the entry already makes unattributed |

Verdict key: `CORRECT` — author, year and work introduced the effect.
`WRONG` — the attribution as written does not match the work.
`IMPRECISE` — real source, but the entry's claim outruns or misnames it.
`MISSING` — no attribution given. `NOT-ACADEMIC` — a heuristic or aphorism, no
empirical origin.

**Ethical guards — and a trap.** Status must be read against **`main`**, not
against this branch. `research/reference-verification` is based on `c975f21` and
does **not** contain `2b12304`, the commit that gave guards to `UX-P07`,
`UX-P10` and `UX-P12`. In this worktree `UX-P12` appears guardless; **on `main`
it has a guard**, and a rewrite working from the branch must not "fix" it.
Assessed against `main`:

| ID | Guard on `main`? | On the [#8](https://github.com/Storzen/skills/issues/8) non-compliant list? |
|---|---|---|
| `UX-P12` | ✅ via `2b12304` | no — resolved |
| `UX-P35` | ❌ | **yes** |
| `UX-P36` | ✅ | no |
| `UX-P37` | ❌ | **yes** |
| `UX-P38` | ✅ | no |
| `UX-P39` | ❌ | **yes** |
| `UX-P40` | ❌ | **yes** |

**#8's list is confirmed exactly** for this family: four owed, three compliant.
Nothing done here. One substantive note for whoever writes them, since #8's
resolution allows the literal value `No meaningful abuse vector — <reason>` and
its body floated `UX-P40` as a likely candidate: **`UX-P37` is not a candidate —
it has a real vector its own ❌ bullet already names** (optimistic UI reporting
success before the operation has succeeded), and there is a literature on exactly
that judgement call (Adar, Tan & Teevan 2013). `UX-P40` is a weaker candidate
than it looks, for the reason recorded in its evidence section below.

---

## Evidence

### UX-P12 — Peak-end rule

**Right family name, no year, no work, and three co-authors erased.** "Peak-end
rule (Kahneman)" names the correct researcher but none of the four papers, and
the first of them is not Kahneman's alone — Barbara Fredrickson is first author
of the paper that established the effect.

**The demonstration.** Fredrickson, B. L. & Kahneman, D. (1993), "Duration
neglect in retrospective evaluations of affective episodes", *Journal of
Personality and Social Psychology* 65(1): 45–55 —
[10.1037/0022-3514.65.1.45](https://doi.org/10.1037/0022-3514.65.1.45). Crossref
confirms both authors, year, volume, issue and pages; APA deposits no abstract.
This is the paper that proposes the **snapshot model**: retrospective evaluations
of affective episodes are predicted by the peak and end affect and are largely
insensitive to how long the episode lasted.

**The result everyone quotes, and it is about pain.** Kahneman, D., Fredrickson,
B. L., Schreiber, C. A. & Redelmeier, D. A. (1993), "When More Pain Is Preferred
to Less: Adding a Better End", *Psychological Science* 4(6): 401–405 —
[10.1111/j.1467-9280.1993.tb00589.x](https://doi.org/10.1111/j.1467-9280.1993.tb00589.x).
Crossref confirms all four authors, November 1993, volume 4, issue 6, pages
401–405, and deposits the abstract, quoted verbatim: *"Subjects were exposed to
two aversive experiences: in the short trial, they immersed one hand in water at
14 °C for 60 s; in the long trial, they immersed the other hand at 14 °C for 60
s, then kept the hand in the water 30 s longer as the temperature of the water
was gradually raised to 15 °C, still painful but distinctly less so for most
subjects. Subjects were later given a choice of which trial to repeat. A
significant majority chose to repeat the long trial, apparently preferring more
pain over less.
The results add to other evidence suggesting that duration plays
a small role in retrospective evaluations of **aversive** experiences; such
evaluations are **often** dominated by the discomfort at the worst and at the
final moments of episodes."* Two words in the authors' own summary are doing work
the entry drops: **aversive**, and **often**.

**The clinical field study.** Redelmeier, D. A. & Kahneman, D. (1996),
"Patients' memories of painful medical treatments: real-time and retrospective
evaluations of two minimally invasive procedures", *Pain* 66(1): 3–8 —
[10.1016/0304-3959(96)02994-6](https://doi.org/10.1016/0304-3959\(96\)02994-6).
Crossref confirms both authors, year, volume, issue and pages.

**The one intervention trial — and the entry should cite it, because it is the
only source that tests the entry's actual advice.** Redelmeier, D. A., Katz, J. &
Kahneman, D. (2003), "Memories of colonoscopy: a randomized trial", *Pain*
104(1): 187–194 —
[10.1016/S0304-3959(03)00003-4](https://doi.org/10.1016/S0304-3959\(03\)00003-4).
Crossref confirms all three authors, July 2003, volume 104, pages 187–194;
abstract read verbatim from PubMed (PMID 12855328). n = 682 consecutive
outpatients, randomised; half had *"a short interval added to the end of their
procedure during which the tip of the colonoscope remained in the rectum"*.
Result: the extended group *"experienced the final moments as less painful (1.7
vs. 2.5…, P<0.001), rated the entire experience as less unpleasant (4.4 vs.
4.9…, P=0.006)"*, and — the finding with the design consequence — *"Rates of
returning for a repeat colonoscopy (median duration of follow-up 5.3 years)
averaged 50.4% and were slightly higher (odds ratio=1.41, P=0.038) for those who
underwent the longer procedure"*. Deliberately engineering the end of an
experience changed *behaviour years later*, while the total quantity of
discomfort went **up**. That is simultaneously the best evidence for the entry's
advice and the exact justification for the ethical guard commit `2b12304` wrote
on `main` — this is a lever that edits memory rather than reality.

**Drift 1 — the entry generalises from pain to everything.** "❌ — applies to
almost any multi-moment journey" is the entry's own claim of universality. The
canonical evidence is cold-pressor trials, colonoscopies and unpleasant films.
Pleasant-domain evidence exists and is thinner: Do, A. M., Rupert, A. V. &
Wolford, G. (2008), "Evaluations of pleasurable experiences: The peak-end rule",
*Psychonomic Bulletin & Review* 15(1): 96–98 —
[10.3758/PBR.15.1.96](https://doi.org/10.3758/PBR.15.1.96) (Crossref confirms all
three authors, year, volume, issue and pages). One study, three pages. The
asymmetry should be stated, not smoothed over.

**Drift 2 — the rule underperforms over long, mixed episodes, which is what a
user journey is.** Kemp, S., Burt, C. D. B. & Furneaux, L. (2008), "A test of the
peak-end rule with extended autobiographical events", *Memory & Cognition* 36(1):
132–138 — [10.3758/MC.36.1.132](https://doi.org/10.3758/MC.36.1.132). Crossref
confirms all three authors, year, volume, issue and pages; abstract read verbatim
from PubMed (PMID 18323069): 49 students on ~7-day vacations reporting daily by
text, *"The duration of the vacation had no effect on the subsequent evaluations…
A number of summary measures provided reasonable prediction of the recalled
overall happiness of the vacation. **The peak-end rule was not an outstandingly
good predictor.** Overall, the results indicate much reconstruction of the
affective states."* Duration neglect held; the peak-end rule specifically did not
beat other summaries.

**Drift 3 — the *end* half has failed in a naturalistic emotional setting.**
Sels, L., Ceulemans, E. & Kuppens, P. (2019), "All's well that ends well? A test
of the peak-end rule in couples' conflict discussions", *European Journal of
Social Psychology* 49(4): 794–806 —
[10.1002/ejsp.2547](https://doi.org/10.1002/ejsp.2547) (Crossref confirms all
three authors, volume, issue and pages; online November 2018, volume year 2019 —
the `UX-P05` vintage lesson from the motivation audit applies). Abstract read
verbatim from Crossref: 101 couples, *"Our results showed that the negative and
positive peaks, **but not the end emotion**, predicted immediate and par[tly
delayed]…"* post-conflict affect. Peaks survived; the ending did not. For a
catalog entry whose entire operational advice is "invest in the last screen",
that is a load-bearing qualification.

**Drift 4 — "not its average" is the clause the meta-analysis does not support,
and this is second-hand.** Alaybek, B., Dalal, R. S., Fyffe, S., Aitken, J. A.,
Zhou, Y., Qu, X., Roman, A. & Baines, J. I. (2022), "All's well that ends (and
peaks) well? A meta-analysis of the peak-end rule and duration neglect",
*Organizational Behavior and Human Decision Processes* 170: 104149 —
[10.1016/j.obhdp.2022.104149](https://doi.org/10.1016/j.obhdp.2022.104149).
Crossref confirms all eight authors, May 2022, volume 170, article 104149, and
also a **corrigendum**: same authors, *OBHDP* 180: 104278 (2024) —
[10.1016/j.obhdp.2023.104278](https://doi.org/10.1016/j.obhdp.2023.104278).
**The article itself could not be read: ScienceDirect returns 403, Crossref
deposits no abstract, Semantic Scholar was unreachable.** Reported second-hand
from secondary summaries and marked as such: the peak-end effect on retrospective
evaluation is large (r ≈ 0.58) and the duration effect is essentially nil —
supporting duration neglect — **but the simple average of the experience predicts
retrospective evaluation about as well as the peak-end composite does.** If that
holds, the entry's headline sentence — "People judge an experience by its
emotional peak and its end, **not its average**" — is the strongest form of the
claim and the one the field's own meta-analysis declines to endorse.
Because
this is second-hand, the rewrite should either obtain the article or phrase the
qualification as "a 2022 meta-analysis reports…" rather than asserting it.
Whichever way, the entry's practical advice survives untouched: peaks and endings
carry disproportionate weight and are cheap to improve. It is only the *contrast
with the average* that should go.

### UX-P35 — Recognition over recall

**A heuristic, correctly numbered, with no year and no work — and a real
literature it never mentions.** Nielsen's heuristics are a practitioner
inspection method, not a study. The primary sources are his own:

- Nielsen, J. & Molich, R. (1990), "Heuristic evaluation of user interfaces",
  *CHI '90*: 249–256 — [10.1145/97243.97281](https://doi.org/10.1145/97243.97281).
  Crossref confirms both authors, 1990, pages 249–256, ACM Press. See also the
  journal statement of the same list: Molich, R. & Nielsen, J. (1990), "Improving
  a human-computer dialogue", *CACM* 33(3): 338–348 —
  [10.1145/77481.77486](https://doi.org/10.1145/77481.77486). **The 1990 list has
  nine heuristics and this one is called "Minimize user memory load".**
- Nielsen, J. (1994), "Enhancing the explanatory power of usability heuristics",
  *CHI '94*: 152–158 —
  [10.1145/191666.191729](https://doi.org/10.1145/191666.191729). Crossref
  confirms author, 24 April 1994, pages 152–158. This is the factor analysis of
  249 usability problems that produced the revised set of ten, and it is where
  the entry's wording and its **#6** actually come from.
- The numbered list as the catalog uses it is published at
  [nngroup.com/articles/ten-usability-heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/),
  Nielsen's own venue, first published 1994, **last updated 30 January 2024**,
  where he states the ten "have remained relevant and unchanged since 1994".
  The page's numbering was checked item by item against the catalog: `UX-P36` =
  #1, `UX-P38` = #5 and #3, `UX-P40` = #4, `UX-P35` = #6. **All four entries'
  heuristic numbers are correct.** This is the NN/g exception, applied on the
  same basis as `UX-P19` in the perception audit.

**What is missing is the science, which exists and is strong.** The heuristic is
true because of a well-replicated asymmetry in memory that the entry never cites:

- Shepard, R. N. (1967), "Recognition memory for words, sentences, and pictures",
  *Journal of Verbal Learning and Verbal Behavior* 6(1): 156–163 —
  [10.1016/S0022-5371(67)80067-7](https://doi.org/10.1016/S0022-5371\(67\)80067-7).
  Crossref confirms author, year, volume, issue and pages. Near-ceiling
  recognition for hundreds of items.
- Standing, L. (1973), "Learning 10,000 pictures", *Quarterly Journal of
  Experimental Psychology* 25(2): 207–222 —
  [10.1080/14640747308400340](https://doi.org/10.1080/14640747308400340).
  Crossref confirms author, May 1973, volume 25, issue 2, pages 207–222. The
  headline demonstration of how far recognition capacity extends.
- Anderson, J. R. & Bower, G. H. (1972), "Recognition and retrieval processes in
  free recall", *Psychological Review* 79(2): 97–123 —
  [10.1037/h0033773](https://doi.org/10.1037/h0033773). Crossref confirms both
  authors, March 1972, volume 79, issue 2, pages 97–123. The generate-recognise
  account that explains *why* a visible cue is cheaper than free recall — the
  entry's mechanism sentence, stated as theory.

**A small editorial note.** The entry's ❌ ("expert interfaces where recall is
faster for power users — offer both") is ours, and it is also, near enough,
Nielsen's **#7 flexibility and efficiency of use**. Attributing it would be more
honest than presenting it as a caveat we invented, and it flags that two of
Nielsen's ten heuristics are being carried in a single catalog entry.

### UX-P36 — Visibility of system status

**Correctly numbered heuristic, no year, no work — and the claim is sound.** The
primary sources are the three listed under `UX-P35`; in the 1990 nine-item list
this heuristic is "**Provide feedback**". Nothing in the entry's principle
sentence is wrong, and the ethical guard is one of the better ones in the
catalog.

**What the entry is missing is quantity.** "Timely" is not actionable, and the
numbers exist:

- Miller, R. B. (1968), "Response time in man-computer conversational
  transactions", *AFIPS Fall Joint Computer Conference*: 267–277 —
  [10.1145/1476589.1476628](https://doi.org/10.1145/1476589.1476628). Crossref
  confirms author, 1968, start page 267, ACM Press. The origin of the three
  thresholds every performance guideline since has restated — roughly 0.1 s for
  the feeling of instantaneous response, 1 s for uninterrupted flow of thought,
  10 s for holding attention at all.
  Note the connection to `UX-P37`: Miller is
  also the psychologist Doherty & Thadhani name in their own opening as the
  source of the two-second standard they set out to overturn.
- Card, S. K., Robertson, G. G. & Mackinlay, J. D. (1991), "The information
  visualizer, an information workspace", *CHI '91*: 181–186 —
  [10.1145/108844.108874](https://doi.org/10.1145/108844.108874). Crossref
  confirms all three authors and pages. The restatement of Miller's bands in
  terms of human information-processing timescales, and the version most
  performance work cites today.
- Myers, B. A. (1985), "The importance of percent-done progress indicators for
  computer-human interfaces", *CHI '85*: 11–17 —
  [10.1145/317456.317459](https://doi.org/10.1145/317456.317459). Crossref
  confirms author, 1985, pages 11–17. The experimental warrant for the entry's
  "progress" advice specifically, as opposed to feedback in general.

**The guard is stricter than the literature, and that is a deliberate position
worth marking.** The entry says status "must be truthful", full stop. There is a
research literature arguing the opposite in bounded cases: Adar, E., Tan, D. S. &
Teevan, J. (2013), "Benevolent deception in human computer interaction", *CHI
'13*: 1863–1872 —
[10.1145/2470654.2466246](https://doi.org/10.1145/2470654.2466246) (Crossref
confirms all three authors and pages), which catalogues deceptions users benefit
from, progress indicators among them. Our guard does not merely go beyond its
source, it **contradicts a published position** — and it should, in a catalog
whose examples are money transfers. But the rewrite should know the position
exists rather than discover it from a reviewer.

### UX-P37 — Doherty threshold

**The hardest entry in the family, and the only one where a specific number is at
stake.** The entry gives no author, no year and no work, and asserts "~400 ms"
twice. The document it descends from was read in full.

**The primary document.** Doherty, W. J. & Thadhani, A. J. (1982), *The Economic
Value of Rapid Response Time*, IBM, November 1982 — IBM form **GE20-0752-0**,
catalogued by the Computer History Museum as a 12-page technical report,
accession X6915.2014, catalog number
[102751398](https://www.computerhistory.org/collections/catalog/102751398). **It
is a technical report, not a journal article**, and specifically it is *not* in
the *IBM Systems Journal* — the claim repeated by lawsofux and every blog
downstream of it. IBM's own hosted copy is dead; the text was read from the
republication IBM authorised, carrying `© Copyright IBM Corporation 1982, 1997.
All rights reserved. Published here with permission.`

**What the document actually says, verbatim.** Its thesis sentence is the one
lawsofux quotes, and it is quoted correctly: *"When a computer and its users
interact at a pace that ensures that neither has to wait on the other,
productivity soars, the cost of the work done on the computer tumbles, employees
get more satisfaction from their work, and its quality tends to improve."* Its
empirical core is Thadhani's curve: *"with system response of three seconds,
Thadhani found that a programmer executes about 180 transactions per hour. But,
bring system response time down to 0.3 seconds and the number of transactions the
programmer can execute in an hour jumps to 371, an increase of 106 percent. Put
another way, a reduction of 2.7 seconds in system response saves 10.3 seconds of
the user's time."* Its conclusion: *"Rapid system response time, ultimately
reaching **sub-second** values and implemented with adequate system support,
offers the promise of substantial improvements in user productivity."*

**And what it does not say.** In the full text: the string 400 occurs **once**,
in "The number of simultaneous users had grown to almost 400" — NIH terminal
users, not milliseconds. The word "millisecond" occurs **zero** times. The word
"addicting" occurs zero times. **No threshold is named anywhere in the
document**, and no quantity is proposed other than "sub-second" and the tabulated
points 3.0 / 2.0 / 1.0 / 0.6 / 0.3 seconds. There is no Doherty threshold in
Doherty.

**Where 400 ms comes from.** Not from the document, and not from the academic
literature: a Crossref bibliographic search returns **no work using "Doherty
threshold" as a term**. The earliest traceable statement of the number attached
to the name that this audit found is a practitioner blog post — Dave Rupert, "The
Economic Value of Rapid Response Time", 15 June 2015,
[daverupert.com/2015/06/doherty-threshold](https://daverupert.com/2015/06/doherty-threshold/)
— which asserts that "a sub-400 millisecond response time creates a dramatic
increase in users' interactions at all different skill levels", below which "an
activity is addicting".
The number is then entrenched by
[lawsofux.com/doherty-threshold](https://lawsofux.com/doherty-threshold/), whose
definition reads "Productivity soars when a computer and its users interact at a
pace (<400ms)…" — the parenthesis is the interpolation — and **whose own source
list cites Jim Elliott's reproduction of the 1982 brief**, i.e. the document that
contains neither the number nor the word "millisecond". Neither of these is
recorded here as a citation; they are recorded as the *provenance of the number*,
which is the honest thing the entry owes its reader. Jon Yablonski's *Laws of UX*
(O'Reilly, 2020) is where the name became canon in UX; it is a trade book, on the
`UX-P34` pattern.

**The citable antecedents, which are real and peer-reviewed-adjacent.** Both are
in the *IBM Systems Journal* and both are the actual research the 1982 brief
summarises:

- Doherty, W. J. & Kelisky, R. P. (1979), "Managing VM/CMS systems for user
  effectiveness", *IBM Systems Journal* 18(1): 143–163 —
  [10.1147/sj.181.0143](https://doi.org/10.1147/sj.181.0143). Crossref confirms
  both authors, 1979, volume 18, issue 1, pages 143–163, publisher IBM. The 1982
  brief quotes it verbatim for the mechanism the entry's "stay in flow" clause
  descends from: *"…each second of system response degradation leads to a similar
  degradation added to the user's time for the following [command]. This
  phenomenon seems to be related to an individual's attention span… Increases in
  SRT seem to disrupt the thought processes, and this may result in having to
  rethink the sequence of actions to be continued."* **This, not a threshold, is
  the citable claim.**
- Thadhani, A. J. (1981), "Interactive user productivity", *IBM Systems Journal*
  20(4): 407–423 — [10.1147/sj.204.0407](https://doi.org/10.1147/sj.204.0407).
  Crossref confirms author, 1981, volume 20, issue 4, pages 407–423. The source
  of the transactions-per-hour curve.

**A bibliographic caution the rewrite should not trip over.** The second author's
name is spelled three ways in three places: **"Ahrvind J. Thadani"** in the 1982
brief's own header note, **"Arvind J. Thadhani"** in the same document's body,
and **"Thadhani, A. J."** in Crossref's record of the 1981 journal article. Use
Thadhani and note the variant, or a reader searching for Thadani will conclude
the citation is invented.

**Contested evidence the entry ignores.** The entry implies response time is
monotonic — faster is always better. Barber, R. E. & Lucas, H. C. (1983), "System
response time operator productivity, and job satisfaction", *CACM* 26(11):
972–986 — [10.1145/182.358464](https://doi.org/10.1145/182.358464) (Crossref
confirms both authors, November 1983, volume 26, issue 11, pages 972–986) is the
standard counterweight: operator **error rates rise at both very slow and very
fast response times**, so a system that answers instantly is not automatically
better for accuracy. In a family whose examples are money transfers, that is not
a footnote. Note that Miller 1968 and Card et al. 1991 (cited under `UX-P36`) are
both better founded than the 400 ms, and one of them is **fourteen years older**
than the document the entry credits.

**What the entry can honestly keep.** Everything except the number's provenance.
Sub-second response, immediate acknowledgement, optimistic UI and skeletons are
all defensible; the ❌ bullet warning against faking completion is exactly right
and cross-references `UX-P36` correctly. The defect is that "~400 ms" is
presented as a measured threshold from a named source, and it is neither.

### UX-P38 — Error prevention & forgiveness

**Correctly numbered heuristics, no year, no work — and one detail in the entry's
favour.** The entry's phrase "**Users need clearly marked exits**" is not a
paraphrase: "Provide clearly marked exits" is the verbatim wording of the
corresponding heuristic in the **1990** nine-item list (Molich & Nielsen 1990;
Nielsen & Molich 1990), before it was renamed "User control and freedom" in 1994.
Whoever wrote the entry was reading the older formulation, and the citation
should say 1990 rather than being left blank.

**The academic substrate, which the entry lacks entirely.** "Stopping a mistake
beats a good error message" is not Nielsen's insight; it is Norman's, and it has
a theory behind it:

- Norman, D. A. (1981), "Categorization of action slips", *Psychological Review*
  88(1): 1–15 —
  [10.1037/0033-295X.88.1.1](https://doi.org/10.1037/0033-295X.88.1.1). Crossref
  confirms author, January 1981, volume 88, issue 1, pages 1–15. The taxonomy of
  slips — errors of execution rather than of intention — which is what a
  constraint prevents and what an error message cannot undo.
- Norman, D. A. (1983), "Design rules based on analyses of human error", *CACM*
  26(4): 254–258 — [10.1145/2163.358092](https://doi.org/10.1145/2163.358092).
  Crossref confirms author, April 1983, volume 26, issue 4, pages 254–258. This
  is the paper that turns the taxonomy into the design rules the entry states:
  make errors physically hard to commit, make actions reversible, make the
  irreversible ones difficult to reach. **It is the correct origin citation for
  `UX-P38`, and it predates the Nielsen heuristics by seven years.**
- Reason, J. (1990), *Human Error*, Cambridge University Press — the canonical
  monograph on the slips/mistakes/violations distinction. `source type: book
  (academic)`; no DOI, which is normal and not a defect.

**"Roach motel" is a practitioner coinage and its name has since changed.** The
guard uses the term without attribution. Per Brignull's own taxonomy at
[deceptive.design/types/hard-to-cancel](https://www.deceptive.design/types/hard-to-cancel),
the pattern is now catalogued as "**Hard to Cancel**", with "Roach Motel"
recorded as the earlier name **coined by Brignull himself in 2010**. This is the
same exception the persuasion audit applied to confirmshaming: a practitioner's
own catalogue is primary for the term he catalogued. The difference is worth
recording — for confirmshaming the catalogue disclaims authorship; here it claims
it. The rewrite should keep "roach motel" only if it also gives the current name,
or a reader searching the taxonomy will not find it.

**No drift.** The claim as stated is what the sources support. This entry is the
best-founded of the four Nielsen entries; its defect is purely that it names none
of its sources.

### UX-P39 — Curse of knowledge

**The only entry in the family that names nobody at all — and the origin it
should name is about something else.** No author, no year, no work: `MISSING`
without qualification.

**The term, read primary.** Camerer, C., Loewenstein, G. & Weber, M. (1989), "The
Curse of Knowledge in Economic Settings: An Experimental Analysis", *Journal of
Political Economy* 97(5): 1232–1254 —
[10.1086/261651](https://doi.org/10.1086/261651). Crossref confirms all three
authors, October 1989, volume 97, issue 5, pages 1232–1254, University of Chicago
Press. **Read in full from George Loewenstein's own PDF at CMU.**
Abstract,
verbatim: *"In economic analyses of asymmetric information, better-informed
agents are assumed capable of reproducing the judgments of less-informed agents.
We discuss a systematic violation of this assumption that we call the 'curse of
knowledge.' Better-informed agents are unable to ignore private information even
when it is in their interest to do so; more information is not always better.
Comparing judgments made in individual-level and market experiments, we find that
market forces reduce the curse by approximately 50 percent but do not eliminate
it."* And the coinage, from the paper's own footnote 1, verbatim: **"This term
was suggested by Robin Hogarth."** The rewrite should credit Camerer, Loewenstein
& Weber 1989 for the term and, if it wants to be exact, Hogarth for the phrase.

**The drift, and it is a real one.** Camerer et al. ran market experiments in
which better-informed subjects predicted less-informed subjects' earnings
forecasts. The finding is about **asymmetric information and its market
consequences** — the paper's own examples are lemons, bid-ask spreads and wages.
It is not about experts and jargon, and it does not test whether specialists
write unusable help text. The entry's claim — "experts forget what novices don't
know; design and write for someone seeing the product for the first time" — is
also true, and also has sources, but they are different ones:

- **The entry's claim, tested.** Hinds, P. J. (1999), "The curse of expertise:
  The effects of expertise and debiasing methods on prediction of novice
  performance", *Journal of Experimental Psychology: Applied* 5(2): 205–221 —
  [10.1037/1076-898X.5.2.205](https://doi.org/10.1037/1076-898X.5.2.205).
  Crossref confirms author, June 1999, volume 5, issue 2, pages 205–221. Experts
  systematically underestimate how long a task takes a novice, and the paper also
  tests **debiasing methods** — which is precisely what the entry's advice is.
  This is the single best citation for `UX-P39` and it is absent.
- **The general review.** Nickerson, R. S. (1999), "How we know — and sometimes
  misjudge — what others know: Imputing one's own knowledge to others",
  *Psychological Bulletin* 125(6): 737–759 —
  [10.1037/0033-2909.125.6.737](https://doi.org/10.1037/0033-2909.125.6.737).
  Crossref confirms author, November 1999, volume 125, issue 6, pages 737–759.
- **The parent bias, which Camerer et al. cite as their own prior evidence.**
  Fischhoff, B. (1975), "Hindsight is not equal to foresight: The effect of
  outcome knowledge on judgment under uncertainty", *JEP: Human Perception and
  Performance* 1(3): 288–299 —
  [10.1037/0096-1523.1.3.288](https://doi.org/10.1037/0096-1523.1.3.288).
  Crossref confirms author, August 1975, volume 1, issue 3, pages 288–299.
- **The developmental form.** Birch, S. A. J. & Bloom, P. (2007), "The curse of
  knowledge in reasoning about false beliefs", *Psychological Science* 18(5):
  382–386 —
  [10.1111/j.1467-9280.2007.01909.x](https://doi.org/10.1111/j.1467-9280.2007.01909.x).
  Crossref confirms both authors, May 2007, volume 18, issue 5, pages 382–386.

**The famous study behind the UX version — read primary, and the popular numbers
are wrong.** Newton, E. L. (1990), *The rocky road from actions to intentions*,
PhD dissertation, Stanford University — the tappers-and-listeners experiment.
**Read in full from the ProQuest scan.** From the dissertation's own Results and
Table 1, verbatim: *"When asked to estimate the likelihood that their listeners
correctly guessed the name of the tune that they had just tapped, subjects'
guesses averaged 50%, and ranged from 10 to 95. Similarly, when asked to estimate
what percentage of an audience of 100 listeners would be able to name the tune if
they heard the tapping amplified in a recital hall, subjects mean estimate was
51%, with a range from 8 to 95. In reality, however, there were only 3 hits in
120 tries, a success rate of only 2.5 percent — a rate that was outside the
entire range of the tapper's estimates."* Table 1 note: *"N = 40 tappers, 40
listeners, 120 songs."*
**The widely repeated "2 out of 150" and "3 out of 150"
figures do not match Study 1's table**, which gives 3/120 (a separate figure
later in the dissertation gives 3 of 150 for a different comparison). Two
cautions for the rewrite: it is an **unpublished dissertation**, not a
peer-reviewed article, and the number should be quoted as 3 of 120 (2.5%) with
tapper predictions of ~50%.

**The popularizer to name and not cite.** The route by which "curse of knowledge"
and the tapping study reached UX is Heath, C. & Heath, D. (2007), *Made to Stick*
(Random House) — a trade book. It is why the term is in the catalog at all, and
it should not be the citation.

### UX-P40 — Consistency & standards

**Correctly numbered heuristic, no year, no work — and a caveat that is more
citable than the principle.** In the 1990 nine-item list the heuristic is "**Be
consistent**"; the wording "consistency and standards" and the **#4** are from
Nielsen 1994. The cross-reference to `UX-P19` (Jakob's law, external convention)
is correct, and it is the catalog's only acknowledgement that these two entries
come from the same author.

**The entry's ❌ is a published position, not our invention.** "When rigid
consistency would keep a known-bad pattern — consistency serves usability, it
isn't the goal itself" restates, unattributed, one of the better-known arguments
in HCI: Grudin, J. (1989), "The case against user interface consistency", *CACM*
32(10): 1164–1173 — [10.1145/67933.67934](https://doi.org/10.1145/67933.67934).
Crossref confirms author, October 1989, volume 32, issue 10, pages 1164–1173.
Grudin's argument is that consistency is not a primitive design goal, that
"consistent with what?" has several incompatible answers (internal, external,
with the user's task), and that consistency pursued for itself can degrade
usability. Citing it converts our caveat into a thirty-five-year-old debate the
reader can check, and it pairs naturally with the Nielsen citation because the
two are the two sides of the same argument. See also the volume that framed the
debate: Nielsen, J. (ed.) (1989), *Coordinating User Interfaces for Consistency*
(Academic Press).

**Measurement, if the entry wants any.** Ozok, A. A. & Salvendy, G. (2000),
"Measuring consistency of web page design and its effects on performance and
satisfaction", *Ergonomics* 43(4): 443–460 —
[10.1080/001401300184332](https://doi.org/10.1080/001401300184332). Crossref
confirms both authors, April 2000, volume 43, issue 4, pages 443–460. Follow-up:
Ozok & Salvendy (2001), *Behaviour & Information Technology* 20(6): 433–447 —
[10.1080/01449290110092260](https://doi.org/10.1080/01449290110092260). These are
the closest thing to an experimental test of the entry's claim, and they are
worth a line, because the entry is otherwise the least evidenced in the family.

**On the guard #8 still owes this entry.** #8's resolution nominated `UX-P40` as
a likely home for the literal value `No meaningful abuse vector`. That is
defensible but not obvious: an interface that is *visibly* consistent while one
instance behaves differently weaponises exactly the expectation this heuristic
builds — the user stops reading because everything so far meant the same thing.
That mechanism is documented in the dark-pattern taxonomies: Gray, C. M., Kou,
Y., Battles, B., Hoggatt, J. & Toombs, A. L. (2018), "The Dark (Patterns) Side of
UX Design", *CHI '18*: 1–14 —
[10.1145/3173574.3174108](https://doi.org/10.1145/3173574.3174108); Crossref
confirms all five authors and pages. Recorded for #7 and #8, not decided here.

---

## IDs whose claim text needs rewording

All seven, in descending order of how wrong the current text is:

1. **`UX-P37`** — the family's hardest rewrite, and the only factual error in it.
   **Drop "~400 ms" or attribute it honestly as a practitioner number.** The
   document it is credited to argues for **sub-second** response and contains
   neither the figure nor the word "millisecond"; it is an IBM technical report
   (form GE20-0752-0, November 1982, CHM 102751398), **not** an *IBM Systems
   Journal* paper. Cite the brief for the thesis sentence, and cite Doherty &
   Kelisky 1979 for the attention-span mechanism and Thadhani 1981 for the
   productivity curve — those are the real, resolvable sources. If a number is
   wanted, use Miller 1968's 0.1 / 1 / 10 s bands (via Card et al. 1991), and
   record Barber & Lucas 1983's finding that errors rise at both extremes, which
   contradicts the entry's implied monotonicity. Spell the second author
   Thadhani and note the variants.
2. **`UX-P12`** — supply the four papers (Fredrickson & Kahneman 1993; Kahneman
   et al. 1993; Redelmeier & Kahneman 1996; **Redelmeier, Katz & Kahneman 2003**,
   the randomised trial that is the only test of the entry's actual advice) and
   stop crediting Kahneman alone. Then soften two things: the evidence base is
   **aversive** episodes, not journeys in general (Do et al. 2008 is the thin
   pleasant-domain case); and **delete or qualify "not its average"**, the one
   clause the 2022 meta-analysis reportedly does not support — flagging that this
   qualification is second-hand. Record that the rule underperformed over
   week-long vacations (Kemp et al. 2008, verbatim: "not an outstandingly good
   predictor") and that the *end* half failed in couples' conflicts (Sels et al.
   2019). The guard on `main` stays as it is; Redelmeier 2003's return-rate
   result (odds ratio 1.41) is its evidential warrant and could be named in it.
3. **`UX-P39`** — the entry names nobody. Supply Camerer, Loewenstein & Weber
   1989 for the **term** (crediting Hogarth for the phrase), and say plainly that
   their experiments are about asymmetric information in markets. Then supply the
   sources for what the entry actually claims: **Hinds 1999** (the curse of
   expertise, with debiasing), Nickerson 1999, Fischhoff 1975, Birch & Bloom
   2007. Newton 1990 may be used for the tapping study if it is marked as an
   unpublished dissertation and quoted correctly — **3 hits in 120, 2.5%, against
   tapper predictions of ~50%**, not the "2 of 150" of the popular retelling.
   Name *Made to Stick* as the popularizer, not as the source.
4. **`UX-P35`** — say plainly it is Nielsen's heuristic #6, cite Nielsen & Molich
   1990 (where it is "minimize user memory load") and Nielsen 1994 (where the
   current wording and numbering originate), then cite the memory literature that
   makes it true: Shepard 1967, Standing 1973, Anderson & Bower 1972. Note that
   the ❌ bullet is essentially Nielsen's #7.
5. **`UX-P40`** — supply the heuristic's work as above, and **attribute the ❌ to
   Grudin 1989**, which argues precisely that consistency is not a primitive
   goal. Bring in Ozok & Salvendy 2000 if the entry wants any measurement. Keep
   the `UX-P19` cross-reference and strengthen it to say both descend from
   Nielsen.
6. **`UX-P38`** — cite the **1990** list, since "clearly marked exits" is its
   verbatim wording, and supply **Norman 1983** (with Norman 1981 and Reason
   1990) as the real origin of "prevent the slip rather than message it" and of
   reversibility as a design rule. Give "roach motel" its attribution — Brignull,
   2010 — and its current name in the taxonomy, "Hard to Cancel".
7. **`UX-P36`** — lightest. Supply the heuristic's work, bring in Miller 1968's
   thresholds (via Card et al. 1991) so "timely" becomes a number, and Myers 1985
   for progress indicators specifically. Mark the guard as deliberately stricter
   than — in fact contrary to — the benevolent-deception literature (Adar et al.
   2013), rather than leaving that collision undiscovered.

Four of these seven also owe an `Ethical guard` under
[#8](https://github.com/Storzen/skills/issues/8) — `UX-P35`, `UX-P37`, `UX-P39`,
`UX-P40`, exactly as listed there. **`UX-P12` does not**: it received one in
commit `2b12304` on `main`, which this branch does not contain. Not this ticket's
business; flagged so the rewrite neither loses the four nor duplicates the one.

## Findings for the v2 entry template (#7)

The trust family **confirms all seven** fields established so far, supplies new
values for four of them, and demands **one new field** that only a family
carrying a quantity could have surfaced.

- **Source standing** (`replicated` / `contested` / `not-academic` /
  `popularization` / `replication-mixed`) — confirmed, and `not-academic` is
  finally the *majority* value in a family: five of seven. But the value is doing
  too much work as a single flag. `UX-P35`, `UX-P36`, `UX-P38` and `UX-P40` are
  heuristics **with a solid independent literature underneath** (Shepard and
  Standing, Miller, Norman, Ozok & Salvendy); `UX-P37` is a heuristic **with a
  corporate sales brief underneath and a number nobody can source**. Those are
  not the same epistemic object and the template cannot currently tell them
  apart. Proposed refinement: `not-academic` should be paired with the standing
  of its *warrant*, not only of its origin.
  `UX-P12` also supplies a variant of persuasion's `replication-mixed`: the
  effect is robust, but one **component** of it (the end) failed in a
  naturalistic test while the other (the peak) held — **partial-component
  failure**, which is finer grained than "mixed".
- **Origin citation separated from mechanism citation** — confirmed, and this
  family needs it in **six of seven** entries, in a shape neither previous family
  produced: *heuristic origin* versus *empirical warrant*. `UX-P35` (Nielsen
  1990/94 heuristic / Shepard 1967 and Standing 1973 evidence), `UX-P36` (Nielsen
  / Miller 1968 and Myers 1985), `UX-P38` (Nielsen / Norman 1983 — where the
  warrant is **seven years older** than the heuristic), `UX-P40` (Nielsen /
  Grudin 1989 and Ozok & Salvendy 2000), `UX-P37` (IBM brief / Doherty & Kelisky
  1979 and Thadhani 1981), `UX-P39` (Camerer 1989 for the *term* / Hinds 1999 for
  the *claim*). `UX-P39` is the cleanest argument yet for making both slots
  required: its term and its claim come from different literatures in different
  disciplines.
- **`source type`** — confirmed, and trust adds **two values nothing in the
  catalog can currently express**: `corporate technical report` (Doherty &
  Thadhani 1982 — no DOI, no peer review, no publisher page, catalogued only by a
  museum, and its own web home is dead) and `unpublished dissertation` (Newton
  1990). Both are legitimate primary sources and both need to be visibly *not*
  peer reviewed. Also confirmed from persuasion: `trade book` (Yablonski 2020;
  Heath & Heath 2007) and `book (academic)` (Reason 1990, no DOI, which is
  normal). And a value the perception audit's `practitioner article` nearly
  covers but should be split: NN/g's heuristics page is a **living document**,
  last updated 30 January 2024 for a 1994 list — the template should record the
  *access date* for sources that can change under it.
- **`guard divergence`** — confirmed, and trust supplies a **fourth value** after
  `stricter than source`, `independent of source` and `supported by source`:
  **`contradicts source`**. `UX-P36`'s "status must be truthful, full stop" is
  not merely stricter than its literature — Adar, Tan & Teevan 2013 argues the
  opposite case in print. A guard that overrides a published position should say
  so, both because it is honest and because it is a stronger guard once the
  reader knows it was a decision. `UX-P12` meanwhile is the strongest instance of
  persuasion's `supported by source` yet found: Redelmeier et al. 2003 shows the
  lever changes behaviour years later while total suffering rises, which is
  exactly what the guard forbids.
- **`vintage` / `superseded by`** — confirmed, and inverted a second time.
  Perception found old origin, then a modern review to read instead; persuasion
  found old origin, then a modern meta-analysis that **changes the advice**.
  Trust finds `UX-P37`: a 1982 origin whose best replacement references are
  **older than it** (Miller 1968) and whose modern popular reference (lawsofux,
  Yablonski 2020) is a **degradation** — it supplied a number the origin does not
  contain. The field must be able to say "the canonical modern reference is
  *worse* than the origin", not only "read this instead".
- **Editorial-stance marker** — confirmed, with the same wrinkle persuasion
  found, now on a second instance, which is enough to promote it from wrinkle to
  requirement. `UX-P40`'s ❌ reads as our editorial caution and is in fact
  **Grudin 1989's published thesis**; `UX-P35`'s ❌ is ours and is also nearly
  Nielsen's own #7. A stance can be (a) ours alone, (b) ours and independently
  supported, or (c) not ours at all but an uncredited restatement of someone's
  argument. The catalog renders all three identically, and (c) is a citation
  defect wearing the costume of an opinion.
- **`adjacent-principle collision`** — confirmed, and extended with a kind
  persuasion could not see, because its entries all shared one *synthesiser* but
  had different *origins*. Trust has the mirror case: **same-source collision**.
  Five entries across two families — `UX-P19`, `UX-P35`, `UX-P36`, `UX-P38`,
  `UX-P40` — are all items from **one list by one author**, and the catalog never
  says so; a reader meets "Jakob's law" in perception and four numbered
  "heuristics" in trust without learning they are the same body of work with the
  same evidentiary status. There are also two intra-family collisions the entries
  already half-acknowledge and should make explicit: `UX-P37` against `UX-P36`
  (each entry's ❌ points at the other — responsiveness must not become a lie
  about the result) and `UX-P38` against `UX-P12` (a forgiving undo *is* an
  investment in the end of a failure journey).

**One new field this family demands:**

- **`figure provenance`** — every *number* in an entry carries its own source,
  recorded separately from the principle's source. `UX-P37` is the proof: the
  principle has a traceable origin (an IBM brief, an attention-span observation
  in a 1979 journal article) while its number — the only thing in the entry a
  developer will actually implement against — has **no primary warrant at all**
  and traces to a 2015 blog post. The two provenances are independent, and the
  current template merges them, which is precisely how "~400 ms" survived into a
  public catalog with a straight face. This is not `source standing` (the
  principle's standing is fine), not `origin vs mechanism` (the number is
  neither), and not `vintage` (nothing superseded it — it was never sourced).
  #7's own body already lists "quantified thresholds — Doherty at 400 ms, Hick's
  formula, Miller's contested 7±2" as a candidate addition; this audit's finding
  is that the field must carry a **citation per figure**, not just the figure,
  because two of those three named examples are exactly the cases where the
  number and the principle have different — or missing — sources.
