# Cognition — cognitive load & decision-making

For choice-heavy screens: forms, settings, pricing, anything asking the user to
decide. Entry template: `FORMAT.md`. Catalog rules: `SKILL.md`.

- `UX-P01` — Smart defaults
- `UX-P06` — Anchoring / contrast
- `UX-P07` — Hick's law
- `UX-P08` — Miller's law
- `UX-P13` — Tesler's law (conservation of complexity)
- `UX-P14` — Choice overload
- `UX-P15` — Occam's razor
- `UX-P16` — Decoy effect
- `UX-P17` — Framing effect

---

## UX-P01 — Smart defaults

**Principle.** Never show an empty field when a likely value exists: pre-fill
with the most common, safe, reversible choice.

**Mechanism.** Status-quo bias — people rarely change a value already set, since
the effort and doubt of changing outweigh the perceived gain (Samuelson &
Zeckhauser, 1988; Johnson & Goldstein, 2003). Each default also removes a
decision, easing cognitive load (Hick's law).

**Applies / doesn't.**
- ✅ Forms, settings, repeated selections, onboarding — anywhere a choice is
  right for most people.
- ❌ High-stakes or irreversible choices: pre-fill ≠ pre-decide. Never default a
  money movement or a bundled add-on.

**Ethical guard.** Ethical when the default serves the *user's* most likely
intent and is trivially changeable. It becomes manipulation when it exploits
inertia for a choice the user would not make knowingly — a pre-checked opt-in or
hidden opt-out is a dark pattern.

**Example.** A shipping form defaults country from locale and quantity to 1; the
user confirms instead of typing.

---

## UX-P06 — Anchoring / contrast

**Principle.** The first number or option seen becomes the reference for judging
the rest; never present a price or option in isolation.

**Mechanism.** Anchoring and adjustment (Tversky & Kahneman, 1974): judgments
stay biased toward an initial value.

**Applies / doesn't.**
- ✅ Pricing pages, plan comparison, the ordering of options.
- ❌ Contexts where a controlled first impression would hide a material fact.

**Ethical guard.** A real, relevant reference (a higher-tier plan shown first) is
fair. Inventing a fake "original price" to fabricate a discount is deceptive and,
in many jurisdictions, illegal.

**Example.** A three-tier plan page lists the premium tier first so the middle
tier reads as reasonable.

---

## UX-P07 — Hick's law

**Principle.** Decision time grows with the number and complexity of choices;
reduce or segment options.

**Mechanism.** Hick–Hyman law: reaction time rises logarithmically with the
number of alternatives.

**Applies / doesn't.**
- ✅ Navigation, menus, long forms (split into steps), option-heavy screens.
- ❌ When collapsing options hides a consequential choice the user needs to see.

**Ethical guard.** Reducing options serves the user only when nothing
consequential leaves the screen. Collapsing, nesting, or defaulting away a
choice that changes what the user pays, agrees to, or gives up is not
simplification — it is concealment. Segment a consequential choice; never remove
it from view.

**Example.** A long signup form becomes a three-step wizard, each step a handful
of fields.

---

## UX-P08 — Miller's law

**Principle.** Working memory holds only a handful of items (~4; the popular
"7±2" overstates it); chunk information.

**Mechanism.** Capacity limits of short-term memory (Miller, 1956; refined by
Cowan, 2001).

**Applies / doesn't.**
- ✅ Grouping digits in a phone or card number, limiting nav length, stepwise
  forms.
- ❌ Reference material meant to be scanned, not memorized.

**Example.** A 10-digit number is grouped as 3-3-4 rather than one run.

---

## UX-P13 — Tesler's law (conservation of complexity)

**Principle.** Every process has an irreducible complexity that cannot be
removed, only shifted; decide deliberately whether the system or the user
absorbs it — default to the system.

**Mechanism.** Tesler's law of conservation of complexity: simplifying one side
moves the burden, it does not delete it.

**Applies / doesn't.**
- ✅ Any flow where a step could be automated, inferred, or pre-filled instead of
  asked of the user.
- ❌ Cases where hiding complexity would strip control the user genuinely needs
  (expert tools, legal consent).

**Ethical guard.** Absorbing complexity for the user is good — unless "absorbing"
means making a consequential decision on their behalf without disclosure. Hide
effort, not stakes.

**Example.** An address form auto-fills city and region from a postal code
rather than making the user type all three.

---

## UX-P14 — Choice overload

**Principle.** Too many options at once raise the odds the user picks nothing;
cut, group, or stage the choices.

**Mechanism.** Choice overload / the paradox of choice — more alternatives
increase effort and regret, depressing decisions (Iyengar & Lepper, 2000).
Related to Hick's law but about *abandonment*, not just speed.

**Applies / doesn't.**
- ✅ Product grids, plan pickers, long settings — reduce to a curated set or add
  filtering and sensible defaults.
- ❌ Catalogs users come specifically to browse widely; there, invest in
  filtering rather than cutting.

**Ethical guard.** Curate to help the user decide, not to bury the option that
serves them (e.g. hiding the free tier among noise).

**Example.** A pricing page shows three plans with one marked "recommended"
instead of a matrix of ten.

---

## UX-P15 — Occam's razor

**Principle.** Among designs that work, prefer the one with the fewest moving
parts; remove every element that doesn't earn its place.

**Mechanism.** Occam's razor applied to interfaces: each added element costs
attention and maintenance, so the simplest adequate solution usually wins.

**Applies / doesn't.**
- ✅ Reviewing a screen for elements to cut; resisting feature creep on a view.
- ❌ When "simpler" removes a genuine affordance and pushes complexity onto the
  user (see Tesler's law) — simplicity of the screen is not the goal, simplicity
  of the *task* is.

**Example.** A checkout drops optional fields (company, address line 2 behind a
toggle) to the essentials.

---

## UX-P16 — Decoy effect

**Principle.** Adding a deliberately inferior third option shifts preference
toward a target option by making it look dominant.

**Mechanism.** The decoy effect (asymmetric dominance; Huber, Payne & Puto,
1982) — a dominated option reshapes the comparison, as in the classic Economist
subscription pricing.

**Applies / doesn't.**
- ✅ Understanding *why* a comparison set steers choices; auditing whether your
  own tiers contain an accidental decoy.
- ❌ As a tactic to push users toward the option that serves *you*, not them.

**Ethical guard.** This is the catalog's clearest manipulation risk. Use it to
*detect and remove* accidental decoys and to present honest, comparable options —
not to engineer a phantom option that nudges users away from what they'd choose
informed. Never deploy around money the user is spending under pressure.

**Example.** Audit finding: a "print-only" tier priced equal to "print + digital"
exists only to make the bundle look better — flag it, don't ship it as a trick.

---

## UX-P17 — Framing effect

**Principle.** The same fact framed as a gain or a loss, a percentage or a count,
changes the decision; choose the frame that is both accurate and clearest.

**Mechanism.** Framing effect (Tversky & Kahneman, 1981): preferences flip with
logically equivalent wordings. Pairs with loss aversion (`UX-P03`).

**Applies / doesn't.**
- ✅ Copy for a choice with real trade-offs — "90% fat-free" vs "10% fat",
  "save 3 hours" vs "lose 3 hours".
- ❌ Where the honest frame is neutral and any spin misleads.

**Ethical guard.** Legitimate when both frames are true and you pick the clearer;
manipulation when the frame hides a downside or exaggerates a benefit. The
frame must not change what a careful user would conclude.

**Example.** A backup setting reads "Protects the last 30 days of your work"
rather than a vague "Enable versioning".
