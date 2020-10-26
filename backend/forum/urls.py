from django.urls import path, include
from .views import QuestionListView, QuestionDetailView, AnswerListView, AnswerDetailView, \
    CommentListView, CommentDetailView, AnswerUpvoteToggle, CommentUpvoteToggle

urlpatterns = [
    path('questions/<int:pk>',QuestionDetailView.as_view()),
    path('questions/',QuestionListView.as_view(),name='question_list'),
    path('answers/<int:pk>',AnswerDetailView.as_view()),
    path('answers/',AnswerListView.as_view(),name='answer_list'),
    path('comments/<int:pk>',CommentDetailView.as_view()),
    path('comments/',CommentListView.as_view(),name='comment_list'),
    path('answers/upvote/',AnswerUpvoteToggle.as_view(),name='answer_upvote_toggle'),
    path('comments/upvote/',CommentUpvoteToggle.as_view(),name='comment_upvote_toggle')
]