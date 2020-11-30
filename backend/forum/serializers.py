from django.contrib.auth import get_user_model
from rest_framework import serializers
from forum.models import Question, Answer, Comment, AnswerUpvote, CommentUpvote

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('id','text','created_at','updated_at','user','answer_count')
        extra_kwargs={'user':{'read_only':True}}

class AnswerSerializer(serializers.ModelSerializer):
    has_user_upvoted=serializers.SerializerMethodField(source='get_has_user_upvoted', read_only=True)
    username=serializers.SerializerMethodField(source='get_username',read_only=True)

    def get_username(self,obj):
        return obj.user.username

    def get_has_user_upvoted(self,obj):
        return obj.answerupvote_set.filter(user=self.context.get('request').user).exists()

    class Meta:
        model=Answer
        fields=('id','body','answered_at','updated_at','user','username','comment_count','question','upvote','views','has_user_upvoted')
        extra_kwargs={'user':{'read_only':True},'upvote':{'read_only':True},'views':{'read_only':True}}

class CommentSerializer(serializers.ModelSerializer):
    has_user_upvoted=serializers.SerializerMethodField(source='get_has_user_upvoted', read_only=True)
    username=serializers.SerializerMethodField(source='get_username',read_only=True)

    def get_username(self,obj):
        return obj.user.username

    def get_has_user_upvoted(self,obj):
        return obj.commentupvote_set.filter(user=self.context.get('request').user).exists()

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