from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)


class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photoUrl = models.URLField()
    thumbnailUrl = models.URLField()
