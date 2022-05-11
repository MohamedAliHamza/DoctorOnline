import pytest

from django.urls import reverse

from rest_framework import status


@pytest.mark.django_db
def test_get_ok(authenticate_superuser, customer):

    response = authenticate_superuser.get(reverse('customers_list'))

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
