# 🛠️ Troubleshooting Guide

## Issue 1: Glue Job Fails

Possible Causes:
- Column mismatch
- NULL values not handled
- Incorrect IAM permissions

Solution:
- Check CloudWatch logs
- Validate schema mapping
- Verify Glue role permissions

---

## Issue 2: SNS Email Not Received

Possible Causes:
- Subscription not confirmed

Solution:
- Confirm email subscription
- Check spam folder

---

## Issue 3: Step Function Stuck

Possible Causes:
- Crawler not finishing
- Incorrect state transitions

Solution:
- Check execution graph
- Verify state definitions

---

## Issue 4: Redshift Load Error

Possible Causes:
- Table not created
- Data type mismatch

Solution:
- Re-run SQL scripts
- Validate schema consistency
