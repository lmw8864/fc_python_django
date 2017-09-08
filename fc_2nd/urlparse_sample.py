from http.server import BaseHTTPRequestHandler, HTTPServer

from urllib.parse import parse_qs, urlparse

PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        query_text = urlparse(self.path).query
        queries = parse_qs(query_text)

        message = "Hello "
        message += queries['name'][0]

        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

run()
# localhost:8000/?name=minwoo
