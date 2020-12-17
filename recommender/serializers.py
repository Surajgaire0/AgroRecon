from rest_framework import serializers
from .models import Recommend, Plant
import json

class RecommendSerializer(serializers.ModelSerializer):

    def validate(self,data):
        """Check that minimun precipitation is less than the maximum precipitation."""
        if data['min_precipitation']>data['max_precipitation']:
            raise serializers.ValidationError('Minimum precipitation cannot be higher than the maximum precipitation.')
        return data

    class Meta:
        model=Recommend
        fields='__all__'


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plant
        fields='__all__'