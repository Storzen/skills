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

## How to apply

1. Name the screen's job (see the mapping below) and open the matching family
   file(s).
2. Take the principles whose "applies / doesn't" section covers that job.
3. Apply them — then clear each one's **ethical guard** before shipping.

## Catalog rules

- **Append-only IDs.** A `UX-Pxx` is never renumbered or reused; new principles
  are added at the end. A dropped one is marked DEPRECATED but keeps its number.
- **Ethical guard is mandatory.** Many of these levers sit one step from a dark
  pattern. Every principle states the line between serving the user and
  manipulating them. Heightened caution where money, legal status, or
  irreversible actions are at stake: never exploit anxiety, fabricate urgency,
  or steer an unwanted commitment. Persuasion is non-coercive and respects the
  user's autonomy; anything that relies on deception or pressure is out.
- **Application context is mandatory.** A conversion-funnel lever (reciprocity,
  price anchoring, scarcity) does not transfer as-is to a transactional screen
  where the user is already committed. Every principle says where it applies and
  where it does not.

## Families — pick by the screen's job

Each family is a separate file, loaded only when its screen job is in play.

| Screen job / question | Family file |
| --- | --- |
| Choices, forms, settings, pricing — reduce load, aid a decision | `PRINCIPLES-cognition.md` |
| Visual hierarchy, attention, grouping, layout, navigation | `PRINCIPLES-perception.md` |
| Onboarding, multi-step flows, progress, retention, commitment | `PRINCIPLES-motivation.md` |
| Acquisition, landing, conversion — social influence | `PRINCIPLES-persuasion.md` |
| Transactional, high-stakes, feedback, errors, memory, trust | `PRINCIPLES-trust.md` |

Each family file opens with its own ID→name index. `FORMAT.md` holds the entry
template for adding a principle.

## Adding a principle

New principles enter through `FORMAT.md`: state the mechanism with an academic
reference, the application context, and — where the lever can be misused — the
ethical guard. Reuse the canonical name (a shared anchor the agent already
knows), give it the next free ID, and place it in the family that matches its
screen job.
