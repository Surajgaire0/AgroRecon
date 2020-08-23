from django.urls import path, include
from .views import CustomUserListView, CustomUserDetailView

urlpatterns = [
    path('<int:pk>',CustomUserDetailView.as_view()),
    path('',CustomUserListView.as_view()),
]