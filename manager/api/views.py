from .models import Photo, Album
from .serializers import PhotoSerializer, AlbumSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'albums': reverse('album-list', request=request, format=format),
        'photos': reverse('photo-list', request=request, format=format)
    })


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer