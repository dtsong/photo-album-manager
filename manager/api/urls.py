from django.conf.urls import url
from . import views


# API Endpoints
urlpatterns = [
    url(r'^', views.api_root),
    url(r'^albums/$', views.AlbumList, name='album-list'),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    url(r'^photos/$', views.PhotoList, name='photo-list'),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view()),
    url(r'^users/$', views.UserList, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
