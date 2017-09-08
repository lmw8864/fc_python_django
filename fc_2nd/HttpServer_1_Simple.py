# python -m http.server 8000
# localhohst:8000
# python -m http.server 8000 --bind 127.0.0.1
# python -m http.server --cgi 8000

import http.server
import socketserver

PORT = 8000  # port 번호는 딱히 의미가 없음.(바꿔도 됨)

Handler = http.server.SimpleHTTPRequestHandler  # 핸들러: 요청을 처리하기 위해 내부적으로 수행하는 작업을 관리

with socketserver.TCPServer(("", PORT), Handler) as httpd:  # "" 안에는 IP주소(127.0.0.1)
    print("serving at port", PORT)
    httpd.serve_forever()  # 서버 실행
