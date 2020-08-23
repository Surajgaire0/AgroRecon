from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    address=models.CharField(max_length=127,null=True,blank=True)
    website=models.URLField(null=True,blank=True)
    phone=models.PositiveIntegerField(null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    #profile_picture=models.ImageField(default='profile/default.jpg',upload_to='profile',blank=True)
    #age=models.PositiveIntegerField(null=True,blank=True)