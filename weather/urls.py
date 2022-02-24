from .views import TopView
from django.urls import path, include

urlpatterns = [
    path('top/', TopView.as_view()),
]