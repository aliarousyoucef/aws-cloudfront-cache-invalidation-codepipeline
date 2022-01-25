import boto3
import time
import os
import json

pipeline = boto3.client('codepipeline')


def lambda_handler(event, context):
    dist=event["CodePipeline.job"]["data"]["actionConfiguration"]["configuration"]["UserParameters"]
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
