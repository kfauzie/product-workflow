# 6. Design: screen specs (pm-4)

> **FICTIONAL EXAMPLE.** Corvane, Riskline, Retrofit Planner, Ashgrove Partners, Project Lantern and Lantern Group are invented. All data is synthetic. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

Screens: [design/](design/), captured from the prototype. Borrowed patterns: Stripe (numbers with their source one click away), Linear (calm hierarchy).

| Screen | Example input | Expected output | Happy path | Edge cases | Acceptance criteria | Handoff |
|---|---|---|---|---|---|---|
| 1. Set up the deal | 14-site list; EV £360m and 6-year hold from the deal record | "14 of 14 sites found"; inputs confirmed | All sites match; confirm and continue | A site has no address: placed by coordinates, flagged | Nothing calculated yet; every input shows its source | → Brief |
| 2. The brief | Confirmed inputs | £18.6m defended (undefended £58.3m one toggle away), why, defences, deal terms | Read, edit the terms, send | Defences not confirmed: marked "to verify", never assumed | Fits one screen; every number has a "how it's calculated" link | → Send, or → Site detail |
| 3. Site detail | One site (the Port Avelin office) | Its hazards, defences, premiums; attach a document | Attach the insurance policy; see before and after | Document doesn't answer the question: pick another | The site and deal totals update from the document | → Back to the brief |
| 4. Send to the deal team | The brief | Drafted message, PDF and spreadsheet | Edit and send | No questions left without an owner | Every number in the message matches the brief | → The deal team (outside the product) |
