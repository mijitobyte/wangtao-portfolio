import http.server
import socketserver
import webbrowser
import os

# Change to the portfolio directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器运行在 http://localhost:{PORT}")
    print("按 Ctrl+C 停止服务器")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()