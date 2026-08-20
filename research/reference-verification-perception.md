# Reference verification — perception family (UX-P09, P10, P18, P19, P20, P21, P22, P23, P24)

Resolves [#11](https://github.com/Storzen/skills/issues/11). Re-slice of [#4](https://github.com/Storzen/skills/issues/4), perception family only — 9 entries.

**Method.** Every DOI below was resolved against the Crossref metadata API
(`api.crossref.org/works/<doi>`) and its author list, year, journal, volume and
pages checked against the citation as written in `PRINCIPLES-perception.md`.
Sources Crossref cannot settle were verified otherwise: Fitts 1954 was read in
full text from the scanned original (the paper's task descriptions carry three of
this audit's findings); Wertheimer 1923 was read in the Ellis (1938) translation
hosted by *Classics in the History of Psychology*; Ebbinghaus 1885 was verified
against the Ruger & Bussenius (1913) translation at the same archive; Jakob's
law was verified at Nielsen's own publication venue; two abstracts blocked at the
publisher (Palmer 1992, Hunt 1995) were read verbatim from the PubMed record.
Lawsofux, Wikipedia and Medium were used as leads only; none is recorded as a
citation. **NN/g is an exception in this family and only in `UX-P19`** — there it
is not a secondary write-up but Jakob Nielsen's own publication of his own law,
i.e. the primary source.

**Headline.** This is the worst-attributed family of the three. **Six of nine
entries name no author and no year at all** — the four Gestalt entries plus
Fitts and Jakob — and a seventh names an author with no year. Nothing is
fabricated, and no attribution that *exists* is false; but two of the family's
load-bearing claims are the popular UX reading rather than the finding.
`UX-P10` asserts the very mechanism — perceptual salience — that von Restorff's
own data were designed to rule out, and `UX-P23` sits under a "Gestalt" heading
for a principle that was not published until **1992**, sixty-nine years after the
canon the other three entries belong to. `UX-P18` is the family's most contested
claim and reads as settled.

---

## Verdict table

| ID | Cited as | Verdict | Corrected / supplied attribution | Canonical link | Reword? |
|---|---|---|---|---|---|
| `UX-P09` | "Fitts's law" — no author, no year | **MISSING** + **IMPRECISE** | Fitts, P. M. (1954), *JEP* 47(6): 381–391. HCI form and Shannon formulation: MacKenzie 1992. Finger touch needs Bi, Li & Zhai 2013 | [10.1037/h0055392](https://doi.org/10.1037/h0055392) · [10.1207/s15327051hci0701_3](https://doi.org/10.1207/s15327051hci0701_3) | **Yes** — the relation is **logarithmic**, not "scales with distance"; the destructive-actions half is our stance, not Fitts |
| `UX-P10` | von Restorff, 1933 | **CORRECT** (attribution) | — ; full cite is *Psychologische Forschung* 18(1): 299–342, part I of a series completed by Köhler & von Restorff **1937** | [10.1007/BF02409636](https://doi.org/10.1007/BF02409636) · [10.3758/BF03214414](https://doi.org/10.3758/BF03214414) | **Yes** — von Restorff showed perceptual salience is **not** necessary; the effect is *recall*, not action |
| `UX-P18` | Kurosu & Kashimura, 1995 | **CORRECT** (attribution) | — ; the *name* is Lidwell, Holden & Butler 2003, not the 1995 authors. Replications: Tractinsky 1997; Tractinsky, Katz & Ikar 2000 | [10.1145/223355.223680](https://doi.org/10.1145/223355.223680) · [10.1016/S0953-5438(00)00031-X](https://doi.org/10.1016/S0953-5438\(00\)00031-X) | **Yes** — most contested claim in the family: reversed by Tuch 2012, largely a fluency confound (Preßler 2023) |
| `UX-P19` | "Jakob's law (Nielsen)" — no year, no work | **NOT-ACADEMIC** + **MISSING** | Nielsen, J. (2000), "End of Web Design", NN/g Alertbox, 22 July 2000 — a practitioner heuristic, no study. Empirical backing sits elsewhere: Roth et al. 2010; Tuch et al. 2012 | [nngroup.com/articles/end-of-web-design](https://www.nngroup.com/articles/end-of-web-design/) · [10.1016/j.intcom.2009.10.004](https://doi.org/10.1016/j.intcom.2009.10.004) | **Yes** — say plainly it is Nielsen's heuristic, and cite the studies that actually measure convention |
| `UX-P20` | Ebbinghaus (no year); Murdock, 1962 | **IMPRECISE** + **MISSING** (Ebbinghaus year) | Ebbinghaus 1885 (trans. Ruger & Bussenius 1913); Murdock 1962 correct. Precedence: Nipher 1878, recovered by Stigler 1978 | [10.1037/h0045106](https://doi.org/10.1037/h0045106) · [psychclassics — Ebbinghaus](https://psychclassics.yorku.ca/Ebbinghaus/index.htm) | **Yes** — a *free-recall* effect; recency dies under a filled delay (Glanzer & Cunitz 1966) and nav items are never recalled |
| `UX-P21` | "Gestalt principle of proximity" — no author, no year | **MISSING** | Wertheimer, M. (1923), *Psychologische Forschung* 4(1): 301–350. Quantitative model: Kubovy & Wagemans 1995 | [10.1007/BF00410640](https://doi.org/10.1007/BF00410640) · [Ellis 1938 translation](https://psychclassics.yorku.ca/Wertheimer/Forms/forms.htm) | **Yes** — attribution only; the claim itself is sound |
| `UX-P22` | "Gestalt principle of similarity" — no author, no year | **MISSING** | Wertheimer, M. (1923), same paper. Modern review: Wagemans et al. 2012 | [10.1007/BF00410640](https://doi.org/10.1007/BF00410640) · [10.1037/a0029333](https://doi.org/10.1037/a0029333) | **Yes** — attribution only; the claim itself is sound |
| `UX-P23` | "Gestalt principle of common region" — no author, no year | **MISSING** (and **WRONG** if resolved to the 1923 canon) | Palmer, S. E. (**1992**), *Cognitive Psychology* 24(3): 436–447 — **not** in Wertheimer 1923. Sibling principle: Palmer & Rock 1994 | [10.1016/0010-0285(92)90014-S](https://doi.org/10.1016/0010-0285\(92\)90014-S) | **Yes** — the claim is right and Palmer proves it; the *date* is the defect |
| `UX-P24` | "Law of Prägnanz and closure (Gestalt)" — no author, no year | **MISSING** + **IMPRECISE** | Wertheimer 1923 (closure, as one factor among nine); Koffka 1935 (canonical Prägnanz formulation); Hochberg & McAlister 1953 (the simplicity/minimum principle) | [10.1007/BF00410640](https://doi.org/10.1007/BF00410640) · [10.3758/s13423-023-02344-9](https://doi.org/10.3758/s13423-023-02344-9) | **Yes** — three distinct things are conflated in one heading |

Verdict key: `CORRECT` — author, year and work introduced the effect.
`WRONG` — the attribution as written does not match the work.
`IMPRECISE` — real source, but the entry's claim outruns or misnames it.
`MISSING` — no attribution given. `NOT-ACADEMIC` — a heuristic or aphorism, no
empirical origin.

**Ethical guards.** Only `UX-P09` and `UX-P18` carry one. **Seven of nine** —
`UX-P10`, `UX-P19`, `UX-P20`, `UX-P21`, `UX-P22`, `UX-P23`, `UX-P24` — have no
`Ethical guard` section, and are therefore among the non-compliant entries
recorded in [#8](https://github.com/Storzen/skills/issues/8). Flagged only,
nothing done here. Worth saying that most of them are defensible omissions in
substance (there is no obvious dark pattern in "space related things closer
together") — but the guard is now mandatory catalog-wide, so the rewrite owes
them one each, and `UX-P10` in particular has a real one to write: manufactured
visual dominance is exactly how a "confirmshaming" accept/decline pair is built.

---

## Evidence

### UX-P09 — Fitts's law

**Missing attribution.** The entry names "Fitts's law" with neither author nor
year. Supplied: Fitts, P. M. (1954), "The information capacity of the human motor
system in controlling the amplitude of movement", *Journal of Experimental
Psychology* 47(6): 381–391 —
[10.1037/h0055392](https://doi.org/10.1037/h0055392). Crossref confirms author,
year, journal, volume, issue and pages. (The paper was reprinted in *JEP:
General* 121(3): 262–269 in 1992 —
[10.1037/0096-3445.121.3.262](https://doi.org/10.1037/0096-3445.121.3.262) — as a
classic; cite the 1954 original.) The discrete-task companion is Fitts, P. M. &
Peterson, J. R. (1964), *JEP* 67(2): 103–112 —
[10.1037/h0045689](https://doi.org/10.1037/h0045689).

**What the paper actually did**, read from the original text. Three tasks, none
of them a screen: **Experiment I, reciprocal tapping** — "The *S*s were asked to
tap two rectangular metal plates alternately with a stylus. Movement tolerance
and amplitude were controlled by fixing the width of the plates and the distance
between them", four plate widths (2, 1, .5, .25 in.) crossed with four
center-to-center distances (2, 4, 8, 16 in.), sixteen conditions, sixteen
right-handed college men, two stylus weights; **Experiment II, disc transfer**
(plastic washers moved between pins); **Experiment III, pin transfer**. The
instruction given to subjects was "*Emphasize accuracy rather than speed*". The
measure is average time per movement against an index of difficulty in bits
derived from amplitude *A* and tolerance *W*.

**Drift — the entry's own sentence is wrong about the shape of the relation.**
"Time to hit a target scales with its distance and inversely with its size"
describes a *linear* dependence on each. Fitts's result is logarithmic: movement
time is proportional to log₂ of the amplitude-to-tolerance ratio. Doubling the
distance to a button does not double the time to reach it; it adds one bit. This
matters in practice, because it is the reason the honest version of the advice is
"make the primary target **big**" rather than "make it **near**" — width buys
more than distance does over the ranges a screen offers. The formulation UI work
actually uses is the Shannon form, ID = log₂(A/W + 1), introduced to HCI by
MacKenzie, I. S. (1992), "Fitts' Law as a Research and Design Tool in
Human-Computer Interaction", *Human–Computer Interaction* 7(1): 91–139 —
[10.1207/s15327051hci0701_3](https://doi.org/10.1207/s15327051hci0701_3). If the
entry names one paper for the HCI reading, this is it.

**Second drift — the touch case is not plain Fitts.** The entry's headline
application is "touch targets… thumb-reach on mobile". Finger touch has an
absolute precision floor that the 1954 model has no term for; the corrected model
is Bi, X., Li, Y. & Zhai, S. (2013), "FFitts law: modeling finger touch with
Fitts' law", *CHI '13*: 1363–1372 —
[10.1145/2470654.2466180](https://doi.org/10.1145/2470654.2466180). Practically:
below roughly a fingertip's width, enlarging a target stops buying time and
starts buying only accuracy.

**Third drift — the destructive-action half is ours, not Fitts's.** "Destructive
ones small and far" is a design inversion of the law, and a good one, but Fitts
made no prescription of any kind, and the law is a **speed–accuracy** model:
shrinking a target under a fixed time budget raises the *error rate*, which is
the actual reason a small "Delete account" is safer. Say that, rather than
implying the law recommends it. The entry's ethical guard is likewise entirely
editorial — nothing in a motor-control model forbids shrinking "decline".

### UX-P10 — Von Restorff (isolation effect)

**Verified.** von Restorff, H. (1933), "Über die Wirkung von Bereichsbildungen im
Spurenfeld", *Psychologische Forschung* 18(1): 299–342 —
[10.1007/BF02409636](https://doi.org/10.1007/BF02409636). Crossref returns the
author exactly as `von Restorff, Hedwig`, year 1933, volume 18, pages 299–342.
The entry's "von Restorff, 1933" is correct, and the lowercase *von* is right.
Two details for the rewrite: the paper is **part I** of a series in Köhler's lab,
completed by Köhler, W. & von Restorff, H., "Analyse von Vorgängen im
Spurenfeld", *Psychologische Forschung* 21: 56–112 —
[10.1007/BF02441202](https://doi.org/10.1007/BF02441202) — which Crossref dates
to **1937**, not the 1935 the secondary literature often prints. And the paper
has never been translated into English, which is the proximate cause of the
distortion below.

**Drift — the entry states the one mechanism von Restorff's data rule out.** The
entry says "the item that stands out **visually** is the one remembered". Hunt,
R. R. (1995), "The subtlety of distinctiveness: What von Restorff really did",
*Psychonomic Bulletin & Review* 2(1): 105–112 —
[10.3758/BF03214414](https://doi.org/10.3758/BF03214414) — exists precisely to
correct this. Verbatim from the abstract: *"Modern theory of the isolation effect
emphasizes perceptual salience and accompanying differential attention to the
isolated item as necessary for enhanced memory. In fact, von Restorff, whose
paper is not available in English, presented evidence that perceptual salience is
not necessary for the isolation effect. She further argued that the difference
between the isolated and surrounding items is not sufficient to produce isolation
effects but must be considered in the context of similarity."* Von Restorff put
the isolate in the **second serial position** specifically so it would not be
salient at encoding, and the effect still appeared. The critical comparison is
not isolate-vs-neighbours within a list; it is the same item in a *heterogeneous*
list against the same item in a *homogeneous control list*. Later work continues
in this direction — Schmidt, S. R. & Schmidt, C. R. (2017), "Revisiting von
Restorff's early isolation effect", *Memory & Cognition* 45(2): 194–207 —
[10.3758/s13421-016-0651-6](https://doi.org/10.3758/s13421-016-0651-6).

**Second drift — "and acted on".** Every result here is about **recall**. Nothing
in von Restorff, Hunt or Schmidt & Schmidt measures choice, click-through or
action. The claim that the visually dominant element is the one *acted on* is an
attention-capture claim from a different literature — see, for the singleton
pop-out case, Theeuwes, J. (1992), "Perceptual selectivity for color and form",
*Perception & Psychophysics* 51(6): 599–606 —
[10.3758/BF03211656](https://doi.org/10.3758/BF03211656). Two mechanisms, two
citations; the entry currently borrows the memory finding's authority for a
behavioural claim it does not make.

Note that the entry's *advice* — one dominant CTA per screen — survives both
corrections, and survives them better under the similarity framing than under the
salience one: the reason one filled button works is that everything around it is
homogeneous, which is exactly von Restorff's argument and exactly what
`UX-P22` is about. The two entries should cross-reference in the rewrite.

### UX-P18 — Aesthetic-usability effect

**Verified.** Kurosu, M. & Kashimura, K. (1995), "Apparent usability vs. inherent
usability: experimental analysis on the determinants of the apparent usability",
*CHI '95 Conference Companion*: 292–293 —
[10.1145/223355.223680](https://doi.org/10.1145/223355.223680). Crossref confirms
both authors, 1995, and pages. The lead held: this is the Japanese ATM study, 26
layout variants of a cash-dispenser interface. The paper's own abstract states
the finding plainly: *"the apparent usability is strongly affected by the
aesthetic aspects rather than the inherent usability."*

**The name is not theirs.** "Aesthetic-usability effect" was coined by Lidwell,
W., Holden, K. & Butler, J. (2003), *Universal Principles of Design* (Rockport),
which is where the phrase enters design practice. Kurosu & Kashimura never used
it. If the entry keeps the name, it should say whose it is.

**Western replications, as the ticket suspected.** Tractinsky, N. (1997),
"Aesthetics and apparent usability: empirically assessing cultural and
methodological issues", *CHI '97*: 115–122 —
[10.1145/258549.258626](https://doi.org/10.1145/258549.258626) — set out to test
whether the 1995 result was a Japanese cultural artefact and found the
correlation *stronger* in an Israeli sample. Then Tractinsky, N., Katz, A. S. &
Ikar, D. (2000), "What is beautiful is usable", *Interacting with Computers*
13(2): 127–145 —
[10.1016/S0953-5438(00)00031-X](https://doi.org/10.1016/S0953-5438\(00\)00031-X)
— gave the effect the slogan it travels under.

**Drift — this is the most contested claim in the family, and the entry states it
as settled.** Three separate lines of attack, all post-2000:

1. **The relation reverses after use.** Hassenzahl, M. (2004), "The Interplay of
   Beauty, Goodness, and Usability in Interactive Products", *HCI* 19(4):
   319–349 — [10.1207/s15327051hci1904_2](https://doi.org/10.1207/s15327051hci1904_2)
   — found beauty and (pragmatic) usability largely independent once a product is
   actually used. Tuch, A. N., Roth, S. P., Hornbæk, K., Opwis, K. &
   Bargas-Avila, J. A. (2012), "Is beautiful really usable?", *Computers in Human
   Behavior* 28(5): 1596–1607 —
   [10.1016/j.chb.2012.03.024](https://doi.org/10.1016/j.chb.2012.03.024) —
   crossed interface aesthetics (low/high) with interface usability (low/high) in
   a lab study and found **an effect of usability on perceived aesthetics and no
   effect of aesthetics on perceived usability**: "what is beautiful is usable"
   reverses to "what is usable is beautiful".
2. **The correlation is largely a third variable.** Preßler, J., Schmid, L. &
   Hurtienne, J. (2023), "Statistically Controlling for Processing Fluency
   Reduces the Aesthetic-Usability Effect", *CHI EA '23*: 1–7 —
   [10.1145/3544549.3585739](https://doi.org/10.1145/3544549.3585739) —
   replicated the raw effect at r = **.79** and watched it fall to r = **.34**
   once processing fluency was partialled out. Both judgements appear to be
   downstream of how easy the screen is to *process*, not of beauty causing
   perceived usability.
3. **Where a real performance effect exists, it is the opposite of a warning.**
   Sonderegger, A. & Sauer, J. (2010), "The influence of design aesthetics in
   usability testing", *Applied Ergonomics* 41(3): 403–410 —
   [10.1016/j.apergo.2009.09.002](https://doi.org/10.1016/j.apergo.2009.09.002)
   — two functionally identical mobile phones differing only in appearance: the
   attractive one produced both higher perceived usability **and reduced task
   completion times**.

**"Forgive minor flaws" has no source.** Neither Kurosu & Kashimura nor Tractinsky
measured error tolerance, complaint rate or forgiveness of defects. That clause —
the one the entry leans on hardest, and the basis of the "polish can mask problems
in testing" caveat — is design folklore. The defensible version of the caveat is
Sonderegger & Sauer's actual finding: appearance shifts *ratings* in a usability
test, so an attractive prototype will be scored more usable than an ugly one with
the same defects. That is a methodological warning, and it is real; "users forgive
flaws" is a different and unevidenced claim.

### UX-P19 — Jakob's law

**Not academic, and unattributed in the entry.** The entry gives "Jakob's law
(Nielsen)" — surname only, no year, no work. It is a practitioner heuristic, not
a finding: there is no experiment behind it and Nielsen never presented one. The
primary source is Nielsen's own publication of it — Nielsen, J., "End of Web
Design", *Nielsen Norman Group* Alertbox, 22 July 2000 —
[nngroup.com/articles/end-of-web-design](https://www.nngroup.com/articles/end-of-web-design/),
whose first section is headed "**1. Jakob's Law of the Internet User
Experience**" and states it verbatim: *"Users spend most of their time on other
sites."* This is the one place in the audit where NN/g is citable: it is not a
secondary write-up of someone else's work, it is the author publishing his own
law at his own venue. Lawsofux, which is where most of the design world meets
this law, is a tertiary restatement and is not a citation.

**No drift in the claim — but the entry over-claims the standing.** The entry's
"Mechanism" line says "transfer of learned mental models", which reads as if a
cognitive mechanism had been established for the law. It has not been established
*by Nielsen*. It has, however, been measured independently, and those are the
citations the entry is missing:

- Roth, S. P., Schmutz, P., Pauwels, S. L., Bargas-Avila, J. A. & Opwis, K.
  (2010), "Mental models for web objects: Where do users expect to find the most
  frequent objects in online shops, news portals, and company web pages?",
  *Interacting with Computers* 22(2): 140–152 —
  [10.1016/j.intcom.2009.10.004](https://doi.org/10.1016/j.intcom.2009.10.004).
  This is the direct empirical form of the entry's own example: users hold
  strong, shared expectations about where the cart, the search box and the
  navigation live.
- Tuch, A. N., Presslaber, E. E., Stöcklin, M., Opwis, K. & Bargas-Avila, J. A.
  (2012), "The role of visual complexity and prototypicality regarding first
  impression of websites", *IJHCS* 70(11): 794–811 —
  [10.1016/j.ijhcs.2012.06.003](https://doi.org/10.1016/j.ijhcs.2012.06.003) —
  prototypicality (how much a page looks like others of its genre) drives first
  impressions.

So the honest structure is: heuristic from Nielsen 2000, evidence from Roth et al.
2010 and Tuch et al. 2012. This is a `source type` / origin-vs-mechanism split of
exactly the kind the previous two audits asked the template for.

### UX-P20 — Serial position effect

**Half-verified.** Murdock, B. B. Jr. (1962), "The serial position effect of free
recall", *Journal of Experimental Psychology* 64(5): 482–488 —
[10.1037/h0045106](https://doi.org/10.1037/h0045106) — author, year, journal,
volume, issue and pages all confirmed by Crossref. "Ebbinghaus" carries **no
year**, which is the defect the ticket asks to be recorded. Supplied: Ebbinghaus,
H. (1885), *Über das Gedächtnis: Untersuchungen zur experimentellen Psychologie*
(Duncker & Humblot); English as *Memory: A Contribution to Experimental
Psychology*, trans. Ruger, H. A. & Bussenius, C. E. (1913), Teachers College,
Columbia University —
[psychclassics.yorku.ca/Ebbinghaus](https://psychclassics.yorku.ca/Ebbinghaus/index.htm).

**Precedence the entry does not know about.** The bowed serial position curve was
published before Ebbinghaus, by Francis E. Nipher in 1878, in the *Transactions of
the Academy of Science of St. Louis*. That work was lost to the field and
recovered by Stigler, S. M. (1978), "Some forgotten work on memory", *Journal of
Experimental Psychology: Human Learning and Memory* 4(1): 1–4 —
[10.1037/0278-7393.4.1.1](https://doi.org/10.1037/0278-7393.4.1.1). The rewrite
does not have to carry Nipher, but it should not assert Ebbinghaus as the
discoverer without qualification. The safe formulation: position effects in serial
learning, Ebbinghaus 1885; the canonical free-recall curve, Murdock 1962.

**Drift — the effect is about recall, and a UI list is not a recall task.** Two
consequences:

1. **Recency is fragile in exactly the way a UI is not.** Glanzer, M. & Cunitz,
   A. R. (1966), "Two storage mechanisms in free recall", *Journal of Verbal
   Learning and Verbal Behavior* 5(4): 351–360 —
   [10.1016/S0022-5371(66)80044-0](https://doi.org/10.1016/S0022-5371\(66\)80044-0)
   — showed that a filled delay between presentation and recall abolishes the
   recency limb while leaving primacy intact. The recency half of the entry's
   advice therefore has a boundary condition it does not state.
2. **Navigation items are on screen.** They are read, not recalled, so
   working-memory serial position is not the binding constraint — the same
   objection the cognition audit raised against `UX-P08`'s nav-length claim, and
   the entry commits it again. There *is* a real position effect in interface
   lists, but it is a click/attention effect measured directly: Murphy, J.,
   Hofacker, C. & Mizerski, R. (2006), "Primacy and Recency Effects on Clicking
   Behavior", *Journal of Computer-Mediated Communication* 11(2): 522–535 —
   [10.1111/j.1083-6101.2006.00025.x](https://doi.org/10.1111/j.1083-6101.2006.00025.x).
   That is the citation the entry's advice actually needs.

**And the example belongs to another entry.** "A bottom tab bar puts the two
highest-value destinations at the far left and far right" is not a memory
argument at all — the far left and far right of a tab bar are the *easiest to
hit*, which is `UX-P09`. Either re-example or say which law is doing the work.

### UX-P21 — Proximity (Gestalt)

**Missing attribution.** No author, no year. Supplied: Wertheimer, M. (1923),
"Untersuchungen zur Lehre von der Gestalt. II", *Psychologische Forschung* 4(1):
301–350 — [10.1007/BF00410640](https://doi.org/10.1007/BF00410640). Crossref
confirms author, year, volume and pages. The English text usually cited is the
abridged translation "Laws of Organization in Perceptual Forms" in Ellis, W.
(1938), *A Source Book of Gestalt Psychology*: 71–88, readable at
[psychclassics.yorku.ca/Wertheimer/Forms](https://psychclassics.yorku.ca/Wertheimer/Forms/forms.htm)
— and read for this audit, which is how the `UX-P23` and `UX-P24` findings below
were established. Nearness (*Nähe*) is the first factor Wertheimer names.

**No drift.** "Elements placed close together are perceived as related" is what
the paper demonstrates. If the entry wants a quantitative source for how strongly
— proximity grouping as a continuous, measurable function of distance rather than
a binary — that is Kubovy, M. & Wagemans, J. (1995), "Grouping by Proximity and
Multistability in Dot Lattices: A Quantitative Gestalt Theory", *Psychological
Science* 6(4): 225–234 —
[10.1111/j.1467-9280.1995.tb00597.x](https://doi.org/10.1111/j.1467-9280.1995.tb00597.x).
This is the cleanest entry in the family: supply the citation and it is done.

### UX-P22 — Similarity (Gestalt)

**Missing attribution.** No author, no year. Supplied: Wertheimer 1923, same
paper — [10.1007/BF00410640](https://doi.org/10.1007/BF00410640). Similarity
(*Gleichheit*) is Wertheimer's second named factor.

**No drift in the claim.** Two additions for the rewrite, neither a correction:

- The modern review that supersedes the 1923 paper as the *reference* — while
  leaving it as the origin — is Wagemans, J., Elder, J. H., Kubovy, M., Palmer,
  S. E., Peterson, M. A., Singh, M. & von der Heydt, R. (2012), "A century of
  Gestalt psychology in visual perception: I. Perceptual grouping and
  figure–ground organization", *Psychological Bulletin* 138(6): 1172–1217 —
  [10.1037/a0029333](https://doi.org/10.1037/a0029333). One citation covers all
  four Gestalt entries and states which principles are classical and which are
  not, which is the fact `UX-P23` needs.
- The entry's own "❌" line already tells the reader to pair similarity with Von
  Restorff. That is the correct reading of both literatures and, per the
  `UX-P10` section above, it is closer to von Restorff's actual argument than
  `UX-P10`'s own mechanism sentence is.

### UX-P23 — Common region (Gestalt)

**Missing attribution — and the implied one would be wrong.** The entry says
"Gestalt principle of common region" with no author and no year, in a family
where the three sibling Gestalt entries all point at the 1923 canon. Common
region is not in that canon. It was read for this audit in the Ellis translation
of Wertheimer 1923: the factors named there are proximity, similarity, common
fate, direction/good continuation, closure, good curve, objective set, past
experience and figure–ground. **Common region is absent.**

**The real source, sixty-nine years later.** Palmer, S. E. (1992), "Common
region: A new principle of perceptual grouping", *Cognitive Psychology* 24(3):
436–447 — [10.1016/0010-0285(92)90014-S](https://doi.org/10.1016/0010-0285\(92\)90014-S).
Crossref confirms author, year, volume, issue and pages. Wagemans et al. 2012
classifies it explicitly among the *new* principles — "classical (e.g.,
proximity, similarity, common fate, good continuation, closure, symmetry,
parallelism) and new (e.g., synchrony, **common region**, element and uniform
connectedness)".

**The claim, unusually, is exactly right — Palmer proves the strong form.** The
entry says a shared boundary "overrides distance in grouping". From Palmer's
abstract, verbatim: *"A new principle of grouping is proposed that is based on
elements being located within a common region of space. Demonstrations analogous
to Wertheimer's original displays show that this factor strongly influences
perceived grouping and is capable of overcoming the effects of other powerful
grouping factors such as proximity and similarity… it is argued that common
region cannot be reduced to the effects of proximity, closure, or any other
previously known factor and therefore constitutes a genuinely new principle of
grouping."* This is one of the few claims in the whole audit that the source
supports in its strongest form, including the "overrides proximity" part that
looks like UX exaggeration and is not. The rewrite should keep the sentence
verbatim and just attach the citation.

Worth adding: Palmer, S. E. & Rock, I. (1994), "Rethinking perceptual
organization: The role of uniform connectedness", *Psychonomic Bulletin & Review*
1(1): 29–55 — [10.3758/BF03200760](https://doi.org/10.3758/BF03200760) — for the
adjacent principle a UI designer keeps reinventing: a single connected region of
uniform colour or texture is grouped as one unit prior to any of the classical
factors. That is what a filled card *is*, and it explains why the entry's own
"prefer proximity first, enclose only when grouping must be unmistakable" caveat
is right — enclosure is the strongest tool available and therefore the easiest to
over-apply.

### UX-P24 — Prägnanz (simplicity / closure)

**Missing attribution, and three ideas in one heading.** The entry's title and
mechanism line — "Law of Prägnanz and closure (Gestalt): perception favors
simple, complete interpretations and fills gaps" — fuse three things the
literature keeps apart:

1. **Prägnanz / *Gesetz der guten Gestalt*** — the *overarching* tendency toward
   the best available organization. Wertheimer 1923 uses the notion but does not
   define it; the Ellis translation gives only *"one recognizes a resultant 'good
   Gestalt' simply by its own 'inner necessity'"*. The canonical formulation is
   Koffka's, not Wertheimer's: Koffka, K. (1935), *Principles of Gestalt
   Psychology* (Harcourt, Brace; Routledge reissue
   [9780415868815](https://www.routledge.com/Principles-Of-Gestalt-Psychology/Koffka/p/book/9780415868815)),
   *"psychological organization will always be as 'good' as the prevailing
   conditions allow"* — quoted as such in Van Geert & Wagemans 2024 below. If the
   entry quotes Prägnanz, it is quoting Koffka.
2. **Closure (*Geschlossenheit*)** — one specific grouping factor, fifth in
   Wertheimer's list, sitting beside proximity and similarity. It is a *sibling*
   of `UX-P21` and `UX-P22`, not a synonym for the overarching principle it is
   currently bundled under.
3. **Simplicity / the minimum principle** — the quantified reading of "good",
   which is a separate and long-contested research programme, not a restatement
   of Prägnanz. Its founding operationalization is Hochberg, J. & McAlister, E.
   (1953), "A quantitative approach to figural 'goodness'", *Journal of
   Experimental Psychology* 46(5): 361–364 —
   [10.1037/h0055809](https://doi.org/10.1037/h0055809), and it has spent seventy
   years being argued against the rival *likelihood* principle — see Chater, N.
   (1996), "Reconciling simplicity and likelihood principles in perceptual
   organization", *Psychological Review* 103(3): 566–581 —
   [10.1037/0033-295X.103.3.566](https://doi.org/10.1037/0033-295X.103.3.566).

**The conflation is a known error, and there is a recent source that says so.**
Van Geert, E. & Wagemans, J. (2024), "Prägnanz in visual perception",
*Psychonomic Bulletin & Review* 31(2): 541–567 —
[10.3758/s13423-023-02344-9](https://doi.org/10.3758/s13423-023-02344-9) (online
first 3 October 2023; cite the 2024 volume year — the `UX-P05` lesson from the
motivation audit). It exists to clear up precisely the misreadings this entry
makes, and one of its corrections lands directly on the entry's advice:
**simplicity is a property of the whole organization, not of the number of
elements** — "simple stimuli do not necessarily produce simple perceptual
groupings", and *emphasizing* characteristic features contributes to good
organization as much as *removing* detail does. The entry's implicit "fewer lines
= more Prägnanz" is not what the principle says, and this is the same failure mode
the cognition audit found in `UX-P15`, where a minimalism argument borrowed
authority from a principle about something else.

**Where that leaves the entry.** The design advice — imply structure with
alignment and whitespace instead of drawing every line — is good and is
genuinely supported, but by **closure and uniform connectedness** (Wertheimer
1923; Palmer & Rock 1994), not by Prägnanz-as-simplicity. Either split the entry
(closure as a grouping factor alongside `UX-P21`–`UX-P23`; Prägnanz as a separate,
properly-hedged principle) or keep one entry and state the three-way distinction
explicitly. Its "❌" line — when implied tips into ambiguous — is the practical
face of Koffka's "as good as the prevailing conditions allow", and is worth
keeping either way.

---

## IDs whose claim text needs rewording

All nine, in descending order of how wrong the current text is:

1. **`UX-P23`** — supply Palmer 1992 and stop implying the 1923 canon; state that
   common region is a *late* addition to Gestalt grouping (Wagemans et al. 2012
   classifies it as "new"); keep the "overrides distance" sentence exactly as
   written, because Palmer proves it; add Palmer & Rock 1994 for the card case.
2. **`UX-P10`** — remove "stands out **visually**": von Restorff's own design put
   the isolate where it would *not* be salient, and Hunt 1995 exists to correct
   this reading. Reframe as heterogeneity against a homogeneous control, drop or
   re-source "and acted on" (Theeuwes 1992 is the attention-capture citation),
   give the full 1933 reference, and note Köhler & von Restorff **1937** (not
   1935) as part II.
3. **`UX-P18`** — state the effect as *contested and largely a fluency confound*
   (Preßler et al. 2023: r .79 → .34), add the reversal (Tuch et al. 2012: usable
   → beautiful, not the converse) and Hassenzahl 2004; attribute the *name* to
   Lidwell et al. 2003; delete "forgive minor flaws" or replace it with
   Sonderegger & Sauer 2010's real finding, which is a *test-methodology* warning.
4. **`UX-P24`** — separate Prägnanz (Koffka 1935's formulation) from closure (one
   of Wertheimer's nine factors) from simplicity (Hochberg & McAlister 1953,
   contested against likelihood, Chater 1996); carry Van Geert & Wagemans 2024's
   correction that simplicity is a property of the organization, not a count of
   elements; re-ground the whitespace advice in closure and uniform connectedness.
5. **`UX-P20`** — supply Ebbinghaus 1885 (trans. 1913) and note that the curve
   predates him (Nipher 1878, via Stigler 1978); state that recency dies under a
   filled delay (Glanzer & Cunitz 1966); stop applying a free-recall effect to
   on-screen navigation and cite Murphy et al. 2006 for the click-position effect
   the advice actually rests on; move the tab-bar example to `UX-P09`.
6. **`UX-P09`** — supply Fitts 1954; fix "scales with its distance" to the
   logarithmic relation (and draw the practical conclusion: size buys more than
   proximity); cite MacKenzie 1992 for the HCI form and Bi et al. 2013 for finger
   touch; mark the destructive-action rule and the ethical guard as our stance,
   and justify them by *error rate* rather than by the law.
7. **`UX-P19`** — say plainly it is Jakob Nielsen's practitioner heuristic
   (Alertbox, 22 July 2000), not a finding; keep the heuristic, and attach the
   evidence that exists for it — Roth et al. 2010 for object-placement
   expectations, Tuch et al. 2012 for prototypicality.
8. **`UX-P21`** — attribution only: Wertheimer 1923 (Ellis 1938 for the English),
   plus Kubovy & Wagemans 1995 if a quantitative source is wanted. Claim stands.
9. **`UX-P22`** — attribution only: Wertheimer 1923, with Wagemans et al. 2012 as
   the modern reference. Claim stands; strengthen the existing cross-reference to
   `UX-P10`, which is closer to von Restorff's argument than `UX-P10` itself is.

Seven of these nine also owe an `Ethical guard` under
[#8](https://github.com/Storzen/skills/issues/8) — see the note under the verdict
table. Not this ticket's business; flagged so the rewrite does not lose it.

## Findings for the v2 entry template (#7)

The perception family **confirms all five** fields proposed so far — the three
from the cognition audit and the two added by motivation — and demands **one
new one**.

- **Source standing** (`replicated` / `contested` / `not-academic` /
  `popularization`) — confirmed, and this family supplies the sharpest case for
  it. `UX-P18` and `UX-P10` look identical in the current template: an author, a
  year, a confident sentence. One of them (`UX-P10`) rests on a finding whose
  *mechanism* was misread but whose effect is solid; the other (`UX-P18`) rests
  on a correlation that a 2023 experiment cut by more than half and a 2012
  experiment ran in the opposite direction. A reader cannot currently tell them
  apart. Note that "contested" needs to admit *reversal*, not just weakening —
  Tuch et al. 2012 did not find a smaller aesthetic-usability effect, they found
  the causal arrow pointing the other way.
- **Origin citation separated from mechanism citation** — confirmed, five of
  nine. `UX-P09` (Fitts 1954 origin / MacKenzie 1992 HCI form / Bi et al. 2013
  touch — **three** slots, as `UX-P03` needed), `UX-P10` (von Restorff 1933
  memory / Theeuwes 1992 attention), `UX-P19` (Nielsen 2000 heuristic / Roth
  2010 evidence), `UX-P20` (Murdock 1962 recall / Murphy 2006 clicking),
  `UX-P24` (Wertheimer 1923 closure / Koffka 1935 Prägnanz / Hochberg &
  McAlister 1953 simplicity — **three** again).
- **A marker for our own editorial stance** — confirmed. `UX-P09`'s
  "destructive ones small and far" is ours, not Fitts's, and `UX-P24`'s "you can
  imply structure without drawing every line" is ours, not Wertheimer's.
- **`source type`** (`peer-reviewed` / `book (academic)` / `trade book` /
  `essay` / `none`) — confirmed, and this family adds two values the motivation
  list does not have: **`conference paper`** (`UX-P18`'s origin is a two-page
  CHI *companion* abstract, `UX-P23`-adjacent work and `UX-P09`'s touch
  correction are full CHI papers — not the same evidentiary weight as a journal
  article, and `UX-P18`'s in particular is thinner than its fame suggests) and
  **`practitioner article`** (`UX-P19`). Also: three of this family's primary
  sources are **not in English** (von Restorff 1933 untranslated; Wertheimer 1923
  and Ebbinghaus 1885 read in translation), which is the direct cause of the
  `UX-P10` distortion — the template should be able to record *which text was
  actually read*.
- **`guard divergence`** — confirmed but inverted. Motivation found guards
  *stricter* than the source. Perception's problem is the mirror image: seven of
  nine entries have **no guard at all**, and the two that do (`UX-P09`,
  `UX-P18`) have guards with no relation to their sources whatsoever — a
  motor-control model and a correlational ATM study neither support nor forbid
  anything ethically. So the field needs a third value beyond "stricter than
  source": **`independent of source`**, meaning the guard is a pure editorial
  addition with no evidentiary content. Without it, `UX-P09`'s guard reads as
  though Fitts warned about deceptive accept/decline pairs.

**One new field this family demands:**

- **`vintage` / supersession** — a slot for *"the canonical modern reference is
  not the origin"*. Four of the nine entries (`UX-P21`, `UX-P22`, `UX-P23`,
  `UX-P24`) have a 1923 or 1935 origin and a single 2012 review — Wagemans et
  al. — that is the source any current reader should actually consult, and
  `UX-P24` has a 2024 review written specifically to correct the misreading the
  entry makes. This is not `source standing` (the finding is not contested) and
  not `origin vs mechanism` (it is the same mechanism). It is a *reading
  recommendation*, and its absence is why `UX-P23` could sit under a "Gestalt"
  heading for thirty years of catalog-time without anyone noticing that the
  principle postdates the canon by sixty-nine years. A `superseded by` field
  would have caught it on the first pass.
