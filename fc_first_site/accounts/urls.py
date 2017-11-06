from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),  # 장고 내장 로그인 기능 사용 -> forms, views를 직접 구현할 필요가 없음.
]
