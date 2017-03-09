from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^photos/$', views.PhotoList.as_view()),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)