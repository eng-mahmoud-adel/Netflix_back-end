from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.DateField()
    maturity_rating = models.CharField(max_length=10)
    duration = models.IntegerField()
    views =models.IntegerField(deafult=0)
    rate = models.FloatField()
    director = models.CharField(max_length=100)
    #writer

    trailer =models.CharField()
    video = models.CharField()
    poster = models.CharField()

    # category many to many 
    #actors many to amn 

    def __str__(self):
        return self.name


class Actors(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Genre(model.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
