from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# class Movie(models.Model):
#     title= models.CharField(max_length=200)
#     desc = models.TextField(null=True,blank=True)
#     year = models.DateField(null=True,blank=True)
#     poster = models.ImageField(upload_to="movies/posters",null=True,blank=True )
#     video = models.FileField(upload_to="movies/videos",null=True,blank=True)
#     categories = models.ManyToManyField(Category)
#     country = models.ForeignKey(Country , null=True ,on_delete=models.SET_NULL)
#     rate= models.OneToOneField(Rate, null=True,on_delete=models.SET_NULL)


class Profile(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profiles/images",null=True,blank=True )
    isKid = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        