# Trust — memory, feedback & error recovery

For transactional and high-stakes screens, system feedback, error states, and
anything where trust is the currency. Entry template: `FORMAT.md`. Catalog rules:
`SKILL.md`.

- `UX-P12` — Peak-end rule
- `UX-P35` — Recognition over recall
- `UX-P36` — Visibility of system status
- `UX-P37` — Doherty threshold
- `UX-P38` — Error prevention & forgiveness
- `UX-P39` — Curse of knowledge
- `UX-P40` — Consistency & standards

---

## UX-P12 — Peak-end rule

**Principle.** People judge an experience by its emotional peak and its end, not
its average; invest disproportionately in the most intense moment and the last
one.

**Mechanism.** Peak-end rule (Kahneman): retrospective evaluation weights the
peak and the ending.

**Applies / doesn't.**
- ✅ High-stakes confirmation moments, error recovery, completion and success
  screens.
- ❌ — applies to almost any multi-moment journey.

**Example.** A checkout ends on a warm, reassuring confirmation rather than a
bare "Order 12345".

---

## UX-P35 — Recognition over recall

**Principle.** Recognizing is easier than remembering; keep options, actions, and
prior inputs visible instead of making the user recall them.

**Mechanism.** Recognition over recall (Nielsen heuristic #6): retrieval from a
visible cue is far cheaper than free recall.

**Applies / doesn't.**
- ✅ Menus over memorized commands, autocomplete, showing recently used items,
  carrying context between steps.
- ❌ Deliberately minimal expert interfaces where recall is faster for power users
  (command palettes) — offer both.

**Example.** A search field suggests recent queries instead of asking the user to
retype what they searched before.

---

## UX-P36 — Visibility of system status

**Principle.** Always tell the user what's happening; every action gets timely,
clear feedback.

**Mechanism.** Visibility of system status (Nielsen heuristic #1): feedback keeps
the user's mental model aligned with reality and reduces anxiety.

**Applies / doesn't.**
- ✅ Loading states, save confirmations, progress, sync/connection status,
  especially in money and data-critical flows.
- ❌ Over-notifying trivial events until feedback becomes noise — signal only what
  matters.

**Ethical guard.** Status must be truthful. A spinner that implies work not
happening, or a "saved" that didn't save, breaks trust at the worst moment —
critical where money moves.

**Example.** A transfer screen shows "Processing… / Sent ✓ / Failed — retry" with
real states, never a fake success.

---

## UX-P37 — Doherty threshold

**Principle.** Keep system response under ~400 ms; when real work takes longer,
show immediate feedback so the interaction still feels responsive.

**Mechanism.** Doherty threshold: below ~400 ms, people stay in flow and
productivity rises; above it, attention drifts.

**Applies / doesn't.**
- ✅ Perceived performance: optimistic UI, skeletons, progress for slow
  operations, instant acknowledgement of taps.
- ❌ Faking completion before a critical operation has actually succeeded (see
  system status) — responsiveness ≠ lying about the result.

**Example.** A "like" updates instantly (optimistic) while the request settles in
the background, reverting visibly if it fails.

---

## UX-P38 — Error prevention & forgiveness

**Principle.** Prevent errors first; where they're possible, make actions
reversible and confirm the destructive ones. Users need clearly marked exits.

**Mechanism.** Error prevention and user control (Nielsen heuristics #5, #3):
stopping a mistake beats a good error message; an undo restores the sense of
safety.

**Applies / doesn't.**
- ✅ Constraints that disable invalid actions, confirmation on irreversible ones,
  undo, "cancel" always available, autosave.
- ❌ Confirming *everything* until dialogs are dismissed reflexively — reserve
  friction for the consequential and irreversible.

**Ethical guard.** Friction belongs on destructive actions, not on the user's
*exit*. Making "cancel", "unsubscribe", or "delete account" hard to reach is the
"roach motel" dark pattern. Easy in, easy out.

**Example.** Deleting a record shows an undo toast for 10 seconds instead of a
modal, and permanent deletion asks for explicit confirmation.

---

## UX-P39 — Curse of knowledge

**Principle.** Experts forget what novices don't know; design and write for
someone seeing the product for the first time, not for the team that built it.

**Mechanism.** The curse of knowledge — once you know something, you can't easily
model not knowing it, so jargon and skipped steps feel obvious to authors only.

**Applies / doesn't.**
- ✅ Onboarding, empty states, labels, error messages, help — plain language,
  defined terms, no internal jargon or acronyms.
- ❌ Genuine expert tools whose users share the vocabulary — match the audience,
  don't over-explain to specialists.

**Example.** An error says "Your card was declined by the bank" instead of
"Gateway error 402".

---

## UX-P40 — Consistency & standards

**Principle.** The same thing looks and behaves the same way everywhere in the
product; don't make users wonder whether different words or controls mean the
same thing.

**Mechanism.** Consistency and standards (Nielsen heuristic #4): internal
consistency plus platform conventions lower learning cost. Complements Jakob's
law (`UX-P19`), which is about *external* convention.

**Applies / doesn't.**
- ✅ Design systems, shared components, uniform terminology, matching interaction
  patterns across screens.
- ❌ When rigid consistency would keep a known-bad pattern — consistency serves
  usability, it isn't the goal itself.

**Example.** "Delete" always means the same action with the same confirmation
across every screen, never "Delete" here and "Remove" there for the same thing.
