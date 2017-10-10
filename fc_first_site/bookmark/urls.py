from django.conf.urls import url
from .views import BookmarkList, BookmarkDetail

urlpatterns = [
    url(r'^$', BookmarkList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetail.as_view(), name='detail'),
]
