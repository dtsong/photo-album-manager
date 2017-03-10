from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)
router.register(r'albums', views.AlbumViewSet)

# API Endpoints
urlpatterns = [
    url(r'^', include(router.urls)),
]