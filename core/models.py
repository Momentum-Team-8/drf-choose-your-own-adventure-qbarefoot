from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    def __str__(self):
        return self.username


class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    publication_date = models.DateField()
    review = models.TextField(blank=True)

    def __str__(self):
        return self.title

