# Perception — attention, grouping & layout

For visual hierarchy, attention, grouping, and navigation. Entry template:
`FORMAT.md`. Catalog rules: `SKILL.md`. This was the worst-attributed family in
the catalog: six of these nine entries named no source at all, and two of them
stated the popular UX reading rather than the finding — read the mechanism of
`UX-P10` and `UX-P18` before citing either.

- `UX-P09` — Fitts's law
- `UX-P10` — Von Restorff (isolation effect)
- `UX-P18` — Aesthetic-usability effect
- `UX-P19` — Jakob's law
- `UX-P20` — Serial position effect
- `UX-P21` — Proximity (Gestalt)
- `UX-P22` — Similarity (Gestalt)
- `UX-P23` — Common region
- `UX-P24` — Closure (often filed under Prägnanz)

---

## UX-P09 — Fitts's law

**Cue.** a target must be hit fast: CTA, confirm/cancel, touch target

**Principle.** Movement time grows with the logarithm of the distance-to-size
ratio, so size buys more than nearness over the range a screen offers: make the
primary target large and reachable, and keep destructive ones small and set
apart *(our stance)*.

**Mechanism.** Aimed movement is a speed–accuracy trade: the harder a target is
to hit relative to the distance travelled, the longer the movement takes, and
the relation is logarithmic rather than proportional — doubling the distance to
a button adds far less time than halving its width does. Shrinking a target
under a fixed time budget therefore does not merely slow the user, it raises the
error rate, which is the actual reason a small and distant destructive action is
safer. Finger touch adds a floor the model has no term for: below roughly a
fingertip's width, extra size stops buying time and buys only accuracy.

**Applies / doesn't.**
- ✅ Primary CTAs, confirm/cancel pairs, touch targets, thumb reach on mobile.
- ✅ Choosing between moving a control nearer and making it bigger — this is the
  question the law answers, and it usually answers "bigger".
- ❌ As an argument about *which* action should be the easy one. The law is a
  motor model; it ranks nothing, and where the destructive action goes is an
  error-cost judgement *(our stance)*.
- ❌ Below fingertip scale on touch, where the plain law stops predicting.

**Ethical guard.** Keep destructive or irreversible actions off the easy path so
they are not triggered by accident. Never run the law the other way in a
consequential pair: enlarging "accept" while shrinking "decline" makes the cheap
movement the one the business wants, which is confirmshaming at the motor level.
Nothing in the source speaks to any of this — it is a model of pointing, and it
forbids nothing.

**Detection.** Absent: the primary action is one small control among equals, or
a confirm/cancel pair puts the destructive option under the resting thumb.
Weakened: the target looks large but its hit area stops at the visible label, or
a cramped control was moved nearer instead of made bigger.

**Example.** The primary button spans the content width within thumb reach;
"Delete account" is a small text link at the foot of a settings page.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Fitts 1954 — The information capacity of the human motor system in controlling the amplitude of movement, Journal of Experimental Psychology 47(6): 381–391 — peer-reviewed — https://doi.org/10.1037/h0055392 — three tasks, none of them a screen: reciprocal stylus tapping, disc transfer, pin transfer, with subjects instructed to emphasize accuracy rather than speed
`warrant:` MacKenzie 1992 — Fitts' Law as a Research and Design Tool in Human-Computer Interaction, Human-Computer Interaction 7(1): 91–139 — peer-reviewed — https://doi.org/10.1207/s15327051hci0701_3 — the Shannon formulation the HCI literature actually uses, and the form in which the law was validated on pointing devices
`warrant:` Fitts & Peterson 1964 — Information capacity of discrete motor responses, Journal of Experimental Psychology 67(2): 103–112 — peer-reviewed — https://doi.org/10.1037/h0045689 — the discrete-target companion, which is the case a button press resembles rather than the reciprocal tapping of the original
`warrant:` Bi, Li & Zhai 2013 — FFitts law: modeling finger touch with Fitts' law, CHI '13: 1363–1372 — conference paper — https://doi.org/10.1145/2470654.2466180 — adds the absolute precision floor of the fingertip, which the 1954 model has no term for

---

## UX-P10 — Von Restorff (isolation effect)

**Cue.** one action should dominate the others visually

**Principle.** An item is singled out by differing from a uniform set, not by
being loud; earn a dominant action by flattening everything around it.

**Mechanism.** The odd item in a list is remembered better than its neighbours —
but not because it is perceptually striking. The original work placed the
isolate where it would *not* stand out at encoding and the effect appeared
anyway; what does the work is the contrast between a heterogeneous set and a
homogeneous one. Two consequences. Uniformity around the primary action is the
lever (`UX-P22`), and weight added to the action itself on an already busy
screen is not. And every result here measures *recall*: that the dominant
element is also the one acted on belongs to the attention-capture literature,
which is a separate and weaker claim.

**Applies / doesn't.**
- ✅ Emphasizing a single primary action on a screen whose other controls are
  visually uniform.
- ✅ Making one row, plan, or status break an otherwise regular set.
- ❌ Screens where several elements already compete. Adding weight to one does
  not isolate it, it adds another competitor.
- ❌ As a prediction that the emphasized element will be *chosen*. It is a memory
  effect; the click is a different claim with different evidence.

**Ethical guard.** Emphasis must track the user's interest, not the seller's.
Rendering the accept path as a filled button and the decline path as faint grey
text is the isolation effect turned against the reader — the standard
confirmshaming layout. In a consequential pair, both options stay legible and
reachable at a glance; only visual weight may differ, and only where the
emphasized option is the one most users actually want. The source is silent on
all of it.

**Detection.** Absent: a screen offers several equally weighted actions and none
reads as primary. Weakened: the primary action is emphasized but sits among
other emphasized elements, so nothing is isolated — the fix is a quieter
background, not a louder button.

**Example.** One filled button on the screen; every other control is a plain
link of the same weight, so the filled one is the only break in the set.

**Provenance.**
`standing:` reinterpreted
`guard-basis:` independent of source
`origin:` von Restorff 1933 — Über die Wirkung von Bereichsbildungen im Spurenfeld, Psychologische Forschung 18(1): 299–342 — peer-reviewed — https://doi.org/10.1007/BF02409636 — part I of a series from Köhler's lab; never translated into English, which is the proximate cause of the misreading this entry corrects
`warrant:` Hunt 1995 — The subtlety of distinctiveness: What von Restorff really did, Psychonomic Bulletin & Review 2(1): 105–112 — peer-reviewed — https://doi.org/10.3758/BF03214414 — written to correct the salience reading: von Restorff presented evidence that perceptual salience is not necessary, and argued the difference must be weighed against the similarity of its context
`warrant:` Schmidt & Schmidt 2017 — Revisiting von Restorff's early isolation effect, Memory & Cognition 45(2): 194–207 — peer-reviewed — https://doi.org/10.3758/s13421-016-0651-6 — the modern replication, run in the heterogeneous-versus-homogeneous-list design the original used
`current:` Theeuwes 1992 — Perceptual selectivity for color and form, Perception & Psychophysics 51(6): 599–606 — peer-reviewed — https://doi.org/10.3758/BF03211656 — where the "and therefore acted on" half has to be argued from: capture by a singleton, measured on attention rather than on memory
`mis-citation:` Köhler & von Restorff 1935 — Analyse von Vorgängen im Spurenfeld, Psychologische Forschung 21: 56–112 — peer-reviewed — https://doi.org/10.1007/BF02441202 — part II of the series is widely dated 1935; Crossref dates it 1937

---

## UX-P18 — Aesthetic-usability effect

**Cue.** a first impression or trust-sensitive screen

**Principle.** A polished screen is rated more usable than a plain one carrying
the same defects — treat that as a fact about *ratings*, not as evidence that
polish makes an interface work.

**Mechanism.** Beauty and perceived usability correlate strongly at first sight,
but the correlation collapses once how easy the screen is to *process* is held
constant: both judgements look downstream of fluency rather than one causing the
other. Under actual use the arrow reverses — an interface that works comes to be
seen as attractive, not the converse. What survives is a measurement effect with
real teeth: appearance shifts the scores a usability test produces, so an
attractive prototype will be rated more usable than an ugly one with identical
faults.

**Applies / doesn't.**
- ✅ First impressions, landing screens, trust-sensitive moments, the
  marketing-to-product handoff.
- ✅ Reading a usability test: discount satisfaction scores gathered on a
  polished prototype relative to a plain one.
- ❌ As a claim that polish improves usability, or that users forgive flaws.
  Nobody measured error tolerance; the forgiveness clause has no source.
- ❌ As a reason to fund visual work ahead of fixing a broken flow — the
  measured causal arrow runs the other way.

**Ethical guard.** Beauty may not be used to paper over a deceptive or broken
experience. The rule bites hardest in testing: shipping on scores collected from
a beautiful prototype is how a known defect reaches production with evidence
apparently behind it. The source measures perceptions of cash-dispenser layouts
and licenses no ethical claim either way.

**Detection.** Absent: a working screen reads as unfinished — default spacing,
no hierarchy — on a surface that carries a first impression. Weakened: polish is
present and a usability claim rests on it, e.g. a redesign signed off on
satisfaction scores with no task-completion data behind them.

**Example.** A new-user dashboard's empty state is spaced and typeset
deliberately, and the team still gates the redesign on completion rate rather
than on the satisfaction score that rose with it.

**Provenance.**
`standing:` reversed (perceived-usability component)
`guard-basis:` independent of source
`origin:` Kurosu & Kashimura 1995 — Apparent usability vs. inherent usability: experimental analysis on the determinants of the apparent usability, CHI '95 Conference Companion: 292–293 — conference paper — https://doi.org/10.1145/223355.223680 — 26 layout variants of a cash-dispenser interface, concluding that apparent usability is affected by aesthetics rather than by inherent usability; a two-page companion abstract, thinner than the effect's fame suggests
`warrant:` Tractinsky, Katz & Ikar 2000 — What is beautiful is usable, Interacting with Computers 13(2): 127–145 — peer-reviewed — https://doi.org/10.1016/S0953-5438(00)00031-X — the replication that gave the effect its slogan, after Tractinsky 1997 (CHI '97: 115–122, https://doi.org/10.1145/258549.258626) had tested and rejected the reading that the 1995 result was a Japanese cultural artefact
`warrant:` Sonderegger & Sauer 2010 — The influence of design aesthetics in usability testing: effects on user performance and perceived usability, Applied Ergonomics 41(3): 403–410 — peer-reviewed — https://doi.org/10.1016/j.apergo.2009.09.002 — two functionally identical phones differing only in appearance; the attractive one produced both higher perceived usability and faster completion, which is the methodological warning this entry keeps
`contra:` Tuch, Roth, Hornbæk, Opwis & Bargas-Avila 2012 — Is beautiful really usable? Toward understanding the relation between usability, aesthetics, and affect in HCI, Computers in Human Behavior 28(5): 1596–1607 — peer-reviewed — https://doi.org/10.1016/j.chb.2012.03.024 — crossing aesthetics with usability found an effect of usability on perceived aesthetics and none in the other direction
`contra:` Preßler, Schmid & Hurtienne 2023 — Statistically Controlling for Processing Fluency Reduces the Aesthetic-Usability Effect, CHI EA '23: 1–7 — conference paper — https://doi.org/10.1145/3544549.3585739 — the raw effect replicated, then fell by more than half once processing fluency was partialled out
`contra:` Hassenzahl 2004 — The Interplay of Beauty, Goodness, and Usability in Interactive Products, Human-Computer Interaction 19(4): 319–349 — peer-reviewed — https://doi.org/10.1207/s15327051hci1904_2 — beauty and pragmatic quality come out largely independent once a product is actually used
`figure:` "r = .79" and "r = .34" — Preßler, Schmid & Hurtienne 2023: the aesthetic-usability correlation before and after processing fluency is partialled out
`mis-citation:` Lidwell, Holden & Butler 2003 — Universal Principles of Design (Rockport) — trade book — ISBN 978-1-59253-007-6 — the phrase "aesthetic-usability effect" is theirs and is routinely attributed to the 1995 paper; Kurosu & Kashimura never used it

---

## UX-P19 — Jakob's law

**Cue.** a control or layout departs from what users meet elsewhere

**Principle.** Users spend most of their time on *other* products and arrive
expecting yours to work the same way; depart from a convention only where you
can say what the departure buys.

**Mechanism.** A first encounter is read through the patterns the genre has
already taught. Users hold strong, shared expectations about where the cart, the
search field and the navigation sit, and a page that looks like others of its
kind is judged better on sight than one that does not. The law itself is a
practitioner's heuristic rather than a finding: what has been measured is the
expectation and the preference for the typical, not the transfer of mental
models the phrase implies.

**Applies / doesn't.**
- ✅ Placement of navigation, search, cart, account and settings; standard
  control behaviour; icon meaning.
- ✅ Judging a novel interaction — it has to earn the cost of being taught.
- ❌ Where the convention is genuinely worse for the case at hand, or where the
  genre has no settled convention to inherit.
- ❌ As evidence about learning transfer. No study of Nielsen's stands behind
  the law; cite the expectation work instead.

**Ethical guard.** A convention is a promise about what a control will do, so
borrowing its look while changing its effect is deception — a close button that
confirms, a "Continue" that subscribes, an advertisement shaped like a result.
Familiarity is learning the user paid for elsewhere; spend it on their behalf or
not at all. The source, a practitioner article, makes no such argument.

**Detection.** Absent: a common object sits where its genre never puts it —
search buried in a menu, the cart mid-page — with nothing gained in return.
Weakened: the convention is followed visually but not behaviourally, so a
control looks standard and acts otherwise.

**Example.** The cart is a top-right icon and search is a magnifier in the
header, because that is where users already look; the one non-standard gesture
in the app is introduced by a first-run hint.

**Provenance.**
`standing:` qualified
`guard-basis:` independent of source
`origin:` Nielsen 2000 — End of Web Design, Nielsen Norman Group Alertbox, 22 July 2000 — practitioner article — https://www.nngroup.com/articles/end-of-web-design/ — states the law verbatim under its own heading, "Users spend most of their time on other sites"; the one place NN/g is a primary source in this catalog, because it is the author publishing his own law — accessed: 2026-08-19
`warrant:` Roth, Schmutz, Pauwels, Bargas-Avila & Opwis 2010 — Mental models for web objects: Where do users expect to find the most frequent objects in online shops, news portals, and company web pages?, Interacting with Computers 22(2): 140–152 — peer-reviewed — https://doi.org/10.1016/j.intcom.2009.10.004 — measures the shared placement expectations the heuristic asserts, which is the empirical form of this entry's own example
`warrant:` Tuch, Presslaber, Stöcklin, Opwis & Bargas-Avila 2012 — The role of visual complexity and prototypicality regarding first impression of websites: working towards understanding aesthetic judgments, International Journal of Human-Computer Studies 70(11): 794–811 — peer-reviewed — https://doi.org/10.1016/j.ijhcs.2012.06.003 — prototypicality, how far a page looks like others of its genre, drives first impressions

---

## UX-P20 — Serial position effect

**Cue.** the order of a list, menu, or sequence matters

**Principle.** Position in a list is not neutral: the first and last places draw
disproportionate attention and clicks, so put what matters at the ends and never
bury the option the user came for in the middle.

**Mechanism.** In free recall the first and last items are remembered best. An
on-screen list is not a recall task — the items are still there to be read — so
the memory curve is not what carries the advice; what transfers is a position
effect measured directly on *clicking*, where the head of a list takes the most
attention and the final position takes more than its neighbours. The memory
result also has a boundary the interface version never inherits: a filled delay
between reading and recalling abolishes the recency limb while leaving primacy
intact.

**Applies / doesn't.**
- ✅ Ordering navigation, menus, option lists, feature lists, onboarding steps.
- ✅ Auditing a list whose least favourable option has been parked in the middle.
- ❌ Sequences with no importance ranking — alphabetical directories, sorted
  tables, results the user scans by relevance.
- ❌ As a memory argument about items that are on screen. If the list is visible,
  it is being read, not recalled.

**Ethical guard.** The ends are the loudest positions in a list, so putting what
serves the business there and what serves the user in the middle is a dark
pattern at the level of ordering — the cancellation link parked mid-menu, the
cheapest plan mid-row. Order by the user's interest; where a business preference
sets the order, it must be one the user would endorse if told. Neither the
recall literature nor the click study prescribes any of this.

**Detection.** Absent: an important destination or option sits mid-list with no
ordering rationale anyone can state. Weakened: the ends are used, but for the
two items the business favours rather than the two the user needs.

**Example.** A feature list opens with the capability that decides the purchase
and closes with the second strongest, leaving the rest in between.

**Provenance.**
`standing:` qualified (screen transfer)
`guard-basis:` independent of source
`origin:` Ebbinghaus 1885 — Über das Gedächtnis: Untersuchungen zur experimentellen Psychologie (Duncker & Humblot) — book (academic) — https://psychclassics.yorku.ca/Ebbinghaus/index.htm — position effects in serial learning; the bowed curve was in print earlier still, so this is the canonical origin rather than the first — read: Ruger & Bussenius 1913 translation, Memory: A Contribution to Experimental Psychology — accessed: 2026-08-19
`warrant:` Murdock 1962 — The serial position effect of free recall, Journal of Experimental Psychology 64(5): 482–488 — peer-reviewed — https://doi.org/10.1037/h0045106 — the canonical free-recall curve
`warrant:` Murphy, Hofacker & Mizerski 2006 — Primacy and Recency Effects on Clicking Behavior, Journal of Computer-Mediated Communication 11(2): 522–535 — peer-reviewed — https://doi.org/10.1111/j.1083-6101.2006.00025.x — the position effect measured on clicks rather than on recall, which is the evidence this entry's advice actually rests on
`contra:` Glanzer & Cunitz 1966 — Two storage mechanisms in free recall, Journal of Verbal Learning and Verbal Behavior 5(4): 351–360 — peer-reviewed — https://doi.org/10.1016/S0022-5371(66)80044-0 — a filled delay abolishes recency and leaves primacy intact, so the recall reading of the claim carries a boundary condition the interface reading does not
`current:` Stigler 1978 — Some forgotten work on memory, Journal of Experimental Psychology: Human Learning and Memory 4(1): 1–4 — peer-reviewed — https://doi.org/10.1037/0278-7393.4.1.1 — recovers Nipher 1878, who published the bowed serial position curve before Ebbinghaus and was lost to the field

---

## UX-P21 — Proximity (Gestalt)

**Cue.** spacing must say what belongs with what

**Principle.** Elements placed close together are read as one thing; group with
space before reaching for a line or a box.

**Mechanism.** Nearness is the first grouping factor the eye applies, ahead of
any drawn boundary, and it operates as a continuous function of distance rather
than a threshold: what decides the grouping is the gap between items relative to
the gaps around them. A label a hair closer to the field above it than to the
one below belongs to the field above, whatever the designer intended.

**Applies / doesn't.**
- ✅ Form field grouping, label-to-input pairing, card content, clusters of
  related actions.
- ✅ Removing dividers — if the spacing already says it, the rule is redundant.
- ❌ — foundational; the usual failure is under-using space, not over-using it.

**Ethical guard.** Proximity assigns meaning, so placing an unrelated charge,
consent, or add-on inside a block the user reads as a single unit makes them
agree to something they never grouped with the decision. Keep a consent beside
what it consents to and a price beside what it buys. The source describes
perception and prescribes nothing.

**Detection.** Absent: labels sit equidistant from the fields above and below,
or a long form runs at uniform spacing so no section reads as a section.
Weakened: groups are drawn with rules and borders while the spacing inside them
matches the spacing between them, so the two signals disagree.

**Collides with.** `UX-P23` — a drawn boundary overrides spacing outright, so a
box in the wrong place cancels correct grouping rather than reinforcing it.

**Example.** A label sits tight above its field with a wide gap before the next,
so the pairing is unambiguous without a divider.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Wertheimer 1923 — Untersuchungen zur Lehre von der Gestalt. II, Psychologische Forschung 4(1): 301–350 — peer-reviewed — https://doi.org/10.1007/BF00410640 — nearness (Nähe) is the first factor named — read: Ellis 1938 abridged translation, "Laws of Organization in Perceptual Forms", A Source Book of Gestalt Psychology: 71–88
`warrant:` Kubovy & Wagemans 1995 — Grouping by Proximity and Multistability in Dot Lattices: A Quantitative Gestalt Theory, Psychological Science 6(4): 225–234 — peer-reviewed — https://doi.org/10.1111/j.1467-9280.1995.tb00597.x — proximity grouping as a measurable continuous function of distance rather than a binary, which is what makes relative spacing the operative variable
`current:` Wagemans, Elder, Kubovy, Palmer, Peterson, Singh & von der Heydt 2012 — A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure–ground organization, Psychological Bulletin 138(6): 1172–1217 — peer-reviewed — https://doi.org/10.1037/a0029333 — the modern review to consult in place of the 1923 paper, and the source that records which grouping principles are classical and which are not

---

## UX-P22 — Similarity (Gestalt)

**Cue.** elements of the same kind must read as the same kind

**Principle.** Shared colour, shape, or size is read as shared meaning; make
same-function things look alike, and make different ones actually differ.

**Mechanism.** Likeness groups items across distance: the eye assembles a set
out of whatever repeats, and does so before anything is read. That is what makes
a visual language learnable — one accent colour used only for links teaches
interactivity within a screen or two — and it is also what makes uniformity the
precondition for emphasis, since an element can only stand out against a set
that is otherwise the same (`UX-P10`).

**Applies / doesn't.**
- ✅ Link and button styling, status colours, iconography, table row treatments.
- ✅ Preparing a screen for one dominant action by flattening everything else.
- ❌ Where uniformity flattens a hierarchy the user needs — pair with `UX-P10`
  to keep the primary action distinct.
- ❌ As a licence to reuse one style for two behaviours because they look
  adjacent.

**Ethical guard.** If two things look the same, the user is entitled to expect
them to behave the same. Styling an advertisement as content, a sponsored row as
an organic one, or an upsell as a system message uses the grouping to launder
one kind of thing as another. Wertheimer's factor is descriptive; the obligation
is ours.

**Detection.** Absent: two controls with the same function are styled
differently across screens, or the accent colour appears on text that does
nothing. Weakened: the system holds within a screen but drifts across the
product, so the mapping the user learned stops paying off.

**Example.** Every clickable link carries the one accent colour and static text
never does, so the user learns in one screen what is interactive.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Wertheimer 1923 — Untersuchungen zur Lehre von der Gestalt. II, Psychologische Forschung 4(1): 301–350 — peer-reviewed — https://doi.org/10.1007/BF00410640 — similarity (Gleichheit) is the second factor named — read: Ellis 1938 abridged translation, "Laws of Organization in Perceptual Forms", A Source Book of Gestalt Psychology: 71–88
`warrant:` Wagemans, Elder, Kubovy, Palmer, Peterson, Singh & von der Heydt 2012 — A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure–ground organization, Psychological Bulletin 138(6): 1172–1217 — peer-reviewed — https://doi.org/10.1037/a0029333 — the modern review; classifies similarity among the classical grouping principles and gathers the evidence accumulated for it

---

## UX-P23 — Common region

**Cue.** a card, panel, or section boundary groups content

**Principle.** A shared enclosure groups what sits inside it and overrides both
distance and likeness in doing so; it is the strongest grouping tool available,
which is the reason to reach for it last.

**Mechanism.** Elements inside one bounded region read as a unit even where
proximity and similarity argue otherwise — the enclosure beats both outright,
which is why a card binds content that spacing alone would separate. A filled or
uniformly coloured region does the same work ahead of any classical factor, and
that is what a card physically is. The strength is the hazard: enclosure cannot
be applied gently, so every extra box competes with the boxes already there.

**Applies / doesn't.**
- ✅ Cards, panels, grouped settings, toolbars, sectioned forms — wherever the
  grouping must be unmistakable.
- ✅ Binding an action to the content it acts on when the two cannot sit
  adjacent.
- ❌ As a first resort. Proximity and similarity carry most grouping at no
  visual cost; boxes spend a budget that runs out.
- ❌ Where the boundary would assert that things belong together which do not.

**Ethical guard.** An enclosure asserts that what is inside belongs together, so
putting a pre-checked add-on, an optional fee, or a third-party consent inside
the order-summary card makes it read as part of the purchase. What shares a card
must share a fate. Palmer's demonstrations settle a perceptual question and
license nothing here.

**Detection.** Absent: related settings run as a flat list with no boundary, so
where a section ends is guesswork. Weakened: every group is a card, so the page
is boxes within boxes and enclosure has stopped carrying meaning — or a card has
a border but padding so tight that its content reads with the neighbours.

**Collides with.** `UX-P21` — where a boundary and the spacing disagree, the
boundary wins; Palmer shows enclosure overriding proximity outright. That is a
reason to use it sparingly, not a reason to prefer it.

**Example.** A settings section wraps its toggles and its "Save" button in one
card, so the button is visibly bound to the fields it applies to.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Palmer 1992 — Common region: A new principle of perceptual grouping, Cognitive Psychology 24(3): 436–447 — peer-reviewed — https://doi.org/10.1016/0010-0285(92)90014-S — demonstrations analogous to Wertheimer's own displays show the factor overcoming proximity and similarity, and argue it reduces to neither
`warrant:` Palmer & Rock 1994 — Rethinking perceptual organization: The role of uniform connectedness, Psychonomic Bulletin & Review 1(1): 29–55 — peer-reviewed — https://doi.org/10.3758/BF03200760 — a single connected region of uniform colour or texture is grouped as one unit prior to the classical factors, which is what a filled card does
`warrant:` Wagemans, Elder, Kubovy, Palmer, Peterson, Singh & von der Heydt 2012 — A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure–ground organization, Psychological Bulletin 138(6): 1172–1217 — peer-reviewed — https://doi.org/10.1037/a0029333 — classifies common region among the new grouping principles, not the classical ones
`mis-citation:` Wertheimer 1923 — Untersuchungen zur Lehre von der Gestalt. II, Psychologische Forschung 4(1): 301–350 — peer-reviewed — https://doi.org/10.1007/BF00410640 — common region is routinely filed under the 1923 Gestalt canon; the factors listed there are proximity, similarity, common fate, direction, closure, good curve, objective set, past experience and figure–ground, and common region is absent from them by sixty-nine years

---

## UX-P24 — Closure (often filed under Prägnanz)

**Cue.** structure could be implied by alignment instead of drawn

**Principle.** The eye completes an implied form, so alignment and space can
carry structure that would otherwise be drawn — provided the completion the user
makes is the one you meant.

**Mechanism.** Closure is one grouping factor among several: an incomplete
figure resolves to the complete one it most nearly is, and a set of aligned
items resolves to a column with no rule drawn. Two things it is not. It is not
the overarching tendency toward the best available organization — that umbrella
is a separate and looser claim, and it says organization will be as good as the
prevailing conditions allow, not that less is better. And it is not a licence
for minimalism: goodness is a property of the whole organization rather than a
count of elements, and emphasizing a characteristic feature can serve it as much
as removing detail does.

**Applies / doesn't.**
- ✅ Implying columns through alignment, replacing dividers with space, minimal
  iconography that resolves to a known shape.
- ✅ Deciding whether a border carries meaning or only reassurance.
- ❌ Where the implied structure is genuinely ambiguous. The reader should not
  have to solve the layout — draw the line.
- ❌ As an argument that removing elements improves perception. Fewer parts is
  not the same thing as a better organization.

**Ethical guard.** A completed form is one the user filled in themselves, which
makes implication a way to be misread on purpose: a price block that resolves as
a total while a fee arrives later, a progress indicator that implies a last step
which does not exist. Imply only what you will honour. The perceptual literature
makes no such demand.

**Detection.** Absent: every group is fenced by a rule or a box, so the page
draws lines that alignment already stated. Weakened: structure is implied but
the alignment is not tight enough to resolve, leaving the reader to guess which
column an item belongs to.

**Example.** A grid reads as aligned columns from spacing alone with no
gridlines drawn, and the one place two columns could be confused carries a rule.

**Provenance.**
`standing:` qualified
`guard-basis:` independent of source
`origin:` Wertheimer 1923 — Untersuchungen zur Lehre von der Gestalt. II, Psychologische Forschung 4(1): 301–350 — peer-reviewed — https://doi.org/10.1007/BF00410640 — closure (Geschlossenheit) is one factor among the nine listed, a sibling of proximity and similarity rather than the umbrella it is usually bundled under — read: Ellis 1938 abridged translation, "Laws of Organization in Perceptual Forms", A Source Book of Gestalt Psychology: 71–88
`warrant:` Van Geert & Wagemans 2024 — Prägnanz in visual perception, Psychonomic Bulletin & Review 31(2): 541–567 — peer-reviewed — https://doi.org/10.3758/s13423-023-02344-9 — written to clear up exactly the conflation this entry names: simple stimuli do not necessarily produce simple perceptual groupings, and emphasizing characteristic features contributes to good organization as much as removing detail
`warrant:` Palmer & Rock 1994 — Rethinking perceptual organization: The role of uniform connectedness, Psychonomic Bulletin & Review 1(1): 29–55 — peer-reviewed — https://doi.org/10.3758/BF03200760 — the second factor carrying the implied-structure advice alongside closure, and the reason a region of uniform colour needs no border
`warrant:` Koffka 1935 — Principles of Gestalt Psychology (Harcourt, Brace; Routledge reissue) — book (academic) — ISBN 978-0-415-86881-5 — the canonical Prägnanz formulation is Koffka's rather than Wertheimer's, and reads that psychological organization will always be as good as the prevailing conditions allow
`contra:` Chater 1996 — Reconciling simplicity and likelihood principles in perceptual organization, Psychological Review 103(3): 566–581 — peer-reviewed — https://doi.org/10.1037/0033-295X.103.3.566 — the simplicity reading of goodness, operationalized by Hochberg & McAlister 1953 (https://doi.org/10.1037/h0055809), has spent seventy years being argued against the rival likelihood principle, which is why this entry does not rest on it
