import pytest

from django.urls import reverse

from rest_framework import status

from user_controller.user.api.serializers import CustomerSerializer 
from user_controller.user.models import User, UserProfile


@pytest.mark.django_db
def test_get_ok(authenticate_customer):
   
    response = authenticate_customer.get(reverse('detail_user'))

    customer = UserProfile.objects.get(id=1)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == CustomerSerializer(customer).data
