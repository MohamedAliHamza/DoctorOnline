import pytest

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from doctor.models import Doctor
from user.models import User


client = APIClient()

@pytest.mark.django_db
def test_email_exist(doctor):

    data = {
        "email": "doctor@test.com",
        "full_name": "Doctor Name",
        "password_1": "12345",
        "password_2": "12345",
        "phone": "+201021546535",
        "fees": 50,
        "bio": "Bio",
        "address": "Address",
        "specialty": "Specialty",
    }

    response = client.post(reverse('doctor:create'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'This email already exists'


@pytest.mark.django_db
def test_password_not_match():

    data = {
        "email": "doctor@test.com",
        "full_name": "Doctor Name",
        "password_1": "12345",
        "password_2": "123456",
        "phone": "+201021546535",
        "fees": 50,
        "bio": "Bio",
        "address": "Address",
        "specialty": "Specialty",
    }

    response = client.post(reverse('doctor:create'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Passwords do not match'


@pytest.mark.django_db
def test_create_ok():

    data = {
        "email": "doctor@test.com",
        "full_name": "Doctor Name",
        "password_1": "12345",
        "password_2": "12345",
        "phone": "+201021546535",
        "fees": 50,
        "bio": "Bio",
        "address": "Address",
        "specialty": "Specialty",
    }

    assert Doctor.objects.count() == 0
    assert User.objects.count() == 0

    response = client.post(reverse('doctor:create'), data=data)

    user = User.objects.get(id=1)

    assert response.status_code == status.HTTP_201_CREATED
    assert Doctor.objects.count() == 1
    assert User.objects.count() == 1
    assert user.email == 'doctor@test.com'
    assert user.is_doctor == True
    assert user.doctor.full_name == 'Doctor Name'
