from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=127,null=True,blank=True)
    profile_picture=models.ImageField(default='defaultusers.png',upload_to='profile',blank=True)

    @property
    def question_count(self):
        return self.question_set.count()

    @property
    def answer_count(self):
        return self.answer_set.count()

    @property
    def comment_count(self):
        return self.comment_set.count()