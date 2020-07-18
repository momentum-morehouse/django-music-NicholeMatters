from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=255)
    book_title = models.CharField(max_length=255)
    published_year = models.CharField(max_length=4)
    book_cover = models.TextField(null=True, blank=True)
    chapter_list = models.TextField(null=True, blank=True)
    
    
    order_with_respect_to = 'author'

    def __str__(self):
      return f"{self.book_title} by {self.author}"