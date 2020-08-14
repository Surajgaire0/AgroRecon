from django.shortcuts import render
from rest_framework import generics
from recommender.models import Plant_Recommend
from .serializers import PlantRecommendSerializer
#from .permissions import AllowAny

# Create your views here.
class ListFactors(generics.ListCreateAPIView):
    queryset=Plant_Recommend.objects.all()
    serializer_class=PlantRecommendSerializer

class DetailFactors(generics.RetrieveUpdateDestroyAPIView):
    queryset=Plant_Recommend.objects.all()
    serializer_class=PlantRecommendSerializer