from rest_framework import serializers
from .models import Photo, Album


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.HyperlinkedRelatedField(many=True, view_name='photo-detail', read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'photos')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.ReadOnlyField(source='album.id')

    class Meta:
        model = Photo
        fields = ('id', 'title', 'album', 'photoUrl', 'thumbnailUrl')
