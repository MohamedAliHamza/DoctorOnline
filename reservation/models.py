from django.db import models
from user.models import User
from utilities.models import DateModel
from clinic.models import Clinic

class Reservation(DateModel):
       patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_reservation')
       doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_reservation')
       clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='clinic_reservation')

       def __str__(self):
              return str(self.id)