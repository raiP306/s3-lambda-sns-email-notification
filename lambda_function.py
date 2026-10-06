import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    sns.publish(
        TopicArn='YOUR_SNS_TOPIC_ARN',
        Subject='S3 Bucket Event',
        Message=str(event)
    )

    return "Email sent"
