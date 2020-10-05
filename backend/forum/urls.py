from django.urls import path, include
from .views import QuestionListView, QuestionDetailView, AnswerListView, AnswerDetailView, \
    CommentListView, CommentDetailView

urlpatterns = [
    path('questions/<int:pk>',QuestionDetailView.as_view()),
    path('questions/',QuestionListView.as_view(),name='question-list'),
    path('answers/<int:pk>',AnswerDetailView.as_view()),
    path('answers/',AnswerListView.as_view(),name='answer-list'),
    path('comments/<int:pk>',CommentDetailView.as_view()),
    path('comments/',CommentListView.as_view(),name='comment-list'),
]