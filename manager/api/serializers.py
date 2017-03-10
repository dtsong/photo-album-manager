from rest_framework import serializers
from .models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'album', 'title', 'url', 'thumbnailUrl')


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'title')
