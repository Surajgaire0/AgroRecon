from rest_framework import generics
from forum.models import Question, Answer, Comment
from .serializers import QuestionSerializer, AnswerSerializer, CommentSerializer
#from .permissions import AllowAny

# Create your views here.
class QuestionListView(generics.ListCreateAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

class AnswerListView(generics.ListCreateAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer

class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer

class CommentListView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer