import datetime

from django.db import models
from django.contrib.auth import get_user_model


class Question(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True)
    upvote = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    @property
    def answer_count(self):
        return self.answer_set.all().count()

    @answer_count.setter
    def answer_count(self, value):
        pass


class Answer(models.Model):
    body = models.TextField()
    answered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    upvote = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    @property
    def comment_count(self):
        return self.comment_set.count()

    @comment_count.setter
    def comment_count(self, value):
        pass

    class Meta:
        ordering = ('answered_at',)


class Comment(models.Model):
    body = models.CharField(max_length=512)
    commented_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    upvote = models.PositiveIntegerField(default=0)


class QuestionUpvote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class AnswerUpvote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class CommentUpvote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
