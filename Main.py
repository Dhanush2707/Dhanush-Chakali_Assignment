import boto3
import logging
import json
sqs=boto3.resource('sqs')
queue=sqs.create_queue(
 QueueName='my_queue'
 
 )
print("Created queue '%s' with URL=%s",'my_queue',queue.url)

def send_message(queue_url):
    sqs_client = boto3.client("sqs")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )
    print(response)

    send_message("Hello, world!")




