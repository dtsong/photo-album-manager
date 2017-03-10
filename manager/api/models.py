from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Photo(models.Model):
    albumId = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photoUrl = models.URLField()
    thumbnailUrl = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']