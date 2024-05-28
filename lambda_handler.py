import boto3
import os

AWS_REGION = 'eu-west-2'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = 'http://localhost:4566'
#boto3.setup_default_session(profile_name=AWS_PROFILE)


def lambda_handler(event, context):

    s3 = boto3.client('s3')
    bucket_response = s3.list_buckets()

    files_response = s3.list_objects_v2(Bucket="my-bucket")
  
    return {"message": "Greetings earthling!",
           "event": event,
           "context": str(context),
           "buckets": str(bucket_response),
           "files": str(files_response)}
