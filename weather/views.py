from django.shortcuts import render
from django.views.generic import ListView
from .models import Weather
# Create your views here.

class TopView(ListView):
    model = Weather
    template_name = 'top.html'