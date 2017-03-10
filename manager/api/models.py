from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    thumbnailUrl = models.URLField()

    def __str__(self):
        return self.title
