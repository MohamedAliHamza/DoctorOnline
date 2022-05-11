import pytest

from django.urls import reverse

from rest_framework import status

from user_controller.user.models import User, UserProfile


@pytest.mark.django_db
def test_admin_id_not_exist(authenticate_superuser):
    data = {
        "admin_id": 2,
        "email": "superuser@algo.com",
    }

    response = authenticate_superuser.put(reverse('update_admin'), data=data)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['detail'] == 'This admin does not exist'


@pytest.mark.django_db
def test_email_exist(authenticate_superuser, staffuser):
    data = {
        "admin_id": 2,
        "email": "superuser@algo.com",
    }

    response = authenticate_superuser.put(reverse('update_admin'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'This email already exists'


@pytest.mark.django_db
def test_password_not_match(authenticate_superuser, staffuser):
    data = {
        "admin_id": 2,
        "email": "newstaffuser@algo.com",
        "password": "123456",
        "confirm_password": "12345",
    }

    response = authenticate_superuser.put(reverse('update_admin'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Passwords do not match'


@pytest.mark.django_db
def test_update_ok(authenticate_superuser, staffuser):
    data = {
        "admin_id": 2,
        "email": "newstaffuser@algo.com",
        "password": "123456",
        "confirm_password": "123456",
        "name": "New Name",
        "is_superuser": True,
        "is_active": False
    }

    response = authenticate_superuser.put(reverse('update_admin'), data=data)

    user = User.objects.get(email='newstaffuser@algo.com')

    assert response.status_code == status.HTTP_200_OK
    assert user.is_active == False
    assert user.is_superuser == True
    assert UserProfile.objects.get(id=2).name == 'New Name'
