from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # generate 6-digit OTP
        otp = random.randint(100000, 999999)

        body = json.dumps({"otp": otp})

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))
        return

if __name__ == '__main__':
    print("Starting OTP server...")
    server = HTTPServer(('localhost', 8000), handler)
    print("OTP server running at http://localhost:8000/api/otp")
    server.serve_forever()
