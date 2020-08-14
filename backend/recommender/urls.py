from django.urls import path, include
from .views import ListFactors, DetailFactors

urlpatterns = [
    path('<int:pk>',DetailFactors.as_view()),
    path('',ListFactors.as_view()),
]
