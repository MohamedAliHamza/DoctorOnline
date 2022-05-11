import pytest

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


client = APIClient()

@pytest.mark.django_db
def test_wrong_email():
    data = {
        "email": "customer@algo.com",
        "password": "12345",
    }

    response = client.post(reverse('login'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Incorrect email or password'


@pytest.mark.django_db
def test_wrong_password(customer):
    data = {
        "email": "customer@algo.com",
        "password": "123456",
    }

    response = client.post(reverse('login'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Incorrect email or password'


@pytest.mark.django_db
def test_login_ok(customer):
    data = {
        "email": "customer@algo.com",
        "password": "12345",
    }

    response = client.post(reverse('login'), data=data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == 'customer@algo.com'
