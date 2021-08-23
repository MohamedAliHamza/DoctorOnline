from utilities.models import TimeStampedModel, DateModel
from utilities.utility import choice_day
from django.db import models
from user.models import User

class ClinicDate(DateModel):
       end_time = models.DateTimeField()

class Clinic(TimeStampedModel):
       name = models.CharField(max_length=50)
       price = models.FloatField()
       doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_clinic')
       date = models.ManyToManyField(ClinicDate, related_name='clinic_date')

       def __str__(self):
              return self.name