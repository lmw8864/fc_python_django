# naver 실시간 검색어 순위 가져오기

import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
r = requests.get(url)
html = BeautifulSoup(r.text, 'html.parser')

search_keywords = html.select(".PM_CL_realtimeKeyword_rolling .ah_item .ah_a")

for keyword in search_keywords:
    rank = keyword.select_one(".ah_r").text
    search_key = keyword.select_one(".ah_k").text
    print(rank, search_key)
