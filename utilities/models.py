from django.db import models
from .utility import choice_day

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       abstract = True

class DateModel(models.Model):
    day = models.CharField(max_length=10, choices=choice_day)
    start_time = models.DateTimeField()
    
    class Meta:
       abstract = True