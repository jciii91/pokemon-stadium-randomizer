import os
import json
import boto3
import stadium_randomizer

s3_client = boto3.client('s3', region_name=os.environ["PROD_AWS_REGION"])

def file_exists(bucket_name, target_file):
    """Checks if a file exists in an S3 bucket using pagination, exiting early if found."""
    paginator = s3_client.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name):
        if 'Contents' in page:
            if any(item['Key'] == target_file for item in page['Contents']):
                return True
    return False

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    slider1 = int(body.get("slider1", "1"))
    slider2 = int(body.get("slider2", "1"))
    slider3 = int(body.get("slider3", "1"))
    file_name = body.get("fileName", "") + ".z64"
    bucket_name = os.environ["BUCKET_NAME"]
    new_file_name = "new-seed.z64"

    if file_exists(bucket_name, file_name):
        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        file_data = bytearray(response['Body'].read())

        settings_dict = {
            "base_stats" : slider1,
            "rentals_round1" : slider2,
            "gymcastle_round1" : slider3
        }
        
        new_rom = stadium_randomizer.randomizer_func(file_data, settings_dict)

        temp_file_path = f"/tmp/{new_file_name}"  # Temp storage in Lambda
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(new_rom)

        with open(temp_file_path, "rb") as temp_file:
            temp_file.seek(0)
            s3_client.put_object(
                Bucket=bucket_name,
                Key=new_file_name,
                Body=temp_file
            )

        presigned_download_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': new_file_name},
            ExpiresIn=600  # Link valid for 10 minutes
        )
    
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(
                {
                    "link": presigned_download_url
                }
            )
        }