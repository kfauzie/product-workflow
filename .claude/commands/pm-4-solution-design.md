---
name: pm-4-solution-design
description: "Turn the solution concept into screens in the company's design system, one per workflow step, that a reviewer can follow live. Most important screen first. Use after the solution concept, before pm-5-mvp-build."
---

# Solution design

**Role:** turn the concept's workflow into screens a reviewer can follow, one step per screen.
**Users:** the end user named in the concept; me and the reviewers who agree the screens live; the designer who takes them further.
**Target:** a first-time user can tell in five seconds what each screen is for and what to do next.
**Grounding:** the solution concept (Notion page linked in the run notes, fetched fresh every time); `design-system` (Figma via MCP: colours, type, components, existing screens); `product-glossary` (every label); `customer-personas`; `pm-standard`.
**Tone:** the company's voice from `design-system`; the user's own terms from the interview notes. No technical or AI terms on screen.

## Principles
1. **Decision first.** If a screen has a recommended decision, it's at the top, with the reason right under it.
2. **Know the user.** Start from the matching persona, then adjust to the interview notes. The screen answers the persona's "yes" trigger at a glance. Labels use roles, not people's names.
3. **One step per screen.** When the next step belongs to someone else, make the hand-over clear.
4. **Show only what matters.** Sensible defaults, labelled "Default", and a few clear options. Each fact appears once. Every input changes the answer or who gets it.
5. **Hierarchy and progressive disclosure.** Key information big and up front; detail lower, smaller, or one click away.
6. **Trust.** The user can see how each number was produced, and where every choice came from (their input, a default, or changed by them).
7. **Handle edge cases.** Missing data, unclear input, or something the product can't do: say so where it happens, let the user fix it there, then redo what depends on it.
8. **Make it enjoyable.** Serious, with a little personality: friendly wording, a sense of progress.

## Step 1: Specify each screen
- **Input:** the concept's workflow and persona.
- **Output:** for each step of the workflow, one screen spec: example input, expected output, happy path, edge cases (quitting midway, incomplete information), acceptance criteria, and handoff to the next step or person.
- **Happy path:** steps group naturally into screens, one step each.
- **Edge cases:** a step that's outside the product (an email, an approval): show it as a hand-over, not a screen.
- **Acceptance criteria:** every workflow step has a screen or a named hand-over.
- **Handoff:** Step 2.

## Step 2: Design the screens
- **Input:** the screen specs; the design system.
- **Output:** screen images in the run's `design/` folder, one per step, most important first.
- **Happy path:**
  - **Look:** clean B2B SaaS in the company's design system. Primary colour only for the main action; soft tints for status; colour is never the only signal.
  - **Layout:** details as label | value tables; a lighter line under each heading; hover explanations for assumptions; source tags on choices; notes and warnings look different from content.
  - **Actions:** one primary button per screen; others secondary; buttons say what they do.
  - **Borrow patterns:** name the closest comparable product for each step (e.g. Typeform for guided flows, Stripe for numbers with their source one click away, Linear for calm hierarchy).
  - **Prototype frame:** a ribbon at the top ("User: [role]" and "Job to be done: [job]") and a clickable step bar; both left out of exports. No other design notes on screen.
- **Edge cases:**
  - No Figma: use `design-system`'s neutral defaults, and say so in the notes under the image.
  - A screen takes more than a few minutes: it's too detailed; cut it back.
- **Acceptance criteria:** realistic placeholder numbers (no calculations, no data checks: real numbers come in `pm-5`); every label is in the glossary; walk the flow once as the user and fix anything confusing.
- **Handoff:** one screen first, the most important one; get feedback before making the rest. The agreed screens go to `pm-5-mvp-build`.
