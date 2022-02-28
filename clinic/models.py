from phonenumber_field.modelfields import PhoneNumberField

from.constants import Day_CHOICES

from utility.models import TimeStamp
from django.db import models
from user.models import User


class Specialty(models.Model):
    title = models.CharField(max_length=120)


class Clinic(TimeStamp):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clinicdoctor')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='clinicspecialty')
    about = models.CharField(max_length=800)
    fees = models.FloatField()
    phone = PhoneNumberField()

    def __str__(self):
        return str(self.id)


class Availability(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='clinicavailability')
    day = models.IntegerField(choices=Day_CHOICES)
    start_at = models.TimeField()
    end_at = models.TimeField()