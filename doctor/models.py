from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from .constants import Day_CHOICES

from specialty.models import Specialty
from utility.models import TimeStamp
from user.models import User


class Doctor(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='media/patients/', default='media/patients/default.png')
    bio = models.TextField(max_length=800)
    fees = models.FloatField()
    phone = PhoneNumberField()
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, related_name='doctorspecialty', null=True)
    day = models.IntegerField(choices=Day_CHOICES)
    start_at = models.TimeField()
    end_at = models.TimeField()

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Duration(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.IntegerField(choices=Day_CHOICES)
    start_at = models.TimeField()
    end_at = models.TimeField()

    class Meta:
        verbose_name = 'Duration'
        verbose_name_plural = 'Durations'