import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow any origin
        self.end_headers()

        # Parse query parameters
        query = parse_qs(urlparse(self.path).query)
        names = query.get('name', [])

        # Load data from the JSON file
        with open('q-vercel-python.json', 'r') as f:
            data = json.load(f)

        # Build the result array of marks
        marks_list = []
        for name in names:
            item = next((i for i in data if i["name"] == name), None)
            if item:
                marks_list.append(item["marks"])
            else:
                marks_list.append(None)

        # Return the JSON response
        response = {"marks": marks_list}
        self.wfile.write(json.dumps(response).encode())
