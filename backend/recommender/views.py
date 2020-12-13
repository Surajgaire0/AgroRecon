import json
from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Recommend, Plant
from .serializers import RecommendSerializer, PlantSerializer

# Create your views here.
class ListRecommended(generics.ListCreateAPIView):
    queryset=Recommend.objects.all()
    serializer_class=RecommendSerializer

    def post(self,request,*args,**kwargs):
        serializer=RecommendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            predictions=serializer.data['prediction']
            growth=serializer.data['growth_habit']
            duration=serializer.data['duration']
            predictions=json.loads(predictions)
            plantdata=[]
            for prediction in predictions:
                plant_instance=Plant.objects.filter(Q(growth_habit__icontains=growth) & Q(duration__icontains=duration) & Q(common_name__icontains=prediction)).first()
                if plant_instance:
                    plant_serializer=PlantSerializer(plant_instance)
                    plantdata.append(plant_serializer.data)
            response={**serializer.data,'prediction':plantdata}
            return Response(response,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)