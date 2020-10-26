from rest_framework import serializers
from forum.models import Question, Answer, Comment, AnswerUpvote, CommentUpvote

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('id','text','created_at','updated_at','user','answer_count')
        extra_kwargs={'user':{'read_only':True}}

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=('id','body','answered_at','updated_at','user','comment_count','question','upvote','views')
        extra_kwargs={'user':{'read_only':True},'upvote':{'read_only':True},'views':{'read_only':True}}

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        extra_kwargs={'user':{'read_only':True},'upvote':{'read_only':True}}

class AnswerUpvoteToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnswerUpvote
        fields='__all__'
        extra_kwargs={'user':{'read_only':True}}

class CommentUpvoteToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentUpvote
        fields='__all__'
        extra_kwargs={'user':{'read_only':True}}