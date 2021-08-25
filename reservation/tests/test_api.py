from clinic.serializers import ClinicSerializers
from user.models import User, Doctor, Patient
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from rest_framework import status
from clinic.models import Clinic
from django.urls import reverse
import pytest

client = APIClient()
client2 = APIClient()
client3 = APIClient()

# Test -> 

@pytest.mark.django_db
class TestReservation:

       @pytest.fixture
       def setup(self):
              User.objects.create_patient(email="patient1@doctoronline.com", password="12345")
              data = {
                     'email':'patient1@doctoronline.com',
                     'password':'12345', 
              }
              response = client.post(reverse('token_obtain_pair_patient'), data=data)
              self.access_token = response.json()['access']       
              client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

       def test_valid_create_reservation(self, setup):
              pass