from django.db import models

# Create your models here.
class allAlbums(models.Model):
    artistname = models.CharField(max_length=255)
    albumtitle = models.CharField(max_length=255)
    released = models.DateField()

    def __str__(self):
      return f"{self.albumtitle}"

class Users(models.Model):
  pass