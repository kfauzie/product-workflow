---
name: 4-pm-solution-design
description: "Turn the solution concept into screens in the company's design system, one page by default, that a reviewer can follow live. Most important screen first. Use after the solution concept, before 5-pm-mvp-build."
---

# Solution design

**Role:** turn the concept's workflow into screens a reviewer can follow.
**Users:** the end user named in the concept; me and the reviewers who agree the screens live; a designer, if one takes them further.
**Target:** a first-time user can tell in five seconds what each screen is for and what to do next.
**Grounding:** the solution concept (Notion page linked in the run notes, fetched fresh every time); `company-context-design-system` (Figma via MCP: colours, type, components, existing screens); `company-context-glossary` (every label); `company-context-personas`; `0-pm-standard`.
**Tone:** the company's voice from `company-context-design-system`; the user's own terms from the interview notes. No technical or AI terms on screen.

## Principles
1. **Know the user and the job.** Design for the job the user needs done, starting from the matching persona and adjusting to the interview notes; the screen answers their "yes" trigger at a glance. Name a specific, known user with their role ("[Name], [role]"); otherwise use roles.
2. **Most important first, on one page.** Order the page by importance: what answers the user's job sits at the top, big; detail is one click away (expand a row, open a panel). A new screen only when the next step belongs to someone else, with a clear hand-over.
3. **Show only what matters.** Defaults labelled "Default", a few clear options, each fact once. Every input changes the answer or who gets it.
4. **Recommend, let the user decide.** Where the product recommends, show the recommendation with its reason, beside a control the user owns. Mark what the user changed ("[Setting] overridden", "[Field] adjusted"), warn when a change goes beyond the recommendation, and offer a one-click way back.
5. **Show the work.** Mark where each choice came from (their input, a default, or changed by them). Label what each number measures: a column that mixes sources is named for what all rows share, with each row's source marked; anything shown as live moves at a believable pace. Show evidence as the user met it (a chat as a chat, a document as a page), with our evaluation kept apart.
6. **Make it interactive, with little delights.** Make it as interactive as the job allows: numbers recalculate live as the user changes anything, a change shows its direction (green when good, red when not), and a short confirmation follows and fades. Add small moments of delight (a subtle animation, visible progress, live data ticking over, friendly wording) that make the product feel alive without getting in the way. The default state already shows the main interaction, e.g. one change made.
7. **Handle edge cases where they happen.** Missing data, unclear input, or something the product can't do: say so in place, let the user fix it there, then redo what depends on it.

## Step 1: Specify each screen
- **Input:** the concept's workflow and persona.
- **Output:** for each screen, one spec: example input, expected output, happy path, edge cases (quitting midway, incomplete information), acceptance criteria, and handoff to the next step or person.
- **Happy path:** group the workflow's steps into as few screens as the job allows (principle 2).
- **Edge cases:** a step that's outside the product (an email, an approval): show it as a hand-over, not a screen.
- **Acceptance criteria:** every workflow step has a screen or a named hand-over.
- **Handoff:** Step 2.

## Step 2: Design the screens
- **Input:** the screen specs; the design system.
- **Output:** screen images in the run's `design/` folder, one per screen, most important first.
- **Happy path:**
  - **Visual system:** clean B2B SaaS in the company's design system.
    - Colour: one hue per meaning (e.g. good, caution, bad, AI, reference, brand, neutral), each with fixed shades (text, tint, border) defined once as named values. Same meaning, same colour; different meanings, clearly different hues. The primary colour is for the main action only, and colour is never the only signal. Before shipping, list every colour and merge near-duplicates.
    - Icons and marks: small line icons beside labelled facts, in the text colour, never carrying meaning alone. A product mark uses shapes and colours comparable products don't, reads as intended in silhouette, and works at its smallest size (a browser tab).
  - **Layout and actions:** a short header in labelled lines (Customer, User, Job to be done), plus a step bar if there's more than one screen, and no other design notes on screen. Details as label | value tables; hover explanations for assumptions; notes and warnings look different from content. One primary button per screen, saying what it does. Controls side by side share one size; in equal-height cards the flexible part takes the spare space, so footers line up.
  - **Ground the layout in real products:** first study screenshots of three to five strong B2B SaaS products with the same or an adjacent job (websites, help centres, public galleries). Design from the patterns they share (e.g. summary numbers above a filterable table, detail in a side panel), name the source of each, and adapt it to the user; never copy a product's look.
- **Edge cases:**
  - No Figma: use `company-context-design-system`'s neutral defaults, and say so in the notes under the image.
  - A screen takes more than a few minutes: it's too detailed; cut it back.
- **Acceptance criteria:** realistic placeholder numbers that are not suspiciously round (no calculations, no data checks: real numbers come in `5-pm`); every label is in the glossary and has passed the copy review in `0-pm-standard`; walk the flow once as the user and fix anything confusing.
- **Handoff:** one screen first, the most important one; get feedback before making the rest. The agreed screens go to `5-pm-mvp-build` and are the design. If a designer takes them further, share the full set (specs, screens, prototype) as it is; they own the final visual call, and I'll ask for adjustments.
