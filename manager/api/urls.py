from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^photos/$', views.photo_list),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.photo_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)