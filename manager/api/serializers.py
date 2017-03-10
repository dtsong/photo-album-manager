from rest_framework import serializers
from .models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('title', 'photoUrl', 'thumbnailUrl')


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Album
        fields = ('title', 'photos')

    def create(self, validated_data):
        photos_data = validated_data.pop('photos')
        album = Album.objects.create(**validated_data)
        for photo_data in photos_data:
            Photo.objects.create(album=album, **photo_data)
        return album
