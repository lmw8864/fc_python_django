from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', BookmarkList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetail.as_view(), name='detail'),
    url(r'^create/$', BookmarkCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', BookmarkUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', BookmarkDelete.as_view(), name='delete'),
]
