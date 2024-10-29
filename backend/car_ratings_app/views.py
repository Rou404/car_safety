from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer  # Import JSONRenderer
from .models import Car
from .serializers import CarModelSerializer, CarMakeSerializer, CarYearSerializer, CarSearchSerializer, RandomCarSerializer
from random import choice

class CarMakeAPIView(APIView):
    renderer_classes = [JSONRenderer]  # Set the renderer class to JSONRenderer

    def get(self, request, *args, **kwargs):
        try:
            car_makes = Car.objects.values('make').distinct()
            serializer = CarMakeSerializer(car_makes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CarModelsByMakeAPIView(APIView):
    renderer_classes = [JSONRenderer]  # Set the renderer class to JSONRenderer

    def get(self, request, make, *args, **kwargs):
        try:
            car_models = Car.objects.filter(make=make).values('model').distinct()
            serializer = CarModelSerializer(car_models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CarYearByMakeAPIView(APIView):
    renderer_classes = [JSONRenderer]  

    def get(self, request, make, model, *args, **kwargs):
        try:
            cars = Car.objects.filter(make=make, model=model)
            unique_years = cars.values('model_year').distinct()
            serializer = CarYearSerializer(unique_years, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CarSearchAPIView(APIView):
    renderer_classes = [JSONRenderer]  

    def get(self, request, make, model, model_year, *args, **kwargs):
        try:
            cars = Car.objects.filter(make=make, model=model, model_year=model_year)
            vehicle_id = cars.values('vehicle_id').distinct()
            serializer = CarSearchSerializer(vehicle_id, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RandomCarSafetyInfo(APIView):
    renderer_classes = [JSONRenderer]  

    def get(self, request, *args, **kwargs):
        try:
            cars_2022 = Car.objects.filter(model_year=2022)
            random_car_2022 = choice(cars_2022)
            vehicle_id = random_car_2022.vehicle_id
            return Response(vehicle_id, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
