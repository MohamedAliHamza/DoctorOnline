from typing import Optional

from ..models import Patient

from user.api.utils import create_user, update_user
from user.models import User


def create_patient(email: str, password_1: str, password_2: str, full_name: str, age: int
                , gender: int, length: Optional[float] = None, weight: Optional[float] = None):

    user = create_user(email, password_1, password_2, is_patient=True)

    patient = Patient.objects.create(
        user=user, 
        full_name=full_name, 
        age=age,
        gender=gender,
        length=length,
        weight=weight,
        )

    return user, patient


def update_patient(user: User, **kwargs):

    user_fields = update_user(user, kwargs.get('email'), kwargs.get('password_1'), kwargs.get('password_2'))

    patient_fields = []

    patient = user.patient

    for key, value in kwargs.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
                patient_fields.append(key)

    patient_fields.append('updated_at')            

    # Update
    user.save(update_fields=[field for field in user_fields])
    patient.save(update_fields=[field for field in patient_fields])

    return patient
