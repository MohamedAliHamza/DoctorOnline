import pytest

from django.urls import reverse

from rest_framework import status

from user_controller.user.models import User


@pytest.mark.django_db
def test_email_exist(authenticate_superuser):
    data = {
        "email": "superuser@algo.com",
        "name": "Test Admin", 
        "password": "12345",
        "confirm_password": "12345",
    }

    response = authenticate_superuser.post(reverse('create_admin'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'This email already exists'


@pytest.mark.django_db
def test_password_not_match(authenticate_superuser):
    data = {
        "email": "staffuser@algo.com",
        "name": "Test Admin", 
        "password": "123456",
        "confirm_password": "12345",
    }

    response = authenticate_superuser.post(reverse('create_admin'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Passwords do not match'


@pytest.mark.django_db
def test_create_staff_user_ok(authenticate_superuser):
    data = {
        "email": "staffuser@algo.com",
        "name": "Test Admin", 
        "password": "12345",
        "confirm_password": "12345",
    }

    response = authenticate_superuser.post(reverse('create_admin'), data=data)

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.get(email='staffuser@algo.com').is_staff == True
    assert User.objects.get(email='staffuser@algo.com').is_superuser == False


@pytest.mark.django_db
def test_create_superuser_ok(authenticate_superuser):
    data = {
        "email": "superuser2@algo.com",
        "name": "Test Admin", 
        "password": "12345",
        "confirm_password": "12345",
        "is_superuser": 1
    }

    response = authenticate_superuser.post(reverse('create_admin'), data=data)

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.get(email='superuser2@algo.com').is_staff == True
    assert User.objects.get(email='superuser2@algo.com').is_superuser == True

