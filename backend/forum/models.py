from django.db import models
from users.models import CustomUser

# Create your models here.
class Question(models.Model):
    text=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True)

    @property
    def answer_count(self):
        return self.answer_set.all().count()

class Answer(models.Model):
    body=models.TextField()
    answered_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    upvote=models.PositiveIntegerField(default=0)
    views=models.PositiveIntegerField(default=0)

    @property
    def comment_count(self):
        return self.comment_set.all().count()

class Comment(models.Model):
    body=models.CharField(max_length=512)
    answered_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    upvote=models.PositiveIntegerField(default=0)


class AnswerUpvote(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class CommentUpvote(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)