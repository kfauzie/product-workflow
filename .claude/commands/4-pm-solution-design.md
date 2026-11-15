---
name: 4-pm-solution-design
description: "Turn the solution concept into screens in the company's design system, one per workflow step, that a reviewer can follow live. Most important screen first. Use after the solution concept, before 5-pm-mvp-build."
---

# Solution design

**Role:** turn the concept's workflow into screens a reviewer can follow, one step per screen.
**Users:** the end user named in the concept; me and the reviewers who agree the screens live; the designer who takes them further.
**Target:** a first-time user can tell in five seconds what each screen is for and what to do next.
**Grounding:** the solution concept (Notion page linked in the run notes, fetched fresh every time); `design-system` (Figma via MCP: colours, type, components, existing screens); `product-glossary` (every label); `customer-personas`; `0-pm-standard`.
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
9. **One page by default.** Lead with the few numbers that answer the job, then the rule that produces the recommendation, then the detail. Everything else is one click away (expand a row, open a panel), not a second screen.
10. **Recommend, let the user decide.** Show the product's recommendation and a separate control the user owns. Mark anything the user changed, naming what changed ("[Setting] overridden", "Adjusted by user"), warn when a change goes beyond the recommendation, and offer a one-click way back.
11. **Label what each number really measures.** If a column mixes sources (live data and a test run), name it for what all rows share and mark the source on each row; don't call it "live" if some rows aren't. Anything shown as live moves at a pace the reader can believe, or the page says why it doesn't.
12. **Make every change visible.** Numbers recalculate live from the current settings; a change shows its direction (green when good, red when not) and a short confirmation that fades. The default state should already show the main interaction, e.g. one change already made.
13. **Name every actor without ambiguity.** If two things could share a word (a person and an AI, a customer and an end user), always qualify it, and use the same names on every screen.
14. **One word per concept.** When a label changes, change it everywhere it refers to the same thing (headers, rules, summaries, warnings, docs) in the same pass.
15. **Show evidence as the user met it.** Present a record in its native form (a conversation as a chat, a document as a page), in reading order: input, response, the rule it was judged by, the verdict. Keep our analysis (rules, grades) visibly outside the evidence, and let the verdict's colour be readable at a glance.

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
  - **Layout:** details as label | value tables; a lighter line under each heading; hover explanations for assumptions; source tags on choices; notes and warnings look different from content; small line icons beside labelled facts help scanning (they inherit the text colour and never carry meaning alone); in cards of equal height, let the flexible part absorb spare space so related parts stay together and footers line up.
  - **Actions:** one primary button per screen; others secondary; buttons say what they do.
  - **Borrow patterns:** name the closest comparable product for each step (e.g. Typeform for guided flows, Stripe for numbers with their source one click away, Linear for calm hierarchy).
  - **Marks and icons:** list the shapes and colours comparable products use, then pick ones they don't; check the mark at the smallest size it will appear (e.g. a browser tab) and that its silhouette reads as what it is meant to be.
  - **Prototype frame:** a ribbon at the top ("User: [role]" and "Job to be done: [job]") and a clickable step bar; both left out of exports. No other design notes on screen.
- **Edge cases:**
  - No Figma: use `design-system`'s neutral defaults, and say so in the notes under the image.
  - A screen takes more than a few minutes: it's too detailed; cut it back.
- **Acceptance criteria:** realistic placeholder numbers that are not suspiciously round (no calculations, no data checks: real numbers come in `5-pm`); a short header says what the page is and who it is for, in labelled lines, not a paragraph; colours mean the same thing everywhere, including on controls; every label is in the glossary; walk the flow once as the user and fix anything confusing.
- **Handoff:** one screen first, the most important one; get feedback before making the rest. The agreed screens go to `5-pm-mvp-build`.
