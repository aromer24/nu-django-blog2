from turtle import update

from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
         return self.name

class Tag (models.Model):
    name = models.CharField(max_length=16, unique=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



