from django.conf.urls import url
from . import views


# API Endpoints
urlpatterns = [
    url(r'^albums/$', views.AlbumList.as_view()),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    url(r'^photos/$', views.PhotoList.as_view()),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view()),
]
