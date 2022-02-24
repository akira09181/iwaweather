from statistics import mode
from django.db import models

# Create your models here.

class Weather(models.Model):
    location = models.CharField(max_length=32)
    weather = models.CharField(max_length=32)
    temperature = models.IntegerField()
    
    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = verbose_name_plural = '天気情報'