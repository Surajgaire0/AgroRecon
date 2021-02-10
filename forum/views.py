from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Answer, AnswerUpvote, Comment, CommentUpvote,  Question, QuestionUpvote
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    AnswerSerializer,
    AnswerUpvoteToggleSerializer,
    CommentSerializer,
    CommentUpvoteToggleSerializer,
    QuestionSerializer,
    QuestionUpvoteToggleSerializer
)


class QuestionListView(generics.ListCreateAPIView):
    """
    View for list questions and add new questions
    """
    queryset = Question.objects.annotate(
        answer_count=Count('answer')  # 'answer' refers to 'answer_set'
    )
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ('text',)
    filter_fields = ('user__username',)
    ordering_fields = ('created_at', 'answer_count', 'upvote', 'views')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieve, update question and delete question
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AnswerListView(generics.ListCreateAPIView):
    """
    View for list answers and add new answers
    """
    serializer_class = AnswerSerializer
    queryset = Answer.objects.annotate(comment_count=Count(
        'comment'))  # 'comment' refers to 'comment_set'
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ('question', 'user__username')
    search_fields = ('body',)
    ordering_fields = ('answered_at', 'upvote', 'views', 'comment_count')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieve, update answer and delete answer
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommentListView(generics.ListCreateAPIView):
    """
    View for list comments and add new comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ('answer', 'user__username')
    ordering_fields = ('commented_at', 'upvote')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieve, update comment and delete comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class QuestionUpvoteToggle(APIView):
    """
    View for upvote or remove upvote for question
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionUpvoteToggleSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        question = get_object_or_404(Question, id=request.data['question'])
        upvote_instance = QuestionUpvote.objects.filter(
            user=user, question=question)
        # if user has already upvoted
        if upvote_instance:
            upvote_instance.delete()
            question.upvote -= 1
            question.save()
            return Response({'status': 'success', 'message': 'upvote removed'}, status=status.HTTP_201_CREATED)
        else:
            QuestionUpvote.objects.create(user=user, question=question)
            question.upvote += 1
            question.save()
            return Response({'status': 'success', 'message': 'upvoted'}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class AnswerUpvoteToggle(APIView):
    """
    View for upvote or remove upvote for answer
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerUpvoteToggleSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        answer = get_object_or_404(Answer, id=request.data['answer'])
        upvote_instance = AnswerUpvote.objects.filter(user=user, answer=answer)
        # if user has already upvoted
        if upvote_instance:
            upvote_instance.delete()
            answer.upvote -= 1
            answer.save()
            return Response({'status': 'success', 'message': 'upvote removed'}, status=status.HTTP_200_OK)
        else:
            AnswerUpvote.objects.create(user=user, answer=answer)
            answer.upvote += 1
            answer.save()
            return Response({'status': 'success', 'message': 'upvoted'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class CommentUpvoteToggle(APIView):
    """
    View for upvote or remove upvote for comment
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CommentUpvoteToggleSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        comment = get_object_or_404(Comment, id=request.data['comment'])
        upvote_instance = CommentUpvote.objects.filter(
            user=user, comment=comment)
        # if user has already upvoted
        if upvote_instance:
            upvote_instance.delete()
            comment.upvote -= 1
            comment.save()
            return Response({'status': 'success', 'message': 'upvote removed'}, status=status.HTTP_201_CREATED)
        else:
            CommentUpvote.objects.create(user=user, comment=comment)
            comment.upvote += 1
            comment.save()
            return Response({'status': 'success', 'message': 'upvoted'}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
