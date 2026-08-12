# Persuasion — social influence (Cialdini)

For acquisition, landing, and conversion screens. Entry template: `FORMAT.md`.
Catalog rules: `SKILL.md`. These are Cialdini's principles of influence; every
one is dual-use, so the ethical guard is load-bearing. Persuasion is
non-coercive and truthful — anything relying on deception or pressure is out.

- `UX-P04` — Reciprocity
- `UX-P30` — Social proof
- `UX-P31` — Authority
- `UX-P32` — Scarcity
- `UX-P33` — Liking
- `UX-P34` — Unity

---

## UX-P04 — Reciprocity

**Principle.** Give genuine value before asking for commitment; people are
inclined to return a favor.

**Mechanism.** The reciprocity norm (Cialdini): an unsolicited gift creates a
felt obligation to reciprocate.

**Applies / doesn't.**
- ✅ Acquisition and landing: a useful free tool, sample, or report before asking
  for signup.
- ❌ Screens where the user is already committed — the favor reads as friction.

**Ethical guard.** The value must be real and unconditional. A "gift" that is
actually a bait-and-switch, or that quietly incurs an obligation, is manipulation.

**Example.** A tax tool shows the full estimate first, then offers to email a
saved copy in exchange for an address.

---

## UX-P30 — Social proof

**Principle.** People look to others' behavior to decide their own, especially
under uncertainty; show that real people use and endorse the thing.

**Mechanism.** Social proof (Cialdini): the actions of similar others reduce
perceived risk.

**Applies / doesn't.**
- ✅ Genuine reviews, ratings, usage counts, customer logos, "most popular" on a
  truly popular option.
- ❌ Low-trust or low-volume contexts where thin proof backfires — better none
  than "1 review".

**Ethical guard.** Every number and testimonial must be true and current. Fake
reviews, invented counts, or "17 people are viewing this" fabrications are
deceptive and often illegal.

**Example.** A pricing page shows a real, verifiable "used by 12,000 teams" and
labels the tier most customers actually pick.

---

## UX-P31 — Authority

**Principle.** People defer to credible expertise and trust signals; surface real
credentials, certifications, and expert endorsement.

**Mechanism.** Authority (Cialdini): markers of expertise or legitimacy increase
compliance.

**Applies / doesn't.**
- ✅ Trust-sensitive domains (health, finance, security): security badges,
  certifications, expert authorship, credible sourcing.
- ❌ Where authority is irrelevant to the decision, or where badges are decorative
  clutter.

**Ethical guard.** Authority signals must be earned and verifiable. Fake trust
badges, borrowed logos, or implied endorsements you don't have are deceptive —
and corrosive in exactly the high-stakes contexts where they'd help.

**Example.** A payments page shows the actual compliance certifications the
product holds, linked to proof.

---

## UX-P32 — Scarcity

**Principle.** Limited availability raises perceived value and urgency; when
something is genuinely limited, saying so helps the user decide.

**Mechanism.** Scarcity (Cialdini): people weight scarce things more heavily and
fear missing out.

**Applies / doesn't.**
- ✅ Real limits: true low stock, a real deadline, genuinely capped seats.
- ❌ Everything else. This is the most-abused persuasion lever online.

**Ethical guard.** The scarcity must be real and accurate. Fake "only 2 left"
counters, countdowns that reset, and invented deadlines are textbook dark
patterns; several are now regulated. If you can't verify the limit, don't show
one. Never manufacture scarcity around a user's money.

**Example.** An event page shows the true remaining seat count from inventory,
and stops showing urgency once seats are ample.

---

## UX-P33 — Liking

**Principle.** People say yes more readily to those they find likeable, similar,
or warm; a human, friendly, respectful tone lowers resistance.

**Mechanism.** Liking (Cialdini): similarity, warmth, and genuine praise increase
persuasion.

**Applies / doesn't.**
- ✅ Voice and tone, friendly empty states, human error messages, showing the
  real team behind the product.
- ❌ Serious or high-stakes moments where forced friendliness reads as flippant
  (an error moving money, a security warning).

**Ethical guard.** Warmth must be sincere, not a veneer to smooth over a bad
deal. "Confirmshaming" — guilt-tripping the decline option ("No thanks, I like
paying full price") — weaponizes liking and is a dark pattern.

**Example.** A decline link reads plainly "No thanks", never a guilt-laden
sentence.

---

## UX-P34 — Unity

**Principle.** People are most influenced by those they see as *one of us*; a
shared identity or membership deepens trust and belonging.

**Mechanism.** Unity (Cialdini, 2016): shared identity ("we") is a stronger bond
than mere similarity, and amplifies the other principles.

**Applies / doesn't.**
- ✅ Community products, membership, mission-driven brands: language of shared
  identity and belonging that is actually true of the user.
- ❌ Where no real shared identity exists — claimed kinship rings hollow and
  breaks trust.

**Ethical guard.** Belonging must be genuine, opt-in, and never used to pressure
the in-group into choices against their interest ("real members upgrade").
Exploiting identity to sell is manipulation.

**Example.** An open-source tool speaks to "we maintainers" because its users
genuinely are that community.
