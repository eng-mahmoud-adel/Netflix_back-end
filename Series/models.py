from django.db import models

# Create your models here.

class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    views = models.IntegerField()
    seasons = models.IntegerField()
    date = models.DateField()
    maturity_rating = models.CharField(max_length=5)
    img = models.URLField()
    video = models.URLField(upload_to='series/videos')
    #trailer
    def __str__(self):
        return self.name
