from rest_framework import serializers
from .models import Photo, Album
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Photo
        fields = ('id', 'album', 'user', 'title', 'url', 'thumbnailUrl')


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'user', 'photos')


class UserSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True, queryset=Album.objects.all())
    photos = serializers.PrimaryKeyRelatedField(many=True, queryset=Photo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'albums', 'photos')
