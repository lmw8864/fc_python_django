import requests

# get 방식으로 통신
# r = requests.get("http://www.naver.com")
# print(r.text)

# post 방식으로 통신
# r = requests.post("http://www.naver.com")
# print(r.text)


# https://search.naver.com/search.naver?where=nexearch&query=마광수&sm=top_lve&ie=utf8

# get 방식으로 naver 검색
url = "https://search.naver.com/search.naver"
payload = {"where": "nexearch", "query": "마광수", "sm": "top_lve", "ie": "utf8"}
r = requests.get("http://www.naver.com", params=payload)

# print(r.headers)
# print(r.status_code)  # 200

# status_code 확인 과정
if r.status_code == requests.codes.ok:
    print("서버 응답 성공")
    print(r.text)
else:
    print("서버 응답 오류, 프로그램 종료")


# login 과정
jar = requests.cookies.RequestsCookieJar()
login_data = {"id": "myid", "pwd": "mypwd"}
r = requests.get(url, data=login_data, cookies=jar)

# login 이후
r = requests.get(url, cookies=jar)
