from .views import TopView, WeatherAPIView
from django.urls import path, include

urlpatterns = [
    path('top/', TopView.as_view()),
    path('api/', WeatherAPIView.as_view()),
]