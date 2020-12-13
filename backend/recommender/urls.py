from django.urls import path, include
from .views import ListRecommended

urlpatterns = [
    path('',ListRecommended.as_view(),name='predicted'),
]
