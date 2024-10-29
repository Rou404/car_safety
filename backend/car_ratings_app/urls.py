# car_ratings_app/urls.py
from django.urls import path
from .views import CarModelsByMakeAPIView, CarMakeAPIView, CarYearByMakeAPIView, CarSearchAPIView, RandomCarSafetyInfo

urlpatterns = [
    path('car-makes/', CarMakeAPIView.as_view(), name='car-makes'),
    path('car-makes/<str:make>/car-models/', CarModelsByMakeAPIView.as_view(), name='car-models-by-make'),
    path('car-makes/<str:make>/car-models/<str:model>/model_year/', CarYearByMakeAPIView.as_view(), name='car-year-by-models-and-make'),
    path('car-makes/<str:make>/car-models/<str:model>/model_year/<str:model_year>/', CarSearchAPIView.as_view(), name='car-search'),
    path('random/', RandomCarSafetyInfo.as_view(), name='random'),

]
