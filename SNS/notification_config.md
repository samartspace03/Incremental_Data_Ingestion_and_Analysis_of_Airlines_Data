# 📢 SNS Notification Configuration

## 1. Purpose

Amazon SNS is used to send email notifications when the Glue job fails or the Step Function encounters an error.

---

## 2. Steps to Configure SNS

### Step 1: Create SNS Topic

1. Go to Amazon SNS Console
2. Click Create Topic
3. Choose Standard
4. Name it: airline-pipeline-alerts
5. Create topic

---

### Step 2: Create Email Subscription

1. Open the created topic
2. Click Create Subscription
3. Protocol: Email
4. Enter your email address
5. Confirm subscription from your email inbox

⚠️ Important: Confirm the email subscription or alerts will not be delivered.

---

### Step 3: Integrate with Step Functions

In Step Function state machine, add:

- Publish action on failure
- Topic ARN of the created SNS topic

---

## 3. Example Failure Flow

If Glue Job fails:

1. Step Function transitions to Failure state
2. SNS Publish action is executed
3. Email alert is sent

---

## 4. Sample Alert Message

Subject: Airline Pipeline Failure Alert

Message:
Glue Job execution failed.
Check Step Functions execution logs for details.

---

## 5. Best Practices

- Use descriptive subject lines
- Enable retry policies in Step Functions
- Monitor via CloudWatch
- Restrict SNS permissions using IAM
