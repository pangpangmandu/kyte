from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.

class Profile(models.Model):
    COUNTRIES = (
        ('KR', 'South Korea'),
        ('US', 'USA'),
        ('JP', 'Japan'),
        ('CH', 'China'),
        ('FR', 'France'),
        ('GR', 'Germany'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    steamid = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=10, unique=True)
    ranking = models.CharField(max_length=20)
    ##location = models.CharField(max_length=2, choices=COUNTRIES)
    signUpDate = models.DateField(default=timezone.now)
    email = models.CharField(max_length=100, null=True)
    introduction = models.TextField(blank=True)
    running = models.BooleanField(default=False)

    def makeranking(self):
        self.ranking = 50
        self.save()

    def __str__(self):
        return self.nickname+" 's profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    gamename = models.CharField(max_length=100, default='N/A')
    maxPlayer = models.PositiveSmallIntegerField(max_length=12, default=2)

    def __str__(self):
        return self.gamename


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    playerId = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    gameId = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=10.0, default=0.0)
    recentUpdate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.gameId

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    gameId = models.ForeignKey(Game, on_delete=models.CASCADE)
    ##raterId = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    rateeId = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    point = models.PositiveSmallIntegerField(max_length=10, default=5)
    matchDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.gameId


class MatchedUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    chatroom = models.CharField(max_length=10)


class GameSeed(models.Model):
    id = models.AutoField(primary_key=True)
    gamename = models.TextField(default="gamename")
    users = models.ManyToManyField(Profile,related_name = 'seeds',null = True)
    def seed():
        GameSeed.objects.create(gamename="Don't Starve")
        GameSeed.objects.create(gamename="BorderLands")
        GameSeed.objects.create(gamename="GTA")
        GameSeed.objects.create(gamename="BattelGrounds")
        GameSeed.objects.create(gamename="Total War")
        GameSeed.objects.create(gamename="Stardew Valley")
          