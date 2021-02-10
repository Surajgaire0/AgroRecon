from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Answer, AnswerUpvote, Comment, CommentUpvote,  Question, QuestionUpvote


class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(
        source='get_username', read_only=True)
    has_user_upvoted = serializers.SerializerMethodField(
        source='get_has_user_upvoted', read_only=True)

    def get_username(self, obj):
        return obj.user.username

    def get_has_user_upvoted(self, obj):
        if not self.context.get('request').user.is_authenticated:
            return False
        return obj.questionupvote_set.filter(user=self.context.get('request').user).exists()

    class Meta:
        model = Question
        fields = ('id', 'text', 'created_at', 'updated_at', 'user', 'username',
                  'answer_count', 'answer_set', 'views', 'upvote', 'has_user_upvoted')
        extra_kwargs = {'user': {'read_only': True}, 'upvote': {
            'read_only': True}, 'views': {'read_only': True}, 'answer_set': {'read_only': True}}


class AnswerSerializer(serializers.ModelSerializer):
    has_user_upvoted = serializers.SerializerMethodField(
        source='get_has_user_upvoted', read_only=True)
    username = serializers.SerializerMethodField(
        source='get_username', read_only=True)

    def get_username(self, obj):
        return obj.user.username

    def get_has_user_upvoted(self, obj):
        if not self.context.get('request').user.is_authenticated:
            return False
        return obj.answerupvote_set.filter(user=self.context.get('request').user).exists()

    class Meta:
        model = Answer
        fields = ('id', 'body', 'answered_at', 'updated_at', 'user', 'username',
                  'comment_count', 'comment_set', 'question', 'upvote', 'views', 'has_user_upvoted')
        extra_kwargs = {'user': {'read_only': True}, 'upvote': {'read_only': True}, 'views': {
            'read_only': True}, 'comment_set': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):
    has_user_upvoted = serializers.SerializerMethodField(
        source='get_has_user_upvoted', read_only=True)
    username = serializers.SerializerMethodField(
        source='get_username', read_only=True)

    def get_username(self, obj):
        return obj.user.username

    def get_has_user_upvoted(self, obj):
        if not self.context.get('request').user.is_authenticated:
            return False
        return obj.commentupvote_set.filter(user=self.context.get('request').user).exists()

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True},
                        'upvote': {'read_only': True}}


class QuestionUpvoteToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionUpvote
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}


class AnswerUpvoteToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerUpvote
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}


class CommentUpvoteToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentUpvote
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
