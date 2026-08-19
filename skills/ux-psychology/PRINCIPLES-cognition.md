# Cognition — cognitive load & decision-making

For choice-heavy screens: forms, settings, pricing, anything asking the user to
decide. Entry template: `FORMAT.md`. Catalog rules: `SKILL.md`.

- `UX-P01` — Smart defaults
- `UX-P06` — Anchoring / contrast
- `UX-P07` — Hick's law
- `UX-P08` — Chunking (Miller's law)
- `UX-P13` — Tesler's law (conservation of complexity)
- `UX-P14` — Choice overload
- `UX-P15` — Occam's razor
- `UX-P16` — Decoy effect
- `UX-P17` — Framing effect

---

## UX-P01 — Smart defaults

**Cue.** a field could be pre-filled from what is already known

**Principle.** Never show an empty field when a likely value exists: pre-fill
with the most common, safe, reversible choice.

**Mechanism.** A default sticks for three separable reasons: accepting it is the
cheapest option, it reads as the recommended one, and it becomes the reference
point the alternatives are judged against. Only the last is status-quo bias.
Which of the three is doing the work decides whether a given fix helps at all.

**Applies / doesn't.**
- ✅ Forms, settings, repeated selections, onboarding — anywhere one choice is
  right for most people.
- ❌ High-stakes or irreversible choices: pre-fill ≠ pre-decide. Never default a
  money movement or a bundled add-on.

**Ethical guard.** Ethical when the default serves the *user's* most likely
intent and is trivially changeable. Note what that second clause does not buy:
making a default easy to change defuses only the effort pathway. A pre-checked
opt-in stays manipulative through implied endorsement — the user reads the
default as advice, so reversing it is cheap but never occurs to them. A default
the user would not choose knowingly is a dark pattern however light the toggle.

**Detection.** Absent: a field left empty that locale, the account, or the last
use could have filled. Weakened: a default is set, but to the vendor's preferred
value rather than the common case, or changing it is a screen away.

**Example.** A shipping form defaults country from locale and quantity to `"1"`;
the user confirms instead of typing.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Samuelson & Zeckhauser 1988 — Status quo bias in decision making, Journal of Risk and Uncertainty 1(1): 7–59 — peer-reviewed — https://doi.org/10.1007/BF00055564
`warrant:` Jachimowicz, Duncan, Weber & Johnson 2019 — When and why defaults influence decisions: a meta-analysis of default effects, Behavioural Public Policy 3(2): 159–186 — peer-reviewed — https://doi.org/10.1017/bpp.2018.43 — a robust default effect overall, moderated by the three distinct pathways this entry's mechanism names
`warrant:` Johnson & Goldstein 2003 — Do Defaults Save Lives?, Science 302(5649): 1338–1339 — peer-reviewed — https://doi.org/10.1126/science.1091721 — measures registration as a donor, not organs transplanted
`contra:` Arshad, Anderson & Sharif 2019 — Comparison of organ donation and transplantation rates between opt-out and opt-in systems, Kidney International 95(6): 1453–1460 — peer-reviewed — https://doi.org/10.1016/j.kint.2019.01.036 — opt-out countries show higher deceased-donor and lower living-donor rates, with a net effect far below what the registration figures suggest; reason enough not to reach for the famous registration chart as illustration

---

## UX-P06 — Anchoring / contrast

**Cue.** a number or price is judged against something else

**Principle.** The first number or option seen becomes the reference for judging
the rest; never present a price or an option in isolation.

**Mechanism.** An anchor shown first primes the knowledge that fits it, and that
knowledge then dominates the judgment. This is not the same as starting from the
anchor and adjusting too little — that describes an anchor the person generated
themselves, and every anchor a screen supplies is the other kind.

**Applies / doesn't.**
- ✅ Pricing pages, plan comparison, the order options are listed in, any figure
  the user has no independent scale for.
- ❌ Where a controlled first impression would hide a material fact.

**Ethical guard.** A real, relevant reference — a higher tier shown first, last
month's usage next to this month's — is fair. Inventing an "original price" to
manufacture a discount is deceptive and, in many jurisdictions, illegal. The
test is whether the reference would still be there if it flattered nothing.

**Detection.** Absent: a price, quota, or score stated with nothing to judge it
against. Weakened: a reference is present but not comparable — a struck-through
price for a different configuration, a "typical" figure with no stated basis.

**Example.** A three-tier plan page lists the premium tier first, so the middle
tier is read against it rather than against nothing.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Tversky & Kahneman 1974 — Judgment under Uncertainty: Heuristics and Biases, Science 185(4157): 1124–1131 — peer-reviewed — https://doi.org/10.1126/science.185.4157.1124 — names the effect, and names anchoring-and-adjustment as its process; that process is the part later work moved off
`warrant:` Strack & Mussweiler 1997 — Explaining the enigmatic anchoring effect: Mechanisms of selective accessibility, Journal of Personality and Social Psychology 73(3): 437–446 — peer-reviewed — https://doi.org/10.1037/0022-3514.73.3.437 — the mechanism for an anchor the judge did not generate, which is the only kind an interface supplies
`warrant:` Epley & Gilovich 2006 — The Anchoring-and-Adjustment Heuristic: Why the Adjustments Are Insufficient, Psychological Science 17(4): 311–318 — peer-reviewed — https://doi.org/10.1111/j.1467-9280.2006.01704.x — establishes the boundary: insufficient adjustment is about self-generated anchors
`warrant:` Klein et al. 2014 — Investigating Variation in Replicability: A Many Labs Replication Project, Social Psychology 45(3): 142–152 — peer-reviewed — https://doi.org/10.1027/1864-9335/a000178 — anchoring is among the effects that came through replication intact
`current:` Mussweiler & Strack 1999 — Comparing is believing: A selective accessibility model of judgmental anchoring, Journal of Experimental Social Psychology 35(2): 136–164 — peer-reviewed — https://doi.org/10.1006/jesp.1998.1364

---

## UX-P07 — Hick's law

**Cue.** many routes or options are offered at once

**Principle.** The more options offered at once, the longer the choice takes;
segment or stage them rather than laying one flat set in front of the user.

**Mechanism.** Choosing costs time in proportion to the information the option
set carries — its size, and how evenly likely its members are — and not in
proportion to how complicated any single option is. The relation is logarithmic,
and it was measured on practiced, arbitrary responses. Reading a menu of
unfamiliar labels is a different task, closer to searching a list one item at a
time unless the set is ordered enough to be skipped through; more options at
once slows the user either way.

**Applies / doesn't.**
- ✅ Navigation, menus, long forms split into steps, option-heavy screens.
- ✅ Ordering a set so it can be searched rather than read: alphabetical,
  numeric, by frequency.
- ❌ As an argument about a single option's complexity. The law bears on how
  many alternatives sit together, nothing else.
- ❌ When collapsing options hides a consequential choice the user needs to see.

**Ethical guard.** Reducing options serves the user only when nothing
consequential leaves the screen. Collapsing, nesting, or defaulting away a
choice that changes what the user pays, agrees to, or gives up is not
simplification — it is concealment. Segment a consequential choice; never remove
it from view.

**Detection.** Absent: a flat set of many peer options with no grouping, no
ordering, and no staging. Weakened: the options are grouped, but on a division
the user cannot predict, so they still read every label to find theirs.

**Example.** A long signup form becomes a three-step wizard, each step holding a
handful of related fields.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Hick 1952 — On the Rate of Gain of Information, Quarterly Journal of Experimental Psychology 4(1): 11–26 — peer-reviewed — https://doi.org/10.1080/17470215208416600 — establishes the logarithmic form
`warrant:` Hyman 1953 — Stimulus information as a determinant of reaction time, Journal of Experimental Psychology 45(3): 188–196 — peer-reviewed — https://doi.org/10.1037/h0056940 — generalises the law to the information content of the set, including unequal probabilities; this is why the pairing is the standard name
`warrant:` Landauer & Nachbar 1985 — Selection from alphabetic and numeric menu trees using a touch screen, CHI '85 Proceedings: 73–78 — conference paper — https://doi.org/10.1145/317456.317470 — log-form selection times for *ordered* menus, the defensible evidence for the menu case
`current:` Seow 2005 — Information Theoretic Models of HCI: A Comparison of the Hick-Hyman Law and Fitts' Law, Human-Computer Interaction 20(3): 315–352 — peer-reviewed — https://doi.org/10.1207/s15327051hci2003_3 — the boundary conditions: a model of choice reaction, not of visual search or reading

---

## UX-P08 — Chunking (Miller's law)

**Cue.** the user must hold several items in mind at once

**Principle.** Working memory holds roughly 4 chunks, not the 7 the popular name
promises; group anything the user has to carry from one moment to the next.

**Mechanism.** The limit binds on items held *in memory*, not on items visible
on a screen. Chunking beats it by making one unit out of several, so a grouped
card number is a handful of things to hold rather than sixteen. Anything still
on screen and re-readable is not competing for this capacity at all.

**Applies / doesn't.**
- ✅ Grouping the digits of a phone, card, or reference number.
- ✅ Any value the user must carry across a step — a code from an email, a total
  from a previous screen.
- ❌ Navigation length. Menu items stay on screen and can be re-read, so memory
  capacity is not what binds; the cost of a long menu is decision time, which is
  `UX-P07`.
- ❌ Reference material meant to be scanned rather than memorised.

**Ethical guard.** The abuse vector here is the lever run backwards. Deliberately
overrunning the limit — splitting a price across screens, stating a total the
user has to assemble from parts, burying a commitment mid-paragraph so it must
be held whole — turns a capacity limit into a concealment tool. Never make the
user remember what the screen could simply show them.

**Detection.** Absent: an unbroken run of digits, or a value the user must carry
across a step with no way back to it. Weakened: the grouping exists, but differs
between where the value is entered and where it is read back, so the user
re-chunks it anyway.

**Example.** A card field displays what is typed as `"4539 1488 0343 6467"`
rather than one unbroken run.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Miller 1956 — The magical number seven, plus or minus two: Some limits on our capacity for processing information, Psychological Review 63(2): 81–97 — peer-reviewed — https://doi.org/10.1037/h0043158 — proposes no law. It reports two different findings, the channel capacity of absolute judgment and the span of immediate memory, and treats the recurrence of the number as a coincidence; "Miller's law" is the UX community's coinage, which is why this entry is filed under chunking
`warrant:` Cowan 2001 — The magical number 4 in short-term memory: A reconsideration of mental storage capacity, Behavioral and Brain Sciences 24(1): 87–114 — peer-reviewed — https://doi.org/10.1017/S0140525X01003922 — the span this entry states, and the source of its hedge
`figure:` "4" — Cowan 2001, the reconsidered span
`figure:` "7" — Miller 1956, the number the paper is named for

---

## UX-P13 — Tesler's law (conservation of complexity)

**Cue.** a step could be automated or inferred instead of asked

**Principle.** Every flow carries an irreducible complexity that can be moved but
not removed; decide deliberately who absorbs it — the user, the application, or
the platform — and default to the system *(our stance)*.

**Mechanism.** Simplifying one side of a flow shifts the work rather than
deleting it. A field the user no longer fills is a value something else now has
to derive; the only open question is which party pays.

**Applies / doesn't.**
- ✅ Any flow where a step could be automated, inferred, or pre-filled instead of
  asked of the user.
- ❌ Where absorbing the complexity would strip control the user genuinely needs
  — expert tools, legal consent.
- ❌ As authority for the default. Tesler asks *who* absorbs; the answer this
  entry gives is ours.

**Ethical guard.** Absorbing complexity for the user is good — unless
"absorbing" means making a consequential decision on their behalf without
saying so. Hide effort, not stakes.

**Detection.** Absent: the user is asked for something the system already knows
or could derive. Weakened: the work moved off the user, but what it produced is
not shown, so they cannot tell whether the inference was right.

**Example.** An address form derives city and region from a postal code instead
of asking for all three, and displays what it derived so the user can correct it.

**Provenance.**
`standing:` unevidenced
`guard-basis:` independent of source
`origin:` Tesler ca. 1984 — Law of Conservation of Complexity — practitioner article — https://www.nomodes.com/larry-tesler-consulting/complexity-law — Tesler's own page, carrying the original formulation verbatim; it names three parties (user, application developer, platform developer) and asks which of them deals with the complexity, without prescribing an answer — accessed: 2026-08-19
`warrant:` Tesler ca. 1984 — Law of Conservation of Complexity — practitioner article — https://www.nomodes.com/larry-tesler-consulting/complexity-law — the same page is also the only statement of the law; no study stands behind it, which is what `standing: unevidenced` records — accessed: 2026-08-19

---

## UX-P14 — Choice overload

**Cue.** more than a handful of comparable options sit together

**Principle.** Too many options depress choice only under specific conditions;
check whether your picker creates those conditions before you cut the set.

**Mechanism.** More alternatives do not by themselves make people choose less.
What does is the situation the picker builds around them: the user has no
pre-formed preference to apply, the options resist comparison, the task is
effortful, and there is no acceptable way out. With those absent, a larger set
costs nothing — which makes the four conditions, not the count, the thing to fix.

**Applies / doesn't.**
- ✅ Plan pickers, settings, product grids where the options differ on attributes
  the user cannot rank — add comparison, filtering, and a recommended default
  rather than simply cutting.
- ❌ As a general argument for fewer options. The unconditional form does not
  survive meta-analysis, and "we reduced the choices" is not on its own a
  usability improvement.
- ❌ Catalogs users come specifically to browse widely; invest in filtering there.

**Ethical guard.** Curate to help the user decide, not to bury the option that
serves them — hiding the free tier in noise, or trimming to the options with the
best margin, is the same move turned around. And read the four conditions as a
recipe: a picker *built* to be incomparable, effortful and default-less
manufactures the overload it then relieves by steering.

**Detection.** Absent: a long flat set with no filtering, no comparison
affordance, and no recommended option. Weakened: a recommendation exists but
names the vendor's preference rather than the common case, or the filters cut on
attributes that do not distinguish the options.

**Collides with.** `UX-P07` — Hick's law holds broadly and is about how long the
choice takes; this entry holds only under its conditions and is about whether
the user chooses at all. Where they disagree on cutting a set, cut for speed on
Hick's law, and fix comparability rather than cutting on this one.

**Example.** A plan page shows three tiers, a comparison table on the attributes
that actually differ, and one tier marked `"recommended"` — instead of ten tiers
listed flat.

**Provenance.**
`standing:` qualified
`guard-basis:` independent of source
`origin:` Iyengar & Lepper 2000 — When choice is demotivating: Can one desire too much of a good thing?, Journal of Personality and Social Psychology 79(6): 995–1006 — peer-reviewed — https://doi.org/10.1037/0022-3514.79.6.995 — the jam study
`contra:` Scheibehenne, Greifeneder & Todd 2010 — Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload, Journal of Consumer Research 37(3): 409–425 — peer-reviewed — https://doi.org/10.1086/651235 — pools fifty experiments and finds a mean effect indistinguishable from zero, with no reliable moderator identified at the time
`warrant:` Chernev, Böckenholt & Goodman 2015 — Choice overload: A conceptual review and meta-analysis, Journal of Consumer Psychology 25(2): 333–358 — peer-reviewed — https://doi.org/10.1016/j.jcps.2014.08.002 — recovers the effect conditionally, on choice-set complexity, decision-task difficulty, preference uncertainty and decision goal; these are the four conditions this entry states
`mis-citation:` Schwartz 2004 — The Paradox of Choice: Why More Is Less, Ecco — trade book — https://openlibrary.org/works/OL272375W — the phrase is routinely cited as though it named a finding. It is the title of a trade book popularising Iyengar & Lepper, and adds no evidence

---

## UX-P15 — Occam's razor

**Cue.** a screen has accumulated elements and needs cutting

**Principle.** Among designs that do the job, prefer the one with the fewest
moving parts; make every element earn its place *(our stance)*.

**Mechanism.** An element costs something to skip past, and that cost is paid on
every viewing while its benefit is usually banked once. This is a cognitive-load
argument, and it is warranted in `UX-P07` and `UX-P08` — not by the razor, which
is a rule about not multiplying explanations and says nothing about attention.

**Applies / doesn't.**
- ✅ Reviewing an existing screen for elements to cut; resisting accretion on a
  view many hands have edited.
- ❌ Where "simpler" strips a genuine affordance and pushes the work onto the
  user — see `UX-P13`. The goal is a simpler task, not a barer screen.
- ❌ As evidence. This is a design aphorism, not a finding; do not cite it to
  settle a question a study could settle.

**Ethical guard.** Cutting serves the user only when nothing consequential
leaves the screen. An element removed because it complicates the sell — the
total price, the route to cancel, the terms of a renewal — is concealment
wearing the language of simplicity. The test is whose life the cut makes simpler.

**Detection.** Absent: the screen carries elements nobody can name a job for —
decorative panels, a second call to action, a legend for a code nothing uses.
Weakened: things were removed, but the cheap ones went; the screen is shorter
and the task is unchanged.

**Collides with.** `UX-P13` — where cutting an element would move work onto the
user, Tesler's law wins: keep the element and absorb the work in the system.

**Example.** A checkout drops the company field and puts the second address line
behind a toggle, while the shipping total stays on screen.

**Provenance.**
`standing:` unevidenced
`guard-basis:` independent of source
`origin:` William of Ockham ca. 1287–1347 — the principle of ontological parsimony; no single work of his states it, and the canonical Latin formulation is not his — essay — https://plato.stanford.edu/entries/ockham/ — read: Stanford Encyclopedia of Philosophy, "William of Ockham" §4.1, which records that the formulation is "nowhere to be found in his texts" — accessed: 2026-08-19
`warrant:` Cowan 2001 — The magical number 4 in short-term memory: A reconsideration of mental storage capacity, Behavioral and Brain Sciences 24(1): 87–114 — peer-reviewed — https://doi.org/10.1017/S0140525X01003922 — borrowed, and marked as borrowed. What an added element costs is argued in `UX-P07` and `UX-P08`; this entry contributes the editorial preference for the smaller design and nothing else, which is what `standing: unevidenced` records

---

## UX-P16 — Decoy effect

**Cue.** a comparison set includes an option nobody should pick

**Principle.** An option nobody should pick can still change which of the others
gets picked; audit your own comparison sets for one rather than adding one.

**Mechanism.** An alternative that is worse than one option on every attribute,
and not worse than another, hands the comparison an easy verdict where it had
none — the option that dominates it starts reading as the obvious pick. The
effect largely disappears once options are described the way real products are,
in images and prose, rather than as tidy attribute tables.

**Applies / doesn't.**
- ✅ Auditing whether your own tiers already contain an accidental decoy.
- ✅ Explaining *why* a comparison set steers the way it does.
- ❌ As a tactic. Past the ethics, the record does not support it working in the
  conditions a product ships in.
- ❌ Anywhere money is being spent under pressure.

**Ethical guard.** This is the catalog's clearest manipulation risk. Use it to
detect and remove accidental decoys and to present honest, comparable options —
never to engineer a phantom option that steers users off what they would choose
informed. The weak robustness record argues the same way: a move that
unreliably shifts choice but reliably reads as manipulation once noticed is a
bad trade.

**Detection.** Absent: nobody has checked whether a tier exists only to flatter
the one beside it. Weakened: the decoy is gone, but the remaining options are
still described on the attributes that make one of them dominate.

**Example.** Audit finding: a print-only tier priced level with print-plus-digital
exists only to make the bundle look better — flag it, do not ship it.

**Provenance.**
`standing:` qualified
`guard-basis:` stricter than source
`origin:` Huber, Payne & Puto 1982 — Adding Asymmetrically Dominated Alternatives: Violations of Regularity and the Similarity Hypothesis, Journal of Consumer Research 9(1): 90–98 — peer-reviewed — https://doi.org/10.1086/208899 — "asymmetric dominance" is the paper's own term. It presents the move as something to do, which is what this entry's guard forbids
`warrant:` Huber, Payne & Puto 2014 — Let's Be Honest About the Attraction Effect, Journal of Marketing Research 51(4): 520–525 — peer-reviewed — https://doi.org/10.1509/jmr.14.0208 — the original authors concede the boundary conditions while defending the effect within them; the warrant for stating it at all
`contra:` Frederick, Lee & Baskin 2014 — The Limits of Attraction, Journal of Marketing Research 51(4): 487–507 — peer-reviewed — https://doi.org/10.1509/jmr.12.0061 — the effect is essentially absent once options carry images or realistic descriptions instead of numeric attribute lists
`contra:` Yang & Lynn 2014 — More Evidence Challenging the Robustness and Usefulness of the Attraction Effect, Journal of Marketing Research 51(4): 508–513 — peer-reviewed — https://doi.org/10.1509/jmr.14.0020 — the same direction, in real purchase contexts
`mis-citation:` Ariely 2008 — Predictably Irrational, the Economist subscription case — trade book — https://openlibrary.org/works/OL9302660W — the demonstration usually offered as the classic result is a classroom exercise built on one observed pricing page, not a finding from the 1982 paper. Usable as illustration, never as evidence

---

## UX-P17 — Framing effect

**Cue.** copy states a fact that could be framed as gain or loss

**Principle.** The same fact framed as a gain or a loss, a percentage or a count,
changes the decision; pick the frame that is both accurate and clearest.

**Mechanism.** Three different things travel under one name. Describing a
*risky* option by what is saved or lost flips risk preference. Describing a
single *attribute* positively or negatively shifts how it is evaluated — this is
what almost every interface is actually doing. Describing a *goal* by what is
gained or forgone changes how persuasive it is. They run on different mechanisms
and come in different sizes, and an interface decision is hardly ever the first.

**Applies / doesn't.**
- ✅ Copy for a choice with real trade-offs: `"90% fat-free"` against `"10% fat"`
  is attribute framing, `"save 3 hours"` against `"lose 3 hours"` is goal framing.
- ❌ Where the honest frame is neutral and any spin misleads.
- ❌ Citing the risky-choice literature to settle an attribute-framing decision.
  They are separate findings with separate evidence.

**Ethical guard.** Legitimate when both frames are true and you pick the clearer.
Manipulation when the frame hides a downside or inflates a benefit. The frame
must not change what a careful user would conclude.

**Detection.** Absent: copy states a raw fact where a frame would clarify it — a
version count where a benefit was meant. Weakened: a frame was chosen, but for
its effect rather than its clarity, putting the honest reading one step further
away.

**Collides with.** `UX-P03` — loss aversion recommends the loss frame because it
moves people; this entry recommends the frame the user reads most accurately.
Where they differ, accuracy wins: the frame must not change the conclusion.

**Example.** A backup setting reads `"Protects the last 30 days of your work"`
rather than `"Enable versioning"`.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Tversky & Kahneman 1981 — The Framing of Decisions and the Psychology of Choice, Science 211(4481): 453–458 — peer-reviewed — https://doi.org/10.1126/science.7455683 — risky-choice framing: one outcome distribution described as lives saved or as lives lost
`warrant:` Levin, Schneider & Gaeth 1998 — All Frames Are Not Created Equal: A Typology and Critical Analysis of Framing Effects, Organizational Behavior and Human Decision Processes 76(2): 149–188 — peer-reviewed — https://doi.org/10.1006/obhd.1998.2804 — the three-way typology, and the source for the attribute and goal cases this entry's examples belong to
`warrant:` Klein et al. 2018 — Many Labs 2: Investigating Variation in Replicability Across Samples and Settings, Advances in Methods and Practices in Psychological Science 1(4): 443–490 — peer-reviewed — https://doi.org/10.1177/2515245918810225 — the risky-choice framing item replicates
