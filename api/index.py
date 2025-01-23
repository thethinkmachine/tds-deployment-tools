import json

def handler(event, context):
    # Load JSON data from the file
    with open("q-vercel-python.json", "r") as file:
        data = json.load(file)

    # Parse query parameters
    query_params = event.get("queryStringParameters", {})
    names = query_params.get("name")
    
    # Handle single or multiple names
    if isinstance(names, str):
        names = [names]
    elif not names:
        names = []

    # Find marks for the specified names
    marks = [entry["marks"] for entry in data if entry["name"] in names]

    # Return the response as JSON
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # Enable CORS
        },
        "body": json.dumps({"marks": marks})
    }
