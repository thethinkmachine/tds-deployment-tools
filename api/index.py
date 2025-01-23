import json
import os

def handler(event, context):
    # Get the absolute path of the JSON file
    file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

    try:
        # Load JSON data from the file
        with open(file_path, "r") as file:
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
    except Exception as e:
        # Handle errors gracefully and return a 500 response
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
