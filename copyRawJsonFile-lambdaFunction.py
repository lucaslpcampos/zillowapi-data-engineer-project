import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # receive the source bucket and object name from put s3 event json
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
   
    # Check if the object is directly inside the "bronze" folder
    if not object_key.startswith('bronze/'):
        return {
            'statusCode': 400,
            'body': json.dumps('Object is not in the "bronze" folder.')
        }

    # Prepare the target key by replacing "bronze" with "silver"
    target_key = object_key.replace('bronze/', 'silver/', 1)
   
    copy_source = {'Bucket': source_bucket, 'Key': object_key}
   
    # verify if the object exists at source bucket
    waiter = s3_client.get_waiter('object_exists')
    waiter.wait(Bucket=source_bucket, Key=object_key)
    
    # copy the file from source bucket to target bucket
    s3_client.copy_object(Bucket=source_bucket, Key=target_key, CopySource=copy_source)
    return {
        'statusCode': 200,
        'body': json.dumps('Copy completed successfully')
    }
