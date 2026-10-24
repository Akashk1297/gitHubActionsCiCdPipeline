from http.server import SimpleHTTPRequestHandler, HTTPServer

# CRITICAL: Do not use "localhost" or "127.0.0.1" here
server_address = ("0.0.0.0", 8080) 
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Starting server on port 8080...")
httpd.serve_forever()
