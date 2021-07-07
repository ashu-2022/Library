from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg',upload_to='book_pics',blank = True)
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} by {self.author}'
    
    def get_absolute_url(self):
        return reverse("book-home")

    def save(self, *args, **kwargs):
        # super().save()
        super(Book, self).save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height>400 or img.width>400:
            output_size=(400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)