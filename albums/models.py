from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    released = models.DateField()
    image_url = models.TextField(null=True, blank=True)
    track_list = models.TextField(null=True, blank=True)
    
    
    order_with_respect_to = 'title'

    def __str__(self):
      return f"{self.title} by {self.artist}"

    

class Users(models.Model):
  pass
      
class Book(models.Model):
    author = models.CharField(max_length=255)
    book_title = models.CharField(max_length=255)
    date_published = models.DateField()
    book_cover = models.TextField(null=True, blank=True)
    chapter_list = models.TextField(null=True, blank=True)
    
    
    order_with_respect_to = 'author'

    def __str__(self):
      return f"{self.book_title} by {self.author}"

# class Details(models.Model):
#   detail = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="details")
#   text = models.TextField(null=True, blank=True)
#   date_added = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return f"{self.text}"

