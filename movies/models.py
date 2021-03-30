from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.DateField()
    maturity_rating = models.CharField(max_length=10)
    duration = models.IntegerField()
    views =models.IntegerField()
    rate = models.FloatField()
    #trailer
    # category
    #writer
    #director 
    #actors 
    # video = models.FileField()
    # poster = models.ImageField()

    def __str__(self):
        return self.name

