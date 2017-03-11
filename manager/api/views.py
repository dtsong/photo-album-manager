from .models import Photo, Album
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import PhotoSerializer, AlbumSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'albums': reverse('album-list', request=request, format=format),
        'photos': reverse('photo-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format)
    })


class PhotoList(APIView):
    """
    GET all Photos
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)


class PhotoDetail(APIView):
    """
    "GET, POST, PUT, or DELETE a Photo instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    """
    Create a new Photo instance.
    """
    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Associate the Photo with the User
    """
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    """
    Update the Photo instance
    """
    def put(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumList(APIView):
    """
    GET all Albums, or POST a new Album.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumDetail(APIView):
    """
    GET, PUT, or DELETE an Album instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Prevent DELETE of Album if there are associated Photos
    """
    def delete(self, request, pk, format=None):
        album = self.get_object(pk)
        if album.photos.exists():
            return Response({'status': 'Album has photos!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            album.delete()


class UserList(generics.ListAPIView):
    """
    Use a generic ListAPIView solely for listing Users,
    No need to setup POST due to Django's built-in User model and forms.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Use a RetrieveAPIView to view related Django User data
    as defined by UserSerializer
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
