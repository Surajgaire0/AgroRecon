from django.urls import path, include
from .views import CustomUserListView, CustomUserDetailView

urlpatterns = [
    path('<str:username>',CustomUserDetailView.as_view()),
    path('',CustomUserListView.as_view(),name='user-list'),
]