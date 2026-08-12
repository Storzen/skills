---
name: ux-psychology
description: Apply psychology-based UI/UX principles when designing or reviewing an interface — cognitive load and decision-making, perception and layout, motivation and progress, social persuasion, and trust, feedback and error recovery. Use when designing a screen, form, onboarding, funnel, pricing page, or transactional flow, when improving conversion, completion, clarity, or trust, or when auditing an interface for dark patterns. Includes a mandatory ethical guard, with heightened caution for high-stakes and financial flows.
---

# UX Psychology — psychology-based principles for interface design

A catalog of UI/UX principles grounded in human psychology. Consult it while
shaping a screen; cite a principle by its stable ID (`UX-P07`) in design notes,
tickets, or code comments so the same reasoning is reused across a codebase.

This skill supplies the *why* — the mechanism that makes an interface work and
the line past which it manipulates. It does not produce visuals.

## Two modes

**Design** — there is no screen yet, or the screen is being extended. You decide
what the interface *should* do.

**Audit** — a screen exists (code, mockup, screenshot, URL). You judge what it
*already* does. Auditing for dark patterns is this mode read backwards: instead
of asking which lever is missing, ask which lever present crosses its own
ethical guard.

**Which mode.** Default on the artifact: something to examine → Audit; nothing
to examine → Design. An explicit request overrides the default — *"add a step to
this checkout"* ships an existing screen but asks for Design.

## Procedure — Design

1. State the screen's job in one sentence.
2. Scan the **whole** index below and keep every ID whose cue matches. Real
   screens have several jobs at once — a checkout is transactional *and*
   choice-heavy *and* trust-sensitive. Stopping at one group is the most common
   way to miss the lever that mattered.
3. Open the family file of every ID you kept.
4. Drop the ones whose ❌ covers this screen.
5. Write one item per survivor (see the output contract) and clear its ethical
   guard.

## Procedure — Audit

1. Inventory what the screen actually does: what it shows, asks, claims, and
   how it responds.
2. Scan the **whole** index and keep every ID whose cue matches what is present
   — including the levers you suspect are being *misused*, not only the ones you
   would have recommended.
3. Open the family file of every ID you kept.
4. Compare the screen against the entry. Each match resolves to one of: the
   lever is absent where it belongs, applied but weakened, or crossing its
   ethical guard.
5. Write one item per finding and give each its guard verdict. A `refused`
   verdict *is* the dark pattern — name it as the finding, not as a caveat.

## What you hand back

Every mode returns a **list of cited items**. An item carries, at minimum:

- **the ID** — `UX-P14`, so the reasoning is traceable and reusable;
- **what happens on screen** — concrete and specific to this interface;
- **the ethical guard verdict** — `respected`, `adjusted`, or `refused`.
  `adjusted` and `refused` each require one sentence of justification.

Design adds the **recommendation** — what to do. Audit adds the **finding** —
what is wrong — and its severity: `blocking` (the user is harmed or deceived),
`significant` (the screen works against its own goal), `minor`.

The rendering is free: a document, a table, review comments, or a code comment,
whichever fits where the answer lands. The contract binds the **fields**, not
the format. An item with no guard verdict is incomplete — the guard is a step,
not a remark.

## Catalog rules

- **Append-only IDs.** A `UX-Pxx` is never renumbered or reused; new principles
  are added at the end. A dropped one is marked DEPRECATED but keeps its number.
  File placement is not a property of the ID: an entry may move between families
  without renumbering.
- **The index never suffices to cite.** A one-line cue carries neither the
  applies/doesn't section nor the ethical guard. Citing an ID whose entry you
  have not opened produces a name-drop, not a design decision.
- **Ethical guard is universal.** Many of these levers sit one step from a dark
  pattern, so *every* entry carries the field — it is never omitted, and the
  rule admits no exception, DEPRECATED entries included. Where a lever has no
  realistic abuse vector, the field says so, opening with `No meaningful abuse
  vector` and one sentence of justification: a missing field is a defect, not a
  verdict that the lever is safe. Heightened caution where money, legal status, or
  irreversible actions are at stake: never exploit anxiety, fabricate urgency,
  or steer an unwanted commitment. Persuasion is non-coercive and respects the
  user's autonomy; anything that relies on deception or pressure is out.
- **Application context is mandatory.** A conversion-funnel lever (reciprocity,
  price anchoring, scarcity) does not transfer as-is to a transactional screen
  where the user is already committed. Every principle says where it applies and
  where it does not.

## Index — the 40 principles

Reach for a principle when its cue describes the screen in front of you. The
groupings below are the files the entries live in, nothing more: they are not a
routing gate, and a single screen routinely draws from all five.

`PRINCIPLES-cognition.md` — cognitive load & decision-making

- `UX-P01` Smart defaults — a field could be pre-filled from what is already known
- `UX-P06` Anchoring / contrast — a number or price is judged against something else
- `UX-P07` Hick's law — many routes or options are offered at once
- `UX-P08` Miller's law — the user must hold several items in mind at once
- `UX-P13` Tesler's law — a step could be automated or inferred instead of asked
- `UX-P14` Choice overload — more than a handful of comparable options sit together
- `UX-P15` Occam's razor — a screen has accumulated elements and needs cutting
- `UX-P16` Decoy effect — a comparison set includes an option nobody should pick
- `UX-P17` Framing effect — copy states a fact that could be framed as gain or loss

`PRINCIPLES-perception.md` — visual hierarchy, attention, grouping

- `UX-P09` Fitts's law — a target must be hit fast: CTA, confirm/cancel, touch target
- `UX-P10` Von Restorff — one action should dominate the others visually
- `UX-P18` Aesthetic-usability effect — a first impression or trust-sensitive screen
- `UX-P19` Jakob's law — a control or layout departs from what users meet elsewhere
- `UX-P20` Serial position effect — the order of a list, menu, or sequence matters
- `UX-P21` Proximity — spacing must say what belongs with what
- `UX-P22` Similarity — elements of the same kind must read as the same kind
- `UX-P23` Common region — a card, panel, or section boundary groups content
- `UX-P24` Prägnanz — the layout could resolve with fewer lines and boxes

`PRINCIPLES-motivation.md` — progress, commitment, retention

- `UX-P02` Never start at zero — a multi-step journey shows progress from nothing
- `UX-P03` Loss aversion — the user risks losing something real (unsaved work, an expiring draft)
- `UX-P05` IKEA effect — the user invests effort configuring or building something
- `UX-P11` Zeigarnik effect — a task is left unfinished and can be resumed
- `UX-P25` Goal-gradient effect — the end of a flow is in sight and can be shown
- `UX-P26` Commitment & consistency — a small first action precedes a larger ask
- `UX-P27` Sunk cost — the screen invokes what the user has already invested
- `UX-P28` Variable reward — a reward or delight moment repeats unpredictably
- `UX-P29` Parkinson's law — a step carries a time budget, a hold, or a deadline

`PRINCIPLES-persuasion.md` — social influence

- `UX-P04` Reciprocity — value is given before something is asked in return
- `UX-P30` Social proof — others' behavior is shown to guide a choice
- `UX-P31` Authority — credibility must be established: payment, security, health, finance
- `UX-P32` Scarcity — availability, stock, seats, or a deadline is limited
- `UX-P33` Liking — voice, tone, empty states, or error copy carry personality
- `UX-P34` Unity — the product speaks in terms of a shared identity or membership

`PRINCIPLES-trust.md` — feedback, errors, memory, credibility

- `UX-P12` Peak-end rule — a flow has a high point or an ending: confirmation, success, recovery
- `UX-P35` Recognition over recall — the user must carry something in memory across steps
- `UX-P36` Visibility of system status — something happens the user cannot see
- `UX-P37` Doherty threshold — a response takes longer than an instant
- `UX-P38` Error prevention & forgiveness — an action can be invalid, fail, or be irreversible
- `UX-P39` Curse of knowledge — wording assumes product knowledge: onboarding, labels, errors
- `UX-P40` Consistency & standards — the same thing appears in more than one place

Each family file opens with its own ID→name index. `FORMAT.md` holds the entry
template for adding a principle.

## Adding a principle

New principles enter through `FORMAT.md`: state the mechanism with an academic
reference, the application context, and the ethical guard — always, per the
catalog rule above. Reuse the canonical name (a shared anchor the agent already
knows), give it the next free ID, and add its line to the index above with a
cue phrased as a **screen situation**, not as a mechanism.
