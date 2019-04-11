from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Game(models.Model):
    gamename = models.CharField(max_length=256)

    def __str__(self):
        return self.gamename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    ranking = models.CharField(max_length=20, blank=True)

    def makeranking(self):
        self.ranking = 50
        self.save()

    
    def __str__(self):
        return self.user.id+" 's profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()