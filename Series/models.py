from django.db import models
from movies.models import Actors, Genre, Movies
from . import views
# Create your models here.

class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    views = models.IntegerField()
    seasons = models.IntegerField()
    date = models.DateField()
    maturity_rating = models.CharField(max_length=5)
    img = models.URLField()
    video = models.URLField()
    actors = models.ManyToManyField(Actors)
    genre = models.ManyToManyField(Genre)
    trailer = models.URLField()
    def __str__(self):
        return self.name


class Creators(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Episodes(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()
    seasons = models.IntegerField()
    episode_number = models.IntegerField()
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)
    img = models.URLField()
    video = models.URLField()
    #trailer =models.URLField(max_length=100)
    def __str__(self):
        return self.name


