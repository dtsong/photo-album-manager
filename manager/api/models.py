from django.db import models

class Photo(models.Model):
    album = models.ForeignKey('Album', related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photoUrl = models.URLField()
    thumbnailUrl = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Photo"
        verbose_name = "Photos"