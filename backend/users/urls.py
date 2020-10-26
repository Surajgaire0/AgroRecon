from django.urls import path, include
from .views import CustomUserListView, CustomUserDetailView, PasswordChangeView

urlpatterns = [
    path('password-change/',PasswordChangeView.as_view(),name='password_change'),
    path('<str:username>/',CustomUserDetailView.as_view()),
    path('',CustomUserListView.as_view(),name='user_list'),
]