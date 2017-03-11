from rest_framework import serializers
from .models import Photo, Album
from django.contrib.auth.models import User


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Photo
        fields = ('id', 'album', 'user', 'title', 'url', 'thumbnailUrl')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    photos = serializers.HyperlinkedRelatedField(many=True, view_name='photo-detail', read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'user', 'photos')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    albums = serializers.HyperlinkedRelatedField(many=True, view_name='album-detail', read_only=True)
    photos = serializers.HyperlinkedRelatedField(many=True, view_name='photo-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'albums', 'photos')
