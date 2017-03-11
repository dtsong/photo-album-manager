from .models import Photo, Album
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import PhotoSerializer, AlbumSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions
from rest_framework import status


@api_view(['GET'])
def api_root(request, format=None):
    """
    This is the base API Endpoint
    """
    return Response({
        'albums': reverse('album-list', request=request, format=format),
        'photos': reverse('photo-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format)
    })


class PhotoList(generics.ListCreateAPIView):
    """
    Handles:
        GET Photo instances, or POST new Photo
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    """
    Associate User to POST'd Photo
    """
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles:
        Retrieve (GET), Update (PUT),
        and Destroy (DELETE) for a Photo instance.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    """
    Associate User to POST'd Album
    """
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    """
    Override DELETE in order to set a constraint
    on deleting Albums that have Photos associated to them.
    """
    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        if album.photos.exists():
            return Response({'status': 'You cannot delete an Album that has Photos!'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            album.delete()


class UserList(generics.ListAPIView):
    """
    List Users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve User details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
