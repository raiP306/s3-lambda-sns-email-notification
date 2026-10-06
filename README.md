# S3 Event Notification using AWS Lambda & SNS

A simple serverless AWS project that sends an email notification whenever an event occurs in an Amazon S3 bucket.

## Architecture

**Amazon S3 → AWS Lambda → Amazon SNS → Email**

### AWS Services Used

* **Amazon S3** – Stores objects and generates bucket events.
* **AWS Lambda** – Python function triggered by S3 events.
* **Amazon SNS** – Publishes the event notification.
* **Email Subscription** – Receives the notification through SNS.

## Working Flow

1. An event occurs in the S3 bucket.
2. The S3 event triggers the Lambda function.
3. Lambda receives the event details.
4. Lambda publishes the event to an SNS topic.
5. SNS sends the notification to the subscribed email address.

## Lambda Code

```python
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    sns.publish(
        TopicArn='YOUR_SNS_TOPIC_ARN',
        Subject='S3 Bucket Event',
        Message=str(event)
    )

    return "Email sent"
```

## Project Structure

```text
s3-sns-email-notification/
│
├── lambda_function.py
├── architecture-diagram.png
├── working-flow-diagram.png
└── README.md
```

## Configuration

1. Create an SNS topic.
2. Add an email subscription to the SNS topic.
3. Confirm the email subscription.
4. Create a Python Lambda function.
5. Add the SNS `Publish` permission to the Lambda execution role.
6. Configure an S3 event notification to trigger the Lambda function.
7. Replace `YOUR_SNS_TOPIC_ARN` in the Lambda code with your SNS Topic ARN.

## Result

Whenever a configured event occurs in the S3 bucket, Lambda publishes the event details to SNS, and the subscribed email receives the notification.

## Flow Summary

**S3 Event → Lambda → SNS → Email**

## Key Learning

This project demonstrates how AWS managed services can be combined to build a simple **event-driven serverless notification system** without managing any servers.

