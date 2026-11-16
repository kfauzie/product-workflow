---
name: 4-pm-solution-design
description: "Turn the solution concept into screens in the company's design system, one per workflow step, that a reviewer can follow live. Most important screen first. Use after the solution concept, before 5-pm-mvp-build."
---

# Solution design

**Role:** turn the concept's workflow into screens a reviewer can follow, one step per screen.
**Users:** the end user named in the concept; me and the reviewers who agree the screens live; the designer who takes them further.
**Target:** a first-time user can tell in five seconds what each screen is for and what to do next.
**Grounding:** the solution concept (Notion page linked in the run notes, fetched fresh every time); `company-context-design-system` (Figma via MCP: colours, type, components, existing screens); `company-context-glossary` (every label); `company-context-personas`; `0-pm-standard`.
**Tone:** the company's voice from `company-context-design-system`; the user's own terms from the interview notes. No technical or AI terms on screen.

## Principles
1. **Know the user and the job.** Start from the matching persona, then adjust to the interview notes; the screen answers the persona's "yes" trigger at a glance. When the user is a specific, known person, name them with their role ("[Name], [role]"); elsewhere, labels use roles.
2. **Decision first, on one page.** Put the recommended decision at the top with the reason right under it, then how the answer is produced, then the detail. Key information big and up front; everything else one click away (expand a row, open a panel), not a second screen. One step per screen when a flow truly needs several, with a clear hand-over when the next step belongs to someone else.
3. **Show only what matters.** Sensible defaults, labelled "Default", and a few clear options. Each fact appears once. Every input changes the answer or who gets it.
4. **Recommend, let the user decide.** Show the product's recommendation and a separate control the user owns. Mark anything the user changed, naming what changed ("[Setting] overridden", "[Field] adjusted"); warn when a change goes beyond the recommendation; offer a one-click way back.
5. **Show the work.** The user can see how each number was produced and where each choice came from (their input, a default, or changed by them). Label what each number really measures: if a column mixes sources, name it for what all rows share and mark the source on each row; anything shown as live moves at a believable pace. Show evidence as the user met it (a conversation as a chat, a document as a page), in reading order: input, response, then our evaluation, kept visibly apart.
6. **Respond to every change, warmly.** Numbers recalculate live; a change shows its direction (green when good, red when not); a short confirmation follows and fades. Show progress where there is any (a step bar, a progress indicator), and keep the wording friendly. The default state already shows the main interaction, e.g. one change already made.
7. **Handle edge cases where they happen.** Missing data, unclear input, or something the product can't do: say so in place, let the user fix it there, then redo what depends on it.

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
  - **Visual system:** clean B2B SaaS in the company's design system.
    - Colour: few colours, each with one meaning. Give each meaning one hue (e.g. good, caution, bad, AI, reference, brand, neutral) with a fixed set of shades (text, tint, border), defined once as named values; reuse a colour wherever the meaning is the same and keep different meanings clearly different, never near-duplicates. The primary colour is for the main action only; colour is never the only signal. Before shipping, list every colour on the page and merge near-identical shades that mean the same thing.
    - Icons and marks: small line icons beside labelled facts help scanning (they take the text colour and never carry meaning alone). For a product mark, list the shapes and colours comparable products use and pick ones they don't; check it at its smallest size (e.g. a browser tab) and that its silhouette reads as intended.
  - **Layout and actions:** details as label | value tables; a lighter line under each heading; hover explanations for assumptions; source tags on choices; notes and warnings look different from content. One primary button per screen, others secondary, each saying what it does. Controls that sit side by side share one size. In cards of equal height, let the flexible part absorb spare space so related parts stay together and footers line up. A short header in labelled lines (Customer, User, Job to be done), plus a step bar if there's more than one screen; no other design notes on screen.
  - **Ground the layout in real products:** before designing, look at screenshots of three to five well-regarded B2B SaaS products with the same or an adjacent job (their websites, help centres, public galleries). Note the layout patterns they share (e.g. summary numbers above a filterable table, detail in a side panel, settings beside a live preview) and what each does best; name the source for each pattern you use (e.g. Stripe for numbers with their source one click away, Linear for calm hierarchy). Design from the shared pattern, adapted to the user; never copy a product's look.
- **Edge cases:**
  - No Figma: use `company-context-design-system`'s neutral defaults, and say so in the notes under the image.
  - A screen takes more than a few minutes: it's too detailed; cut it back.
- **Acceptance criteria:** realistic placeholder numbers that are not suspiciously round (no calculations, no data checks: real numbers come in `5-pm`); colours mean the same thing everywhere, including on controls; every label is in the glossary and has passed the copy review in `0-pm-standard`; walk the flow once as the user and fix anything confusing.
- **Handoff:** one screen first, the most important one; get feedback before making the rest. The agreed screens go to `5-pm-mvp-build`. The full set (screen specs, screen images and the working prototype) is ready to share with a designer as it is; they own the ideas and the final visual call, and I'll ask for adjustments if they want something different.
