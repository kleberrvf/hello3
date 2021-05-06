import boto3
pipeline = boto3.client('codepipeline')

def lambda_handler(event, context):

    # stuff

    response = pipeline.put_job_success_result(
        jobId=event['codepipeline.job']['id']
    )
    return response

import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

print ("Hello2")