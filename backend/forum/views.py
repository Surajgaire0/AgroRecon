from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Question, Answer, Comment, AnswerUpvote, CommentUpvote
from .serializers import (
    QuestionSerializer, 
    AnswerSerializer, 
    CommentSerializer, 
    AnswerUpvoteToggleSerializer, 
    CommentUpvoteToggleSerializer
)
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class QuestionListView(generics.ListCreateAPIView):
    queryset=Question.objects.annotate(answer_count=Count('answer')) # 'answer' refers to 'answer_set'
    serializer_class=QuestionSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    search_fields=('text',)
    ordering_fields=('created_at','answer_count')

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    permission_classes=[IsOwnerOrReadOnly]

class AnswerListView(generics.ListCreateAPIView):
    serializer_class=AnswerSerializer
    queryset=Answer.objects.annotate(comment_count=Count('comment')) # 'comment' refers to 'comment_set'
    permission_classes=[IsAuthenticatedOrReadOnly]
    filter_fields=('question',)
    search_fields=('body',)
    ordering_fields=('answered_at','upvote','views','comment_count')

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer
    permission_classes=[IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views+=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommentListView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    filter_fields=('answer',)
    ordering_fields=('commented_at','upvote')

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]


class AnswerUpvoteToggle(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class=AnswerUpvoteToggleSerializer

    def post(self,request,*args,**kwargs):
        user=request.user
        answer=get_object_or_404(Answer,id=request.data['answer'])
        upvote_instance=AnswerUpvote.objects.filter(user=user,answer=answer)
        #if user has already upvoted
        if upvote_instance:
            upvote_instance.delete()
            answer.upvote-=1
            answer.save()
            return Response({'status':'success','message':'upvote removed'},status=status.HTTP_200_OK)
        else:
            AnswerUpvote.objects.create(user=user,answer=answer)
            answer.upvote+=1
            answer.save()
            return Response({'status':'success','message':'upvoted'},status=status.HTTP_201_CREATED)
        return Response({'status':'error','message':'Bad Request'},status=status.HTTP_400_BAD_REQUEST)


class CommentUpvoteToggle(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CommentUpvoteToggleSerializer

    def post(self,request,*args,**kwargs):
        user=request.user
        comment=get_object_or_404(Comment,id=request.data['comment'])
        upvote_instance=CommentUpvote.objects.filter(user=user,comment=comment)
        #if user has already upvoted
        if upvote_instance:
            upvote_instance.delete()
            comment.upvote-=1
            comment.save()
            return Response({'status':'success','message':'upvote removed'},status=status.HTTP_201_CREATED)
        else:
            CommentUpvote.objects.create(user=user,comment=comment)
            comment.upvote+=1
            comment.save()
            return Response({'status':'success','message':'upvoted'},status=status.HTTP_200_OK)
        return Response({'status':'error','message':'Bad Request'},status=status.HTTP_400_BAD_REQUEST)