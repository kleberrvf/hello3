import boto3
pipeline = boto3.client('CodePipeline')

def lambda_handler(event, context):

    # stuff

    response = pipeline.put_job_success_result(
        jobId=event['CodePipeline.job']['id']
    )
    return response

print "Hello Wohooo"
