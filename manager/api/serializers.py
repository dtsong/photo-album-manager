from rest_framework import serializers
from .models import Photo, Album


class AlbumListSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.RelatedField(many=True, queryset=Photo.objects.all())

    class Meta:
        model = Album
        fields = ('id', 'url', 'title', 'photos')


class AlbumDetailSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.HyperlinkedRelatedField(many=True, queryset=Photo.objects.all(), view_name='photo-detail')

    class Meta:
        model = Album
        fields = ('id', 'title', 'photos')


class PhotoSerializer(serializers.ModelSerializer):
    album = serializers.Field(source='album.id')

    class Meta:
        model = Photo
        fields = ('id', 'album', 'title', 'url', 'thumbnailUrl')
