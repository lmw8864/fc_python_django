from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^', include('django.contrib.auth.urls')),  # 장고 내장 로그인 기능 사용 -> forms, views를 직접 구현할 필요가 없음.
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
