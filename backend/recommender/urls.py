from django.urls import path, include
from .views import ListRecommended, DetailRecommended

urlpatterns = [
    path('<int:pk>',DetailRecommended.as_view()),
    path('',ListRecommended.as_view(),name='predicted'),
]
