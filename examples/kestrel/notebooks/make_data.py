"""FICTIONAL: synthetic data for the Kestrel example. Kestrel, Gusta, their customers and every ticket are invented.

Writes data/ticket_types.json: 15 ticket types with monthly volume (in-app chat), results on 50 test tickets,
risk if wrong, a one-line reason, and 3 example tickets. Each example has the customer's
message, Kestrel's reply, the rule from Gusta's support playbook that applies, and the grading AI's verdict with a reason.
Also writes data/support_playbook.json (read by build/playbook.html) and .md, the fictional playbook every answer is graded against.
Run from examples/kestrel:  python3 notebooks/make_data.py
"""
import json
# name, tickets a month, correct of 50, cost, cost example, moves money,
# examples: (customer request, Kestrel's reply, playbook rule id, correct, one-line reason)
# Gusta's customer support playbook. FICTIONAL: Kestrel's answers are graded against these rules.
# (section, [(rule id, rule)])
PLAYBOOK = [
 ("Every ticket", [
   ("GEN-1", "Check the person's role on the account (account owner, admin or employee) before helping with any change. If they can't make it, say who can."),
   ("GEN-2", "Check the account itself (payroll runs, invoices, plan history, settings) before answering. Never answer from general knowledge alone."),
   ("GEN-3", "When the customer does something themselves, give the exact place in Gusta, e.g. Settings > Company."),
   ("GEN-4", "Never promise a date, refund or outcome this playbook doesn't allow."),
   ("GEN-5", "Hand over to a support agent when the customer asks for a person, staff pay is late, or no rule covers the question."),
   ("GEN-6", "Plain words, no jargon, one question at a time."),
 ]),
 ("Logging in", [
   ("ACC-1", "Forgotten password: send one reset link. If it hasn't arrived, ask the customer to check spam for an email from Gusta."),
   ("ACC-2", "Reset links expire after 30 minutes. Say so every time you send one."),
   ("ACC-3", "Never change the email someone logs in with. Only the account owner can, under Settings > Users."),
   ("ACC-4", "Accounts lock for 15 minutes after 5 failed attempts. Explain the wait and send a reset link."),
   ("ACC-5", "2-step code not arriving by text: send it by email instead, and show where to update the phone number (Profile > Security)."),
   ("ACC-6", "Can't log in on the mobile app only: check the app version first. If it's out of date, ask them to update before anything else."),
 ]),
 ("Payslips", [
   ("PAY-1", "Payslips are on each employee's profile under Documents. Admins can resend them from there."),
   ("PAY-2", "Employees download their own payslips in the Gusta employee app. Share the employee app guide."),
   ("PAY-3", "Payslips missing for a recent run: check the run status first. Payslips only exist once a run is approved."),
 ]),
 ("Company details", [
   ("CO-1", "Only the account owner can change the registered address, which tax letters go to. Admins can change the trading address."),
   ("CO-2", "The registered and trading addresses are separate. Change or explain only the one the customer asked about."),
   ("CO-3", "Payslips show the trading address, not the registered address."),
   ("CO-4", "A new registered address reaches the tax office in 1 to 2 weeks. Say so."),
 ]),
 ("Employees", [
   ("EMP-1", "Before a new employee's first payroll run, Gusta needs their tax code, ID number, start date and bank details."),
   ("EMP-2", "Part-time staff: set their contracted days. Salary is pro-rata to a 5-day week."),
   ("EMP-3", "Each employee is on one pay schedule. Weekly-paid staff need a weekly schedule; if the account has none, create it first under Settings > Pay schedules."),
 ]),
 ("Bank details", [
   ("BANK-1", "Changing the company bank account needs the account owner's approval and a verification call from Gusta before it takes effect."),
   ("BANK-2", "Admins change an employee's bank details on their profile. The new details must match the bank form the employee signed."),
   ("BANK-3", "No bank changes within 3 working days of a payroll run. Hand over to a support agent for a manual check."),
 ]),
 ("Billing", [
   ("BILL-1", "Duplicate charge: confirm it on the invoice, then refund the duplicate in full."),
   ("BILL-2", "Cancellations take effect at the end of the current billing month. That month is still charged."),
   ("BILL-3", "Annual plans: refunds for unused months are pro-rata and reviewed by a support agent before they're paid."),
   ("BILL-4", "Explain invoice charges line by line, using the invoice breakdown."),
   ("BILL-5", "Invoices are under Settings > Billing > Invoices."),
   ("BILL-6", "Before explaining a price change, check the account's plan history."),
 ]),
 ("Payroll runs", [
   ("RUN-1", "Bank error on a run: check the bank authorisation first. If it has expired, show how to renew it, then rerun."),
   ("RUN-2", "Missing tax codes: name the employees and where to add the codes, then rerun."),
   ("RUN-3", "Before suggesting any rerun, check whether the payment was already sent. If it was, never rerun; hand over to a support agent."),
   ("RUN-4", "A new pay date applies from the next run. Runs must be approved 2 working days before the pay date (the bank cut-off)."),
   ("RUN-5", "Payday on a bank holiday: pay on the working day before."),
   ("RUN-6", "A pay date can't move inside the 2-working-day bank cut-off."),
 ]),
 ("Tax forms", [
   ("TAX-1", "Year-end forms are under Reports > Year end. Admins send them to employees from there."),
   ("TAX-2", "A form differs from the payslips: check for corrections in that tax year before answering."),
   ("TAX-3", "Contractors are not employees: they aren't paid through payroll and use a separate contractor form. Never give the employee process for a contractor."),
 ]),
 ("Cancelling", [
   ("CAN-1", "Before cancelling: run the final payroll, export the records (Reports > Export all), and the account owner confirms."),
   ("CAN-2", "Records are kept, read-only, for 6 years after cancelling, then deleted."),
 ]),
 ("Holiday and leave", [
   ("HOL-1", "Part-time holiday is pro-rata to contracted days."),
   ("HOL-2", "Holiday pay includes regular overtime and regular commission, not just basic pay."),
   ("HOL-3", "Leave is recorded on the employee's profile under Leave."),
 ]),
 ("Reports", [
   ("REP-1", "Payroll summary: default to the last full tax year unless the customer gives dates."),
   ("REP-2", "\"Last quarter\" means the most recent full calendar quarter."),
   ("REP-3", "Only the account owner and admins can export salaries."),
 ]),
 ("Pensions", [
   ("PEN-1", "New starters are enrolled in the workplace pension automatically after a 3-month waiting period."),
   ("PEN-2", "Opt-outs within a month of enrolment get their deductions refunded in the next run."),
   ("PEN-3", "Before confirming a pension deduction is right, check for salary changes that month."),
 ]),
]
RULE = {i: r for _, rs in PLAYBOOK for i, r in rs}

T = [
 ("Password reset", 468, 50, "Low", "Low: customer stays locked out a little longer", False, [
   ("I've forgotten my password and the reset email isn't arriving.", "I've sent a new reset link to the email you log in with. If it isn't in your inbox in a few minutes, check your spam folder for an email from Gusta. The link works for 30 minutes.", 'ACC-1', True, 'Sent one new link and pointed to the spam folder.'),
   ("Can you reset my password? I've lost access to my old work email.", "I can't change the email you log in with, but your account owner can, under Settings > Users. Once they've updated it, I'll send a reset link to the new address.", 'ACC-3', True, "Didn't change the login email; pointed to the account owner."),
   ('Reset link says expired.', "Sorry about that. I've sent you a fresh reset link.", 'ACC-2', False, "Didn't mention the 30-minute limit; the customer opened the link an hour later and it had expired again.")]),
 ("Can't log in", 268, 49, "Low", "Low: customer tries again or asks for a person", False, [
   ("My 2-step code isn't arriving by text.", "I've sent your code by email instead. So texts work next time, check your phone number under Profile > Security.", 'ACC-5', True, 'Sent the code by email and showed where to fix the phone number.'),
   ('It says my account is locked.', "Your account locked after 5 failed attempts. It unlocks by itself in 15 minutes; I've sent a reset link so you can choose a new password then.", 'ACC-4', True, 'Explained the 15-minute wait and sent a reset link.'),
   ("I can't log in on my phone but it works on my laptop.", "Try clearing the app's cache: open your phone's settings, find Gusta and tap Clear cache.", 'ACC-6', False, 'Skipped the version check; the app was 3 versions out of date and needed an update.')]),
 ("Missing payslip", 342, 50, "Low", "Low: wrong month resent, employee asks again", False, [
   ("One of my staff can't find her March payslip.", 'Open her profile under Employees, then Documents. Her March payslip is there, and you can resend it to her from the same page.', 'PAY-1', True, 'Pointed to the right page and offered the resend.'),
   ('Where do employees download payslips?', "Employees download their payslips in the Gusta employee app, under Payslips. Here's a guide you can share with your staff: Getting started with the employee app.", 'PAY-2', True, 'Pointed to the employee app and shared the guide.'),
   ("Payslips for last Friday aren't showing.", "I've resent last Friday's payslips to all your employees.", 'PAY-3', False, "Didn't check the run: it was still a draft, so there were no payslips to send.")]),
 ("Update company address", 97, 50, "Medium", "Medium: tax letters go to the old address", False, [
   ("We've moved office, how do I change our address?", 'As the account owner, you can change it under Settings > Company > Addresses. If both have moved, update the registered address (where tax letters go) and the trading address (shown on payslips).', 'CO-1', True, 'Checked the person is the account owner before giving the steps.'),
   ('Change our trading address to 14 Mill Lane.', 'You can update it under Settings > Company > Addresses > Trading address. Your registered address, where tax letters go, stays as it is.', 'CO-2', True, 'Dealt only with the trading address, as asked.'),
   ('Our address on payslips is wrong.', 'You can correct it under Settings > Company > Addresses > Registered address.', 'CO-3', False, 'Pointed to the registered address; payslips show the trading address.')]),
 ("Add a new employee", 251, 48, "Medium", "Medium: employee set up on the wrong pay schedule", False, [
   ('How do I add someone starting Monday?', "Go to Employees > Add employee. Before their first payroll run, you'll need their tax code, ID number, start date and bank details.", 'EMP-1', True, 'Listed all four details needed before the first run.'),
   ('New starter is part time, 3 days a week.', 'When you add them, set their contracted days to 3. Gusta then pays 3/5 of the full-time salary.', 'EMP-2', True, 'Set contracted days so the salary is pro-rata.'),
   ('Adding a weekly-paid worker to our monthly payroll.', 'Add them under Employees > Add employee and choose your monthly pay schedule.', 'EMP-3', False, 'Put a weekly-paid worker on the monthly schedule; the account had no weekly schedule, so one was needed first.')]),
 ("Change bank details", 154, 49, "High", "High: payroll paid from or to the wrong account", True, [
   ("We've switched banks, need to update the account payroll is paid from.", "I've started the change under Settings > Bank account. It takes effect once your account owner approves it and our team confirms it on a short verification call.", 'BANK-1', True, "Asked for the owner's approval and the verification call."),
   ('An employee gave me new bank details.', "You can update them on the employee's profile under Bank details. Please check the new details against the bank form they signed before saving.", 'BANK-2', True, 'Asked for the check against the signed form.'),
   ('Change our company account number, urgent, payroll is tomorrow.', "I've started the change so it's ready for tomorrow's run. Your account owner needs to approve it first.", 'BANK-3', False, 'Payroll was 1 working day away; inside 3 days it should have gone to a support agent for a manual check.')]),
 ("Refund request", 121, 46, "High", "High: wrong refund paid out", True, [
   ('You charged us twice this month.', "I can see two identical charges on your November invoice. I've refunded the second one in full.", 'BILL-1', True, 'Confirmed the duplicate on the invoice, then refunded it in full.'),
   ('We cancelled on 20 February but were still billed for February.', "Sorry about that. I've refunded February's charge in full.", 'BILL-2', False, 'February was still due: the cancellation only took effect at the end of February.'),
   ('Can I get a refund for the unused months on our annual plan?', 'Annual plans can get a pro-rata refund for unused months. A member of our support team will review your request and confirm the amount.', 'BILL-3', True, 'Sent the pro-rata refund for a support agent to review.')]),
 ("Payroll run failed", 189, 45, "High", "High: staff paid late", True, [
   ('Payroll failed with a bank error.', 'Your bank authorisation expired on 1 November. Renew it under Settings > Bank account > Authorisation, then rerun payroll from Payroll > Runs.', 'RUN-1', True, 'Found the expired authorisation before suggesting a rerun.'),
   ('Run failed, says tax code missing for 2 employees.', 'Priya Shah and Tom Ellis have no tax code. Add them on each profile under Tax, then rerun payroll.', 'RUN-2', True, 'Named both employees and where to add the codes.'),
   ("Payroll didn't go through and staff are asking where their pay is.", 'Sorry about that. Rerun payroll from Payroll > Runs and your staff will be paid.', 'RUN-3', False, "Didn't check the payment: it had already been sent, so a rerun would pay staff twice.")]),
 ("Tax form question", 298, 47, "High", "High: customer files a wrong figure and gets a penalty", False, [
   ('Where do I find the year-end tax forms for my staff?', "They're under Reports > Year end. From there you can download them or send each employee their form.", 'TAX-1', True, 'Gave the right place and how to send the forms.'),
   ('Why is the tax on this form different from the payslips?', "The form includes a correction made in November, after this employee's tax code changed. Payslips before November show the old figures.", 'TAX-2', True, 'Found the November correction before answering.'),
   ('Do I need to file anything for a contractor?', "Yes: add them under Employees and they'll be included in your year-end filing.", 'TAX-3', False, 'Gave the employee process for a contractor.')]),
 ("Cancel subscription", 88, 50, "High", "High: account and payroll history closed by mistake", False, [
   ("We're closing the business, how do I cancel?", "Sorry to see you go. First run your final payroll, then export your records under Reports > Export all. Once your account owner confirms, I'll set up the cancellation.", 'CAN-1', True, "Covered final payroll, export and the owner's confirmation."),
   ('Cancel at the end of this month please.', "I've set your cancellation for the end of this billing month; this month is still charged. Before then, export your records under Reports > Export all.", 'BILL-2', True, "Cancelled for the end of the billing month and said it's still charged."),
   ('Thinking of cancelling, what happens to our data?', 'Your records are deleted when your account closes, so export anything you need first.', 'CAN-2', False, 'Records are kept read-only for 6 years, not deleted at closing.')]),
 ("Change pay date", 132, 47, "High", "High: staff paid on the wrong day", True, [
   ('Can we pay staff on the 25th instead of the last day?', 'Yes. Change it under Settings > Pay schedules; it applies from your next run. Approve each run at least 2 working days before the 25th so the bank pays on time.', 'RUN-4', True, 'Applied it from the next run and gave the bank cut-off.'),
   ('Bank holiday on payday, can we pay a day early?', "Yes. I've moved this month's pay date to the working day before the bank holiday.", 'RUN-5', True, 'Moved pay to the working day before.'),
   ("Move this month's pay date to tomorrow.", "Done: this month's pay date is now tomorrow.", 'RUN-6', False, 'Tomorrow was inside the 2-working-day bank cut-off; staff would have been paid late.')]),
 ("Invoice question", 177, 49, "Low", "Low: customer is confused about a charge", False, [
   ('What is this extra charge on our invoice?', 'That line is for 2 employees added on 12 November, charged pro-rata for the rest of the month.', 'BILL-4', True, 'Explained the line from the invoice breakdown.'),
   ("Can I get a copy of last month's invoice?", "Here's your October invoice. You'll always find invoices under Settings > Billing > Invoices.", 'BILL-5', True, 'Sent the invoice and showed where invoices are kept.'),
   ('Why did our price go up?', 'Gusta raised prices for all customers this year.', 'BILL-6', False, "Didn't check the plan history: they had moved to a bigger plan in September.")]),
 ("Holiday pay calculation", 170, 43, "Medium", "Medium: employee underpaid for leave", False, [
   ('How is holiday pay worked out for part-time staff?', "It's pro-rata to their contracted days: someone on 3 days a week gets 3/5 of the full-time holiday.", 'HOL-1', True, 'Explained the pro-rata rule with an example.'),
   ('An employee says her holiday pay is too low.', "I've checked: her holiday pay matches her basic pay for those days, so it's correct.", 'HOL-2', False, 'Left out the regular overtime she works every month, so she was underpaid.'),
   ('How do I record 2 days of leave?', "Open the employee's profile, go to Leave and add the 2 days on their calendar.", 'HOL-3', True, 'Pointed to the Leave page.')]),
 ("Export payroll report", 131, 50, "Low", "Low: wrong date range exported", False, [
   ('Need a payroll summary for our accountant.', "Here's your payroll summary for the last full tax year, as a spreadsheet. Tell me if your accountant needs different dates.", 'REP-1', True, 'Defaulted to the last full tax year.'),
   ('How do I export last quarter?', 'Go to Reports > Payroll summary, set the dates to April to June, and click Export.', 'REP-2', False, 'The ticket came in October; the most recent full quarter was July to September.'),
   ('Can I get a list of all employees with salaries?', "Here's the list of your 24 employees with their salaries.", 'REP-3', True, 'Checked the person is an admin before exporting salaries.')]),
 ("Pension deduction question", 96, 44, "Medium", "Medium: wrong deduction explained to staff", False, [
   ('Why has pension been taken from a new starter?', "New starters join your workplace pension automatically after a 3-month waiting period. Sam's ended in October, so deductions started this month.", 'PEN-1', True, "Explained the waiting period using Sam's dates."),
   ('An employee wants to opt out of the pension.', "Record the opt-out on their profile under Pension. As they're within a month of enrolment, their deductions will be refunded in the next run.", 'PEN-2', True, 'Recorded the opt-out and the refund.'),
   ('Pension amount looks wrong this month.', "This month's pension deduction is the same as last month's, so it looks right.", 'PEN-3', False, "Didn't check for salary changes: a pay rise this month hadn't reached the pension, so the deduction was too low.")]),
]
# live accuracy: where Kestrel is used, every ticket from the last 30 days (= tickets a month); where it isn't (Human), a test on 50 recent tickets
LIVE = {
 'Password reset': (468, 467),
 "Can't log in": (268, 263),
 'Missing payslip': (342, 340),
 'Update company address': (97, 96),
 'Add a new employee': (251, 242),
 'Change bank details': (154, 152),
 'Refund request': (50, 46),
 'Payroll run failed': (50, 45),
 'Tax form question': (50, 47),
 'Cancel subscription': (88, 87),
 'Change pay date': (50, 47),
 'Invoice question': (177, 174),
 'Holiday pay calculation': (50, 43),
 'Export payroll report': (131, 129),
 'Pension deduction question': (50, 44),
}
REASON = {
 "Password reset": "{p} accurate and a wrong call costs little",
 "Can't log in": "{p} accurate and a wrong call costs little",
 "Missing payslip": "{p} accurate and a wrong call costs little",
 "Update company address": "{p} accurate and a wrong call is easy to fix",
 "Add a new employee": "{p} accurate: good, but not enough to send unchecked",
 "Change bank details": "{p} accurate, but a wrong call is costly, so a support agent checks",
 "Refund request": "Moves money and only {p} accurate",
 "Payroll run failed": "Moves money and only {p} accurate",
 "Tax form question": "Costly if wrong and only {p} accurate",
 "Cancel subscription": "{p} accurate, but a wrong call is costly, so a support agent checks",
 "Change pay date": "Moves money and only {p} accurate",
 "Invoice question": "{p} accurate and a wrong call costs little",
 "Holiday pay calculation": "Only {p} accurate",
 "Export payroll report": "{p} accurate and a wrong call costs little",
 "Pension deduction question": "Only {p} accurate",
}
pct = lambda n: (f"{LIVE[n][1] / LIVE[n][0] * 100:.0f}%" if LIVE[n][0] == 50 else f"{LIVE[n][1] / LIVE[n][0] * 100:.1f}%")
out = {"label": "FICTIONAL and SYNTHETIC: Kestrel example, not real data",
       "product": "Kestrel", "customer": "Gusta", "channel": "In-app chat", "minutes_ai": 10, "minutes_assisted": 5,
       "types": [{"name": n, "tickets": v, "tested": LIVE[n][0], "correct": LIVE[n][1], "risk": c, "risk_example": ce, "reason": REASON[n].format(p=pct(n)),
                  "examples": [{"message": a, "proposed": b, "rule_id": rl, "rule": RULE[rl], "correct": ok, "verdict_reason": rs} for a, b, rl, ok, rs in ex]}
                 for n, v, k, c, ce, mm, ex in T]}
json.dump(out, open("data/ticket_types.json", "w"), indent=1)
json.dump({"label": "FICTIONAL and SYNTHETIC: Gusta support playbook, not real", "customer": "Gusta",
           "sections": [{"name": sec, "rules": [{"id": i, "rule": r} for i, r in rs]} for sec, rs in PLAYBOOK]},
          open("data/support_playbook.json", "w"), indent=1)
with open("data/support_playbook.md", "w") as f:
    f.write("# Gusta customer support playbook (FICTIONAL)\n\nThe rules Kestrel follows and the grading AI checks every answer against. Synthetic, made by `../notebooks/make_data.py`.\n")
    for sec, rs in PLAYBOOK:
        f.write(f"\n## {sec}\n" + "".join(f"- **{i}** {r}\n" for i, r in rs))
print(len(T), "types,", sum(t[1] for t in T), "tickets a month")
