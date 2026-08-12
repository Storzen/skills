# Motivation — progress, commitment & engagement

For onboarding, multi-step flows, progress, retention, and commitment. Entry
template: `FORMAT.md`. Catalog rules: `SKILL.md`. Several levers here are close
to dark patterns — read each ethical guard.

- `UX-P02` — Never start at zero (endowed progress)
- `UX-P03` — Loss aversion
- `UX-P05` — IKEA effect
- `UX-P11` — Zeigarnik effect
- `UX-P25` — Goal-gradient effect
- `UX-P26` — Commitment & consistency
- `UX-P27` — Sunk cost (handle with care)
- `UX-P28` — Variable reward (highest risk)
- `UX-P29` — Parkinson's law

---

## UX-P02 — Never start at zero (endowed progress)

**Principle.** Show a multi-step journey as already partly complete (bar at 20%,
first step ticked) to trigger the drive to finish.

**Mechanism.** Endowed progress effect — people push harder toward a goal when
handed an artificial head start (Nunes & Drèze, 2006) — combined with the
Zeigarnik effect.

**Applies / doesn't.**
- ✅ Onboarding, profile completion, setup checklists, multi-step flows.
- ❌ Critical processes where a fake "20%" misrepresents real state.

**Ethical guard.** The offered progress must map to something actually done
(account created, email verified), never an invented number. Fake progress
erodes trust the moment it is noticed — worse where money or legal status is
involved.

**Example.** A profile checklist opens at 2/6 because sign-up already satisfied
two items.

---

## UX-P03 — Loss aversion

**Principle.** Framing what the user stands to *lose* weighs about twice a
matching gain. Use it to prevent real loss, not to pressure.

**Mechanism.** Loss aversion, core to prospect theory (Kahneman & Tversky,
1979): the value function is steeper on the loss side.

**Applies / doesn't.**
- ✅ Preventing a genuine loss: unsaved changes, an expiring draft, an abandoned
  form or cart.
- ❌ Manufactured scarcity, fake countdowns, fear-based upsell.

**Ethical guard.** Legitimate when it protects the user from a loss they would
suffer by mistake. A dark pattern the moment it *fabricates* fear to serve the
business — a hard stop around the user's money.

**Example.** "You have unsaved changes — leave anyway?"

---

## UX-P05 — IKEA effect

**Principle.** People value what they helped build and abandon it less; involve
the user in creating or configuring the thing.

**Mechanism.** The IKEA effect — labor raises valuation (Norton, Mochon &
Ariely, 2011).

**Applies / doesn't.**
- ✅ Configuration onboarding, personalization, builders and editors.
- ❌ Flows where added effort is pure friction, not investment (checkout).

**Ethical guard.** The invested effort must produce real value for the user, not
busywork engineered only to raise switching cost and lock them in.

**Example.** A dashboard tool has the user pick widgets during setup; the result
feels theirs.

---

## UX-P11 — Zeigarnik effect

**Principle.** Unfinished tasks are remembered better and create tension to
complete them; surface partial progress to pull the user onward.

**Mechanism.** The Zeigarnik effect (Zeigarnik, 1927). Underlies progress bars
and onboarding checklists; pairs with `UX-P02` and `UX-P25`.

**Applies / doesn't.**
- ✅ Onboarding checklists, profile completion, resumable multi-step tasks.
- ❌ Where showing incompleteness would nag without a path to finish.

**Ethical guard.** A reminder of a task the user *wants* done is a service;
manufacturing anxiety about an incompleteness that doesn't serve them is nagging.

**Example.** A persistent "3 of 5 steps done" nudges the user back to finish
setup.

---

## UX-P25 — Goal-gradient effect

**Principle.** Effort intensifies as a visible goal gets closer; show how near
completion is, especially in the final stretch.

**Mechanism.** Goal-gradient effect (Hull, 1932; Kivetz et al., 2006): motivation
rises with proximity to the reward. Distinct from endowed progress — this is
about accelerating *near the end*, not seeding the start.

**Applies / doesn't.**
- ✅ Progress bars, loyalty/rewards, "1 step left", checklist tail.
- ❌ Long or open-ended processes where honest proximity can't be shown — a bar
  that crawls forever demotivates.

**Ethical guard.** The distance shown must be real. Understating how much is left
to keep the user pushing is manipulation.

**Example.** A setup wizard emphasizes "Last step" and shrinks the remaining
count as the user nears the end.

---

## UX-P26 — Commitment & consistency

**Principle.** People act consistently with a prior small commitment; a light
first step makes a larger aligned action more likely.

**Mechanism.** Commitment and consistency (Cialdini): a small public or active
commitment biases later behavior to match.

**Applies / doesn't.**
- ✅ Progressive onboarding: a tiny first action (pick a goal, add one item)
  before asking for more.
- ❌ Using an early trivial commitment to extract a much larger unrelated one the
  user didn't anticipate.

**Ethical guard.** The follow-through you invite must be one the user would
reasonably want given their first step — not a foot-in-the-door toward something
they'd refuse if asked directly.

**Example.** A fitness app asks the user to set one weekly goal before building
the fuller plan around it.

---

## UX-P27 — Sunk cost (handle with care)

**Principle.** People stay invested in what they've already put time or data
into; visible accumulated investment reduces abandonment.

**Mechanism.** The sunk cost fallacy — prior irrecoverable investment irrationally
drives continuation.

**Applies / doesn't.**
- ✅ Reflecting genuine value the user has built (saved work, history, a
  configured workspace) so they see what leaving would waste.
- ❌ Trapping users by inflating a fake sense of investment, or making exit
  costly on purpose.

**Ethical guard.** Show real accumulated value to inform a free choice; never
weaponize it to keep someone in a subscription or flow they want to leave. If
they choose to go, make leaving easy (this is where "roach motel" dark patterns
live).

**Example.** A cancellation screen honestly summarizes what the account holds,
with a one-click way to export it and to proceed with cancelling.

---

## UX-P28 — Variable reward (highest risk)

**Principle.** Unpredictable rewards reinforce a behavior more strongly than
fixed ones; occasional novelty or delight drives return visits.

**Mechanism.** Variable-ratio reinforcement (Skinner) — the engine of the
"Hooked" model (Eyal): trigger → action → variable reward → investment.

**Applies / doesn't.**
- ✅ Sparingly, to add genuine delight — a fresh tip, a surprise-and-delight
  moment that improves the experience.
- ❌ Engagement-for-its-own-sake loops (infinite feeds, slot-machine mechanics,
  streaks that punish absence) that serve retention metrics over the user.

**Ethical guard.** The catalog's most dangerous lever. The test (Eyal's own
Manipulation Matrix): would the designer use it on themselves, and does it
materially improve the user's life? If the reward exists to capture attention
rather than to serve the user, do not build it. Never use in financial products
to drive compulsive engagement.

**Example.** Acceptable: a language app occasionally celebrates a streak
milestone with a useful summary. Not: variable "you might have missed"
notifications engineered to pull users back with no real payoff.

---

## UX-P29 — Parkinson's law

**Principle.** Work expands to fill the time available; a reasonable, honest
constraint helps users complete a task instead of stalling.

**Mechanism.** Parkinson's law — tasks stretch to the time allotted; a bound
focuses effort.

**Applies / doesn't.**
- ✅ Autosave-and-continue, a clearly scoped step, a real reservation hold ("your
  seat is held for 10:00").
- ❌ Fabricated countdowns and fake "only 2 left" timers — those are pressure
  dark patterns, not this principle.

**Ethical guard.** Any time limit shown must be real and enforced by the system,
not a manufactured urgency to rush the user past their judgment. If the timer
resets on reload, it's a dark pattern.

**Example.** A checkout that truly holds inventory shows the genuine hold time;
it never invents one.
