from django.shortcuts import render
from rest_framework import generics
from .models import Recommend
from .serializers import RecommendSerializer
#from .permissions import AllowAny

# Create your views here.
class ListFactors(generics.ListCreateAPIView):
    queryset=Recommend.objects.all()
    serializer_class=RecommendSerializer

class DetailFactors(generics.RetrieveUpdateDestroyAPIView):
    queryset=Recommend.objects.all()
    serializer_class=RecommendSerializer