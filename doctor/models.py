from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from .constants import Day_CHOICES

from common.models import TimeStamp
from user.models import User


class Doctor(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='doctors/avatar/', default='doctors/avatar/default.png')
    background_image = models.ImageField(upload_to='doctors/background.', default='doctors/background/default.png')
    bio = models.TextField(max_length=800)
    fees = models.FloatField()
    phone = PhoneNumberField()
    specialty = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class ClinicDuration(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Doctor', related_name='+')
    day = models.IntegerField(choices=Day_CHOICES)
    start_at = models.TimeField()
    end_at = models.TimeField()

    def get_doctor(self):
        return self.doctor.full_name 

    def __str__(self) -> str:
        return f'DR. {self.get_doctor()} at {self.get_day_display()}'
     
    class Meta:
        verbose_name = 'Clinic Duration'
        verbose_name_plural = 'Durations'
