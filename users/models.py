from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    cover = models.ImageField(upload_to='user_covers', null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    age = models.IntegerField(default=None, null=True, blank=True)
    job = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    hobbie = models.CharField(max_length=64, null=True, blank=True)
    contact = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    


