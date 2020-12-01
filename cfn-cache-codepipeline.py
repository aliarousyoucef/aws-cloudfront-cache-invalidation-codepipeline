import boto3
import time
import os
import json

pipeline = boto3.client('codepipeline')

print("getting environment variable")
print("environment variable: " + os.environ['DISTRIBUTION_ID'])
dist = os.environ['DISTRIBUTION_ID'] #// get the Distribution ID from the lambda environment variable
# dist_str = str(dist) //statement to convert the distribution variable into a string


def lambda_handler(event, context):
    client = boto3.client('cloudfront')
    invalidation = client.create_invalidation(
        DistributionId=dist,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/*',
                ]
        },
        'CallerReference': str(time.time())
    })
    
    response = pipeline.put_job_success_result(
        jobId=event['CodePipeline.job']['id']
    )
    return {
    'statusCode': 200,
    'body': json.dumps('Successully created cache invalidation for ') + dist,
        
    }
