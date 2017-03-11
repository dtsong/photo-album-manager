from rest_framework import serializers
from .models import Photo, Album
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        """
        album: The associated Album to this Photo.
        user: The associated User to this Photo.
        """
        model = Photo
        fields = ('id', 'album', 'user', 'title', 'url', 'thumbnailUrl')


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        """
        user: The associated User to this Album.
        photos: The associated Photo objects to this Album.
        """
        model = Album
        fields = ('id', 'title', 'user', 'photos')


class UserSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        """
        albums: The associated Albums to this User.
        photos: The associated Photos to this User.
        """
        model = User
        fields = ('id', 'username', 'albums', 'photos')
