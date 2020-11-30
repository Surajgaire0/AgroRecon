import datetime
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

    @answer_count.setter
    def answer_count(self,value):
        pass


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
        return self.comment_set.count()

    @comment_count.setter
    def comment_count(self,value):
        pass

    @property
    def score(self):
        delta=datetime.datetime.now()-self.answered_at
        days,seconds=delta.days,delta.seconds
        days=days+(seconds//3600)/24.0
        return max(1,self.upvote*2+views)/(days+1)**2

    class Meta:
        ordering=('answered_at',)


class Comment(models.Model):
    body=models.CharField(max_length=512)
    commented_at=models.DateTimeField(auto_now_add=True)
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