import pytest

from django.urls import reverse

from rest_framework import status

from user.models import User


@pytest.mark.django_db
def test_email_exist(authenticate_doctor):
    data = {
        "email": "doctor@test.com",
    }

    response = authenticate_doctor.put(reverse('doctor:update'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'This email already exists'


@pytest.mark.django_db
def test_wrong_old_password(authenticate_doctor):
    data = {
        "password_1": 53123,
        "password_2": 53123,
    }

    response = authenticate_doctor.put(reverse('doctor:update'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Incorrect Old Password'


@pytest.mark.django_db
def test_update_ok(authenticate_doctor):
    data = {
        "email": "newdoctor@test.com",
        "full_name": "New Name", 
        "bio": "New Bio",
        "website_url": "https://github.com/MohamedAliHamza",
        "password_1": "12345",
        "password_2": "1234567",        
    }

    response = authenticate_doctor.put(reverse('doctor:update'), data=data)
    
    user = User.objects.get(id=1)

    assert response.status_code == status.HTTP_200_OK
    assert user.email == 'newdoctor@test.com'
    assert user.doctor.full_name == 'New Name'
    assert user.doctor.bio == 'New Bio'
    assert user.doctor.website_url == 'https://github.com/MohamedAliHamza'
    assert user.check_password(1234567) == True
