from django.db import models

from .constants import GENDER_CHOICES

from common.models import TimeStamp
from user.models import User


class Patient(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    full_name = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='patients/', default='patients/default.jpg')
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    length = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
