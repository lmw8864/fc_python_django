import http.server
import socketserver
import io

import xlsxwriter

PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        output = io.BytesIO()

        workbook = xlsxwriter.Workbook(output, {'in_memory': True})  # 메모리 형태로 쓰겠다.(용량이 큰 파일은 파일 형태로 써야함)
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, "Hello World")
        workbook.close()

        output.seek(0)  # 탐색 위치를 처음으로 돌리는 코드

        self.send_response(200)
        self.send_header('Content-Disposition', 'attachment;filename=test.xlsx')
        self.send_header('Content-type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        self.end_headers()
        self.wfile.write(output.read())
        return

print("serving at port", PORT)
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
# localhost:8000 -> 엑셀 파일 다운로드
