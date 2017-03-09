from rest_framework import serializers
from .models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    album = serializers.ReadOnlyField(source='album.id')

    class Meta:
        model = Photo
        fields = ('id', 'title', 'album', 'photoUrl', 'thumbnailUrl')
        depth = 1


class AlbumPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return 'Album: %s' % (instance.title)


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'photos')

    def create(self, validated_data):
        photos_data = validated_data.pop('photos')
        album = Album.objects.create(**validated_data)
        for photo_data in photos_data:
            Photo.objects.create(album=album, **photo_data)
        return album

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save()

        # Delete photos not included in the request
        photo_ids = [item['id'] for item in validated_data['photos']]
        for photo in instance.albums:
            if photo.id not in photo_ids:
                photo.delete()

        # Create or update photo instances that are in the request
        for photo in validated_data['photos']:
            photo = Photo(id=photo['id'], title=photo['title'], album=instance,
                          photoUrl=photo['photoUrl'], thumbnailUrl=photo['thumbnailUrl'])
            photo.save()
        return instance
