from django.db import models

# Create your models here.


class Actors(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.DateField()
    maturity_rating = models.CharField(max_length=10)
    duration = models.IntegerField()
    views =models.IntegerField()
    rate = models.FloatField()
    director = models.CharField(max_length=100)

    trailer =models.URLField(max_length=100)
    video = models.URLField(max_length=100)
    img = models.URLField(max_length=100)

    writers =models.ManyToManyField(Writer)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actors) 

    def __str__(self):
        return self.name

