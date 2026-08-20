# Persuasion — social influence

For acquisition, landing, and conversion screens. Entry template: `FORMAT.md`.
Catalog rules: `SKILL.md`.

Cialdini named and organised these levers, and this family was drawn from that
synthesis — *Influence* (Cialdini, William Morrow, 1984;
[OL3902892W](https://openlibrary.org/works/OL3902892W), whose work record spans
five imprints and returns a first-publication year of 1983, so cite the edition
actually consulted). With one exception he ran none of the experiments beneath
them, so each entry's `origin:` credits the work that established the effect and
Cialdini is named only where he genuinely is the source. `UX-P34` is that
exception, and it arrives late: unity is introduced in *Pre-Suasion* and joins
the canonical set only in *Influence: New and Expanded*, so a reader checking
these entries against an older copy will find six principles and no unity.

Every one is dual-use, so the ethical guard is load-bearing. Persuasion here is
non-coercive and truthful — anything relying on deception or pressure is out,
which is also why the obedience literature is not evidence for `UX-P31`.

- `UX-P04` — Reciprocity
- `UX-P30` — Social proof
- `UX-P31` — Authority
- `UX-P32` — Scarcity
- `UX-P33` — Liking
- `UX-P34` — Unity

---

## UX-P04 — Reciprocity

**Cue.** an ask is coming and the user has been given nothing yet

**Principle.** Give something genuinely useful and unconditional before asking
for anything; the obligation forms whether or not the user likes you.

**Mechanism.** An unsolicited gift creates a felt debt, and that debt runs on the
giving rather than on the relationship: a user indifferent or mildly hostile to
the brand carries it about as heavily as a fond one. The independence is the
whole point — it is what makes this a separate lever from `UX-P33` rather than a
special case of it, and it is why a free tool works on an audience that has no
goodwill toward you yet.

**Applies / doesn't.**
- ✅ Acquisition and landing: a useful free tool, sample, or report before asking
  for signup.
- ✅ Cold audiences — the one lever here that does not need to be liked first.
- ❌ Screens where the user is already committed: the favor reads as friction.

**Ethical guard.** The value must be real and unconditional. A "gift" that is
actually a bait-and-switch, or that quietly incurs an obligation, is
manipulation. The test is whether the user still has the thing after saying no.

**Detection.** Absent: the ask stands in front of the value — a signup wall where
a working sample would do. Weakened: something is given, but conditionally; a
"free" report that unlocks only after the email address is a price, not a gift.

**Collides with.** `UX-P33` — a compliment works partly by *being* a favor, so
warmth and reciprocity are not independent tools. The overlap is one-way: the
favor still works on a user who dislikes you, so for a cold audience the evidence
favours this entry.

**Example.** A tax tool shows the full estimate first, then offers to email a
saved copy in exchange for an address.

**Provenance.**
`standing:` qualified (compliance effect)
`guard-basis:` independent of source
`origin:` Gouldner 1960 — The Norm of Reciprocity: A Preliminary Statement, American Sociological Review 25(2): 161–178 — peer-reviewed — https://doi.org/10.2307/2092623 — the norm as a general, cross-societal moral rule, twenty-four years before *Influence*; sociological, and it prescribes nothing about interfaces
`warrant:` Regan 1971 — Effects of a favor and liking on compliance, Journal of Experimental Social Psychology 7(6): 627–639 — peer-reviewed — https://doi.org/10.1016/0022-1031(71)90025-4 — the compliance experiment this entry's advice rests on, and the source of the independence-from-liking result. Closed at Elsevier with no open-access copy, so its design and result are reported here from secondary accounts and the entry claims no more than that. The initials are D. T., not the widely copied R. T.
`warrant:` Grant, Krieger, Nemirov, Fabrigar & Norris 2021 — I'll scratch your back if you give me a compliment, British Journal of Social Psychology 61(1): 37–54 — peer-reviewed — https://doi.org/10.1111/bjso.12469 — compliments raise compliance partly through reciprocity, which is the `UX-P33` collision measured rather than assumed

---

## UX-P30 — Social proof

**Cue.** the user cannot judge the thing directly and others already have

**Principle.** Where the user has no independent way to evaluate an option, show
what real people actually did; where they can evaluate it themselves, this adds
little.

**Mechanism.** Others' behaviour works two ways and only one of them belongs on a
screen. As *evidence*, it tells a user who cannot assess the thing what it is
probably worth. As *pressure*, it tells them what they must do to be accepted.
An interface supplies the first, which is why social proof earns its place on a
pricing page and not on a choice the user already understands. Neither route is a
constant: how far people follow a group varies by culture and has weakened over
the decades, so this is a lever to be sized locally rather than assumed.

**Applies / doesn't.**
- ✅ Genuine reviews, ratings, usage counts, customer logos, "most popular" on a
  truly popular option.
- ✅ As a truthful demand signal — the best-evidenced form of scarcity is this
  entry, not `UX-P32`.
- ❌ Low-trust or low-volume contexts where thin proof backfires: better none
  than "1 review".
- ❌ On users already above the norm. A descriptive norm pulls toward the average
  from both sides, so telling your best-converting segment what most people do
  can drag them down to it.

**Ethical guard.** Every number and testimonial must be true and current. Fake
reviews, invented counts, or "17 people are viewing this" fabrications are
deceptive and often illegal.

**Detection.** Absent: an unevaluable choice — an unfamiliar plan, an unknown
vendor, a new category — presented with nothing but its own description.
Weakened: proof is present but not comparable to the user's situation, or too
thin to carry the weight put on it.

**Example.** A pricing page shows a real, verifiable "used by 12,000 teams" and
labels the tier most customers actually pick.

**Provenance.**
`standing:` mixed
`guard-basis:` independent of source
`origin:` Sherif 1935 — A study of some social factors in perception, Archives of Psychology 27(187) — monograph — Archives of Psychology issue no. 187, the series' own catalogue number; no DOI, which is normal for this series and not a defect. Full text is hosted in the Mead Project scholarly archive at Brock University, named here rather than deep-linked because the host sits behind a bot challenge. The autokinetic studies, in which subjects converge on a shared estimate and then carry that norm back into solitary judgement
`warrant:` Deutsch & Gerard 1955 — A study of normative and informational social influences upon individual judgment, Journal of Abnormal and Social Psychology 51(3): 629–636 — peer-reviewed — https://doi.org/10.1037/h0046408 — the split this entry's mechanism is built on: informational influence (others' behaviour is evidence) versus normative influence (others' behaviour is pressure)
`warrant:` Asch 1956 — Studies of independence and conformity: I. A minority of one against a unanimous majority, Psychological Monographs: General and Applied 70(9): 1–70 — monograph — https://doi.org/10.1037/h0093718 — the line-judgement work is habitually cited to the 1951 Guetzkow chapter; the full data are in this monograph, and it is the one to cite
`warrant:` Milgram, Bickman & Berkowitz 1969 — Note on the drawing power of crowds of different size, Journal of Personality and Social Psychology 13(2): 79–82 — peer-reviewed — https://doi.org/10.1037/h0028070 — stimulus crowds of rising size on a street; the closest field analogue to a usage count on a page, and a better warrant for this entry's example than anything in the lab literature
`warrant:` Goldstein, Cialdini & Griskevicius 2008 — A Room with a Viewpoint: Using Social Norms to Motivate Environmental Conservation in Hotels, Journal of Consumer Research 35(3): 472–482 — peer-reviewed — https://doi.org/10.1086/586910 — the flagship field result for descriptive norms, and the ancestor of every "most guests choose" line on a screen
`contra:` Bohner & Schlüter 2014 — A Room with a Viewpoint Revisited: Descriptive Norms and Hotel Guests' Towel Reuse Behavior, PLOS ONE 9(8): e104086 — peer-reviewed — https://doi.org/10.1371/journal.pone.0104086 — a direct replication of the entry above that failed on the point that matters: both messages beat no message, but the descriptive norm was not more effective than a plain appeal. This is what `standing: mixed` records — the phenomenon holds, its flagship demonstration did not
`contra:` Schultz, Nolan, Cialdini, Goldstein & Griskevicius 2007 — The Constructive, Destructive, and Reconstructive Power of Social Norms, Psychological Science 18(5): 429–434 — peer-reviewed — https://doi.org/10.1111/j.1467-9280.2007.01917.x — the boomerang effect, and the source of this entry's second ❌
`current:` Bond & Smith 1996 — Culture and conformity: A meta-analysis of studies using Asch's line judgment task, Psychological Bulletin 119(1): 111–137 — peer-reviewed — https://doi.org/10.1037/0033-2909.119.1.111 — conformity is substantially higher in collectivist than individualist cultures and has declined in US studies since the 1950s; the reason a catalog shared across markets states no coefficient

---

## UX-P31 — Authority

**Cue.** the user must judge a claim they cannot verify themselves

**Principle.** Where the user cannot check a claim, the credibility of its source
does the work; surface real credentials, certifications, and named authorship,
each linked to something checkable.

**Mechanism.** Two separate things move the decision. The first is source
credibility: the same message shifts more opinion when attributed to a source the
reader rates as competent and honest. The second is cheaper and needs no
credential at all — a *symbol* of authority, a uniform or a badge, raises
compliance on its own. That second finding is why a borrowed badge is not a small
lie: the symbol is doing the persuading, so a fake one is not a shortcut to the
effect, it is the whole effect.

**Applies / doesn't.**
- ✅ Trust-sensitive domains (health, finance, security): certifications, expert
  authorship, credible sourcing, each linked to an issuing body.
- ❌ Where authority is irrelevant to the decision, or where badges are
  decorative clutter.
- ❌ As a licence for pressure. Compliance under an escalating instruction is a
  different phenomenon, and this file's own rule puts it out of the catalog.

**Ethical guard.** Authority signals must be earned and verifiable. Fake trust
badges, borrowed logos, or implied endorsements you don't have are deceptive —
and corrosive in exactly the high-stakes contexts where they'd help. The evidence
for the lever is the evidence for the guard: a symbol alone moves behaviour, so
wearing one you have not earned is the manipulation itself.

**Detection.** Absent: a consequential claim — a security posture, a health
figure, a legal term — stated by nobody in particular. Weakened: badges are
present but inert; a logo that links nowhere and names no issuer.

**Example.** A payments page shows the actual compliance certifications the
product holds, each linked to the issuer's record.

**Provenance.**
`standing:` reinterpreted
`guard-basis:` supported by source
`origin:` Hovland & Weiss 1951 — The Influence of Source Credibility on Communication Effectiveness, Public Opinion Quarterly 15(4): 635–650 — peer-reviewed — https://doi.org/10.1086/266350 — identical messages attributed to high- versus low-credibility sources produce different opinion change. This is the entry's claim, tested
`warrant:` Bickman 1974 — The Social Power of a Uniform, Journal of Applied Social Psychology 4(1): 47–61 — peer-reviewed — https://doi.org/10.1111/j.1559-1816.1974.tb02599.x — compliance with identical requests from an experimenter dressed as a civilian, a milkman, or a guard. The badge case, tested, and the direct warrant for this entry's ethical guard
`mis-citation:` Milgram 1963 — Behavioral Study of obedience, Journal of Abnormal and Social Psychology 67(4): 371–378 — peer-reviewed — https://doi.org/10.1037/h0040525 — the study everyone reaches for, and the wrong one. It measured destructive obedience under a fixed escalating prod ending "You have no other choice, you must go on"; the authority was a lab coat and a building, no credential was ever shown to a subject, and the dependent variable was harm to a third party. It is not evidence that a credential makes an offer more credible, and its method is what this file's preamble excludes. `standing: reinterpreted` records exactly this: the field's most famous result means something other than the popular reading
`contra:` Perry 2013 — Behind the Shock Machine: The Untold Story of the Notorious Milgram Psychology Experiments, The New Press — trade book — https://openlibrary.org/works/OL17582341W — from the Yale archive: the experimenter frequently improvised prods well beyond the published four, and many subjects were not properly debriefed. The paradigm as run was not the paradigm as published. First published in Australia by Scribe the previous year
`contra:` Haslam, Reicher, Millard & McDonald 2015 — 'Happy to have been of service': The Yale archive as a window into the engaged followership of participants in Milgram's 'obedience' experiments, British Journal of Social Psychology 54(1): 55–83 — peer-reviewed — https://doi.org/10.1111/bjso.12074 — subjects identifying with a mission rather than deferring to a man in a coat. If that reading is right the best-known authority result is better evidence for `UX-P34` than for this entry. Crossref stamps it to the online-first year; the volume year is the one cited here
`contra:` Burger 2009 — Replicating Milgram: Would people still obey today?, American Psychologist 64(1): 1–11 — peer-reviewed — https://doi.org/10.1037/a0010932 — ethically constrained to stop at the first point of verbal protest, so it replicates the first third of the procedure and can say nothing about the headline figure
`current:` Griggs 2017 — Milgram's Obedience Study: A Contentious Classic Reinterpreted, Teaching of Psychology 44(1): 32–37 — peer-reviewed — https://doi.org/10.1177/0098628316677644 — how textbooks pass on the headline and drop the criticism. A UX catalog citing Milgram for trust badges would be that failure one level further downstream, which is why it is recorded here rather than quietly dropped. Crossref stamps it to the online-first year; the volume year is the one cited here

---

## UX-P32 — Scarcity

**Cue.** availability is limited and the limit is about to be shown

**Principle.** State a real limit, and say *why* it is limited: scarcity that
comes from demand outperforms the stock counter and the countdown, which the
evidence barely supports.

**Mechanism.** Restricted availability raises what a thing seems to be worth, and
how much depends entirely on what the restriction says. "Others took them"
carries information about value; "we only made a few" carries none; and a
deadline runs on a third route altogether — the pressure of a freedom about to
close, which is also why it irritates. Treating the three as one lever is what
makes scarcity look unreliable.

**Applies / doesn't.**
- ✅ A truthful demand signal: what is actually selling, actually booked,
  actually going. This is the well-evidenced form, and it is `UX-P30`.
- ✅ Real limits stated plainly where the user needs them to plan — a genuine
  deadline, genuinely capped seats.
- ❌ As a general-purpose conversion lever. Averaged over the literature the
  effect is small — r = 0.12 — and heterogeneous enough that the average is a
  poor guide to any one case.
- ❌ Everything invented. This is the most-abused persuasion lever online.

**Ethical guard.** The scarcity must be real and accurate. Fake "only 2 left"
counters, countdowns that reset, and invented deadlines are textbook dark
patterns; several are now regulated. If you can't verify the limit, don't show
one. Never manufacture scarcity around a user's money. The line is ours, but it
costs less than it looks: the forms most often faked are also the ones the
meta-analytic evidence supports least.

**Detection.** Absent: a genuinely limited thing sold as though unlimited, so the
user plans wrong and misses it. Weakened: a limit is shown but unexplained — a
bare counter with no stated cause — or shown permanently, which tells the user it
is decorative.

**Collides with.** `UX-P30` — the best-evidenced form of scarcity *is* social
proof. Where both are available, show what others did rather than what is left.

**Example.** An event page shows the true remaining seat count from inventory
next to how many people booked this week, and stops showing urgency once seats
are ample.

**Provenance.**
`standing:` qualified
`guard-basis:` independent of source
`origin:` Brock 1968 — Implications of commodity theory for value change, in Greenwald, Brock & Ostrom (eds.), Psychological Foundations of Attitudes: 243–275 — book chapter — https://openlibrary.org/works/OL161850W — commodity theory: any commodity is valued to the extent that it is unavailable, with unavailability covering limits on supply, costs of acquisition, restrictions on possession and delays. Sixteen years before *Influence* — read: Lynn 1991's exposition, which quotes the core claim directly
`warrant:` Worchel, Lee & Adewole 1975 — Effects of supply and demand on ratings of object value, Journal of Personality and Social Psychology 32(5): 906–914 — peer-reviewed — https://doi.org/10.1037/0022-3514.32.5.906 — the cookie-jar study, and the source of this entry's central claim: value rose more when scarcity was attributed to high demand than when it was attributed to accident
`warrant:` Brehm 1966 — A Theory of Psychological Reactance, Academic Press — book (academic) — https://openlibrary.org/works/OL9393463W — the motivational arousal that follows a threatened freedom; the separate route a deadline runs on, and why it behaves unlike a stock count
`figure:` "r = 0.12" — Lynn 1991, the mean effect size across the commodity-theory literature
`contra:` Lynn 1991 — Scarcity effects on value: A quantitative review of the commodity theory literature, Psychology & Marketing 8(1): 43–57 — peer-reviewed — https://doi.org/10.1002/mar.4220080105 — verbatim: "Although highly reliable, the scarcity effects in this meta-analysis were fairly small with a mean effect size (r) of 0.12… they ranged from -0.54 to 0.43 and were significantly heterogeneous." Read from the author's copy in Cornell eCommons. Its own coding puts the famous 1975 study near the top of the range and that study's second experiment near zero
`current:` Barton, Zlatevska & Oppewal 2022 — Scarcity tactics in marketing: A meta-analysis of product scarcity effects on consumer purchase intentions, Journal of Retailing 98(4): 741–758 — peer-reviewed — https://doi.org/10.1016/j.jretai.2022.06.003 — demand-based scarcity is most effective for utilitarian products, supply-based for experiences, time-based for high-involvement products. Not one lever, three
`current:` Ladeira, Lim, de Oliveira Santini, Rasul, Perin & Altinay 2023 — A meta-analysis on the effects of product scarcity, Psychology & Marketing 40(7): 1267–1279 — peer-reviewed — https://doi.org/10.1002/mar.21816 — purchase likelihood rises under excessive demand rather than restricted supply, and not under urgency scarcity at all. This is the finding that redirects the entry's advice, not merely its reading list
`mis-citation:` O'Donnell, Dev, Antonoplis et al. 2021 — Empirical audit and review and an assessment of evidentiary value in research on the psychological consequences of scarcity, PNAS 118(44): e2103313118 — peer-reviewed — https://doi.org/10.1073/pnas.2103313118 — surfaces first on any search for "scarcity replication" and is a different literature entirely: the scarcity *mindset* programme, about what being poor in money or time does to cognition. It says nothing about commodity-theory scarcity and must never be cited against this entry

---

## UX-P33 — Liking

**Cue.** the product's voice, persona, or human presence is being written

**Principle.** People say yes more readily to what feels like them; use a human,
respectful voice and real commonality, never a manufactured one.

**Mechanism.** Three separable things sit under "liking" and they are not
interchangeable. Shared attitudes raise attraction. Trivial, contentless
similarity — a shared first name, a shared birthday — raises *compliance* on its
own, which is the uncomfortable one: it works precisely because it means nothing.
Praise raises liking even when the recipient knows it is instrumental, and it
raises compliance partly by functioning as a favor, which belongs to `UX-P04`
rather than here.

**Applies / doesn't.**
- ✅ Voice and tone, friendly empty states, human error messages, showing the
  real team behind the product.
- ✅ Real commonality the user actually shares with the people behind the
  product.
- ❌ Serious or high-stakes moments where forced friendliness reads as flippant —
  an error moving money, a security warning.
- ❌ Manufactured commonality. The lever fires on similarity with no
  informational content at all, which is what makes an invented one effective and
  exactly why it is out.

**Ethical guard.** Warmth must be sincere, not a veneer to smooth over a bad
deal. Confirmshaming — guilt-tripping the decline option ("No thanks, I like
paying full price") — weaponizes liking and is a dark pattern. The strictness is
warranted rather than fussy: since a commonality with no content moves behaviour,
a fabricated one is not harmless brand voice.

**Detection.** Absent: system-voice copy at a moment where a person is obviously
on the other end — a bare error code when something the user cares about has
failed. Weakened: warmth applied uniformly, including where it does not belong,
so it reads as a template rather than as a person.

**Collides with.** `UX-P04` — the overlap is asymmetric and easy to get backwards:
a compliment works partly through reciprocity, but a favor works without liking.
For a cold audience, give rather than charm.

**Example.** A decline link reads plainly "No thanks", never a guilt-laden
sentence.

**Provenance.**
`standing:` qualified
`guard-basis:` supported by source
`origin:` Byrne 1961 — Interpersonal attraction and attitude similarity, Journal of Abnormal and Social Psychology 62(3): 713–715 — peer-reviewed — https://doi.org/10.1037/h0044721 — the founding demonstration of the attitude-similarity effect, and the head of a very large subsequent literature
`warrant:` Burger, Messian, Patel, del Prado & Anderson 2004 — What a Coincidence! The Effects of Incidental Similarity on Compliance, Personality and Social Psychology Bulletin 30(1): 35–43 — peer-reviewed — https://doi.org/10.1177/0146167203258838 — a shared birthday or first name, similarity with no informational content whatsoever, raises compliance. The one a product designer should know, and the direct warrant for this entry's guard: the lever fires on manufactured commonality, which is what a fake "we're just like you" voice is
`warrant:` Drachman, deCarufel & Insko 1978 — The extra credit effect in interpersonal attraction, Journal of Experimental Social Psychology 14(5): 458–465 — peer-reviewed — https://doi.org/10.1016/0022-1031(78)90042-2 — flattery raises liking even where the recipient knows it is instrumental
`warrant:` Grant, Krieger, Nemirov, Fabrigar & Norris 2021 — I'll scratch your back if you give me a compliment, British Journal of Social Psychology 61(1): 37–54 — peer-reviewed — https://doi.org/10.1111/bjso.12469 — the compliance path runs partly through reciprocity, which is the `UX-P04` collision
`current:` Anon. 2016 — the coinage of "confirmshaming", originally on confirmshaming.tumblr.com — practitioner article — https://deceptive.design/types/confirmshaming/ — Brignull's deceptive-design catalogue names, defines and popularised the term while explicitly disclaiming authorship of it. Not academic, and not Cialdini's; recorded so the guard's own vocabulary is attributed honestly — accessed: 2026-08-19

---

## UX-P34 — Unity

**Cue.** the product and its users genuinely belong to the same group

**Principle.** Speak as a member where membership is real; shared identity moves
people differently from resemblance, and only when it is true.

**Mechanism.** Being sorted into a group is enough to produce favouritism toward
it, even when the category is explicitly arbitrary and everyone knows it.
Identity is therefore not a stronger flavour of similarity but a different thing:
"like me" invites a comparison, "one of us" removes the question.

**Applies / doesn't.**
- ✅ Community products, membership, mission-driven brands: language of shared
  identity that is actually true of the user.
- ❌ Where no real shared identity exists — claimed kinship rings hollow and
  breaks trust faster than a plain sales voice would.
- ❌ As a ranked lever. That identity beats the other principles is an argument
  made in a trade book, not a measured result; treat it as one of the six here,
  not as the strongest *(our stance)*.

**Ethical guard.** Belonging must be genuine, opt-in, and never used to pressure
the in-group into choices against their interest ("real members upgrade").
Exploiting identity to sell is manipulation.

**Detection.** Absent: a genuine community addressed as a market — "customers"
where "we" would be true. Weakened: the language of membership over a product
with no membership behind it, which reads as costume.

**Example.** An open-source tool speaks to "we maintainers" because its users
genuinely are that community.

**Provenance.**
`standing:` qualified (the claim of primacy)
`guard-basis:` independent of source
`origin:` Cialdini 2016 — Pre-Suasion: A Revolutionary Way to Influence and Persuade, Simon & Schuster — trade book — https://openlibrary.org/works/OL17592794W — where unity is introduced as a seventh principle. The one entry in this family where crediting Cialdini for the idea is honest, and the one whose sole origin is a trade book: no independent experimental work tests unity as distinct from the other six, which is what the scoped `standing:` records
`warrant:` Tajfel, Billig, Bundy & Flament 1971 — Social categorization and intergroup behaviour, European Journal of Social Psychology 1(2): 149–178 — peer-reviewed — https://doi.org/10.1002/ejsp.2420010202 — the minimal group paradigm: in-group favouritism arising from a categorisation that is arbitrary and content-free. Forty-five years older than *Pre-Suasion*, and the evidence a sceptical reader will want
`current:` Cialdini 2021 — Influence, New and Expanded: The Psychology of Persuasion, Harper Business — trade book — https://openlibrary.org/works/OL24348752W — the edition in which unity joins the canonical set. A reader checking this entry against a pre-2021 copy of *Influence* will find six principles and conclude the entry is wrong
