# car_ratings_app/serializers.py
from rest_framework import serializers
from .models import Car

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make']

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['model']

class CarYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['model_year']

class CarSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['vehicle_id']

class RandomCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['vehicle_id']
