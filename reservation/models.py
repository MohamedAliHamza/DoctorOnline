from django.db import models

from .constants import RESERVATION_STATUS, RESERVATION_STATUS_CHOICES

from doctor.constants import Day_CHOICES
from utility.models import TimeStamp
from patient.models import Patient
from doctor.models import Doctor


class Reservation(TimeStamp):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='+')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='+')
    status = models.IntegerField(choices=RESERVATION_STATUS_CHOICES, default=RESERVATION_STATUS.PENDING)
    day = models.IntegerField(choices=Day_CHOICES)
    time = models.TimeField()
    
    def __str__(self):
       return str(self.id)