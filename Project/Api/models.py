from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'
    WORK_TYPES = (
        (YOUTUBE, 'YouTube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPES)
    artists = models.ManyToManyField('Artist')

class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work)
