from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# API Endpoints
urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^photos/$', views.PhotoList.as_view(), name='photo-list'),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name='photo-detail'),
    url(r'^albums/$', views.AlbumList.as_view(), name='album-list'),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='album-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)