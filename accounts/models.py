from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profiles/images",null=True,blank=True )
    isKid = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(str(instance.id))

class Payment(models.Model):
    plan_type = models.CharField(max_length=50)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        