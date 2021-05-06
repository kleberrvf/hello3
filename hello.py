import json
import boto3

pipeline = boto3.client('codepipeline')

def lambda_handler(event, context):

    # stuff

    response = pipeline.put_job_success_result(
        jobId=event['CodePipeline.job']['id']
       
    )
    return response
   
print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')

