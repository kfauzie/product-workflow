# 5. Spec: solution concept (3-pm)

> **FICTIONAL EXAMPLE.** Kestrel, Gusta, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

> **Recommendation: a one-page analytics view in Kestrel.** Each ticket type gets one of three outcomes from a rule anyone can read: AI, AI-assisted human, or Human. For Gusta: **47.5% of tickets handled by AI, 372 hours saved a month, 14 wrong answers a month reaching customers**, none on High-risk tickets. Only Other (tickets that match no type) goes to a human.

## The rule
- **AI:** accuracy 98% or more, and risk Low or Medium.
- **AI-assisted human:** accuracy 60% or more, any risk: a support agent checks every draft.
- **Human:** accuracy below 60%, where a draft would not save a support agent time and may confuse them instead.

## What AI, code and people do
- **AI:** Kestrel answers or drafts; a separate grading AI checks test answers against the playbook.
- **Code:** the rule, every number.
- **People:** support agents approve drafts; the Head of Customer Support signs off the table.

## Success criteria
- Wrong answers reaching customers stay under 15 a month, none on High-risk types.
- Test cases: 3,122 tickets; 1,483 handled by AI (47.5%); 372 hours; 14 wrong answers a month; overriding Refund request to AI adds 121 AI tickets and 10 wrong answers. See `build/test_mvp.js`.

## Assumptions (for the MVP review)
- Is 50 test tickets per type, graded by a separate AI against the playbook, enough for the team to trust a type?
- Is 10 minutes a fair average for a ticket Kestrel handles on its own, and 5 minutes for one a support agent approves?
