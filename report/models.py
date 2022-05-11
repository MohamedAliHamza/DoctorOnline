from django.db import models

from common.models import TimeStamp
from patient.models import Patient
from doctor.models import Doctor

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
