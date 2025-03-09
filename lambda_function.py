import json

def lambda_handler(event, context):
    
    body = json.loads(event.get("body", "{}"))
    slider1 = body.get("slider1")
    slider2 = body.get("slider2")
    slider3 = body.get("slider3")
    seedCount = body.get("seedCount")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "message": f"Extracted values: Slider 1 is {slider1}, Slider 2 is {slider2}, Slider 3 is {slider3}, Number of seeds requested {seedCount}", 
                "status": "success"
            }
        )
    }
