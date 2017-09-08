import http.server

PORT = 8000


class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/cgi']  # /cgi 디렉토리 하위에서만 통신을 허락하겠다.(보안)

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
