---
name: 5-pm-mvp-build
description: "Turn the agreed screens into a working first version, fast: one HTML file, numbers calculated by code. Use when building or changing the prototype."
---

# Build: the working first version

**Role:** make the agreed screens work end to end, with real numbers, so the customer can try the flow.
**Users:** me and the customer in the MVP review; whoever takes it to production: an engineer, or me.
**Target:** the whole flow clicks through with no errors; every number matches the concept's test cases.
**Grounding:** the agreed screens from `4-pm`; the solution concept (workflow, AI / code / people split, success criteria, test cases) from the Notion page in the run notes, fetched fresh; `company-context-design-system`; `company-context-glossary`; `0-pm-standard`.
**Tone:** match the agreed screens exactly.

## Step 1: First build
- **Input:** the screens, the concept, the data.
- **Output:** one plain HTML file with inline JS and CSS (no framework, no build step), plus a test file and a headless check.
- **Happy path:** build all agreed screens in one go, so the flow can be tried end to end. Calculations sit in plain functions that tests can import. Use the data provided directly. Add a small animation when the step changes.
- **Edge cases:**
  - No real data: use a small synthetic file, clearly labelled on screen, and make it believable:
    - **Grounded:** base it on how comparable real products and official guidance handle the same situations (their public help content), paraphrased, never copied; say when a source couldn't be read directly.
    - **Source first:** write the reference the examples depend on (the policy, rulebook, price list or catalogue), then derive every example from it, so each example quotes its source by ID, every outcome follows from it, and a test checks the quotes.
    - **As messy as the real thing:** a classification has a catch-all for what fits no category; numbers are plausible, never suspiciously round.
    - **Expert-proof:** read each example as a domain expert would; the input, the response and the verdict must hold together.
  - The concept leaves a number undefined: stop and name it, don't invent a formula.
- **Acceptance criteria:**
  - **Correct:** every number is calculated by code, following the concept's AI / code / people split; when the brief gives data or rules, tests check them exactly (every row, every rule outcome); the concept's test cases pass; text that quotes a number reads it from the same value, so the two never disagree.
  - **Interactive:** every control recalculates everything that depends on it, and tests cover the override paths, not just the default; anything the user may want to check (a rule, a source) is one click from where it's cited, opening at the exact item.
  - **Shippable:** a headless check (about 10 seconds) loads the page, clicks through the main flow and finds no errors; wording rules (banned words, punctuation) are enforced by a check; it works at phone and tablet widths with no sideways scrolling, and small-screen changes leave the desktop view untouched (compare desktop screenshots before and after).
- **Handoff:** tell me how to open it; screenshots only if I ask. If the work is public, a live link (static hosting) and checks that run on every push make it easy to review.

## Step 2: Change one thing at a time
- **Input:** my feedback.
- **Output:** an edited file (never regenerate the whole file), with tests and the headless check rerun.
- **Happy path:** each change takes about two minutes.
- **Edge cases:**
  - A change will take longer: tell me first and suggest a smaller step.
  - Something is wrong (a bug, a wrong number): find how far it reaches (one case or all), find the root cause, fix the pattern not the case, add a test that would have caught it, and tell whoever was affected.
- **Acceptance criteria:** tests and the headless check pass after every change. A change to wording or examples leaves the numbers untouched unless I ask; prove it by comparing the data before and after. When a change does move numbers, update everything that quotes them (tests, docs, screenshots, the concept's test cases), and flag any target or success criterion the new numbers miss rather than quietly moving it.
- **Handoff:** back to me, or to `6-pm-mvp-review` when the flow is ready to show.

## Later, only if I ask
- Branch and PR with screenshots, how to run it and test results
- Dark mode
- A clickable demo that replays precomputed answers
- Taking it to production: with no engineer, I ship it myself from the PR with tests; with engineers, deliver the spec, the prototype and the PR together, adjusted afterwards if they want something different. Either way: one PR per screen behind a feature flag, engineer review, staging, release, and measurement against the agreed targets. Size the launch note to the change: a small change gets a line in the product update; a big one gets updated guides, the teams who need to know told, and a check-in afterwards.
