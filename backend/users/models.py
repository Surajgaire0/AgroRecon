from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    profile_picture=models.ImageField(default='profile/default.jpg',upload_to='profile',blank=True)
    age=models.PositiveIntegerField(null=True,blank=True)