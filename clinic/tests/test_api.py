from user.models import User, Doctor, Patient
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from rest_framework import status
from django.urls import reverse
import pytest
from clinic.serializers import ClinicSerializers
from clinic.models import Clinic

client = APIClient()
client2 = APIClient()
client3 = APIClient()

# Test -> add clinic -> get all clinics -> update clinic -> delete clinic -> get doctor's clinic

@pytest.mark.django_db
class TestClinic:

       @pytest.fixture
       def setup(self):
              User.objects.create_doctor(email="doctor1@doctoronline.com", password="12345")
              data = {
                     'email':'doctor1@doctoronline.com',
                     'password':'12345', 
              }
              response = client.post(reverse('token_obtain_pair_doctor'), data=data)
              self.access_token = response.json()['access']       
              client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

       def test_valid_create_clinic(self, setup):
              data = {
                     "name": "Clinic 1",
                     "price": 1000,
                     "date": [
                     {
                     "day": "WENESDAY",
                     "start_time": "2021-08-24T21:21:17.960Z",
                     "end_time": "2021-08-24T21:21:17.960Z"
                     }
                     ]
              } 
              response = client.post(reverse('clinic-create'), data=data)
              assert Clinic.objects.all().count() == 1
              # clinic = Clinic.objects.get(id=1)
              # DT = clinic.date.all().count()
              # assert DT == 1
              # assert DT[0].day == "SATURDAY"
              assert response.status_code == status.HTTP_201_CREATED  

              response = client.get(reverse('list-clinic'))
              assert response.status_code == status.HTTP_200_OK

       # def test_get_all_clinic(self, setup):
       #        response = client.get(reverse('list-clinic'))
       #        assert response.status_code == status.HTTP_200_OK
