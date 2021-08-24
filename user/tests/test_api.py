from user.models import User, Doctor, Patient
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from rest_framework import status
from django.urls import reverse
import pytest
from user.serializer import UserSerializer, UserUpdateSerializer

client = APIClient()
client2 = APIClient()

# Test -> register -> login"doctor&patient" -> get -> put

@pytest.mark.django_db
class TestRegistration():

       def test_valid_register(self):
              data = {
                     'email':'doctor1@doctoronline.com',
                     'password':'12345', 
                     'type':'DOCTOR',
                     'mobile':'01021546535',
              }
              response = client.post(reverse('register'), data=data)
              assert response.status_code == status.HTTP_201_CREATED

       def test_invalid_register(self):
              data = {
                     'email':'doctor1@doctoronline.com',
                     'password':'123', 
                     'type':'DOCTOR',
                     'mobile':'0102154653544',
              }
              response = client.post(reverse('register'), data=data)
              assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestDoctorLogin():

       @pytest.fixture
       def setup(self):
              User.objects.create_doctor(email="doctor1@doctoronline.com", password="12345")

       def test_valid_login_doctor(self, setup):
              data = {
                     'email':'doctor1@doctoronline.com',
                     'password':'12345', 
              }
              response = client.post(reverse('token_obtain_pair_doctor'), data=data)
              assert response.status_code == status.HTTP_200_OK

       def test_invalid_login_doctor(self, setup):
              data = {
                     'email':'unknowndoctor@doctoronline.com',
                     'password':'12345', 
              }
              response = client.post(reverse('token_obtain_pair_doctor'), data=data)
              assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestPatientLogin():

       @pytest.fixture
       def setup(self):
              User.objects.create_patient(email="patient1@doctoronline.com", password="12345")

       def test_valid_login_patient(self, setup):
              data = {
                     'email':'patient1@doctoronline.com',
                     'password':'12345', 
              }
              response = client.post(reverse('token_obtain_pair_patient'), data=data)
              assert response.status_code == status.HTTP_200_OK

       def test_invalid_login_patient(self, setup):
              data = {
                     'email':'unknownpatient@doctoronline.com',
                     'password':'12345', 
              }
              response = client.post(reverse('token_obtain_pair_patient'), data=data)
              assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestUserGet():

       @pytest.fixture
       def setup(self):
              self.user = User.objects.create_doctor(email="doctor1@doctoronline.com", password="12345")
              data = {
                     'email':'doctor1@doctoronline.com',
                     'password':'12345', 
              }
              response = client.post(reverse('token_obtain_pair_doctor'), data=data)
              self.access_token = response.json()['access']              
              client2.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

       def test_valid_get(self, setup):
              response = client2.get(reverse('info'))
              serializer = UserUpdateSerializer(self.user)
              assert response.status_code == status.HTTP_200_OK
              assert response.data == serializer.data

@pytest.mark.django_db
class TestUserUpdate():

       @pytest.fixture
       def setup(self):
              User.objects.create_doctor(email="doctor1@doctoronline.com", password="12345")
              data = {
                     'email':'doctor1@doctoronline.com',
                     'password':'12345', 
              }
              response = client.post(reverse('token_obtain_pair_doctor'), data=data)
              self.access_token = response.json()['access']              
              client2.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

       def test_valid_update_full_name(self, setup):
              data = {
                     'full_name': 'Mohamed Hamza' 
              }
              response = client2.patch(reverse('update'), data=data)
              assert response.status_code == status.HTTP_200_OK

       def test_valid_update_password(self, setup):
              data = {
                     'old_password': '12345',
                     'new_password': '123456' 
              }
              response = client2.patch(reverse('update'), data=data)
              assert response.status_code == status.HTTP_200_OK

       def test_invalid_update_old_password(self, setup):
              data = {
                     'old_password': '',
                     'new_password': '123456' 
              }
              response = client2.patch(reverse('update'), data=data)
              assert response.status_code == status.HTTP_400_BAD_REQUEST

       def test_invalid_update_new_password(self, setup):
              data = {
                     'old_password': '12345',
                     'new_password': '' 
              }
              response = client2.patch(reverse('update'), data=data)
              assert response.status_code == status.HTTP_400_BAD_REQUEST