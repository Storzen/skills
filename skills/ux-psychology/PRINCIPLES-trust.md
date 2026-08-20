# Trust — memory, feedback & error recovery

For transactional and high-stakes screens, system feedback, error states, and
anything where trust is the currency. Entry template: `FORMAT.md`. Catalog rules:
`SKILL.md`.

Four of these seven entries — `UX-P35`, `UX-P36`, `UX-P38`, `UX-P40` — are items
from one list by one author: the usability heuristics of Nielsen & Molich
(*Heuristic evaluation of user interfaces*, CHI '90;
[10.1145/97243.97281](https://doi.org/10.1145/97243.97281)), reworded and
numbered into the familiar ten by Nielsen's later factor analysis
([10.1145/191666.191729](https://doi.org/10.1145/191666.191729)). `UX-P19` in the
perception family is the same author again. That list is an inspection method,
not a body of findings, so each of the four is stated here as the heuristic it
is and carries separately the empirical work that makes it true — work that is
sometimes older than the heuristic that gets the credit. `UX-P37` is not a
finding either: its origin is a corporate sales brief, and the number its popular
name promises is not in it.

- `UX-P12` — Peak-end rule
- `UX-P35` — Recognition over recall
- `UX-P36` — Visibility of system status
- `UX-P37` — Sub-second response (Doherty threshold)
- `UX-P38` — Error prevention & forgiveness
- `UX-P39` — Curse of knowledge
- `UX-P40` — Consistency & standards

---

## UX-P12 — Peak-end rule

**Cue.** a flow has a high point or an ending: confirmation, success, recovery

**Principle.** What the user remembers of a journey is built from its most
intense moment and its last one, and barely at all from how long it took; spend
disproportionately on those two, above all when the journey was unpleasant.

**Mechanism.** A finished episode is not replayed, it is reconstructed from a
couple of salient samples. Duration is one of the things that does not survive
the reconstruction: an episode twice as long is not remembered as twice as bad.
The peak is the sturdier of the two samples — the ending has held up less well
outside the lab — and the whole effect is best established for episodes the user
did not enjoy, which in an interface means failure, waiting, and recovery.

**Applies / doesn't.**
- ✅ Failure and recovery journeys: a declined payment, a lost draft, an outage.
  This is where the evidence for the rule is strongest.
- ✅ The last screen of a flow, including the flows that lead away: cancellation,
  downgrade, export, account deletion.
- ✅ Alongside `UX-P38` — an undo that arrives at the moment of the mistake is an
  investment in the peak and the end of the same journey.
- ❌ As permission to neglect the middle. The claim that peak and end beat the
  *average* of an experience is the strong form of the rule, and it is the one
  the field's own meta-analysis declines to endorse.
- ❌ Long, mixed journeys spread over days or sessions, where the rule predicts
  what the user recalls no better than any other summary of it.

**Ethical guard.** The rule cuts both ways: a cancellation, downgrade, or export
flow can be engineered to *end* badly so that leaving is remembered as worse than
it was. Guilt copy on the final step, a cold confirmation, a deliberately bleak
last screen — that is manipulation of the memory itself, not of the decision.
Invest in the peak and the end of every journey, including the ones that lead
away from the product. The evidence is what makes this guard non-negotiable
rather than fastidious: in the one randomised test of the lever, a gentler ending
raised the rate at which people came back years later (odds ratio 1.41) while the
total quantity of discomfort went *up*. It edits the memory, not the experience.

**Detection.** Absent: the flow ends on a bare system string — an order number,
a status code — or a failure ends at the error with nothing after it. Weakened:
the final screen has been styled while the worst moment of the flow, the one the
user will actually remember, has never been looked at.

**Example.** A failed transfer ends on a screen that says what happened, what
happened to the money, and what the next step is — and the retry lands on a
confirmation written for a person who has just had a bad minute.

**Provenance.**
`standing:` mixed (end component)
`guard-basis:` supported by source
`origin:` Fredrickson & Kahneman 1993 — Duration neglect in retrospective evaluations of affective episodes, Journal of Personality and Social Psychology 65(1): 45–55 — peer-reviewed — https://doi.org/10.1037/0022-3514.65.1.45 — the snapshot model: retrospective evaluations track peak and end affect and are largely insensitive to duration. Fredrickson is first author; the catalog previously credited "Kahneman" alone for a literature with four papers and several co-authors
`warrant:` Kahneman, Fredrickson, Schreiber & Redelmeier 1993 — When More Pain Is Preferred to Less: Adding a Better End, Psychological Science 4(6): 401–405 — peer-reviewed — https://doi.org/10.1111/j.1467-9280.1993.tb00589.x — the cold-pressor result everyone quotes. Two words of the authors' own summary are load-bearing and were dropped in the previous version of this entry: evaluations of **aversive** experiences are **often** dominated by the worst and final moments
`warrant:` Redelmeier, Katz & Kahneman 2003 — Memories of colonoscopy: a randomized trial, Pain 104(1): 187–194 — peer-reviewed — https://doi.org/10.1016/S0304-3959(03)00003-4 — 682 patients randomised to a procedure with or without a gentler final interval; the only source that tests this entry's actual advice rather than the phenomenon behind it, and the warrant for its guard
`warrant:` Redelmeier & Kahneman 1996 — Patients' memories of painful medical treatments: real-time and retrospective evaluations of two minimally invasive procedures, Pain 66(1): 3–8 — peer-reviewed — https://doi.org/10.1016/0304-3959(96)02994-6 — the clinical field study between the lab result and the trial
`warrant:` Do, Rupert & Wolford 2008 — Evaluations of pleasurable experiences: The peak-end rule, Psychonomic Bulletin & Review 15(1): 96–98 — peer-reviewed — https://doi.org/10.3758/PBR.15.1.96 — one study, three pages: the whole of the pleasant-domain evidence, which is why this entry now points designers at failure journeys first
`contra:` Kemp, Burt & Furneaux 2008 — A test of the peak-end rule with extended autobiographical events, Memory & Cognition 36(1): 132–138 — peer-reviewed — https://doi.org/10.3758/MC.36.1.132 — week-long vacations reported daily. Duration neglect held; the rule itself, verbatim, "was not an outstandingly good predictor" of recalled happiness
`contra:` Sels, Ceulemans & Kuppens 2019 — All's well that ends well? A test of the peak-end rule in couples' conflict discussions, European Journal of Social Psychology 49(4): 794–806 — peer-reviewed — https://doi.org/10.1002/ejsp.2547 — 101 couples: the negative and positive peaks predicted post-conflict affect, verbatim, "but not the end emotion". This is why `standing:` scopes the failure to the end component. Online 2018, volume year 2019
`contra:` Alaybek, Dalal, Fyffe, Aitken, Zhou, Qu, Roman & Baines 2022 — All's well that ends (and peaks) well? A meta-analysis of the peak-end rule and duration neglect, Organizational Behavior and Human Decision Processes 170: 104149 — peer-reviewed — https://doi.org/10.1016/j.obhdp.2022.104149 — reported **second-hand**: closed at the publisher, no deposited abstract, unread by this catalog. Secondary summaries agree that the peak-end effect on retrospective evaluation is large and duration neglect holds, but that the simple average predicts about as well as the peak-end composite. On that basis, and only that basis, "not its average" was removed from this entry. Corrigendum: same authors 2024, OBHDP 180: 104278, https://doi.org/10.1016/j.obhdp.2023.104278
`figure:` "odds ratio 1.41" — Redelmeier, Katz & Kahneman 2003: rate of returning for a repeat colonoscopy over a median 5.3 years of follow-up, 50.4% overall, higher for the group given the gentler ending (P = 0.038)

---

## UX-P35 — Recognition over recall

**Cue.** the user must carry something in memory across steps

**Principle.** Put the options, the prior inputs and the available actions on the
screen instead of asking the user to retrieve them; recognising a visible thing
is far cheaper than producing it from memory.

**Mechanism.** Recall makes the user generate a candidate out of nothing.
Recognition only makes them judge one already in front of them, and the gap
between the two is one of the largest and most reliable asymmetries in memory:
people recognise thousands of items they could never have listed. A screen that
names the options has converted the harder task into the easier one; a screen
that asks the user what they entered two steps ago has done the opposite.

**Applies / doesn't.**
- ✅ Menus over memorised commands, autocomplete, recently used items, visible
  filters, values carried forward between the steps of a flow.
- ✅ Confirmations and error messages that restate the value in question rather
  than referring to it.
- ❌ Expert interfaces where a memorised command beats a hunt through a menu —
  offer both. That caveat is not ours: it is Nielsen's own heuristic #7,
  flexibility and efficiency of use, which means this entry carries two items
  from the same list.

**Ethical guard.** A recognition cue borrows the authority of the user's own
memory, so it must show the user's own history. A "recently viewed" list seeded
with what you want sold, or a field pre-filled with a value the user never
entered, dresses a suggestion as a recollection — the user recognises it and
stops checking, which is exactly the effect this lever exists to produce. Label a
recommendation as one. The second edge is exposure: making something
recognisable can mean displaying it, and a stored card number or an address is
not made safer by being convenient.

**Detection.** Absent: a step asks the user to retype or remember something an
earlier step already had — a reference number, an address, a filter set.
Weakened: the value is on the screen but not where the decision is made, so the
user still carries it across a boundary.

**Example.** A multi-step booking shows the dates and passenger count from step
one at the top of every later step, and the payment screen restates them beside
the total.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Nielsen & Molich 1990 — Heuristic evaluation of user interfaces, CHI '90: 249–256 — conference paper — https://doi.org/10.1145/97243.97281 — a usability inspection method, not a study. In this nine-item list the heuristic is "minimize user memory load"; it becomes "recognition rather than recall" and heuristic #6 in the later revision. See also the journal statement of the same list, Molich & Nielsen 1990, CACM 33(3): 338–348, https://doi.org/10.1145/77481.77486
`current:` Nielsen 1994 — Enhancing the explanatory power of usability heuristics, CHI '94: 152–158 — conference paper — https://doi.org/10.1145/191666.191729 — the factor analysis of 249 usability problems that produced the ten heuristics as practitioners now meet them, and the source of this entry's wording and number
`warrant:` Shepard 1967 — Recognition memory for words, sentences, and pictures, Journal of Verbal Learning and Verbal Behavior 6(1): 156–163 — peer-reviewed — https://doi.org/10.1016/S0022-5371(67)80067-7 — near-ceiling recognition for hundreds of items; the asymmetry the heuristic asserts without citing
`warrant:` Standing 1973 — Learning 10,000 pictures, Quarterly Journal of Experimental Psychology 25(2): 207–222 — peer-reviewed — https://doi.org/10.1080/14640747308400340 — how far recognition capacity extends, and the demonstration this entry's mechanism sentence leans on
`warrant:` Anderson & Bower 1972 — Recognition and retrieval processes in free recall, Psychological Review 79(2): 97–123 — peer-reviewed — https://doi.org/10.1037/h0033773 — the generate-recognise account of *why* a visible cue is cheaper: recall runs recognition plus a generation step that a visible option removes

---

## UX-P36 — Visibility of system status

**Cue.** something happens the user cannot see

**Principle.** Every action gets feedback, the feedback reports what the system
actually did, and anything slow says which state it is in — not merely that it is
busy.

**Mechanism.** The interface is the user's only evidence about the system, so
silence is not neutral: it gets read as failure, and the user retries, leaves, or
starts doubting the parts that did work. Attention also has a shape. An
acknowledgement inside roughly 0.1 s reads as instantaneous; under about 1 s the
user's train of thought stays intact; past 10 s they have left the task, and
whatever comes back has to re-earn their attention. Those bands are what "timely"
means in practice.

**Applies / doesn't.**
- ✅ Anything asynchronous: uploads, payments, sync, background jobs, connection
  state, anything another system has to confirm.
- ✅ Percent-done progress for work long enough that the user would otherwise
  wonder whether it is stuck — the one form of feedback with an experiment
  behind it rather than a heuristic.
- ❌ Narrating trivia until feedback is noise, which trains the user to ignore
  the notice that mattered.
- ❌ A spinner standing in for a status. It says "not finished"; it does not say
  whether it is safe to close the tab.

**Ethical guard.** Status must be truthful. A spinner that implies work not
happening, or a "saved" that didn't save, breaks trust at the worst moment —
critical where money moves. Know that this is a position, not a platitude: there
is a published argument that some deceptions serve users, progress indicators
among them, and this catalog takes the opposite line on purpose. A user who finds
out that one status was cosmetic has no way to tell which of the others were.

**Detection.** Absent: an action produces no visible change, so the user does it
again — the second payment, the duplicate record. Weakened: feedback exists but
is generic where the user needs specifics, or arrives only at the end of a wait
they had already started worrying about.

**Collides with.** `UX-P37` — an optimistic update is a claim about an outcome
the system has not confirmed. Where the two conflict, this entry wins: show the
pending state rather than a result you do not have.

**Example.** A transfer moves through "Sent — awaiting confirmation" to
"Completed" or "Failed — retry", each state written from what the backend
actually reported, and a success is never shown before the backend confirms one.

**Provenance.**
`standing:` qualified (response-time bands)
`guard-basis:` contradicts source
`origin:` Nielsen & Molich 1990 — Heuristic evaluation of user interfaces, CHI '90: 249–256 — conference paper — https://doi.org/10.1145/97243.97281 — in the nine-item list this heuristic is "provide feedback"; it becomes "visibility of system status" and heuristic #1 in the later revision
`current:` Nielsen 1994 — Enhancing the explanatory power of usability heuristics, CHI '94: 152–158 — conference paper — https://doi.org/10.1145/191666.191729 — where the current wording and numbering come from
`warrant:` Miller 1968 — Response time in man-computer conversational transactions, AFIPS Fall Joint Computer Conference: 267–277 — conference paper — https://doi.org/10.1145/1476589.1476628 — the origin of the three response-time bands every performance guideline since restates. Analytic design guidance rather than a measured constant, which is what this entry's `standing:` scopes. Miller is also the source of the two-second standard the `UX-P37` brief set out to overturn, and he predates it by fourteen years
`warrant:` Myers 1985 — The importance of percent-done progress indicators for computer-human interfaces, CHI '85: 11–17 — conference paper — https://doi.org/10.1145/317456.317459 — the experimental warrant for the progress advice specifically, as against feedback in general
`current:` Card, Robertson & Mackinlay 1991 — The information visualizer, an information workspace, CHI '91: 181–186 — conference paper — https://doi.org/10.1145/108844.108874 — Miller's bands restated as human information-processing timescales; the version most performance work cites today
`contra:` Adar, Tan & Teevan 2013 — Benevolent deception in human computer interaction, CHI '13: 1863–1872 — conference paper — https://doi.org/10.1145/2470654.2466246 — catalogues deceptions users demonstrably benefit from, progress indicators among them. The guard above overrides a published position rather than merely going further than a silent one, and says so
`figure:` "0.1 s", "1 s", "10 s" — Miller 1968: the bands for the feeling of instantaneous response, for uninterrupted flow of thought, and for holding attention at all

---

## UX-P37 — Sub-second response (Doherty threshold)

**Cue.** a response takes longer than an instant

**Principle.** Answer inside a second wherever the system can; where the real
work takes longer, acknowledge the action at once and show its state, so the user
is never waiting without evidence.

**Mechanism.** A wait costs more than the wait. An interruption that lands
mid-plan makes the user rebuild the plan, so each second of system delay takes
more than a second out of their working time and the cost compounds across a
sequence of actions. Below the point where the system answers before attention
drifts, the interaction stops feeling like a series of requests and starts
feeling like one continuous thing — which is the whole of the effect, and it is
not a threshold anyone measured.

**Applies / doesn't.**
- ✅ Perceived performance: instant acknowledgement of a tap, optimistic UI for
  cheap reversible actions, skeletons, progress for anything slow.
- ✅ Budgeting engineering effort — the delays worth paying to cut are the ones
  sitting inside a user's train of thought.
- ❌ Faking completion before a critical operation has succeeded. Responsiveness
  is not a licence to lie about a result — see `UX-P36`.
- ❌ As authority for a 400 ms threshold. That number is a practitioner
  interpolation: it is absent from the document it is credited to, which argues
  for sub-second response and names no threshold at all.
- ❌ As a claim that faster is always better. Operator error rates rise at both
  very slow *and* very fast response times, which matters most on exactly the
  screens this family covers.

**Ethical guard.** Optimistic UI is a promise about the interface, never about
the outcome. Showing a save, a send, or a payment as done before the system has
confirmed it converts responsiveness into a false statement of fact, and the user
discovers it at the point where it costs them — reserve the optimistic path for
actions that are cheap to reverse, and reverse them visibly when they fail.
Speed is not permission to outrun the user either: an irreversible confirmation
that arrives faster than the user can read it is a dark pattern wearing
performance as a costume.

**Detection.** Absent: a control produces nothing until the response lands, so
the user presses it again. Weakened: the feedback starts only after the wait the
user has already noticed, or a skeleton stands in for a state the system could
have reported.

**Collides with.** `UX-P36` — where an optimistic update would have to assert an
outcome the system has not confirmed, status wins. This entry buys the feeling of
speed; it never buys the claim.

**Example.** A "like" fills instantly and settles in the background, reverting
visibly if the request fails; the checkout's pay button, which cannot be
reverted, shows a pending state until the gateway answers.

**Provenance.**
`standing:` qualified
`guard-basis:` independent of source
`origin:` Doherty & Thadhani 1982 — The Economic Value of Rapid Response Time, IBM form GE20-0752-0, November 1982, 12 pp. — corporate technical report — https://www.computerhistory.org/collections/catalog/102751398 — the source of the name and nothing else. Catalogued by the Computer History Museum as a 12-page technical report, accession X6915.2014; it is **not** an *IBM Systems Journal* paper, the claim repeated by every blog downstream of one. Read end to end from the republication IBM authorised, its own hosted copy being dead: no threshold is named anywhere in it, the word "millisecond" never occurs, and its conclusion argues for "sub-second" values. The second author's name is spelled Thadani in its header note and Thadhani in its body — read: Jim Elliott's authorised republication of the 1982 text
`warrant:` Doherty & Kelisky 1979 — Managing VM/CMS systems for user effectiveness, IBM Systems Journal 18(1): 143–163 — peer-reviewed — https://doi.org/10.1147/sj.181.0143 — this entry's mechanism, verbatim: "each second of system response degradation leads to a similar degradation added to the user's time for the following [command]… Increases in SRT seem to disrupt the thought processes". This, not a threshold, is the citable claim. IBM's own house journal, so treat the refereeing as weaker than an independent venue's
`warrant:` Thadhani 1981 — Interactive user productivity, IBM Systems Journal 20(4): 407–423 — peer-reviewed — https://doi.org/10.1147/sj.204.0407 — the transactions-per-hour curve the 1982 brief summarises, running from 3.0 s down to 0.3 s. Same house-journal caveat. Spelled Thadhani here and in Crossref; a reader who searches the brief's "Thadani" will conclude the citation is invented
`contra:` Barber & Lucas 1983 — System response time operator productivity, and job satisfaction, Communications of the ACM 26(11): 972–986 — peer-reviewed — https://doi.org/10.1145/182.358464 — error rates rise at both very slow and very fast response times, which contradicts the monotonic reading of this entry. Title reproduced as deposited, comma and all
`mis-citation:` Yablonski 2020 — Laws of UX, O'Reilly, and lawsofux.com — trade book — https://lawsofux.com/doherty-threshold/ — where the name became canon in UX and acquired a number: the definition reads "Productivity soars when a computer and its users interact at a pace (<400ms)", the parenthesis being an interpolation, while its own source list points at the 1982 brief, which contains neither the figure nor the word "millisecond" — accessed: 2026-08-20
`figure:` "400 ms" — no primary source exists. In the 1982 brief the string 400 appears once, counting simultaneous NIH terminal users. The earliest statement of the figure under this name that the citation audit could trace is a practitioner blog post, Rupert 2015, https://daverupert.com/2015/06/doherty-threshold/, from which lawsofux entrenched it. Recorded here so it is never re-imported as a measured threshold

---

## UX-P38 — Error prevention & forgiveness

**Cue.** an action can be invalid, fail, or be irreversible

**Principle.** Make the mistake impossible first; where it stays possible, make
it reversible; reserve confirmation for what cannot be undone. Every step needs a
clearly marked way out.

**Mechanism.** Most interface errors are slips — the intention was right and the
execution went wrong — and a slip cannot be argued out of with a message, because
nothing in the user's plan was mistaken. What removes a slip is a change to what
the interface makes possible: a constraint that blocks the invalid action, a
layout that puts the destructive control out of the path of the routine one, and
an undo that reduces the consequence of a slip to a moment of surprise.

**Applies / doesn't.**
- ✅ Constraints that make invalid input unselectable rather than rejected on
  submit, autosave, undo, a visible cancel at every step.
- ✅ Destructive actions: confirm, and say in the confirmation exactly what will
  be lost.
- ❌ Confirming everything until dialogs are dismissed reflexively. Friction
  spent on the routine is friction unavailable for the irreversible.
- ❌ As a justification for friction on the way *out* — see the guard.

**Ethical guard.** Friction belongs on destructive actions, not on the user's
*exit*. Making "cancel", "unsubscribe", or "delete account" hard to reach is a
catalogued dark pattern — coined "roach motel", now filed as "hard to cancel" —
and in several jurisdictions it is regulated rather than merely frowned upon. The
test is symmetry: leaving should cost about what joining cost. Easy in, easy out.

**Detection.** Absent: an irreversible action sits one tap from a routine one,
with nothing between them but the user's attention. Weakened: the error is caught
only on submit, or an undo exists and is announced in a toast that has already
disappeared by the time the user notices the mistake.

**Example.** Deleting a record shows an undo toast for a few seconds while
permanent deletion asks the user to confirm what will be lost, and an unavailable
date is unselectable rather than rejected after submission.

**Provenance.**
`standing:` qualified (a design rule derived from an error taxonomy, not tested against one)
`guard-basis:` supported by source
`origin:` Nielsen & Molich 1990 — Heuristic evaluation of user interfaces, CHI '90: 249–256 — conference paper — https://doi.org/10.1145/97243.97281 — this entry carries two items of the nine-item list, "prevent errors" and "provide clearly marked exits". The second is quoted verbatim in this entry's principle; it is renamed "user control and freedom", heuristic #3, in the later revision, and "error prevention" becomes #5
`current:` Nielsen 1994 — Enhancing the explanatory power of usability heuristics, CHI '94: 152–158 — conference paper — https://doi.org/10.1145/191666.191729 — the renumbering, and the wording a reader will meet today
`warrant:` Norman 1983 — Design rules based on analyses of human error, Communications of the ACM 26(4): 254–258 — peer-reviewed — https://doi.org/10.1145/2163.358092 — the real origin of what this entry prescribes: make errors physically hard to commit, make actions reversible, make the irreversible ones difficult to reach. Seven years older than the heuristic that gets the credit for it
`warrant:` Norman 1981 — Categorization of action slips, Psychological Review 88(1): 1–15 — peer-reviewed — https://doi.org/10.1037/0033-295X.88.1.1 — the taxonomy underneath: slips are errors of execution, not of intention, which is why an error message cannot address them
`warrant:` Reason 1990 — Human Error, Cambridge University Press — book (academic) — https://openlibrary.org/works/OL9006915W — the canonical monograph on the slips, mistakes and violations distinction. No DOI, which is normal for a 1990 monograph and not a defect
`warrant:` Brignull 2010 — Hard to Cancel, Deceptive Design pattern taxonomy — practitioner article — https://www.deceptive.design/types/hard-to-cancel — the guard's claim, catalogued: the taxonomy records "roach motel" as the earlier name and credits the coinage to its own author, which is the narrow case where a practitioner's catalogue is primary for the term he coined — accessed: 2026-08-20

---

## UX-P39 — Curse of knowledge

**Cue.** wording assumes product knowledge: onboarding, labels, errors

**Principle.** Write for someone meeting the product for the first time:
knowing the system makes you a poor judge of what a newcomer will understand,
and being aware of that does not repair the judgement.

**Mechanism.** Once you know something you cannot reliably reconstruct not
knowing it. Your own knowledge leaks into your model of the other person, so you
overestimate how obvious a label is, how far an abbreviation carries, and how
long a first attempt will take. The classic demonstration has people tap out a
familiar tune and predict that half their listeners will name it; 3 listeners in
120 did. The bias survives being pointed out, which is why the fix is a reader
who genuinely does not know, not a harder effort to imagine one.

**Applies / doesn't.**
- ✅ Onboarding, empty states, labels, error messages, help text: plain language,
  expanded acronyms, terms defined where they are first used.
- ✅ Estimating — how long a first-timer needs, how many steps they will find,
  where they will stop.
- ❌ Genuine expert tools whose users share the vocabulary. Matching the audience
  is the goal; simplifying past them is the same error in the other direction.
- ❌ As a claim that an expert can debias by trying harder. What has been shown
  to work is testing on someone outside the team.

**Ethical guard.** The gap runs both ways and only one of them is an accident.
Vocabulary the user cannot evaluate can be chosen deliberately: a fee buried
under industry terminology, a permission described in the language of the system
rather than of its consequence, an acronym standing where the plain word would
have given the user pause. The test is whether the wording makes the user's
decision easier or your disclosure quieter. Where a term must be technical —
legal or regulatory copy — put the plain version beside it, never instead of it.

**Detection.** Absent: an error message names a system state — "Gateway error
402" — instead of what happened to the user and what to do next. Weakened: the
jargon is glossed once at first use and then used freely for the rest of the
flow, which helps only the reader who was already going to be fine.

**Example.** A declined payment says "Your bank declined this card — try another
card or contact your bank", and the internal code goes to the support log rather
than the screen.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Camerer, Loewenstein & Weber 1989 — The Curse of Knowledge in Economic Settings: An Experimental Analysis, Journal of Political Economy 97(5): 1232–1254 — peer-reviewed — https://doi.org/10.1086/261651 — the term, credited in the paper's own footnote 1 to Robin Hogarth. Read in full: its experiments are about asymmetric information in markets, its examples are lemons, bid–ask spreads and wages, and its result is that market forces roughly halve the curse without eliminating it. The name is all this entry takes from it
`warrant:` Hinds 1999 — The curse of expertise: The effects of expertise and debiasing methods on prediction of novice performance, Journal of Experimental Psychology: Applied 5(2): 205–221 — peer-reviewed — https://doi.org/10.1037/1076-898X.5.2.205 — this entry's claim, tested: experts systematically underestimate how long a task takes a novice, and the paper tests the debiasing methods that are this entry's advice. The single best citation for the entry, and the previous version had none
`warrant:` Nickerson 1999 — How we know – and sometimes misjudge – what others know: Imputing one's own knowledge to others, Psychological Bulletin 125(6): 737–759 — peer-reviewed — https://doi.org/10.1037/0033-2909.125.6.737 — the review of the imputation literature this entry generalises from. The title's dashes are em dashes in the original, normalised to en dashes here because the em dash is this file's citation-field separator
`warrant:` Fischhoff 1975 — Hindsight is not equal to foresight: The effect of outcome knowledge on judgment under uncertainty, Journal of Experimental Psychology: Human Perception and Performance 1(3): 288–299 — peer-reviewed — https://doi.org/10.1037/0096-1523.1.3.288 — the parent bias, and Camerer et al.'s own prior evidence for theirs
`warrant:` Birch & Bloom 2007 — The Curse of Knowledge in Reasoning About False Beliefs, Psychological Science 18(5): 382–386 — peer-reviewed — https://doi.org/10.1111/j.1467-9280.2007.01909.x — the developmental form, and the reason to treat this as a property of knowing rather than a habit of experts
`warrant:` Newton 1990 — The rocky road from actions to intentions, PhD dissertation, Stanford University — unpublished dissertation — ProQuest scan, no DOI; not peer reviewed, and cited here only for the demonstration — the tappers-and-listeners study, read in full. Its own Table 1 gives the numbers this entry uses, and they are not the ones in circulation
`mis-citation:` Heath & Heath 2007 — Made to Stick, Random House — trade book — https://openlibrary.org/works/OL8423528W — the route by which both the term and the tapping study reached UX, and the source of the widely repeated "2 of 150" and "3 of 150" figures that do not match the dissertation's own table. Named as the popularizer, never as the source. The OpenLibrary work record spans fifteen editions and returns a first-publication year earlier than the book's, so cite the edition consulted
`figure:` "3 hits in 120 tries", "2.5%", predictions averaging "50%" — Newton 1990, Table 1, N = 40 tappers, 40 listeners, 120 songs; the real rate sits outside the entire range of the tappers' own estimates

---

## UX-P40 — Consistency & standards

**Cue.** the same thing appears in more than one place

**Principle.** One thing, one name, one behaviour, everywhere in the product —
and where a platform convention exists, inherit it rather than invent a local
one. Consistency is a means: where it would preserve a known-bad pattern, it
loses.

**Mechanism.** Every repetition teaches the user a rule, and after a few
consistent instances they stop reading and start predicting. That is the benefit
and the exposure in one sentence: prediction is what makes a consistent product
fast to use, and it is what makes the single inconsistent instance invisible.

**Applies / doesn't.**
- ✅ Terminology, component behaviour, iconography, the position of primary
  actions, the shape of a destructive confirmation.
- ✅ Platform and genre conventions — the external half of this argument is
  `UX-P19`, and it is by the same author as this entry's own source.
- ❌ Where consistency would carry a known-bad pattern into every screen.
  Consistency is not a primitive design goal, and "consistent with what?" has
  several incompatible answers — internal, external, and with the user's task.
  That is a published argument in its own right, not a caution of ours.

**Ethical guard.** The consistency you build is a promise the user stops
checking. Breaking it exactly where the stakes are highest — a confirm button
that sits where cancel sat, a destructive action styled like a routine one, one
screen where the toggle's default is inverted — weaponises the attention every
other screen earned. This is a documented interference pattern, not a
hypothetical. Where an instance genuinely must differ, make the difference
visible and slow: the trained prediction you are breaking was the user's safety
mechanism.

**Detection.** Absent: two screens name the same object differently, or the same
control does different things in two places. Weakened: a design system exists and
one flow predates it — worse than having no system, because the user has learned
a rule that one screen quietly breaks.

**Example.** "Delete" means the same operation with the same confirmation on
every screen, and the one place where deletion cannot be undone says so rather
than looking identical to the places where it can.

**Provenance.**
`standing:` qualified
`guard-basis:` supported by source
`origin:` Nielsen & Molich 1990 — Heuristic evaluation of user interfaces, CHI '90: 249–256 — conference paper — https://doi.org/10.1145/97243.97281 — in the nine-item list the heuristic is "be consistent"; the wording "consistency and standards" and the number #4 come from the later revision
`current:` Nielsen 1994 — Enhancing the explanatory power of usability heuristics, CHI '94: 152–158 — conference paper — https://doi.org/10.1145/191666.191729 — the current wording and numbering
`warrant:` Grudin 1989 — The case against user interface consistency, Communications of the ACM 32(10): 1164–1173 — peer-reviewed — https://doi.org/10.1145/67933.67934 — this entry's ❌ *is* Grudin's thesis: consistency is not a primitive goal, "consistent with what?" has incompatible answers, and consistency pursued for itself degrades usability. The previous version of this entry restated the argument unattributed. Framing volume: Nielsen (ed.) 1989, Coordinating User Interfaces for Consistency, Academic Press
`warrant:` Ozok & Salvendy 2000 — Measuring consistency of web page design and its effects on performance and satisfaction, Ergonomics 43(4): 443–460 — peer-reviewed — https://doi.org/10.1080/001401300184332 — the closest thing to an experimental test of this entry's claim, and the reason its standing is not merely a heuristic's. Follow-up: same authors 2001, Behaviour & Information Technology 20(6): 433–447, https://doi.org/10.1080/01449290110092260
`warrant:` Gray, Kou, Battles, Hoggatt & Toombs 2018 — The Dark (Patterns) Side of UX Design, CHI '18: 1–14 — conference paper — https://doi.org/10.1145/3173574.3174108 — interface interference in the dark-pattern taxonomy: the documented case of a product that trains an expectation and then breaks it where breaking it pays. This warrants the guard, which is why this entry is not the "no meaningful abuse vector" candidate it was once nominated as
