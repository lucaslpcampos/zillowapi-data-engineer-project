import boto3
import json
import pandas as pd

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # receive the source bucket and object name from put s3 event json
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Check if the object is directly inside the "bronze" or "silver" folder
    if not (object_key.startswith('bronze/') or object_key.startswith('silver/')):
        return {
            'statusCode': 400,
            'body': json.dumps('Object is not in the "bronze" or "silver" folder.')
        }

    
    target_bucket = source_bucket
    target_prefix = 'gold/'
    target_file_name = object_key.split('/')[-1][:-5]
   
    waiter = s3_client.get_waiter('object_exists')
    waiter.wait(Bucket=source_bucket, Key=object_key)
    
    response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
    data = response['Body'].read().decode('utf-8')
    data = json.loads(data)
    
    f = []
    for i in data["results"]:
        f.append(i)
    df = pd.DataFrame(f)
    
    # Select specific columns
    selected_columns = ['bathrooms', 'bedrooms', 'city', 'homeStatus', 
                    'homeType','livingArea','price', 'rentZestimate','zipcode']
    df = df[selected_columns]
    
    # Convert DataFrame to CSV format
    csv_data = df.to_csv(index=False)
    
    # Upload CSV to S3 with "gold/" prefix
    object_key = f"{target_prefix}{target_file_name}.csv"
    s3_client.put_object(Bucket=target_bucket, Key=object_key, Body=csv_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps('CSV conversion and S3 upload completed successfully')
    }
