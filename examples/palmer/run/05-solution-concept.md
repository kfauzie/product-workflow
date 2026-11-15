# 5. Spec: solution concept (pm-3)

> **FICTIONAL EXAMPLE.** Palmer, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

> **Recommendation: a one-page decision table.** Each ticket type gets one of three outcomes from a rule anyone can read: resolve alone, draft for approval, or human only. For Palmer: **49.7% of tickets resolved alone, 198 hours saved a month, 9 wrong answers a month reaching customers**, none on tickets that move money.

## The rule
- **Resolve alone:** accuracy 98% or more, and the cost of a wrong call is Low or Medium.
- **Draft for approval:** accuracy 90% or more, or a High-cost type with accuracy 98% or more.
- **Human only:** everything else, including any type that moves money with accuracy under 98%.

## What AI, code and people do
- **AI:** answers tickets, or drafts for approval.
- **Code:** the rule, every number.
- **People:** the support team grades test tickets and approves drafts; the Head of Support signs off the table.

## Success criteria
- Wrong answers reaching customers stay under 10 a month, none on money types.
- Test cases: 2,982 tickets; 1,483 resolved alone (49.7%); 198 hours; 8.9 wrong answers a month. See `build/test_mvp.js`.

## Assumptions (for the MVP review)
- Is 50 test tickets per type enough for the team to trust a type?
- Is 8 minutes a fair average for a ticket a person would otherwise handle?
