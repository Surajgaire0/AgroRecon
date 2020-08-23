from rest_framework import serializers
from recommender.models import Plant_Recommend

class PlantRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plant_Recommend
        fields='__all__'