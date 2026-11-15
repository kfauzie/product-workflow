# 1. Data review (pm-1, Initial review)

> **FICTIONAL EXAMPLE.** Relaywise, Relay Agent, Relay Studio and Pellmore are invented. The use case and all data are synthetic. In a real run these pages live in Notion; here they are Markdown so the workflow can be read end to end.

**The data:** 13,537 tickets in Dec 2026 across 10 categories, with 12 months of volume and handle time; plus 2,390 past tickets the AI answered in shadow mode, graded by agents (correct, minor error, serious error, escalated). Usable; no gaps.

| # | Finding | Why it might matter (guess) |
|---|---|---|
| 1 | **Volume and effort sit in different places.** The top 3 categories by tickets (Password and login, Order status, Billing disputes) are 51% of tickets; the top 3 by agent time (Billing disputes, API errors, Shipment exceptions) are 53% of agent minutes | The easy wins and the big wins aren't the same categories |
| 2 | **API errors nearly doubled.** 713 tickets in January, 1,391 in December (+95%), against +13% for everything else | Something changed in the product; automation may be treating a symptom |
| 3 | **Billing disputes: high volume, costly mistakes.** 87.5% accurate in shadow mode, with 4.9% serious errors (wrong refunds, escalations) | Auto-resolving it could cost more than it saves |
| 4 | **Two categories were barely checked.** Integrations setup (80 tickets) and Contract and pricing (40) | Their accuracy can't be trusted yet, either way |

**Questions**
1. The data shows Billing disputes is 87.5% accurate with 4.9% serious errors. What happens today when an agent gets one wrong?
2. The data shows API errors nearly doubled this year. What's behind that?
3. The data shows the categories with most tickets aren't the ones taking most agent time. Which matters more to your team?

**Clarifications:** what a serious wrong answer costs; who signs off a rollout; how many graded tickets they'd trust.
