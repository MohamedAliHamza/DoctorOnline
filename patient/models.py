from django.db import models

from utility.models import TimeStamp
from user.models import User


class Patient(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='media/patients/', default='media/patients/default.png')

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
