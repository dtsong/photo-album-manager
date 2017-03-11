from django.conf.urls import url, include
from . import views


# API Endpoints for Albums, Photos, and Users
urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^albums/$', views.AlbumList.as_view(), name='album-list'),
    url(r'^albums/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    url(r'^photos/$', views.PhotoList.as_view(), name='photo-list'),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view()),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

# Login and logout views for the browse-able API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]