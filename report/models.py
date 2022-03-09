from django.db import models

from utility.models import TimeStamp
from doctor.models import Doctor
from patient.models import Patient


class Report(TimeStamp):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.content

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        ordering = ['-created_at']

