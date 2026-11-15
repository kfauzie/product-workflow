"""FICTIONAL: synthetic data for the Palmer example. Palmer, its customers and every ticket are invented.

Writes data/ticket_types.json: 15 ticket types with monthly volume (in-app chat, email and the help-centre form), results on 50 test tickets,
cost of a wrong call, whether the type moves money, and 3 example tickets. Each example has its channel, the customer's
message, what the AI agent proposed, the playbook rule that applies, and the grading AI's verdict with a reason.
Run from examples/palmer/run:  python3 notebooks/make_data.py
"""
import json
# name, tickets a month, correct of 50, cost, cost example, moves money,
# examples: (customer message, AI agent proposed, playbook rule, correct, one-line reason)
T = [
 ("Password reset", 468, 50, "Low", "Low: customer stays locked out a little longer", False, [
   ("I've forgotten my password and the reset email isn't arriving.", "Send a new reset link and ask them to check spam for an email from Palmer.", "Resend the reset link once; point to the spam folder.", True, "Followed the rule."),
   ("Can you reset my password? I've lost access to my old work email.", "Explain that the account owner must change the login email first, and how to ask them.", "Never change a login email without the account owner.", True, "Did not change the email itself."),
   ("Reset link says expired.", "Send a fresh link and explain links expire after 30 minutes.", "Expired link: send a new one and give the 30-minute limit.", True, "Followed the rule.")]),
 ("Can't log in", 268, 49, "Low", "Low: customer tries again or asks for a person", False, [
   ("My 2-step code isn't arriving by text.", "Send the code by email instead and show how to update the phone number.", "Offer email codes when text fails.", True, "Followed the rule."),
   ("It says my account is locked.", "Unlock after the 15-minute timeout and send a reset link.", "Locked accounts unlock after 15 minutes; send a reset link.", True, "Followed the rule."),
   ("I can't log in on my phone but it works on my laptop.", "Ask them to clear the app cache.", "Check the app version first; ask them to update if it's out of date.", False, "Skipped the version check; the app needed an update.")]),
 ("Missing payslip", 342, 50, "Low", "Low: employee is pointed to the wrong month", False, [
   ("One of my staff can't find her March payslip.", "Show where payslips sit under Employees > Documents and how to resend March.", "Show the documents page and offer to resend.", True, "Followed the rule."),
   ("Where do employees download payslips?", "Link the employee app guide and the resend option.", "Link the employee app guide.", True, "Followed the rule."),
   ("Payslip for last Friday isn't showing.", "Explain payslips appear once the payroll run is approved; this one is still in draft.", "Check the run status before anything else.", True, "Checked the run status first.")]),
 ("Update company address", 97, 50, "Medium", "Medium: tax letters go to the old address", False, [
   ("We've moved office, how do I change our address?", "Update the registered address after confirming the account owner; tax letters follow in 1 to 2 weeks.", "Only the account owner can change the registered address.", True, "Confirmed the account owner first."),
   ("Change our trading address to 14 Mill Lane.", "Update the trading address and leave the registered address as it is.", "Trading and registered addresses are separate; change only the one asked for.", True, "Changed only the trading address."),
   ("Our address on payslips is wrong.", "Explain payslips use the trading address and update it.", "Payslips show the trading address.", True, "Followed the rule.")]),
 ("Add a new employee", 251, 48, "Medium", "Medium: employee set up on the wrong pay schedule", False, [
   ("How do I add someone starting Monday?", "Walk through Add employee and the tax details needed before the first run.", "List the tax details needed before the first payroll run.", True, "Followed the rule."),
   ("New starter is part time, 3 days a week.", "Set up a part-time contract with pro-rata salary.", "Part-time staff get a pro-rata salary on their contract.", True, "Followed the rule."),
   ("Adding a weekly-paid worker to our monthly payroll.", "Add them to the monthly schedule.", "Weekly-paid staff need a weekly pay schedule first.", False, "Put a weekly worker on the monthly schedule.")]),
 ("Change bank details", 154, 49, "High", "High: payroll paid from or to the wrong account", True, [
   ("We've switched banks, need to update the account payroll is paid from.", "Draft the change; ask for owner approval and a verification call before it takes effect.", "Company bank changes need owner approval and a verification call.", True, "Asked for both checks."),
   ("An employee gave me new bank details.", "Draft the update on the employee record and flag it to check against the signed form.", "Employee bank changes must match a signed form.", True, "Flagged the form check."),
   ("Change our company account number, urgent, payroll is tomorrow.", "Draft the change for tomorrow's run.", "No bank changes within 3 working days of a payroll run without a manual check.", False, "Missed the 3-day rule.")]),
 ("Refund request", 121, 46, "High", "High: wrong refund paid out", True, [
   ("You charged us twice this month.", "Confirm the duplicate charge and propose a refund of the second payment.", "Refund duplicate charges in full once confirmed on the invoice.", True, "Confirmed the duplicate, then refunded it."),
   ("We cancelled in January but were billed in February.", "Propose a full refund for February.", "Cancellations take effect at the end of the current billing month.", False, "February was still due; no refund owed."),
   ("Can I get a refund for the unused months on our annual plan?", "Explain the annual plan terms and propose a pro-rata refund for a person to review.", "Annual plans: pro-rata refunds only, reviewed by a person.", True, "Sent it for review as the rule says.")]),
 ("Payroll run failed", 189, 45, "High", "High: staff paid late", True, [
   ("Payroll failed with a bank error.", "Point to the expired bank authorisation, show how to renew it, then rerun.", "Bank errors: check the authorisation before rerunning.", True, "Found the expired authorisation."),
   ("Run failed, says tax code missing for 2 employees.", "List the 2 employees and where to add their tax codes.", "Fix missing tax codes before rerunning.", True, "Followed the rule."),
   ("Payroll didn't go through and staff are asking where their pay is.", "Tell them to rerun payroll.", "Check whether payment was sent before any rerun.", False, "Payment had gone; a rerun would pay staff twice.")]),
 ("Tax form question", 298, 47, "Medium", "Medium: customer files with the wrong figure", False, [
   ("Where do I find the year-end tax forms for my staff?", "Show Reports > Year end and how to send forms to employees.", "Year-end forms live under Reports > Year end.", True, "Followed the rule."),
   ("Why is the tax on this form different from the payslips?", "Explain the form includes a correction made in November.", "Check for corrections in the tax year before answering.", True, "Found the November correction."),
   ("Do I need to file anything for a contractor?", "Say contractors are filed the same way as employees.", "Contractors use a separate form; never treat them as employees.", False, "Gave the employee process for a contractor.")]),
 ("Cancel subscription", 88, 50, "High", "High: account and payroll history closed by mistake", False, [
   ("We're closing the business, how do I cancel?", "Explain the final payroll steps and how to export records, then draft the cancellation.", "Before cancelling: final payroll, export records, owner confirms.", True, "Covered all three steps."),
   ("Cancel at the end of this month please.", "Draft the cancellation for the end of the month and list what to export first.", "Cancellations take effect at the end of the billing month.", True, "Followed the rule."),
   ("Thinking of cancelling, what happens to our data?", "Explain records are kept for 6 years and can be exported at any time.", "Records are kept for 6 years after cancelling.", True, "Followed the rule.")]),
 ("Change pay date", 132, 47, "High", "High: staff paid on the wrong day", True, [
   ("Can we pay staff on the 25th instead of the last day?", "Show how to change the pay date from next month and the bank cut-off.", "Pay date changes apply from the next run; give the bank cut-off.", True, "Followed the rule."),
   ("Bank holiday on payday, can we pay a day early?", "Move this month's pay date one working day earlier.", "Bank holidays: pay the working day before.", True, "Followed the rule."),
   ("Move this month's pay date to tomorrow.", "Move the pay date to tomorrow.", "Pay dates can't move inside the 2-day bank cut-off.", False, "Tomorrow was past the cut-off; staff would be paid late.")]),
 ("Invoice question", 177, 49, "Low", "Low: customer is confused about a charge", False, [
   ("What is this extra charge on our invoice?", "Explain the charge is for 2 employees added mid-month.", "Explain each line using the invoice breakdown.", True, "Used the breakdown."),
   ("Can I get a copy of last month's invoice?", "Send the invoice and show where invoices are kept.", "Invoices are under Settings > Billing.", True, "Followed the rule."),
   ("Why did our price go up?", "Say prices rose for all customers.", "Check the customer's plan history before explaining a price change.", False, "They had moved to a bigger plan.")]),
 ("Holiday pay calculation", 170, 43, "Medium", "Medium: employee underpaid for leave", False, [
   ("How is holiday pay worked out for part-time staff?", "Explain pro-rata holiday based on contracted days.", "Part-time holiday is pro-rata to contracted days.", True, "Followed the rule."),
   ("An employee says her holiday pay is too low.", "Say the calculation was correct.", "Holiday pay includes regular overtime.", False, "Left out her regular overtime."),
   ("How do I record 2 days of leave?", "Show how to add leave on the employee's calendar.", "Record leave on the employee calendar.", True, "Followed the rule.")]),
 ("Export payroll report", 131, 50, "Low", "Low: wrong date range exported", False, [
   ("Need a payroll summary for our accountant.", "Export the summary for the last tax year as a spreadsheet.", "Default to the last full tax year unless asked.", True, "Followed the rule."),
   ("How do I export last quarter?", "Show the date filter on Reports and export Q3.", "Use the date filter for custom ranges.", True, "Followed the rule."),
   ("Can I get a list of all employees with salaries?", "Export the employee list with salaries.", "Only admins can export salaries; this user is an admin.", True, "Checked the user is an admin.")]),
 ("Pension deduction question", 96, 44, "Medium", "Medium: wrong deduction explained to staff", False, [
   ("Why has pension been taken from a new starter?", "Explain automatic enrolment after the waiting period.", "New starters are enrolled after the waiting period.", True, "Followed the rule."),
   ("An employee wants to opt out of the pension.", "Show how to record the opt-out and refund the first deduction.", "Opt-outs within a month get the deduction refunded.", True, "Followed the rule."),
   ("Pension amount looks wrong this month.", "Say it was correct.", "Check for salary changes before confirming a deduction.", False, "Missed a salary change.")]),
]
CHANNELS = ["In-app chat", "Email", "Help-centre form"]   # each type's examples rotate through the channels
out = {"label": "FICTIONAL and SYNTHETIC: Palmer example, not real data",
       "company": "Palmer", "channels": CHANNELS, "minutes_per_ticket": 8, "test_tickets_per_type": 50,
       "types": [{"name": n, "tickets": v, "correct": k, "cost": c, "cost_example": ce, "moves_money": mm,
                  "examples": [{"channel": CHANNELS[(i + j) % 3], "message": a, "proposed": b, "rule": rl, "correct": ok, "reason": rs}
                              for j, (a, b, rl, ok, rs) in enumerate(ex)]}
                 for i, (n, v, k, c, ce, mm, ex) in enumerate(T)]}
json.dump(out, open("data/ticket_types.json", "w"), indent=1)
print(len(T), "types,", sum(t[1] for t in T), "tickets a month")
