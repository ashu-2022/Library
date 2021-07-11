from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse

LANGUAGE_CHOICES = (
    (0, 'English'),
    (1, 'Hindi'),
    (2, 'German'),
    (3, 'English(U.S.)'),
    (4, 'English(India)'),
)

GENRE_CHOICES = (
    (0, 'CS'),
    (1, 'Non-CS'),
    (2, 'Common'),
)

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.CharField(max_length=100)
    genre = models.IntegerField(choices=GENRE_CHOICES,null=True)
    language = models.IntegerField(choices=LANGUAGE_CHOICES,null=True)
    image = models.ImageField(default='default.jpg',upload_to='book_pics',blank = True)
    date_posted=models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (('name', 'author','genre','language'))

    def __str__(self):
        return f'{self.name} by {self.author}'
    
    def get_absolute_url(self):
        return reverse("book-home")

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height>400 or img.width>400:
            output_size=(400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)


    # genre = models.CharField(max_length=100)
    # language = models.CharField(max_length=100)
    # genre = models.CharField(max_length=100,null=True, choices=STATUS_CHOICES)
    # language = models.IntegerField(choices=LANGUAGE_CHOICES, default=0)
    # genre = models.ForeignKey(Genre,null=True,on_delete=models.SET_NULL)
    # language = models.ForeignKey(Language,null=True,on_delete=models.SET_NULL)
    # genre = models.CharField(max_length=100,null=True, choices=GENRE_CHOICES)
    # language = models.CharField(max_length=100,choices=LANGUAGE_CHOICES,null=True)

# class Genre(models.Model):
#     genre = models.IntegerField(choices=STATUS_CHOICES, null=True,default=0)

#     def __str__(self):
#         return self.genre

# class Language(models.Model):
#     language = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.language



# GENRE_CHOICES = (
#     ('CS', 'CS'),
#     ('Non-CS', 'Non-CS'),
#     ('Non-CS', 'Common'),
# )

# STATUS= (
#     (0, 'Regular'),
#     (1, 'Manager'),
#     (2, 'Admin'),
# )