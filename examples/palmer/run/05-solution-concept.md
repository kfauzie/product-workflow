# 5. Spec: solution concept (pm-3)

> **FICTIONAL EXAMPLE.** Palmer, the use case and all data are synthetic. Any resemblance to a real company is unintended. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

> **Recommendation: a one-page analytics view in our AI support agent.** Each ticket type gets one of three outcomes from a rule anyone can read: AI, AI-assisted human, or Human. For Palmer: **49.7% of tickets handled by AI, 198 hours saved a month, 9 wrong answers a month reaching customers**, all on Low-cost tickets.

## The rule
- **AI:** accuracy 98% or more, and the cost of a wrong call is Low or Medium.
- **AI-assisted human:** accuracy 90% or more, or a High-cost type with accuracy 98% or more.
- **Human:** everything else, including any type that moves money with accuracy under 98%.

## What AI, code and people do
- **AI:** the AI agent answers or drafts; a separate grading AI checks test answers against the playbook.
- **Code:** the rule, every number.
- **People:** support agents approve drafts; the Head of Customer Support signs off the table.

## Success criteria
- Wrong answers reaching customers stay under 10 a month, none on money types.
- Test cases: 2,982 tickets; 1,483 handled by AI (49.7%); 198 hours; 8.9 wrong answers a month. See `build/test_mvp.js`.

## Assumptions (for the MVP review)
- Is 50 test tickets per type, graded by a separate AI against the playbook, enough for the team to trust a type?
- Is 8 minutes a fair average for a ticket a person would otherwise handle?
