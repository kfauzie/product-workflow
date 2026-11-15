# 5. Spec: solution concept (pm-3)

> **FICTIONAL EXAMPLE.** Relaywise, Relay Agent, Relay Studio and Pellmore are invented. The use case and all data are synthetic. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

> **Recommendation: a one-page automation brief in Relay Agent.** It recommends a mode for each ticket category (auto-resolve, AI drafts with agent approval, or agents only) from shadow-mode accuracy, prices wrong answers, and turns the result into a rollout plan with a guardrail. For Pellmore: **£349k net saving a year**, 1,313 agent hours a month, with auto-resolve on 4 categories. Auto-resolving everything would lose £151k.

## 1. The problem
- **Asked for:** "Can we switch auto-resolve on for more ticket types?"
- **Real problem:** the Head of Support Operations has a target to cut agent hours but can't show which categories are safe to automate, or what a mistake would cost, so she can't get a bigger rollout approved.
- **Evidence:** the notes in [03-discovery-notes.md](03-discovery-notes.md); tested claims in [04-synthesis.md](04-synthesis.md).

## 2. Impact
- **Head of Support Operations:** decisions on gut feel she can't defend; a target she can't commit to.
- **VP and Finance:** no saving they can bank, no sized risk.

## 3. Solution ideas
| | A. Automation brief per category | B. One global confidence slider | C. Relaywise analysts run a readiness review |
|---|---|---|---|
| User | Shows which categories are safe and why, in £ and wrong answers. *Judgement* | Simple, but one setting is wrong for most categories. *Judgement* | Trusted, but slow and not repeatable. *Judgement* |
| Commercial | Upsell: more tickets auto-resolved at a per-ticket price | Little | Services revenue; doesn't scale |
| Effort | Small to medium; uses existing shadow-mode data | Small | High per customer |

## 4. Recommendation
**A.** It answers the real blocker (proof and risk) with the customer's own tickets, and it drives the per-ticket revenue. User value tipped it. **Later:** C for the largest accounts.

## 5. Workflow
- The Head of Support Operations opens Relay Agent and clicks **Create the brief**; volumes come from the helpdesk, accuracy from shadow mode.
- The product recommends a mode per category and works out hours saved, wrong answers and net £ for three plans: recommended, review everything, auto everything.
- She opens Billing disputes, attaches 400 newly graded tickets, and sees it move to auto-resolve (+£158k a year).
- The product drafts a rollout plan with a guardrail; she edits it and sends it to her VP and Finance for approval.

## 6. What AI, code and people do
- **AI:** answers tickets (shadow mode, then live); drafts the rollout wording.
- **Code:** every number, the category rule, the guardrail.
- **People:** agents grade answers; she sets costs and approves the plan; VP and Finance sign off.

## 7. Success criteria
- **Target:** a rollout approved within the quarter; agent hours down without CSAT dropping.
- **Mustn't get worse:** no category auto-resolves without its accuracy lower bound and sample size shown.
- **Test cases (known answers):** recommended £349,100; review everything £271,487; auto everything −£150,807; with the labelled set £506,769. See `build/test_mvp.js`.

## 8. Assumptions (for the MVP review)
- Would Finance accept £400 as the cost of a serious wrong answer, or does it need their own figure?
- Is "3 of the last 50 answers reversed" the right point to switch a category off?
- Would agents grade enough tickets to move the small categories out of "agents only"?
