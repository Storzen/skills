# Perception — attention, grouping & layout

For visual hierarchy, attention, grouping, and navigation. Entry template:
`FORMAT.md`. Catalog rules: `SKILL.md`.

- `UX-P09` — Fitts's law
- `UX-P10` — Von Restorff (isolation)
- `UX-P18` — Aesthetic-usability effect
- `UX-P19` — Jakob's law
- `UX-P20` — Serial position effect
- `UX-P21` — Proximity (Gestalt)
- `UX-P22` — Similarity (Gestalt)
- `UX-P23` — Common region (Gestalt)
- `UX-P24` — Prägnanz (simplicity / closure)

---

## UX-P09 — Fitts's law

**Principle.** Time to hit a target scales with its distance and inversely with
its size; make primary actions large and near, destructive ones small and far.

**Mechanism.** Fitts's law, a model of rapid pointing movements.

**Applies / doesn't.**
- ✅ Touch targets, primary CTAs, confirm/cancel placement, thumb-reach on
  mobile.
- ❌ — a general constraint, rarely inapplicable.

**Ethical guard.** Keep destructive or irreversible actions out of easy reach so
they are not triggered by accident — and never shrink a "decline" while
enlarging "accept" to trick the tap.

**Example.** The primary button is large and thumb-reachable; "Delete account"
is small and set apart.

---

## UX-P10 — Von Restorff (isolation effect)

**Principle.** The item that stands out visually is the one remembered and acted
on; give each screen one dominant call to action.

**Mechanism.** The isolation effect (von Restorff, 1933): the distinctive item
in a set is recalled best.

**Applies / doesn't.**
- ✅ Emphasizing the single primary action on a screen.
- ❌ When everything is emphasized, nothing is — competing CTAs cancel out.

**Ethical guard.** Emphasis must track the user's interest, not the seller's.
Rendering the accept path as a filled button and the decline path as faint grey
text is the isolation effect turned against the reader — the standard
confirmshaming layout. In a consequential pair, both options stay legible and
reachable at a glance; only visual weight may differ, and only where the
emphasized option is the one most users actually want.

**Example.** One filled primary button per screen; secondary actions are quiet
links.

---

## UX-P18 — Aesthetic-usability effect

**Principle.** Users perceive good-looking interfaces as easier to use and
forgive minor flaws in them; visual polish is a usability lever, not just decor.

**Mechanism.** The aesthetic-usability effect (Kurosu & Kashimura, 1995):
perceived beauty raises perceived usability and tolerance for problems.

**Applies / doesn't.**
- ✅ First impressions, trust-sensitive screens, marketing-to-product handoff.
- ❌ As a substitute for fixing real usability bugs — polish can *mask* problems
  in testing, so don't let it hide broken flows.

**Ethical guard.** Beauty may not be used to paper over a deceptive or broken
experience; it should make an honest interface pleasant, not disguise a bad one.

**Example.** A clean, well-spaced empty state makes a new-user dashboard feel
approachable rather than unfinished.

---

## UX-P19 — Jakob's law

**Principle.** Users spend most of their time on *other* products, so they
expect yours to work the same way; follow established conventions unless you have
a strong reason not to.

**Mechanism.** Jakob's law (Nielsen): transfer of learned mental models — people
apply patterns from familiar sites to yours.

**Applies / doesn't.**
- ✅ Standard controls, icon meanings, layout of nav/cart/search/settings.
- ❌ Where a convention is genuinely worse for your case, or you're deliberately
  creating a novel interaction — then teach it explicitly.

**Example.** The cart icon sits top-right and search is a magnifier, because
that's where users already look.

---

## UX-P20 — Serial position effect

**Principle.** People remember the first and last items in a series best; place
the most important items at the start and end, not buried in the middle.

**Mechanism.** Serial position effect — primacy and recency (Ebbinghaus;
Murdock, 1962).

**Applies / doesn't.**
- ✅ Navigation order, menu items, onboarding steps, a list of key features.
- ❌ Sequences with no importance ranking (alphabetical directories, sorted
  data).

**Example.** A bottom tab bar puts the two highest-value destinations at the far
left and far right.

---

## UX-P21 — Proximity (Gestalt)

**Principle.** Elements placed close together are perceived as related; use
spacing, not just lines or boxes, to group.

**Mechanism.** Gestalt principle of proximity: the mind groups nearby objects.

**Applies / doesn't.**
- ✅ Form field grouping, label-to-input pairing, card content, related actions.
- ❌ — foundational; the risk is under-using whitespace, not over-.

**Example.** A label sits tight above its field and far from the next field, so
pairing is unambiguous without dividers.

---

## UX-P22 — Similarity (Gestalt)

**Principle.** Elements that share color, shape, or size are read as the same
kind of thing; make same-function things look alike and different ones differ.

**Mechanism.** Gestalt principle of similarity: shared visual traits imply shared
meaning.

**Applies / doesn't.**
- ✅ Making all links look like links, all primary buttons identical, status
  colors consistent.
- ❌ When over-uniformity flattens a needed hierarchy — pair with Von Restorff to
  keep the primary action distinct.

**Example.** Every clickable link is the same accent color; static text never
uses it, so users learn what's interactive.

---

## UX-P23 — Common region (Gestalt)

**Principle.** Elements inside a shared boundary (a card, a panel) are perceived
as a group; use enclosure to bind related content and actions.

**Mechanism.** Gestalt principle of common region: a common background or border
overrides distance in grouping.

**Applies / doesn't.**
- ✅ Cards, grouped settings, a toolbar's actions, sectioned forms.
- ❌ When boxes multiply into visual clutter — prefer proximity/whitespace first,
  enclose only when grouping must be unmistakable.

**Example.** A settings section wraps its toggles in one bordered card so they
read as one unit.

---

## UX-P24 — Prägnanz (simplicity / closure)

**Principle.** The mind resolves complex or incomplete visuals into the simplest
stable form; you can imply structure and shape without drawing every line.

**Mechanism.** Law of Prägnanz and closure (Gestalt): perception favors simple,
complete interpretations and fills gaps.

**Applies / doesn't.**
- ✅ Minimal iconography, implied columns via alignment, letting whitespace do
  the work of borders.
- ❌ When "implied" tips into "ambiguous" and the user can't tell the structure —
  make the completion obvious, not a puzzle.

**Example.** A grid reads as aligned columns from spacing alone, with no
gridlines drawn.
