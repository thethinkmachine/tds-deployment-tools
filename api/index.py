import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Load data from the JSON file
with open("q-vercel-python.json", "r") as file:
    data = json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get 'name' parameters from the query string
    names = request.args.getlist('name')
    
    # Find marks for the specified names
    marks = [entry['marks'] for entry in data if entry['name'] in names]
    
    # Return the result as JSON
    return jsonify({"marks": marks})

# Vercel requires this for deployment
def handler(request, *args, **kwargs):
    return app(request, *args, **kwargs)
