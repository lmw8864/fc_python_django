from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello World! Hello World!!"
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

run()
