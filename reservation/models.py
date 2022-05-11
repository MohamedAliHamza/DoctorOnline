from django.db import models

from .constants import RESERVATION_STATUS, RESERVATION_STATUS_CHOICES

from doctor.constants import Day_CHOICES
from common.models import TimeStamp
from patient.models import Patient
from doctor.models import Doctor


class Reservation(TimeStamp):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='+')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='+')
    status = models.IntegerField(choices=RESERVATION_STATUS_CHOICES, default=RESERVATION_STATUS.PENDING)
    day = models.IntegerField(choices=Day_CHOICES)
    time = models.TimeField()

    channel = models.CharField(max_length=800, blank=True, null=True)
    app_id = models.CharField(max_length=800, blank=True, null=True)
    
    def __str__(self):
       return f'{self.day} at {self.time}'

    class Meta:
        ordering = ['-created_at']   


class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name