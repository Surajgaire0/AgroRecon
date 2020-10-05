from django.db import models
from users.models import CustomUser

# Create your models here.
class Question(models.Model):
    text=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    userId=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True)

class Answer(models.Model):
    body=models.TextField()
    answered_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    userId=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True)
    questionId=models.ForeignKey(Question,on_delete=models.CASCADE)
    upvote=models.PositiveIntegerField(default=0)
    downvote=models.PositiveIntegerField(default=0)

class Comment(models.Model):
    body=models.CharField(max_length=512)
    answered_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    userId=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True)
    answerId=models.ForeignKey(Answer,on_delete=models.CASCADE)
    upvote=models.PositiveIntegerField(default=0)
    downvote=models.PositiveIntegerField(default=0)

    
