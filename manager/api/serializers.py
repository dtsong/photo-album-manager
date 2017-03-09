from rest_framework import serializers
from .models import Photo, Album


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'photos')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title', 'photoUrl', 'thumbnailUrl')
