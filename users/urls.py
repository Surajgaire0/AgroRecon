from django.urls import path, include
from .views import CustomUserListView, CustomUserDetailView, PasswordChangeView, MeUserView

urlpatterns = [
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('me/', MeUserView.as_view(), name='me'),
    path('<str:username>/', CustomUserDetailView.as_view()),
    path('', CustomUserListView.as_view(), name='user_list'),
]
