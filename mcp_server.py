import json
import http.server
import socketserver
import threading
import time
from datetime import datetime

# === MCP Server Implementation ===

# Global tool registry
TOOLS = {
    "get_current_time": {
        "description": "Returns the current system time in ISO 8601 format.",
        "parameters": {}
    }
}

# SSE (Server-Sent Events) handler class
class SSEHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/sse':
            # Set headers for SSE
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()

            # Keep connection open and send periodic updates
            while True:
                try:
                    # Send current time every 5 seconds
                    current_time = datetime.utcnow().isoformat() + 'Z'
                    message = f"data: {json.dumps({\"time\": current_time})}\n\n"
                    self.wfile.write(message.encode('utf-8'))
                    self.wfile.flush()
                    time.sleep(5)
                except (ConnectionResetError, BrokenPipeError):
                    # Client disconnected
                    break

        elif self.path == '/tools':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(TOOLS).encode('utf-8'))

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/tool':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request = json.loads(post_data.decode('utf-8'))
            tool_name = request.get('tool_name')

            if tool_name not in TOOLS:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Tool not found"}).encode('utf-8'))
                return

            # Execute the tool
            if tool_name == "get_current_time":
                current_time = datetime.utcnow().isoformat() + 'Z'
                response = {
                    "tool_name": "get_current_time",
                    "result": current_time
                }
            else:
                response = {"error": "Unknown tool"}

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def log_message(self, format, *args):
        # Suppress default logging
        pass

# === Main Server Setup ===
if __name__ == '__main__':
    PORT = 8080
    print(f"Starting MCP server on http://localhost:{PORT}")
    
    # Start server in a separate thread to allow for graceful shutdown
    server = socketserver.TCPServer(('', PORT), SSEHandler)
    
    # Run server in background
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.shutdown()
        server.server_close()
        print("Server stopped.")