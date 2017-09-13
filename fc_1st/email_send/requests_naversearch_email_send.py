# naver 실시간 검색어 순위 가져오기 + 이메일로 보내기

import requests
from bs4 import BeautifulSoup

# email 전송 모듈 불러오기
from smtp_email_send import send_mail

url = "http://www.naver.com"
r = requests.get(url)
html = BeautifulSoup(r.text, 'html.parser')

search_keywords = html.select(".PM_CL_realtimeKeyword_rolling .ah_item .ah_a")

search_url = "https://search.naver.com/search.naver?where=nexearch&query=%s&sm=top_lve&ie=utf8"

html_contents = ""

text_contents = ""

for keyword in search_keywords:
    rank = keyword.select_one(".ah_r").text
    search_key = keyword.select_one(".ah_k").text
    print(rank, search_key)

    # html_contents 만들기
    html_contents += rank + "위 " + search_key + "<br>"
    html_contents += "<a href='" + (search_url % search_key) + "'>검색 페이지</a><br>"

    # text_contents 만들기
    text_contents += rank + "위 " + search_key + "\n"

# print(html_contents)

# text_contents = BeautifulSoup(html_contents, "html.parser").get_text()
# print(text_contents)  # get_text() 사용하니까 모양이 별로라 for문 내에서 처리

# 메일 보내기
send_mail("from@gmail.com", "to@email.com", text_contents, html_contents)
