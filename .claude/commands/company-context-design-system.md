---
name: company-context-design-system
description: "The company's design system and voice: colour roles, fonts, logo, components, on-screen voice and a copy checklist. Pulled from Figma via MCP, else from the active context folder. Use for any screen, prototype or customer-facing copy."
---

# Design system

**Role:** make screens and prototypes look and sound like the company's real product.
**Users:** `pm-4-solution-design` and `pm-5-mvp-build`; a designer, if one takes the screens further.
**Target:** a reviewer would accept the screens as the company's product at a glance; no colour, font or word that the design system doesn't allow.
**Grounding:**
1. Figma via MCP: variables and styles (colours, type), components, existing screens for patterns
2. `design-system.md` in the active context folder
3. If neither exists: neutral defaults (greyscale plus one accent), labelled as defaults

**Tone:** the company's voice. If none is given: expert, plain, confident; no jargon, no alarmist framing.

## Step 1: Load
- **Input:** the Figma file named in the context folder, or `design-system.md`.
- **Output:** colour roles (main action, text, headings, background, panels, status colours), fonts with fallbacks, logo use, the components to reuse, voice rules, and a copy checklist.
- **Happy path:** Figma is connected and the file has variables and components. Reuse them as they are.
- **Edge cases:**
  - No Figma: use the context file. With neither, use the neutral defaults and say so on the design notes, not on the screen.
  - Brand fonts not available in a prototype: use the named fallback.
  - The voice rules clash with the customer's own terms: the customer's terms win on screen; flag the clash.
- **Acceptance criteria:** every colour on a screen has a role from the system; the main action uses the system's primary colour; colour is never the only signal (a warning also says "Warning").
- **Handoff:** `pm-4` and `pm-5` apply it. If there's a designer, they make the final visual call.
