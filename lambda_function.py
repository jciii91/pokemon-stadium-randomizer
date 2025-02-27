import json

def lambda_handler(event, context):
    # Print the event for logging purposes
    print('Event: ', event)
    
    # Extract information from the event
    http_method = event['httpMethod']
    path = event['path']
    query_string_parameters = event.get('queryStringParameters', {})
    body = event.get('body')
    
    # Process the request based on the HTTP method and path
    if http_method == 'GET' and path == '/hello':
        message = f"Hello! Query parameters: {query_string_parameters}"
    elif http_method == 'POST' and path == '/data':
        # If the body is JSON, parse it
        if body:
            try:
                body_json = json.loads(body)
                message = f"Received data: {body_json}"
            except json.JSONDecodeError:
                message = "Invalid JSON in request body"
        else:
            message = "No data received in body"
    else:
        message = "Unsupported method or path"
    
    # Construct the response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': message}),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    
    return response
