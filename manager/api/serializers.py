from rest_framework import serializers
from .models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'title', 'album', 'photoUrl', 'thumbnailUrl')

class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, source='photo_set')

    class Meta:
        model = Album
        fields = ('id', 'title', 'photos')

    def create(self, validated_data):
        photos_data = validated_data.pop('photos')
        album = Album.objects.create(**validated_data)
        for photo_data in photos_data:
            Photo.objects.create(album=album, **photo_data)
        return album
