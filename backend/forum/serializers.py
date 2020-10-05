from rest_framework import serializers
from forum.models import Question, Answer, Comment

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'
        extra_kwargs={'userId':{'read_only':True}}

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields='__all__'
        extra_kwargs={'userId':{'read_only':True}}

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        extra_kwargs={'userId':{'read_only':True}}