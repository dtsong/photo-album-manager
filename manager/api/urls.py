from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'photos', views.PhotoViewSet)

albums_router = routers.NestedSimpleRouter(router, r'albums', lookup='album')
albums_router.register(r'photo', views.PhotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(albums_router.urls)),
]