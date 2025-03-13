import io
import os
import json
import boto3
import stadium_randomizer

s3_client = boto3.client('s3', region_name=os.environ["PROD_AWS_REGION"])

def lambda_handler(event, context):
    
    body = json.loads(event.get("body", "{}"))
    slider1 = body.get("slider1")
    slider2 = body.get("slider2")
    slider3 = body.get("slider3")
    seedCount = body.get("seedCount")

    bucket_name = os.environ["BUCKET_NAME"]
    file_name = "PKStadium1-0US.z64"
    new_file_name = "new-seed.z64"
    response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    file_data = bytearray(response['Body'].read())

    settings_dict = {
        "base" : 1,
        "attack" : 1
    }
    
    new_rom = stadium_randomizer.randomizer_func(file_data, settings_dict)
    
    temp_file_path = f"/tmp/{new_file_name}"  # Temp storage in Lambda
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(new_rom)

    with open(temp_file_path, "rb") as temp_file:
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
                "link": presigned_download_url, 
                "status": "success"
            }
        )
    }
