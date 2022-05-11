import pytest

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from patient.models import Patient
from user.models import User


client = APIClient()

@pytest.mark.django_db
def test_email_exist(patient):

    data = {
        "email": "patient@test.com",
        "full_name": "Patient Name",
        "password_1": "12345",
        "password_2": "12345",
        "gender": 0,
        "age": 22
    }

    response = client.post(reverse('patient:create'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'This email already exists'


@pytest.mark.django_db
def test_password_not_match():

    data = {
        "email": "patient@test.com",
        "full_name": "Patient Name",
        "password_1": "12345",
        "password_2": "123456",
        "gender": 0,
        "age": 22
    }

    response = client.post(reverse('patient:create'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Passwords do not match'


@pytest.mark.django_db
def test_create_ok():

    data = {
        "email": "patient@test.com",
        "full_name": "Patient Name",
        "password_1": "12345",
        "password_2": "12345",
        "gender": 0,
        "age": 22,
        "length": 140,
        "weight": 70
    }

    assert Patient.objects.count() == 0
    assert User.objects.count() == 0

    response = client.post(reverse('patient:create'), data=data)

    user = User.objects.get(id=1)

    assert response.status_code == status.HTTP_201_CREATED
    assert Patient.objects.count() == 1
    assert User.objects.count() == 1
    assert user.email == 'patient@test.com'
    assert user.is_patient == True
    assert user.patient.full_name == 'Patient Name'
    assert user.patient.length == 140
