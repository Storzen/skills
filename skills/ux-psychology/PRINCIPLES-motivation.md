# Motivation — progress, commitment & engagement

For onboarding, multi-step flows, progress, retention, and commitment. Entry
template: `FORMAT.md`. Catalog rules: `SKILL.md`. Several levers here sit one
step from a dark pattern, and three carry guards stricter than the evidence they
rest on — read each ethical guard before citing.

- `UX-P02` — Endowed progress (never start at zero)
- `UX-P03` — Loss aversion
- `UX-P05` — IKEA effect
- `UX-P11` — Resumption of interrupted tasks (Zeigarnik effect)
- `UX-P25` — Goal-gradient effect
- `UX-P26` — Foot-in-the-door (commitment & consistency)
- `UX-P27` — Sunk cost
- `UX-P28` — Variable reward
- `UX-P29` — Excess time effect (Parkinson's law)

---

## UX-P02 — Endowed progress (never start at zero)

**Cue.** a multi-step journey shows progress from nothing

**Principle.** Open a multi-step journey already partly advanced, and name what
earned the advance — an unexplained head start motivates no better than none.

**Mechanism.** A journey shown as begun reads as a task partly completed, and
effort rises with proximity to a goal already in view (`UX-P25`). The head start
works through that reading, not through a reluctance to waste what was handed
over — the same evidence tested the sunk-cost account and rejected it, which is
why this is not a `UX-P27` argument. It also needs a reason: progress credited
with no justification attached moves nobody.

**Applies / doesn't.**
- ✅ Onboarding, profile completion, setup checklists — where signing up already
  satisfied real steps.
- ✅ Any journey whose opening steps can be credited honestly: verified email,
  connected account, imported data.
- ❌ Critical processes where a head start misrepresents real state — identity
  checks, compliance flows, anything with legal or financial standing.
- ❌ Where no true reason for the advance can be stated. Without one the lever is
  inert, and inventing one crosses the guard.

**Ethical guard.** The offered progress must map to something actually done, and
the reason given must be the real one. Both halves are stricter than the
evidence: the source found an arbitrary justification for the head start works
as well as a genuine one, so nothing in the literature stops a designer from
fabricating either. Fake progress erodes trust the moment it is noticed, and
worse where money or legal status is involved.

**Detection.** Absent: a checklist or wizard opens at zero although the account
already satisfies one of its items. Weakened: the bar starts above zero but
nothing says why, so it reads as decoration — or the credited step is real and
the copy never names it.

**Example.** A profile checklist opens at `"2 of 6 done"` and names the two it
credited: account created, email verified.

**Provenance.**
`standing:` qualified
`guard-basis:` stricter than source
`origin:` Nunes & Drèze 2006 — The Endowed Progress Effect: How Artificial Advancement Increases Effort, Journal of Consumer Research 32(4): 504–512 — peer-reviewed — https://doi.org/10.1086/500480 — a car-wash loyalty programme, not an interface: every step in its design costs the user a purchase, which is why this entry states the transfer as a transfer
`warrant:` Nunes & Drèze 2006 — The Endowed Progress Effect, study 3, Journal of Consumer Research 32(4): 504–512 — peer-reviewed — https://doi.org/10.1086/500480 — with progress tallied in purchases and no reason given for the endowment, the endowed programme rated no better than the plain one; and an entirely arbitrary reason worked as well as one based on purchase history, which is the finding this entry's guard refuses
`warrant:` Kivetz, Urminsky & Zheng 2006 — The Goal-Gradient Hypothesis Resurrected: Purchase Acceleration, Illusionary Goal Progress, and Customer Retention, Journal of Marketing Research 43(1): 39–58 — peer-reviewed — https://doi.org/10.1509/jmkr.43.1.39 — the goal-gradient half of the mechanism, in humans; stated in full at `UX-P25`
`figure:` "34%" and "19%" — Nunes & Drèze 2006, study 1: redemption on the endowed card against the plain one
`mis-citation:` Zeigarnik 1927 — Das Behalten erledigter und unerledigter Handlungen, Psychologische Forschung 9: 1–85 — peer-reviewed — https://doi.org/10.1007/BF02409755 — the endowed-progress paper rests its first hypothesis on the Zeigarnik effect, and UX writing inherits the citation through it. The recall effect it names does not replicate (`UX-P11`), and the paper's own data favour perceived task completion over interruption tension

---

## UX-P03 — Loss aversion

**Cue.** the user risks losing something real (unsaved work, an expiring draft)

**Principle.** Naming what the user stands to lose moves them more than naming an
equivalent gain; use it to prevent a real loss, never to manufacture one.

**Mechanism.** Outcomes are judged as changes from a reference point rather than
as final states, and the value curve is steeper below that point than above it.
Two things follow for interface copy. The reference point is whatever the screen
makes salient — what the user holds right now, unless something else is put in
front of it. And the asymmetry is smaller than its reputation: the ratio usually
quoted comes from experiments on gambles, while a confirmation dialog is a
riskless choice about something already held.

**Applies / doesn't.**
- ✅ Preventing a genuine loss: unsaved changes, an expiring draft, an abandoned
  cart, a subscription lapsing with data attached.
- ✅ Naming what is already the user's — saved work, an accrued balance — at the
  moment they are about to act against it.
- ❌ Manufactured scarcity, fake countdowns, fear-based upsell. Nothing is being
  lost, so this is not the lever; it is `UX-P32` run past its guard.
- ❌ As a size argument. Do not build a case on losses weighing twice their
  matching gains: the coefficient has been re-estimated downward, and serious
  reviews find no general asymmetry at all.

**Ethical guard.** Legitimate when it protects the user from a loss they would
suffer by mistake, and when the loss named is one that would actually occur. A
dark pattern the moment it fabricates the loss, or inflates a real one, to serve
the business — a hard stop around the user's money.

**Detection.** Absent: a destructive or abandoning action passes silently —
closing an editor with unsaved work, leaving a part-filled form, downgrading a
plan that holds data. Weakened: the loss is named but not specified, so the user
cannot weigh it, or the dialog's easiest exit is the one that loses the work.

**Collides with.** `UX-P17` — framing recommends the wording the user reads most
accurately; this entry recommends the wording that moves them. Where they
differ, accuracy wins: the loss frame is legitimate only when the loss is the
fact.

**Example.** A close dialog reads `"Leave without saving? The last 12 minutes of
edits will be discarded."` rather than `"Discard changes?"`.

**Provenance.**
`standing:` qualified
`guard-basis:` independent of source
`origin:` Kahneman & Tversky 1979 — Prospect Theory: An Analysis of Decision under Risk, Econometrica 47(2): 263–291 — peer-reviewed — https://doi.org/10.2307/1914185 — posits a value function steeper on the loss side, and supplies no coefficient for how much steeper
`warrant:` Tversky & Kahneman 1991 — Loss Aversion in Riskless Choice: A Reference-Dependent Model, Quarterly Journal of Economics 106(4): 1039–1061 — peer-reviewed — https://doi.org/10.2307/2937956 — the riskless case, which is what every interface example in this entry is; the 1979 paper is about gambles
`figure:` "2.25" — Tversky & Kahneman 1992, Advances in prospect theory: Cumulative representation of uncertainty, Journal of Risk and Uncertainty 5(4): 297–323, https://doi.org/10.1007/BF00122574 — the median λ behind the "about twice" this entry no longer states, and not a number the 1979 paper contains
`figure:` "1.31" — Walasek, Mullett & Stewart 2024, λ re-estimated across the usable datasets
`contra:` Gal & Rucker 2018 — The Loss of Loss Aversion: Will It Loom Larger Than Its Gain?, Journal of Consumer Psychology 28(3): 497–516 — peer-reviewed — https://doi.org/10.1002/jcpy.1047 — concludes the evidence does not support losses being generally more impactful than gains, and that the endowment effect and status-quo bias admit other explanations
`contra:` Walasek, Mullett & Stewart 2024 — A meta-analysis of loss aversion in risky contexts, Journal of Economic Psychology 103: 102740 — peer-reviewed — https://doi.org/10.1016/j.joep.2024.102740 — re-fitting prospect theory to individual choices puts the coefficient about a third above parity, not at double
`contra:` Yechiam & Zeif 2025 — Loss aversion is not robust: A re-meta-analysis, Journal of Economic Psychology 107: 102801 — peer-reviewed — https://doi.org/10.1016/j.joep.2025.102801

---

## UX-P05 — IKEA effect

**Cue.** the user invests effort configuring or building something

**Principle.** People value what they built — but only what they finished;
involve the user in making the thing, and make sure the making completes.

**Mechanism.** Assembling something raises what it is worth to whoever assembled
it, and what the labour buys is a feeling of competence and ownership rather
than the effort itself. Work abandoned half-built, or undone afterwards, earns
no premium at all: the finish is the mechanism, not the toil.

**Applies / doesn't.**
- ✅ Configuration onboarding, personalization, builders and editors — where the
  artifact is the user's and stays theirs.
- ✅ Anywhere completion can be relied on: short setups, resumable ones
  (`UX-P11`), steps with a visible end (`UX-P25`).
- ❌ Flows where added effort is friction, not investment — checkout,
  verification, anything the user wants over with.
- ❌ Long configuration a first-time user is likely to abandon. An unfinished
  build earns nothing and still costs them the effort.

**Ethical guard.** The invested effort must produce real value for the user, not
busywork engineered to raise switching cost. The test is what happens on the way
out: if the artifact leaves with them — exportable, portable, usable elsewhere —
the effort bought them something. If it only makes leaving expensive, the lever
was lock-in wearing the language of personalization (`UX-P27`).

**Detection.** Absent: a product that could be shaped by the user is handed over
pre-built and generic, with nothing of theirs in it. Weakened: the user
configures something but never sees it take effect, or setup is long enough that
most abandon it — no finish, no premium.

**Example.** A dashboard tool has the user pick and place a handful of widgets
during setup, then opens on that layout every time.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Norton, Mochon & Ariely 2012 — The IKEA effect: When labor leads to love, Journal of Consumer Psychology 22(3): 453–460 — peer-reviewed — https://doi.org/10.1016/j.jcps.2011.08.002 — the year of record is 2012; the DOI suffix and the online-first stamp both read 2011, which is what the mis-dated version of this citation copies. Participants who disassembled or failed to complete their creation showed no premium
`warrant:` Mochon, Norton & Ariely 2012 — Bolstering and restoring feelings of competence via the IKEA effect, International Journal of Research in Marketing 29(4): 363–369 — peer-reviewed — https://doi.org/10.1016/j.ijresmar.2012.05.001 — competence, not effort, is what the completed labour buys
`warrant:` Sarstedt, Neubert & Barth 2017 — The IKEA Effect. A Conceptual Replication, Journal of Marketing Behavior 2(4): 307–312 — peer-reviewed — https://doi.org/10.1561/107.00000039 — supports the original effect and identifies psychological ownership as the mediator; the one entry in this family with a positive replication record, which is why it may be stated plainly

---

## UX-P11 — Resumption of interrupted tasks (Zeigarnik effect)

**Cue.** a task is left unfinished and can be resumed

**Principle.** People return to finish what they started when the way back is
obvious; surface the unfinished task and the step it stopped on — never rely on
them remembering it.

**Mechanism.** An interrupted task carries a tendency to be picked up again, and
that tendency is what a saved draft or a half-done checklist recruits. What it
does not do is make the task memorable: the belief that unfinished business is
better remembered is the half of this effect that failed to replicate, so the
screen has to carry the reminder rather than the user's head.

**Applies / doesn't.**
- ✅ Resumable multi-step tasks: a saved draft, a part-filled form, an
  interrupted upload, a checklist with a visible remainder.
- ✅ Returning the user to the exact step they left rather than to the start.
- ❌ As a memory argument. If the user must carry something across steps, that is
  `UX-P35`, and the answer is to show it, not to count on tension.
- ❌ Where showing incompleteness would nag with no path to finish — an item
  blocked on something the user cannot do yet.

**Ethical guard.** A reminder of a task the user wants done is a service;
manufacturing incompleteness to create the pull is not. Two forms of that: a
checklist padded with items nobody asked for, and a permanent badge on a task
the user has decided against. What they decline must be dismissible for good,
and the pull must not follow them off the screen — unfinished work left in mind
after hours shows up as rumination, not as motivation.

**Detection.** Absent: leaving a flow discards the partial state, or returning
drops the user at step one. Weakened: progress is saved but not surfaced —
nothing says a task is waiting, or it says so without naming what comes next.

**Example.** A part-filled application appears on the home screen as
`"Application — 3 of 7 steps"`, linking straight to the step it stopped on.

**Provenance.**
`standing:` mixed (recall component)
`guard-basis:` independent of source
`origin:` Ovsiankina 1928 — Die Wiederaufnahme unterbrochener Handlungen, Psychologische Forschung 11: 302–379 — peer-reviewed — https://doi.org/10.1007/BF00410261 — the resumption tendency, which is the half of the pair this entry claims
`warrant:` Ghibellini & Meier 2025 — Interruption, recall and resumption: a meta-analysis of the Zeigarnik and Ovsiankina effects, Humanities and Social Sciences Communications 12: 962 — peer-reviewed — https://doi.org/10.1057/s41599-025-05000-w — pools twenty resumption studies against thirty-eight on recall: interrupted tasks are resumed about two thirds of the time, while the memory advantage is absent and stays absent when Zeigarnik's own data are removed
`figure:` "67%" — Ghibellini & Meier 2025, resumption rate for interrupted tasks
`figure:` "0.99" — Ghibellini & Meier 2025, pooled recall ratio: no memory advantage for interrupted tasks
`contra:` Wendsche, Weigelt & Syrek 2026 — Unfinished work tasks and work-related thoughts during off-job time: meta-analysis of the Zeigarnik effect in a work-recovery context, Anxiety, Stress, & Coping 39: 385–407 — peer-reviewed — https://doi.org/10.1080/10615806.2026.2616302 — what an unfinished task leaves behind outside the flow is intrusive thought, not useful drive
`mis-citation:` Zeigarnik 1927 — Das Behalten erledigter und unerledigter Handlungen, Psychologische Forschung 9: 1–85 — peer-reviewed — https://doi.org/10.1007/BF02409755 — the name the resumption claim travels under, and the wrong source for it: Zeigarnik measured recall, and recall is the half that died. Crossref's record for this DOI credits K. Lewin, the series editor, and omits Zeigarnik entirely — the metadata is wrong, not the DOI, so do not "correct" the author from the API

---

## UX-P25 — Goal-gradient effect

**Cue.** the end of a flow is in sight and can be shown

**Principle.** Effort rises as a goal comes into view; show how near the end is,
and make the distance shown the true one.

**Mechanism.** Proximity to a reward accelerates the behaviour that earns it —
measured first in animals running a maze, then in people filling a purchase
card, who buy faster as the card fills and slow again once the reward resets.
What carries over to a screen is the shape rather than the size: a flow whose
remaining distance is visible pulls harder at the end than in the middle. This
is the far end of the journey from `UX-P02`, which seeds the start.

**Applies / doesn't.**
- ✅ Progress bars, checklists, `"one step left"`, the tail of any flow with a
  real end.
- ✅ Reward and loyalty schemes, where the human evidence actually sits — and
  where the goal has to be demanding enough that reaching it means something.
- ❌ Long or open-ended processes where honest proximity cannot be shown; a bar
  that crawls forever demotivates.
- ❌ As evidence about progress bars in particular. The human studies are about
  purchase programmes, and the transfer to software flows is an extension.

**Ethical guard.** The distance shown must be real. Understating what is left, or
padding a card with steps that cost nothing so the bar moves faster, keeps the
user pushing against a picture rather than a fact. This is stricter than the
source, which reports illusionary goal progress as an effective tactic and
recommends it: effective is not the test.

**Detection.** Absent: a multi-step flow shows no position and no remainder, so
the last step feels as far off as the first. Weakened: the bar exists but is not
proportional — steps of wildly different cost drawn as equal segments, or a
percentage that stalls and then jumps at the end.

**Example.** A setup wizard labels its final screen `"Last step"`, and the count
of what remains shrinks as the user advances.

**Provenance.**
`standing:` qualified
`guard-basis:` stricter than source
`origin:` Hull 1932 — The goal-gradient hypothesis and maze learning, Psychological Review 39(1): 25–43 — peer-reviewed — https://doi.org/10.1037/h0072640 — rats accelerating toward food in a maze. The origin is animal work and states nothing about people, which is why this entry does not rest on it alone
`warrant:` Kivetz, Urminsky & Zheng 2006 — The Goal-Gradient Hypothesis Resurrected: Purchase Acceleration, Illusionary Goal Progress, and Customer Retention, Journal of Marketing Research 43(1): 39–58 — peer-reviewed — https://doi.org/10.1509/jmkr.43.1.39 — the human evidence, in café loyalty cards: purchases accelerate as the card fills, slow after the reward resets, and the effect strengthens over successive cycles. Its illusionary-progress finding is exactly what this entry's guard refuses
`warrant:` Drèze & Nunes 2011 — Recurring Goals and Learning: The Impact of Successful Reward Attainment on Purchase Behavior, Journal of Marketing Research 48(2): 268–281 — peer-reviewed — https://doi.org/10.1509/jmkr.48.2.268 — the lift from a completed goal appears only where that goal was challenging; the support for this entry's caveat about flows with no meaningful end

---

## UX-P26 — Foot-in-the-door (commitment & consistency)

**Cue.** a small first action precedes a larger ask

**Principle.** A small first step makes a larger aligned one more likely —
modestly, and only where the second follows from the first; sequence the ask
rather than piling it up front.

**Mechanism.** Having done something small, people become somewhat more willing
to do something larger of the same kind. Why is unsettled: the tidy story is a
drive to stay consistent with what one has already done, but seeing oneself as
the sort of person who does this predicts as well, and pushing too far too soon
produces refusal instead. The effect is small and fails often — a reason to
order a flow, never a mechanism to lean on.

**Applies / doesn't.**
- ✅ Progressive onboarding: one tiny real action — pick a goal, add one item —
  before the fuller setup.
- ✅ Ordering asks so the cheap, obviously useful one comes first: import a
  single file before connecting the whole account.
- ❌ Using an early trivial commitment to extract a larger unrelated one the user
  did not see coming.
- ❌ Where the first step is manufactured — a click invented to be a commitment
  rather than to accomplish something.

**Ethical guard.** The follow-through you invite must be one the user would
reasonably want given their first step, not a foot in the door toward something
they would refuse if asked directly. The test is whether the larger ask would
survive being made first: if stating it up front would lose the user, sequencing
it does not make it fair, only quieter.

**Detection.** Absent: the flow opens on its largest ask — full profile, every
permission, payment details — before the product has done anything for the user.
Weakened: a small first step exists but is disconnected from what follows, so it
reads as a hoop rather than as the start of the same task.

**Example.** A fitness app asks for one weekly goal, builds the plan around it,
and only then offers to connect a wearable.

**Provenance.**
`standing:` qualified
`guard-basis:` independent of source
`origin:` Freedman & Fraser 1966 — Compliance without pressure: The foot-in-the-door technique, Journal of Personality and Social Psychology 4(2): 195–202 — peer-reviewed — https://doi.org/10.1037/h0023552 — the experiments the effect is named for; the magnitude reported here has not been reproduced since
`warrant:` Burger 1999 — The Foot-in-the-Door Compliance Procedure: A Multiple-Process Analysis and Review, Personality and Social Psychology Review 3(4): 303–325 — peer-reviewed — https://doi.org/10.1207/s15327957pspr0304_2 — the standard review: real under specific conditions, and produced by several competing processes — self-perception, commitment, consistency, reactance, conformity, attribution — rather than by consistency alone
`warrant:` Beaman, Cole, Preston, Klentz & Steblay 1983 — Fifteen Years of Foot-in-the-Door Research: A Meta-Analysis, Personality and Social Psychology Bulletin 9(2): 181–196 — peer-reviewed — https://doi.org/10.1177/0146167283092002 — pools a hundred and twenty experimental groups: significant but modest, with a large share of null and reversed results
`mis-citation:` Cialdini 2021 — Influence, New and Expanded: The Psychology of Persuasion, Harper Business — trade book — https://openlibrary.org/isbn/9780062937650 — where UX writing routinely credits this principle. Cialdini synthesises the experiments and supplies the chapter title this entry used to carry as its name; he did not run them, and the book is not evidence. Cite the edition in hand — the first edition is usually given as 1984 and the edition history does not settle cleanly — accessed: 2026-08-19

---

## UX-P27 — Sunk cost

**Cue.** the screen invokes what the user has already invested

**Principle.** Show what the user has actually built so they can weigh leaving
it; never dress up what they have already spent as a reason to stay.

**Mechanism.** Money, time or effort already spent and unrecoverable pushes
people to continue even where continuing is the worse choice. It is a minority
behaviour and it is a mistake — which turns this entry the other way round from
the rest of the family. The effect is the thing to refuse; what an honest screen
shows instead is the value that still exists, and that is a switching cost, a
real reason a careful person may act on.

**Applies / doesn't.**
- ✅ Reflecting genuine remaining value at a decision point: saved work, history,
  a configured workspace, a balance the user keeps or forfeits.
- ✅ Auditing a cancellation or downgrade flow for the move run backwards — a
  screen warning of losses that would not in fact occur.
- ❌ As a retention tactic. Reminding someone what they have sunk, so that
  leaving feels wasteful, exploits the fallacy instead of informing a choice.
- ❌ As the machinery behind a progress bar. Endowed progress works through
  perceived completion; the two accounts were tested against each other and this
  one lost (`UX-P02`).

**Ethical guard.** Show real accumulated value to inform a free choice; never
weaponise it to hold someone in a subscription or a flow they want to leave.
Two hard lines: what is shown must still exist for the user after the decision,
and leaving must stay as easy as arriving. Roach-motel exits — cancellation
behind a phone call, an export that never arrives — are this lever crossed, and
are the first thing to look for when auditing a cancellation path.

**Detection.** Absent: a cancellation screen says nothing about what the account
holds, so the user cannot tell what leaving actually costs. Weakened: the value
is shown with no way to take it out — an inventory of what will be destroyed is
a threat, not disclosure.

**Example.** A cancellation screen lists what the account holds, offers a
one-click export, and keeps `"Cancel my plan"` as the primary action.

**Provenance.**
`standing:` replicated
`guard-basis:` independent of source
`origin:` Arkes & Blumer 1985 — The psychology of sunk cost, Organizational Behavior and Human Decision Processes 35(1): 124–140 — peer-reviewed — https://doi.org/10.1016/0749-5978(85)90049-4 — the ski-trip and season-ticket experiments, and the source of the standard definition: a greater tendency to continue once money, effort or time has been invested
`warrant:` Ronayne, Sgroi & Tuckwell 2021 — Evaluating the sunk cost effect, Journal of Economic Behavior & Organization 186: 318–327 — peer-reviewed — https://doi.org/10.1016/j.jebo.2021.03.029 — the effect survives a real-effort task with a dominated-versus-dominant switch, and is a minority behaviour; the endowment effect accounts for about a third of it, and cognitive reflection predicts who resists
`warrant:` Staw 1976 — Knee-deep in the big muddy: A study of escalating commitment to a chosen course of action, Organizational Behavior and Human Performance 16(1): 27–44 — peer-reviewed — https://doi.org/10.1016/0030-5073(76)90005-2 — escalation of commitment, the organisational sibling, framed around self-justification rather than waste-avoidance; the reason a team defending its own past decision is the hardest audience for this entry
`figure:` "23%" — Ronayne, Sgroi & Tuckwell 2021, subjects sticking with the dominated option

---

## UX-P28 — Variable reward

**Cue.** a reward or delight moment repeats unpredictably

**Principle.** Unpredictable rewards sustain a behaviour longer than predictable
ones — in animals, working for food; read this entry as a detector for the
pattern in a product, not as a recipe for building one.

**Mechanism.** Under partial reinforcement — a reward that arrives on some
responses and not others — responding persists far longer once the reward stops
than it does after every response has been rewarded, and variable schedules
produce high, steady rates of response. That is a finding about rate and
persistence in deprived animals with a single consumed reward. The products that
borrow it push unconsumed information at a satiated person choosing among a
hundred other things, and nothing in that literature establishes the transfer.

**Applies / doesn't.**
- ✅ Auditing an existing product for the pattern: feeds refreshing into novelty,
  streaks that punish absence, rewards timed to reengage rather than to reward.
- ✅ Sparingly, where the unpredictable thing is worth having on its own — a tip
  that is actually useful, a milestone summary worth reading.
- ❌ As a retention mechanism. The evidence does not reach the case, and the
  ethics do not survive it.
- ❌ In financial products, in anything aimed at minors, and anywhere compulsive
  use is a known harm. No version of this lever is acceptable there.

**Ethical guard.** The catalog's most dangerous lever, and the one whose guard
sits furthest from its sources: the operant literature is silent on ethics, and
the trade book that popularised the loop for products exists to teach it. That
book's own test is still the right one — would the designer use this on
themselves, and does it materially improve the user's life — and both answers
must be yes before anything unpredictable ships. Where engagement and the user's
interest pull apart, the user's interest wins; that part is ours, not the book's.
If the reward exists to capture attention rather than to serve the user, do not
build it.

**Detection.** Absent: rarely the finding — a product with no unpredictable
reward is not missing a lever. What is missing is the check: nobody has asked
whether notification timing, feed refresh, or reward drops already run on
unpredictability that was never designed as a reward. Weakened: the loop was
recognised and softened rather than removed — the streak survives with a gentler
penalty, the surprise still fires on a schedule tuned to reengagement.

**Example.** Audit finding: a learning app's streak notification fires at the
hour the user most often lapses and threatens a counter rather than anything
learned — name it as the finding and cut the timing rule, keeping the milestone
summary that has its own value.

**Provenance.**
`standing:` qualified (animal evidence; the transfer to interfaces is untested)
`guard-basis:` stricter than source
`origin:` Ferster & Skinner 1957 — Schedules of Reinforcement, Appleton-Century-Crofts — monograph — https://doi.org/10.1037/10627-000 — the systematic treatment of variable-ratio and variable-interval schedules, in pigeons and rats under food deprivation. It describes rates and patterns of responding; "reinforces more strongly" is not a quantity it defines
`warrant:` Humphreys 1939 — The effect of random alternation of reinforcement on the acquisition and extinction of conditioned eyelid reactions, Journal of Experimental Psychology 25(2): 141–158 — peer-reviewed — https://doi.org/10.1037/h0058138 — the partial reinforcement extinction effect, which is the actual finding behind "unpredictable rewards last longer". Note the contrast it draws: partial against continuous, not variable against fixed
`warrant:` Eyal 2014 — Hooked: How to Build Habit-Forming Products, Portfolio/Penguin — trade book — https://openlibrary.org/isbn/9781591847786 — not evidence for the mechanism, and cited for what it is: the published playbook for this loop in consumer products, and the source of the Manipulation Matrix this entry's guard borrows and turns against it — accessed: 2026-08-19
`mis-citation:` Schultz, Dayan & Montague 1997 — A Neural Substrate of Prediction and Reward, Science 275(5306): 1593–1599 — peer-reviewed — https://doi.org/10.1126/science.275.5306.1593 — the dopamine result routinely offered as proof that unpredictability brings users back. It characterises a reward-prediction-error learning signal and says nothing about product engagement

---

## UX-P29 — Excess time effect (Parkinson's law)

**Cue.** a step runs without a stated end, or carries a real deadline

**Principle.** Work stretches to fill whatever time is available, and the fix is
a clear goal rather than a shorter clock; state what finishing means, and show a
deadline only where one genuinely exists.

**Mechanism.** Given more time than a task needs, people slow to fill it — not
because pressure motivates, but because an unbounded task sets no standard for
completion. Supplying that standard explicitly does the work the deadline was
assumed to do. A real external deadline — a held seat, an expiring quote — is a
fact about the world and belongs on screen for that reason, not as a lever.

**Applies / doesn't.**
- ✅ Naming the end of a step: what completing it means, and how much is left
  (`UX-P25`).
- ✅ Autosave-and-continue, and a clearly scoped step inside a long flow.
- ✅ A genuine, system-enforced hold or expiry, stated plainly.
- ❌ Fabricated countdowns and invented stock counts. Those are pressure dark
  patterns and they answer to `UX-P32`'s guard, not to this entry.
- ❌ As grounds for imposing an artificial time limit where none exists. The
  evidence points at the goal, not at the clock.

**Ethical guard.** Any time limit shown must be real and enforced by the system.
A timer that resets on reload, a hold the system would never actually release, a
countdown attached to a price that does not change — each manufactures urgency
to push the user past their own judgment. Where the constraint is real, state it
plainly, including what happens when it expires, and let the user act on it —
walking away included.

**Detection.** Absent: a step gives no sense of what finishing means — an
open-ended editor, a form with no stated scope, a review screen with no end.
Weakened: a deadline is shown without its consequence, so the user cannot tell
whether it matters; or the goal is stated in the vendor's terms rather than in
the user's.

**Example.** A booking step reads `"Your seat is held until 18:40"`, the hold is
real, and nothing else on the screen counts down.

**Provenance.**
`standing:` reinterpreted
`guard-basis:` independent of source
`origin:` Parkinson 1955 — Parkinson's Law, The Economist, 19 November 1955 — essay — https://www.economist.com/news/1955/11/19/parkinsons-law — an unsigned satirical essay on the growth of civil-service staffing, whose evidence is a comic extrapolation from Admiralty headcount. It is the source of the sentence and it is a joke, not a finding about users — accessed: 2026-08-19
`warrant:` Bryan & Locke 1967 — Parkinson's Law as a goal-setting phenomenon, Organizational Behavior and Human Performance 2(3): 258–275 — peer-reviewed — https://doi.org/10.1016/0030-5073(67)90021-9 — reframes the observation as goal-setting: people given excess time slow down because no goal is set, and an explicit goal restores the pace. This is the claim this entry actually makes
`warrant:` Aronson & Landy 1967 — Further steps beyond Parkinson's Law: A replication and extension of the excess time effect, Journal of Experimental Social Psychology 3(3): 274–285 — peer-reviewed — https://doi.org/10.1016/0022-1031(67)90029-7 — the replication that gives the effect the name this entry carries
