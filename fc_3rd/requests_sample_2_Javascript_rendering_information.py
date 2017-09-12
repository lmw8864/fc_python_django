import requests
# from bs4 import BeautifulSoup
import json

# url = "http://datalab.naver.com/keyword/sectionSearch.naver"
#
# r = requests.get(url)
#
# if r.status_code == requests.codes.ok:
#     data = BeautifulSoup(r.text, "html.parser")
#     print(r.text)
#     keywords = data.select(".sub_title .title")
#     for keyword in keywords:
#         print(keyword.text)


# 이전의 방법으로는 자바스크립트 렌더링 후 나오는 정보는 가져올 수 없어!

# Settings > Consloe > log XMLHttpRequests 체크
# Console 창에 뜨는 log를 눌러보면 Network 탭에서 반짝! (자바스크립트 렌더링 항목을 쉽게 찾을 수 있음)
# 눌러보면 Headers, Preview 등의 탭에서 찾고자 하는 정보를 찾아보자.

# 자바스크립트 렌더링 Request URL
url = "http://datalab.naver.com/rc/rankList.naver"

# r = requests.get(url)
r = requests.post(url)  # Request Method: POST
# print(r.text)

if r.status_code == requests.codes.ok:
    encoded_json = json.loads(r.text)
    data = encoded_json["data"]
    for section in data:
        print("\n" + section["name"])
        # print(section["items"])
        for item in section["items"]:
            # print(item)
            print(item['rank'], item['keyword'])
        # 각 섹션마다 총 10개의 랭킹이랑 키워드가 출력되도록
