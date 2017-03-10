from rest_framework import serializers
from .models import Photo, Album
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'album', 'title', 'url', 'thumbnailUrl')


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Album
        fields = ('id', 'title', 'user', 'photos')


class UserSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True, queryset=Album.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'albums')
