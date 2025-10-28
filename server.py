#!/usr/bin/env python3
"""
Custom HTTP server that automatically lists JSON files in the materials folder.
This eliminates the need to manually update materials/index.json
"""

import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

class QuizServerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle the materials/index.json endpoint dynamically
        if self.path == '/materials/index.json':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            # Scan materials folder for JSON files
            materials_dir = Path.cwd() / "materials"
            json_files = sorted([
                f.name for f in materials_dir.glob("*.json")
                if f.name != "index.json"
            ])

            # Return as JSON
            self.wfile.write(json.dumps(json_files, ensure_ascii=False).encode('utf-8'))
        else:
            # Serve all other files normally
            super().do_GET()

def run_server(port=8000):
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, QuizServerHandler)
    print(f'✓ Quiz server running at http://127.0.0.1:{port}')
    print(f'  Materials are auto-discovered from the materials/ folder')
    print(f'  Press Ctrl+C to stop\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n✓ Server stopped')

if __name__ == '__main__':
    run_server()
