import json

def lambda_handler(event, context):
    
    slider1 = event.get("slider1")
    slider2 = event.get("slider2")
    slider3 = event.get("slider3")
    seedCount = event.get("seedCount")

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
