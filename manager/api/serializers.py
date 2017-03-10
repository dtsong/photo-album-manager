from rest_framework import serializers
from .models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('albumId', 'id', 'title', 'photoUrl', 'thumbnailUrl')


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, source='photo_set', read_only=True)

    class Meta:
        model = Album
        fields = ('title', 'photos')
