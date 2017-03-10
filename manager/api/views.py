from .models import Photo, Album
from .serializers import PhotoSerializer, AlbumListSerializer, AlbumDetailSerializer
from rest_framework_extensions.mixins import DetailSerializerMixin
from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'albums': reverse('album-list', request=request, format=format),
#         'photos': reverse('photo-list', request=request, format=format)
#     })


class AlbumViewSet(DetailSerializerMixin, viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumListSerializer
    serializer_detail_class = AlbumDetailSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        album_id = self.kwargs.get('album_pk', None)
        if album_id:
            return Photo.objects.filter(album=album_id)
        return super(PhotoViewSet, self).get_queryset()