import pytest

from django.urls import reverse

from rest_framework import status

from user.models import User


@pytest.mark.django_db
def test_email_exist(authenticate_patient):
    data = {
        "email": "patient@test.com",
    }

    response = authenticate_patient.put(reverse('patient:update'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'This email already exists'


@pytest.mark.django_db
def test_wrong_old_password(authenticate_patient):
    data = {
        "password_1": 53123,
        "password_2": 53123,
    }

    response = authenticate_patient.put(reverse('patient:update'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Incorrect Old Password'


@pytest.mark.django_db
def test_update_ok(authenticate_patient):
    data = {
        "email": "newpatient@test.com",
        "full_name": "New Name", 
        "gender": 1,
        "age": 24,
        "length": 190,
        "weight": 80,
        "password_1": "12345",
        "password_2": "1234567",        
    }

    response = authenticate_patient.put(reverse('patient:update'), data=data)
    
    user = User.objects.get(id=1)

    assert response.status_code == status.HTTP_200_OK
    assert user.email == 'newpatient@test.com'
    assert user.patient.full_name == 'New Name'
    assert user.patient.gender == 1
    assert user.patient.length == 190
    assert user.patient.weight == 80
    assert user.check_password(1234567) == True
