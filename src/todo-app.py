import json
import boto3;
import os

def lambda_handler(event, context):
    dynaclient = boto3.resource('dynamodb')
    # table tasks should exist in dynamodb
    table = dynaclient.Table("tasks")
    table.put_item(Item=event)
    return {
        'statusCode': 200,
        'body': json.dumps('tasks created successfully!')
    }
