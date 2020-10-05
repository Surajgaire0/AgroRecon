from django.shortcuts import render
from rest_framework import generics
from .models import Recommend
from .serializers import RecommendSerializer
#from .permissions import AllowAny

# Create your views here.
class ListRecommended(generics.ListCreateAPIView):
    queryset=Recommend.objects.all()
    serializer_class=RecommendSerializer

class DetailRecommended(generics.RetrieveUpdateDestroyAPIView):
    queryset=Recommend.objects.all()
    serializer_class=RecommendSerializer