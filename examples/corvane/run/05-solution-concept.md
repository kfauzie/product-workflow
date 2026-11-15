# 5. Spec: solution concept (pm-3)

> **FICTIONAL EXAMPLE.** Corvane, Riskline, Retrofit Planner, Ashgrove Partners, Project Lantern and Lantern Group are invented. All data is synthetic. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

> **Recommendation: a one-page Deal Climate Brief in Riskline, with the defended case at the centre.** It names the defences behind the defended figure (which, who provides them, to what standard), counts rising insurance premiums as a cost, puts the method one click from every number, and turns the result into deal terms. For Lantern: **£18.6m over the 6-year hold if the Port Avelin office is defended, £58.3m if not.**

## 1. The problem
- **Asked for:** "more useful to the deal side".
- **Real problem:** the Head of Sustainability needs the deal team to act on climate findings, but the output assumes no flood defences, so the deal team dismisses it and climate never changes a price or terms.
- **Evidence:** the notes in [03-discovery-notes.md](03-discovery-notes.md) (paraphrase); defended vs undefended moves the total from £58.3m to £18.6m ([04-synthesis.md](04-synthesis.md)).

## 2. Impact
- **Head of Sustainability's team:** analysis that ends as a checklist tick.
- **Deal team:** prices up to £58.3m of climate damage at zero, and assumes insurance is free.

## 3. Solution ideas
| | A. One-page deal brief | B. Defence verification service | C. Spreadsheet feed for the deal model |
|---|---|---|---|
| User | Answers the defences objection on the page, in deal terms. *Judgement* | Trusted, but adds days. *Judgement* | Into the model, but no "why". *Judgement* |
| Commercial | Retention and upsell (more deals assessed) | New revenue; doesn't scale | Retention |
| Effort | Small to medium; data: a defence register for key sites | High per deal | Small |

## 4. Recommendation
**A, with C's spreadsheet as its export.** User value tipped it. **Later:** B for the largest deals.

## 5. Workflow
- The Head of Sustainability opens Lantern's 14 sites in Riskline and clicks **Create the brief**; EV and hold come from the deal record.
- The product works out both cases (middle scenario): defended £18.6m, undefended £58.3m.
- It shows the defence evidence for the Port Avelin office (marked "to verify") and premiums rising over the hold.
- It drafts deal terms: a price adjustment, a condition before closing, a 100-day plan item. He edits them and sends the brief and the yearly cost spreadsheet to the deal team.

## 6. What AI, code and people do
- **AI:** suggests defence evidence from documents and public sources (marked "to verify"); drafts the terms' wording.
- **Code:** every number; the checks.
- **People:** the Head of Sustainability confirms the evidence and terms; the deal team decides.

## 7. Success criteria
- **Target:** on the next deal, the deal team builds the climate cost into its model, offer or terms (today: never).
- **Test cases (known answers):** defended £18.55m; undefended £58.28m; 4-year hold £38.70m; very high scenario £60.81m; premiums £31.57–42.09m (defended). See `build/test_mvp.js`.

## 8. Assumptions (for the MVP review)
- Will the deal team accept a defended figure if the defences are named, with who provides them and to what standard?
- Are the premium assumptions credible, or should they come from a broker?
- Would a spreadsheet of yearly cost lines drop into their model as is?
