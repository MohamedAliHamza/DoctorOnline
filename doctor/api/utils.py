from decimal import Decimal

from rest_framework import serializers

from ..models import Doctor

from user.api.utils import create_user, update_user
from user.models import User


def create_doctor(email: str, password_1: str, password_2: str, full_name: str
                , bio: str, fees: Decimal, phone: str, address: str, specialty: str):

    user = create_user(email, password_1, password_2, is_doctor=True)

    doctor = Doctor.objects.create(
        user=user, 
        full_name=full_name, 
        bio=bio,
        fees=fees,
        phone=phone,
        address=address,
        specialty=specialty,
        )

    return user, doctor


def update_doctor(user: User, **kwargs):

    user_fields = update_user(user, kwargs.get('email'), kwargs.get('password_1'), kwargs.get('password_2'))
    doctor_fields = []

    doctor = user.doctor

    for key, value in kwargs.items():
            if hasattr(doctor, key):
                setattr(doctor, key, value)
                doctor_fields.append(key)

    doctor_fields.append('updated_at')            

    # Update
    user.save(update_fields=[field for field in user_fields])
    doctor.save(update_fields=[field for field in doctor_fields])

    return doctor
