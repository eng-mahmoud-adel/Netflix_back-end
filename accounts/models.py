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



PLANS_CHOICES = [
    ("Basic", "Basic"),
    ("Standard", "Standard"),
    ("Premium","Premium")
]

PRICES_CHOICES = [
    (120, 120),
    (165, 165),
    (200,200)
]

class Payment(models.Model):
    plan_type = models.CharField(max_length=50, choices=PLANS_CHOICES)
    price = models.FloatField(choices=PRICES_CHOICES)
    # todo >> move this relationship to user model
    # create user model and extend from User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        