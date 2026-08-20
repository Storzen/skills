# Reference verification — persuasion family (UX-P04, P30, P31, P32, P33, P34)

Resolves [#12](https://github.com/Storzen/skills/issues/12). Re-slice of [#4](https://github.com/Storzen/skills/issues/4), persuasion family only — 6 entries.

**Method.** Every DOI below was resolved against the Crossref metadata API
(`api.crossref.org/works/<doi>`) and its author list, year, journal, volume and
pages checked against the citation as written in `PRINCIPLES-persuasion.md`.
Where the finding itself carries a verdict, the source was read rather than
summarised: **Milgram 1963 was read in full from the Bobbs-Merrill reprint scan
of the original** (the abstract, the subject table, the four prods and the
results section all carry findings below); **Lynn 1991 was read from the
author's own copy in Cornell eCommons**, which is where this report's scarcity
effect size comes from; Barton, Zlatevska & Oppewal 2022 was read from the
authors' open-access copy in the Bond University repository (CC BY-NC-ND);
Bohner & Schlüter 2014 is open access at PLOS ONE and its abstract is quoted
verbatim. Two sources resisted: **Regan 1971 is closed at Elsevier, has no
open-access copy (Unpaywall: `is_oa: null`), and Semantic Scholar records the
abstract as elided by the publisher** — its bibliographic record is verified
against Crossref *and* the ERIC record `EJ046625`, but its design and result are
reported here from secondary accounts and are **marked as such**; Worchel, Lee &
Adewole 1975 is behind APA PsycNet SSO, so its result is taken from **Lynn's
Table 1, which codes it directly** (`Worchel, 1975`, Study 1 *r* = 0.32, Study 2
*r* = 0.08) — a primary meta-analytic coding rather than a blog retelling.
Lawsofux, NN/g, Wikipedia and Medium were used as leads only; none is recorded as
a citation. **The one non-academic source recorded as primary is
`deceptive.design`**, and only for the coinage of "confirmshaming" in `UX-P33` —
the same exception pattern the perception audit applied to Nielsen at NN/g: a
practitioner's own catalogue is the primary source *for the term he catalogued*,
and it is cited here precisely because it disclaims authorship (see below).

**Headline.** This family's defect is uniform and structural, not scattered:
**all six entries cite Cialdini and only Cialdini, and five of the six carry no
year at all.** Cialdini named and organised these principles; with one exception
he ran none of the experiments beneath them, so five entries credit the
synthesiser for the finding. Nothing is fabricated and the sixth attribution
(`UX-P34`, "Cialdini, 2016") is the only *correct* one in the family — it is
correct precisely because unity **is** Cialdini's own contribution. Two claims
have drifted materially: `UX-P31` borrows Milgram's authority for a proposition
about credentials and trust badges that Milgram neither tested nor supports —
Milgram's experimenter did not persuade, he issued "You have no other choice, you
*must* go on", which the file's own preamble rules out of the catalog — and
`UX-P32` states as a general lever an effect that its own meta-analytic
literature puts at *r* = 0.12 and finds **weakest in exactly the supply-limited
form the entry recommends**. On the family's ethical hygiene the news is good and
worth recording: **all six entries carry an `Ethical guard`**, and the guards are
the most substantive in the catalog.

---

## Verdict table

| ID | Cited as | Verdict | Corrected / supplied attribution | Canonical link | Reword? |
|---|---|---|---|---|---|
| `UX-P04` | "The reciprocity norm (Cialdini)" — no year | **IMPRECISE** + **MISSING** | Norm: Gouldner, A. W. (1960), *ASR* 25(2): 161–178. Compliance experiment: Regan, D. T. (1971), *JESP* 7(6): 627–639. Cialdini 1984 is the synthesis, not the origin | [10.2307/2092623](https://doi.org/10.2307/2092623) · [10.1016/0022-1031(71)90025-4](https://doi.org/10.1016/0022-1031\(71\)90025-4) | **Yes** — Regan's point is that the favor works **independently of liking**; the entry misses the one result that separates `UX-P04` from `UX-P33` |
| `UX-P30` | "Social proof (Cialdini)" — no year | **IMPRECISE** + **MISSING** | Term is Cialdini's; findings are Sherif 1935 (*Archives of Psychology* 27/187), Asch 1956 (*Psych. Monographs* 70(9): 1–70), Deutsch & Gerard 1955 (*JASP* 51(3): 629–636), Milgram, Bickman & Berkowitz 1969 | [10.1037/h0046408](https://doi.org/10.1037/h0046408) · [10.1037/h0093718](https://doi.org/10.1037/h0093718) | **Yes** — "under uncertainty" is *informational* influence (Deutsch & Gerard) and should say so; conformity is culture-bound and has declined (Bond & Smith 1996); the descriptive-norm field effect failed to replicate (Bohner & Schlüter 2014) |
| `UX-P31` | "Authority (Cialdini)" — no year | **IMPRECISE** + **MISSING** | The entry's actual claim is **source credibility** — Hovland & Weiss (1951), *POQ* 15(4): 635–650 — and **symbols** of authority: Bickman (1974), *JASP* 4(1): 47–61. Milgram 1963 is the usual citation and is the **wrong** one for this claim | [10.1086/266350](https://doi.org/10.1086/266350) · [10.1111/j.1559-1816.1974.tb02599.x](https://doi.org/10.1111/j.1559-1816.1974.tb02599.x) | **Yes** — hardest in the family. Milgram measured *destructive obedience under coercive prods*, not deference to credentials; and Milgram's own standing is contested (Perry 2013; Haslam et al. 2015; Griggs 2017) |
| `UX-P32` | "Scarcity (Cialdini)" — no year | **IMPRECISE** + **MISSING** | Theory: Brock, T. C. (1968), commodity theory. Experiment: Worchel, Lee & Adewole (1975), *JPSP* 32(5): 906–914. Reactance: Brehm (1966). Evidence state: Lynn 1991; Barton et al. 2022; Ladeira et al. 2023 | [10.1037/0022-3514.32.5.906](https://doi.org/10.1037/0022-3514.32.5.906) · [10.1002/mar.4220080105](https://doi.org/10.1002/mar.4220080105) | **Yes** — the effect is real but **small** (*r* = 0.12, Lynn 1991) and both modern meta-analyses find **demand-based** scarcity beats the supply-based "only 2 left" the entry builds on |
| `UX-P33` | "Liking (Cialdini)" — no year | **IMPRECISE** + **MISSING** | Similarity: Byrne (1961), *JASP* 62(3): 713–715. Incidental similarity: Burger et al. (2004), *PSPB* 30(1): 35–43. Praise: Drachman, deCarufel & Insko (1978), *JESP* 14(5): 458–465. **"Confirmshaming" is separately `NOT-ACADEMIC`** — Anon. (2016), `confirmshaming.tumblr.com`, catalogued by Brignull | [10.1037/h0044721](https://doi.org/10.1037/h0044721) · [deceptive.design/types/confirmshaming](https://www.deceptive.design/types/confirmshaming) | **Yes** — moderate. Split the three distinct levers Cialdini bundles as "liking", and attribute confirmshaming honestly rather than implying it is a Cialdini term |
| `UX-P34` | "Unity (Cialdini, 2016)" | **CORRECT** — the only one in the family | — ; name the work: *Pre-Suasion* (Simon & Schuster, 2016), where unity is introduced; it joins the canonical set in *Influence: New and Expanded* (Harper Business, 2021). Underlying theory: Tajfel et al. (1971) | [10.1002/ejsp.2420010202](https://doi.org/10.1002/ejsp.2420010202) | **Light** — add which book, and mark unity as a **trade-book synthesis** resting on social identity theory, not a tested principle in its own right |

Verdict key: `CORRECT` — author, year and work introduced the effect.
`WRONG` — the attribution as written does not match the work.
`IMPRECISE` — real source, but the entry's claim outruns or misnames it.
`MISSING` — no attribution given. `NOT-ACADEMIC` — a heuristic or aphorism, no
empirical origin.

**Ethical guards.** **All six entries carry one**, and none of the six appears on
the known-missing list in [#8](https://github.com/Storzen/skills/issues/8)
(`UX-P08`, `UX-P15`, `UX-P19`–`UX-P24`, `UX-P35`, `UX-P37`, `UX-P39`, `UX-P40`).
This is the only fully guard-compliant family audited so far, which is what the
file's own preamble promises — "every one is dual-use, so the ethical guard is
load-bearing". Flagged for completeness only; nothing done here. Two of the
guards are also, unusually, *evidentially* grounded rather than editorial —
see the `guard divergence` finding at the end.

---

## Evidence

### UX-P04 — Reciprocity

**Missing year, and the wrong kind of credit.** The entry gives "The reciprocity
norm (Cialdini)" — no year, and Cialdini as though he had established it. He did
not. There are two real sources and they do different jobs.

**The norm.** Gouldner, A. W. (1960), "The Norm of Reciprocity: A Preliminary
Statement", *American Sociological Review* 25(2): 161–178 —
[10.2307/2092623](https://doi.org/10.2307/2092623). Crossref confirms author,
year, journal, volume, issue and start page. Gouldner's argument is
sociological and universal: a generalised moral norm that one should help those
who have helped one, which he proposes as a stabilising mechanism found across
societies. This is where the *idea* the entry names comes from, twenty-four
years before *Influence*.

**The compliance experiment — the one the entry's advice actually rests on.**
Regan, D. T. (1971), "Effects of a favor and liking on compliance", *Journal of
Experimental Social Psychology* 7(6): 627–639 —
[10.1016/0022-1031(71)90025-4](https://doi.org/10.1016/0022-1031\(71\)90025-4).
Crossref returns `Regan, Dennis T.`, 1971, volume 7, issue 6, pages 627–639, and
the ERIC record `EJ046625` independently confirms the same author name and
pagination. **This matters because a widely-copied secondary citation gives the
initials as "R. T. Regan"; they are D. T.** The paper itself is closed at
Elsevier and has no open-access copy, so what follows is the design and result as
consistently reported in the secondary literature and **is marked as
second-hand**: a confederate and a subject rate paintings; the confederate leaves
and returns with an unsolicited Coca-Cola for the subject, or with one only for
himself, or (third condition) the experimenter supplies the drink; later the
confederate asks the subject to buy raffle tickets. Subjects who received the
unsolicited drink bought roughly twice as many tickets.

**Drift — the entry misses the single most useful thing Regan found.** Regan
manipulated *liking* for the confederate independently of the favor. The favor
raised compliance; the effect of the favor **did not depend on liking** —
subjects who disliked the confederate bought as many tickets as those who liked
him. That is the finding that makes reciprocity a *separate* principle from
`UX-P33` rather than a special case of it, and it is a genuinely useful design
fact: a free tool works on users who are indifferent or mildly hostile to the
brand. The entry's mechanism sentence ("an unsolicited gift creates a felt
obligation to reciprocate") is right, and "unsolicited" is doing correct work —
but the rewrite should say *obligation, not affection*, and cross-reference
`UX-P33` to mark the boundary.

**Where Cialdini belongs.** As the synthesis, cited as such: Cialdini, R. B.
(1984), *Influence: The Psychology of Persuasion*, New York: William Morrow,
chapter 2 ("Reciprocation"). One bibliographic caution the rewrite should not
trip over: **catalogue records for the 1984 Morrow printing disagree on the
subtitle** (some give *The New Psychology of Modern Persuasion*), and OpenLibrary
returns a first-publication year of 1983 across a work record spanning Morrow,
Quill, Scott Foresman, HarperCollins and Pearson imprints. Cite the edition
actually consulted rather than a generic "Cialdini 1984".

### UX-P30 — Social proof

**Missing year, and the term is the only part that is Cialdini's.** "Social
proof" as a phrase is his, from *Influence* (1984), chapter 4. Every finding
underneath it predates him by twenty to fifty years, and the entry's own claim
sentence points at a specific one it does not cite.

**The two mechanisms, which the entry conflates into one.** Deutsch, M. & Gerard,
H. B. (1955), "A study of normative and informational social influences upon
individual judgment", *Journal of Abnormal and Social Psychology* 51(3): 629–636
— [10.1037/h0046408](https://doi.org/10.1037/h0046408). Crossref confirms both
authors, 1955, volume 51, issue 3, pages 629–636. This is the paper that split
conformity into **informational** influence (others' behaviour is *evidence*
about reality) and **normative** influence (others' behaviour is *pressure* to be
accepted). The entry's clause "**especially under uncertainty**" is exactly
informational influence and is correct — but it is correct because of Deutsch &
Gerard, and naming them turns a vague appeal into a citable boundary condition:
social proof does the most work where the user cannot evaluate the thing
directly, which is precisely why it belongs on a pricing page and not on a
choice the user already understands.

**The two founding demonstrations.** Sherif, M. (1935), *A study of some social
factors in perception*, *Archives of Psychology* 27(187) — the autokinetic
studies, in which subjects judging the illusory movement of a point of light
converge on a shared group estimate and then carry that norm back into solitary
judgement. Full text is available in the Mead Project scholarly archive at Brock
University ([brocku.ca/MeadProject/Sherif](https://brocku.ca/MeadProject/Sherif/Sherif_1935a/Sherif_1935a_3.html));
this monograph has no DOI, which is normal for *Archives of Psychology* and is not
a defect. And Asch, S. E. (1956), "Studies of independence and conformity: I. A
minority of one against a unanimous majority", *Psychological Monographs: General
and Applied* 70(9): 1–70 —
[10.1037/h0093718](https://doi.org/10.1037/h0093718). **A note on the year the
rewrite should get right:** the line-judgement work is habitually cited as "Asch
1951" (the chapter in Guetzkow's *Groups, Leadership and Men*), but the full
monograph is 1956, and Bond & Smith's meta-analysis titles itself against "Asch's
(1952b, 1956) line judgment task" — cite 1956 for the data.

**The field version, which is the one a UI actually resembles.** Milgram, S.,
Bickman, L. & Berkowitz, L. (1969), "Note on the drawing power of crowds of
different size", *Journal of Personality and Social Psychology* 13(2): 79–82 —
[10.1037/h0028070](https://doi.org/10.1037/h0028070). Crossref confirms all three
authors. Stimulus crowds of 1 to 15 people looking up at a window; the proportion
of passers-by who also look up rises with crowd size. This is the direct analogue
of "used by 12,000 teams" and is a better citation for the entry's example than
anything in the lab literature.

**Drift 1 — the entry states as settled a phenomenon that is culture-bound and
time-bound.** Bond, R. & Smith, P. B. (1996), "Culture and conformity: A
meta-analysis of studies using Asch's (1952b, 1956) line judgment task",
*Psychological Bulletin* 119(1): 111–137 —
[10.1037/0033-2909.119.1.111](https://doi.org/10.1037/0033-2909.119.1.111).
Crossref confirms both authors, year, volume, issue and pages. 133 studies across
17 countries: conformity is **substantially higher in collectivist than in
individualist cultures**, and **conformity in US studies has declined since the
1950s**. Neither fact is fatal to the entry's advice, but both bear on it
directly — a catalog shared across projects and markets should not imply a fixed
coefficient.

**Drift 2 — the strongest field evidence for descriptive norms did not
replicate.** The study the entry's "most popular" advice descends from is
Goldstein, N. J., Cialdini, R. B. & Griskevicius, V. (2008), "A Room with a
Viewpoint: Using Social Norms to Motivate Environmental Conservation in Hotels",
*Journal of Consumer Research* 35(3): 472–482 —
[10.1086/586910](https://doi.org/10.1086/586910) — the hotel-towel signs, in
which a descriptive-norm message ("the majority of guests reuse their towels")
beat a standard environmental appeal, and a *provincial* norm ("guests in this
room") beat the generic one. A direct replication failed. Bohner, G. & Schlüter,
L. E. (2014), "A Room with a Viewpoint Revisited: Descriptive Norms and Hotel
Guests' Towel Reuse Behavior", *PLOS ONE* 9(8): e104086 —
[10.1371/journal.pone.0104086](https://doi.org/10.1371/journal.pone.0104086) —
open access, abstract read verbatim: *"Results showed that reuse rates were high
overall and that both standard and descriptive norm messages increased reuse
rates compared to a no-message baseline. However, **descriptive norm messages
were not more effective than the standard message**, and effects of proximity
were inconsistent across studies."* Two German hotels, N = 724 and N = 204. So:
telling people something is true still beat saying nothing; telling them *others
do it* added nothing over a plain appeal. The honest reading is that social proof
is a real but not automatically superior lever, and the entry's confident "❌ low
volume backfires" caveat is better company for that nuance than the current
mechanism sentence is.

**Worth keeping.** The related Schultz, P. W., Nolan, J. M., Cialdini, R. B.,
Goldstein, N. J. & Griskevicius, V. (2007), "The Constructive, Destructive, and
Reconstructive Power of Social Norms", *Psychological Science* 18(5): 429–434 —
[10.1111/j.1467-9280.2007.01917.x](https://doi.org/10.1111/j.1467-9280.2007.01917.x)
— documents the **boomerang effect**: a descriptive norm pulls below-average
performers up *and drags above-average performers down* toward the mean. That is
a design hazard the entry does not mention and should: telling your best-converting
segment what "most users" do can cost you.

### UX-P31 — Authority

**Missing year, and — the family's sharpest finding — the canonical citation is
the wrong source for the entry's claim.** The entry's principle is: "People defer
to credible expertise and trust signals; surface real credentials,
certifications, and expert endorsement", applied to "security badges,
certifications, expert authorship". The study everyone reaches for is Milgram.
Milgram does not support this.

**What Milgram actually did**, read from the original reprint scan. Milgram, S.
(1963), "Behavioral Study of obedience", *Journal of Abnormal and Social
Psychology* 67(4): 371–378 —
[10.1037/h0040525](https://doi.org/10.1037/h0040525). Crossref confirms author,
year, journal, volume, issue and pages. From the paper's own abstract, verbatim:
*"This article describes a procedure for the study of destructive obedience in
the laboratory… **26 Ss obeyed the experimental commands fully, and administered
the highest shock on the generator.** 14 Ss broke off the experiment at some
point after the victim protested and refused to provide further answers. The
procedure created extreme levels of nervous tension in some Ss. Profuse
sweating, trembling, and stuttering were typical expressions of this emotional
disturbance."* The sample: **40 males aged 20 to 50** from New Haven, recruited
by newspaper advertisement and direct mail, paid \$4.50, "a wide range of
occupations… postal clerks, high school teachers, salesmen, engineers, and
laborers".

Three details from the method section decide the verdict:

1. **The authority was situational legitimacy, not expertise.** The experimenter
   was "a 31-year-old high school teacher of biology… his manner was impassive,
   and his appearance somewhat stern… **He was dressed in a gray technician's
   coat.**" The paper flags the setting itself as load-bearing: the study ran at
   Yale "in the elegant interaction laboratory. (**This detail is relevant to the
   perceived legitimacy of the experiment.**)" No credential was ever presented
   to a subject. A lab coat and a building did the work.
2. **The compliance was produced by escalating verbal coercion.** When a subject
   balked, the experimenter delivered a fixed sequence of prods, verbatim: *"Prod
   1: Please continue. Prod 2: The experiment requires that you continue. Prod 3:
   It is absolutely essential that you continue. **Prod 4: You have no other
   choice, you must go on.**"* Plus a special prod for subjects who raised
   permanent injury. **This is not persuasion; it is pressure**, and
   `PRINCIPLES-persuasion.md`'s own preamble excludes it by name — "Persuasion is
   non-coercive and truthful — anything relying on deception or pressure is out."
   The entry therefore rests its authority principle on a study whose method the
   file's opening paragraph forbids.
3. **The dependent variable is harm to a third party.** "Destructive obedience",
   in the paper's own words. Nothing in it measures whether a credential makes an
   offer more *credible*, which is the entry's entire claim.

**The sources that do support the entry.** Two, and they should replace Milgram
outright:

- Hovland, C. I. & Weiss, W. (1951), "The Influence of Source Credibility on
  Communication Effectiveness", *Public Opinion Quarterly* 15(4): 635–650 —
  [10.1086/266350](https://doi.org/10.1086/266350). Crossref confirms both
  authors, year, volume, issue and start page. Identical messages attributed to
  high- versus low-credibility sources produce different opinion change. **This
  is the entry's claim, tested.**
- Bickman, L. (1974), "The Social Power of a Uniform", *Journal of Applied Social
  Psychology* 4(1): 47–61 —
  [10.1111/j.1559-1816.1974.tb02599.x](https://doi.org/10.1111/j.1559-1816.1974.tb02599.x).
  Crossref confirms author, year, volume, issue and pages. Compliance with
  identical requests from an experimenter dressed as a civilian, a milkman, or a
  guard. **This is the entry's *badge* case, tested** — the finding is about
  *symbols* of authority, which is what a trust badge is, and it is the honest
  empirical warrant for the entry's ethical guard about fake badges: if the
  symbol alone moves behaviour, then a borrowed symbol is not a small lie.

**And Milgram's own standing is contested — record it even after removing it.**
The entry does not cite Milgram explicitly, but any rewrite will be tempted to,
and the reader who goes looking will land there. Four lines of critique:

- **Archival.** Perry, G. (2013), *Behind the Shock Machine: The Untold Story of
  the Notorious Milgram Psychology Experiments* (The New Press) — from the Yale
  archive, the experimenter frequently improvised prods well beyond the published
  four, and many subjects were not properly debriefed. The paradigm as run was
  not the paradigm as published.
- **Theoretical.** Haslam, S. A., Reicher, S. D., Millard, K. & McDonald, R.
  (2015), "'Happy to have been of service': The Yale archive as a window into the
  engaged followership of participants in Milgram's 'obedience' experiments",
  *British Journal of Social Psychology* 54(1): 55–83 —
  [10.1111/bjso.12074](https://doi.org/10.1111/bjso.12074) (Crossref confirms all
  four authors, volume, issue and pages; online 2014, volume year 2015 — the
  `UX-P05` lesson from the motivation audit applies). Their **engaged
  followership** account: subjects were not blindly obeying but actively
  identifying with what they took to be a worthwhile scientific mission. See also
  Haslam, Reicher & Millard (2015), "Shock Treatment: Using Immersive Digital
  Realism to Restage and Re-examine Milgram's 'Obedience to Authority' Research",
  *PLOS ONE* 10(3): e109015 —
  [10.1371/journal.pone.0109015](https://doi.org/10.1371/journal.pone.0109015),
  and the earlier framing in Haslam & Reicher (2012), *PLOS Biology* 10(11):
  e1001426 — [10.1371/journal.pbio.1001426](https://doi.org/10.1371/journal.pbio.1001426).
  **This flips the design lesson**: if compliance comes from *identification with
  a cause*, the mechanism is closer to `UX-P34` unity than to `UX-P31` authority.
- **Partial replication.** Burger, J. M. (2009), "Replicating Milgram: Would
  people still obey today?", *American Psychologist* 64(1): 1–11 —
  [10.1037/a0010932](https://doi.org/10.1037/a0010932). Crossref confirms author,
  year, volume, issue and pages. Ethically constrained: **stopped at 150 volts**,
  the first point of verbal protest, with obedience up to that point broadly
  comparable to Milgram's. It is a genuine replication of the *first third* of the
  procedure and cannot speak to the 450-volt figure at all.
- **Transmission.** Griggs, R. A. (2017), "Milgram's Obedience Study: A
  Contentious Classic Reinterpreted", *Teaching of Psychology* 44(1): 32–37 —
  [10.1177/0098628316677644](https://doi.org/10.1177/0098628316677644) (Crossref:
  online November 2016, volume year 2017), and Griggs, R. A. & Whitehead, G. I.
  (2015), "Coverage of Milgram's Obedience Experiments in Social Psychology
  Textbooks", *Teaching of Psychology* 42(4): 315–322 —
  [10.1177/0098628315603065](https://doi.org/10.1177/0098628315603065). The
  finding is that textbooks pass on the headline and drop the criticism. A UX
  catalog citing Milgram for trust badges would be the same failure one level
  further downstream, which is the specific reason to record it here.

### UX-P32 — Scarcity

**Missing year, and Cialdini is again the synthesiser.** Two real origins, and a
body of evidence that materially qualifies the entry.

**The theory.** Brock, T. C. (1968), "Implications of commodity theory for value
change", in A. G. Greenwald, T. C. Brock & T. M. Ostrom (eds.), *Psychological
Foundations of Attitudes* (Academic Press): 243–275. Read here through Lynn's
exposition, which quotes the core claim directly: *"any commodity will be valued
to the extent that it is unavailable"* (Brock 1968, p. 246), with "unavailability"
operationalised as limits on supply, costs of acquisition, restrictions on
possession, or delays. Commodity theory, not Cialdini, is the theoretical origin
of `UX-P32`, and it predates *Influence* by sixteen years.

**The experiment.** Worchel, S., Lee, J. & Adewole, A. (1975), "Effects of supply
and demand on ratings of object value", *Journal of Personality and Social
Psychology* 32(5): 906–914 —
[10.1037/0022-3514.32.5.906](https://doi.org/10.1037/0022-3514.32.5.906).
Crossref confirms all three authors, year, volume, issue and pages. The cookie-jar
study. **Its most important result is the one the UX literature drops:** cookies
were rated more valuable when supply changed from abundant to scarce than when
constantly scarce, and more valuable still when the scarcity was attributed to
**high demand** rather than to accident. Scarcity-because-others-want-it beat
scarcity-as-such in 1975, and it has kept beating it ever since.

**The companion mechanism.** Brehm, J. W. (1966), *A Theory of Psychological
Reactance* (Academic Press) — the motivational arousal that follows a threatened
freedom, which is why a *deadline* works differently from a *stock count*. Cite it
if the entry keeps its "urgency" framing.

**Drift — the effect is real, reliable, and small; the entry implies it is
strong.** Lynn, M. (1991), "Scarcity effects on value: A quantitative review of
the commodity theory literature", *Psychology & Marketing* 8(1): 43–57 —
[10.1002/mar.4220080105](https://doi.org/10.1002/mar.4220080105). Crossref
confirms author, year, volume, issue and pages; **the paper was read from Lynn's
own copy in Cornell eCommons.** Verbatim from the results: *"Although highly
reliable, the scarcity effects in this meta-analysis were fairly small with a mean
effect size (r) of 0.12. Even omitting the significant reversals (as outliers)
produced a mean effect size (r) of only 0.17. Of course, not all the scarcity
effects were this small—they ranged from -0.54 to 0.43 and were significantly
heterogeneous."* And the fair summary, also verbatim: *"scarcity's enhancement of
value is very robust even if small."* Lynn's Table 1 codes Worchel 1975 itself at
*r* = 0.32 (Study 1) and *r* = 0.08 (Study 2) — the famous study is one of the
larger effects in the literature, and its own second study is near zero.

**Second drift — the two modern meta-analyses both find the entry's recommended
tactic is the weak one.** This is the finding with the most direct design
consequence in the whole audit.

- Barton, B., Zlatevska, N. & Oppewal, H. (2022), "Scarcity tactics in marketing:
  A meta-analysis of product scarcity effects on consumer purchase intentions",
  *Journal of Retailing* 98(4): 741–758 —
  [10.1016/j.jretai.2022.06.003](https://doi.org/10.1016/j.jretai.2022.06.003).
  Crossref confirms all three authors, year, volume, issue and pages; read from
  the authors' open-access copy at Bond University. Abstract, verbatim: *"This
  research presents a meta-analysis of 416 effect sizes from 131 studies. Results
  show that **demand-based scarcity is most effective for utilitarian products,
  supply-based scarcity for experiences, and time-based scarcity for high
  involvement products.**"* The effect is not one lever; it is three, each with a
  different product fit.
- Ladeira, W. J., Lim, W. M., de Oliveira Santini, F., Rasul, T., Perin, M. G. &
  Altinay, L. (2023), "A meta-analysis on the effects of product scarcity",
  *Psychology & Marketing* 40(7): 1267–1279 —
  [10.1002/mar.21816](https://doi.org/10.1002/mar.21816). Abstract, verbatim:
  purchase likelihood is greater under *"scarcity conditions of excessive demand
  (rather than restricted supply) and variety (rather than a category), **but not
  urgency (limited quantity and limited time) scarcity**"*.

Read together: **"only 2 left" and countdown timers — the entry's ✅ examples of
"true low stock, a real deadline, genuinely capped seats" — are the forms with the
least meta-analytic support, while "lots of people are buying this", which is
`UX-P30`, is the form that works.** That is an uncomfortable result for an entry
whose ethical guard is built entirely around verifying stock counts, and the
rewrite should state it: the honest, effective and ethical version of scarcity is
usually a truthful demand signal, not a supply counter.

**A trap to avoid, recorded so the rewrite does not fall into it.** Searching
"scarcity replication" surfaces O'Donnell, M. et al. (2021), "Empirical audit and
review and an assessment of evidentiary value in research on the psychological
consequences of scarcity", *PNAS* 118(44): e2103313118 —
[10.1073/pnas.2103313118](https://doi.org/10.1073/pnas.2103313118), whose
abstract (read in full) describes replications of 20 studies on *"the role of
scarcity priming in pain sensitivity, resource allocation, materialism"*. **This
is a different literature** — the Mullainathan & Shafir scarcity-*mindset*
programme, about what being poor in money or time does to cognition — and it says
nothing about commodity-theory scarcity as a persuasion lever. It must not be
cited against `UX-P32`. Lynn 1991, Barton 2022 and Ladeira 2023 are the relevant
evidence.

### UX-P33 — Liking

**Missing year, and three separable levers under one name.** Cialdini's "liking"
chapter bundles similarity, praise, familiarity, cooperation and physical
attractiveness. The entry inherits the bundle — "similarity, warmth, and genuine
praise" — and so inherits its vagueness. Each has its own source:

- **Similarity → attraction.** Byrne, D. (1961), "Interpersonal attraction and
  attitude similarity", *Journal of Abnormal and Social Psychology* 62(3):
  713–715 — [10.1037/h0044721](https://doi.org/10.1037/h0044721). Crossref
  confirms author, year, volume, issue and pages. The founding demonstration of
  the attitude-similarity effect, and the origin of a very large subsequent
  literature.
- **Trivial, incidental similarity → compliance.** Burger, J. M., Messian, N.,
  Patel, S., del Prado, A. & Anderson, C. (2004), "What a Coincidence! The
  Effects of Incidental Similarity on Compliance", *Personality and Social
  Psychology Bulletin* 30(1): 35–43 —
  [10.1177/0146167203258838](https://doi.org/10.1177/0146167203258838). Crossref
  confirms all five authors, year, volume, issue and pages. **This is the one a
  product designer should know**: a shared birthday or first name — a similarity
  with no informational content whatsoever — raises compliance. It is also the
  sharpest possible warrant for the entry's ethical guard, because it shows the
  lever works on manufactured commonality, which is exactly what a fake "we're
  just like you" brand voice is.
- **Praise.** Drachman, D., deCarufel, A. & Insko, C. A. (1978), "The extra credit
  effect in interpersonal attraction", *Journal of Experimental Social
  Psychology* 14(5): 458–465 —
  [10.1016/0022-1031(78)90042-2](https://doi.org/10.1016/0022-1031\(78\)90042-2).
  Crossref confirms all three authors, year, volume, issue and pages. The
  standard citation for flattery raising liking even when the recipient knows it
  is instrumental. Recent work refining the compliance path: Grant, N. K.,
  Krieger, L. R., Nemirov, H., Fabrigar, L. R. & Norris, M. E. (2021), "I'll
  scratch your back if you give me a compliment", *British Journal of Social
  Psychology* 61(1): 37–54 —
  [10.1111/bjso.12469](https://doi.org/10.1111/bjso.12469) — which finds
  compliments operate partly through reciprocity, i.e. through `UX-P04`, not
  purely through liking.

**The `UX-P04` boundary, restated from the other side.** Regan 1971's independence
result cuts both ways: a favor raises compliance without liking, and (per Grant et
al. 2021) a compliment raises compliance partly *by being* a favor. The two
entries are adjacent and partly overlapping, and the rewrite should say so rather
than let a reader assume they are independent tools.

**"Confirmshaming" is not academic and is not Cialdini's — and its own
catalogue says so.** The entry's ethical guard names confirmshaming without
attribution, in a paragraph that otherwise reads as Cialdini-derived. It is not.
It is a practitioner coinage, and the authoritative catalogue —
[deceptive.design/types/confirmshaming](https://www.deceptive.design/types/confirmshaming),
Harry Brignull's site, successor to `darkpatterns.org` — **explicitly disclaims
authorship**, crediting the term as *"Confirmshaming (Anon, 2016)"* with a link to
`confirmshaming.tumblr.com`. So the honest record is: **term coined anonymously
on Tumblr in 2016; named, defined and popularised by Brignull's deceptive-design
taxonomy; no academic origin.** This is the same exception pattern the perception
audit used for Nielsen at NN/g — a practitioner's own venue is primary for the
practitioner's own contribution — with the twist that here the venue is primary
*for the fact that the coinage is anonymous*. The entry should never imply the
term is Cialdini's or that it comes from a study. There is real measurement of
confirmshaming's prevalence if the rewrite wants it — Mathur, A. et al. (2019),
"Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites",
*PACM HCI* 3(CSCW): 1–32 — but the *coinage* is as recorded above.

### UX-P34 — Unity

**The only correct attribution in the family, and correct for the right reason.**
"Unity (Cialdini, 2016)" is right: unity is Cialdini's own addition, not a
principle he borrowed, so he is the correct name — and 2016 is the correct year.
This is the one entry where crediting Cialdini for the idea is honest.

**Supply the work, and the second work.** Unity is introduced as the seventh
principle in Cialdini, R. B. (2016), *Pre-Suasion: A Revolutionary Way to
Influence and Persuade* (Simon & Schuster). It joins the canonical set — which had
been six since 1984 — only in Cialdini, R. B. (2021), *Influence: New and
Expanded: The Psychology of Persuasion* (Harper Business). The ticket's suspicion
was right on both counts. The rewrite should name *Pre-Suasion* (2016) as the
origin and cite *Influence: New and Expanded* (2021) as the edition where the
seven-principle framing lives, because a reader checking "Cialdini's principles"
against a pre-2021 copy of *Influence* will find six and conclude the entry is
wrong.

**The academic substrate the entry lacks.** Unity is a trade-book synthesis of a
large, well-established research programme that the entry does not name: social
identity theory and the minimal group paradigm. Tajfel, H., Billig, M. G., Bundy,
R. P. & Flament, C. (1971), "Social categorization and intergroup behaviour",
*European Journal of Social Psychology* 1(2): 149–178 —
[10.1002/ejsp.2420010202](https://doi.org/10.1002/ejsp.2420010202). Crossref
confirms all four authors, year, volume, issue and pages. The minimal group
studies show in-group favouritism arising from categorisation that is explicitly
arbitrary and content-free. That is the mechanism behind "one of us", it is
forty-five years older than *Pre-Suasion*, and it is the evidence a sceptical
reader will want.

**The standing caveat, which is a `source standing` matter rather than drift.**
The entry's claim that shared identity "is a stronger bond than mere similarity,
and amplifies the other principles" is Cialdini's own thesis, argued in a trade
book. Unlike reciprocity (Regan), authority-as-credibility (Hovland & Weiss) or
scarcity (Lynn's 49-effect meta-analysis), **there is no body of independent
experimental work testing unity *as a distinct seventh principle* against the
other six.** The underlying social-identity literature is enormous and solid; the
*claim of distinctness and primacy* is not independently established. The entry
should not be removed — the design advice is sound and the ethical guard is the
best in the family — but its confident comparative ("stronger than mere
similarity") is a book's argument, not a measured result, and should be marked as
such. Note also the loop back to `UX-P31`: if Haslam and Reicher are right that
Milgram's subjects complied through identification with a mission rather than
deference to a man in a coat, then the best-known "authority" result in
psychology is better evidence for `UX-P34` than for `UX-P31`.

---

## IDs whose claim text needs rewording

All six, in descending order of how wrong the current text is:

1. **`UX-P31`** — the family's hardest rewrite. Detach the entry from Milgram
   entirely and re-ground it in **source credibility** (Hovland & Weiss 1951) and
   **symbols of authority** (Bickman 1974), which are what the entry actually
   claims and what its badge examples actually are. If Milgram is mentioned at
   all, mark him as *contested* (Perry 2013; Haslam et al. 2015; Burger 2009's
   150-volt ceiling; Griggs 2017) and say plainly that his paradigm measured
   destructive obedience under the coercive prod "You have no other choice, you
   must go on" — a method the file's own preamble excludes from the catalog.
2. **`UX-P32`** — supply Brock 1968 (theory), Worchel et al. 1975 (experiment) and
   Brehm 1966 (reactance); state that the effect is reliable but **small**
   (Lynn 1991, *r* = 0.12, range −0.54 to 0.43, significantly heterogeneous); and
   carry the finding that reverses the entry's advice — both modern
   meta-analyses (Barton et al. 2022; Ladeira et al. 2023) find **demand-based**
   scarcity outperforms the supply- and time-limited forms the entry recommends,
   with Ladeira finding urgency scarcity non-significant. Cross-reference
   `UX-P30`. Do **not** cite the PNAS scarcity audit; it is a different
   literature.
3. **`UX-P30`** — supply Sherif 1935, Asch **1956** (not 1951), Deutsch & Gerard
   1955 and Milgram, Bickman & Berkowitz 1969; name "under uncertainty" as
   *informational* influence per Deutsch & Gerard; state that conformity is
   culturally variable and has declined since the 1950s (Bond & Smith 1996); and
   record that the flagship descriptive-norm field result did not replicate
   (Bohner & Schlüter 2014) and that descriptive norms can **boomerang** on
   above-average users (Schultz et al. 2007).
4. **`UX-P04`** — supply Gouldner 1960 for the norm and Regan 1971 for the
   compliance experiment; add Regan's key result, that the favor's effect is
   **independent of liking**, which is the fact that makes this a separate
   principle from `UX-P33`; keep Cialdini 1984 as the synthesis and cite the
   edition actually used, since catalogue records disagree on the 1984 subtitle.
5. **`UX-P33`** — split the bundle: similarity (Byrne 1961), incidental/trivial
   similarity (Burger et al. 2004 — the most design-relevant and the strongest
   warrant for the existing guard), praise (Drachman et al. 1978; Grant et al.
   2021). Attribute **confirmshaming** honestly as an anonymous 2016 coinage
   catalogued by Brignull at deceptive.design, not as anything Cialdini said.
   Note the partial overlap with `UX-P04`.
6. **`UX-P34`** — lightest. Keep "Cialdini, 2016", add the work (*Pre-Suasion*,
   Simon & Schuster) and note that unity enters the canonical set only in
   *Influence: New and Expanded* (2021); add Tajfel et al. 1971 as the academic
   substrate; and mark the comparative claim ("stronger than mere similarity")
   as Cialdini's argued thesis rather than an independently measured result.

Unlike the perception family, **none of these six owes an `Ethical guard`** —
all six already have one, and none appears on the
[#8](https://github.com/Storzen/skills/issues/8) list. Recorded so the rewrite
does not "fix" something that is not broken.

## Findings for the v2 entry template (#7)

The persuasion family **confirms all six** fields established so far, supplies
new values for three of them, and demands **one new field** that no previous
family could have surfaced.

- **Source standing** (`replicated` / `contested` / `not-academic` /
  `popularization`) — confirmed, and this family finally exercises the value the
  perception audit could only gesture at. `UX-P30` needs to record a **failed
  direct replication** (Bohner & Schlüter 2014 vs. Goldstein et al. 2008) while
  the underlying phenomenon stays solid — that is neither "contested" in
  perception's reversal sense nor "replicated". Proposed additional value:
  **`replication-mixed`**. And `UX-P31`'s Milgram is the field's canonical
  contested source in a *fourth* way again — not reversed, not failed, but
  **method-impeached** (Perry's archive) and **reinterpreted** (engaged
  followership), with a partial replication that only covers the first third of
  the procedure. The field needs to distinguish "the effect is smaller than
  claimed" from "the effect is real but means something else".
- **Origin citation separated from mechanism citation** — confirmed, and this is
  the family that makes it non-optional: **five of six entries need it**, all in
  the same shape. Every one of `UX-P04`, `UX-P30`, `UX-P31`, `UX-P32`, `UX-P33`
  currently names the *synthesiser* where the *origin* belongs. Perception found
  this split in five of nine entries scattered across different causes;
  persuasion has a single systematic cause, which suggests the template should
  make the origin slot **required** and the synthesis slot optional, not the
  reverse.
- **A marker for our own editorial stance** — confirmed, and `UX-P32` is the
  strongest case yet. "❌ Everything else. This is the most-abused persuasion
  lever online" and "Never manufacture scarcity around a user's money" are
  entirely ours; Brock, Worchel and Lynn make no prescription. But note the
  wrinkle: `UX-P32`'s stance turns out to be **vindicated by** the evidence
  (Ladeira finds urgency scarcity non-significant), which the current template
  cannot express — an editorial stance can be merely ours, or ours *and*
  independently supported, and those are different things to a reader deciding
  whether to follow it.
- **`source type`** — confirmed, and persuasion adds the value the whole audit has
  been circling: **`trade book`** as the *sole* cited source. `UX-P34` has no
  peer-reviewed origin at all; its origin is a Simon & Schuster hardback. Also
  needed here: **`book chapter`** (Brock 1968, in an edited Academic Press
  volume; Asch 1951 in Guetzkow) and **`monograph`** (Sherif 1935 and Asch 1956
  are both in monograph series, and Sherif has no DOI — which is normal, not a
  defect, and the template should not treat DOI-lessness as a warning sign).
- **`guard divergence`** — confirmed, and persuasion supplies the **third value
  the perception audit predicted would be needed but could not evidence**:
  alongside `stricter than source` (motivation) and `independent of source`
  (perception), this family has guards that are **`supported by source`**.
  `UX-P33`'s guard against manufactured warmth is directly warranted by Burger et
  al. 2004, which shows the lever fires on *arbitrary* commonality; `UX-P31`'s
  guard against fake badges is directly warranted by Bickman 1974, which shows
  the symbol alone moves behaviour. These are not editorial additions — they are
  the ethical corollary of the finding, and marking them as such makes them much
  harder to argue with.
- **`vintage` / `superseded by`** — confirmed, and inverted relative to
  perception. There the pattern was old origin, one modern review to consult
  instead. Here it is old origin, **modern meta-analysis that changes the
  advice**: Lynn 1991 → Barton 2022 → Ladeira 2023 do not merely supersede
  Worchel 1975 as a reference, they redirect the design recommendation from
  supply-scarcity to demand-scarcity. `superseded by` needs to be able to carry
  "and the recommendation changed", not just "read this instead".

**One new field this family demands:**

- **`adjacent-principle collision`** — a slot naming the sibling entries a
  principle overlaps, competes with, or collapses into. Persuasion is the first
  family where the entries are not independent, and the collisions are load-bearing
  rather than decorative: `UX-P32`'s strongest evidenced form (demand-based
  scarcity) **is** `UX-P30`; `UX-P33`'s compliment effect runs partly through
  `UX-P04`'s reciprocity (Grant et al. 2021) while `UX-P04`'s favor effect runs
  *independently* of `UX-P33`'s liking (Regan 1971) — an asymmetry a reader will
  never infer; and `UX-P31`'s canonical study is better evidence for `UX-P34`
  than for itself if Haslam and Reicher are right. Without this field a designer
  reading `UX-P32` alone will build a stock counter, when the same entry's own
  literature says the demand signal in `UX-P30` would work better. This is
  distinct from `origin vs mechanism` (which relates an entry to its sources) and
  from a cross-reference note (which the perception audit wanted for `UX-P10`/
  `UX-P22` on purely expository grounds): it records that **two entries make
  claims on the same underlying effect**, and which one the evidence favours.
