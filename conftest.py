import pytest

from rest_framework.test import APIClient

from patient.models import Patient
from doctor.models import Doctor
from user.models import User



@pytest.fixture
def doctor():
    user = User.objects.create_user(
        'doctor@test.com', 
        '12345',
        is_doctor=True,
        )
    doctor = Doctor.objects.create(
        user=user,
        full_name='Doctor Name', 
        bio='Bio',
        fees=40,
        phone='+201021546535',
        address='Egypt',
        specialty='Heart',
        )

    return doctor


@pytest.fixture
def authenticate_doctor(doctor):

    user = User.objects.get(email='doctor@test.com')
    client = APIClient()
    client.force_authenticate(user=user)

    return client


@pytest.fixture
def patient():
    user = User.objects.create_user(
        'patient@test.com', 
        '12345',
        is_patient=True,
        )
    patient = Patient.objects.create(
        user=user,
        full_name='Patient Name', 
        age=22,
        gender=0
        )

    return patient


@pytest.fixture
def authenticate_patient(patient):

    user = User.objects.get(email='patient@test.com')
    client = APIClient()
    client.force_authenticate(user=user)

    return client


# @pytest.fixture
# def superuser():
#     user = User.objects.create_user(
#         'superuser@algo.com', 
#         '12345',
#         is_superuser=True,      
#         )
#     superuser = UserProfile.objects.create(
#         user=user,
#         name='Mohamed', 
#         )

#     return superuser


# @pytest.fixture
# def authenticate_superuser(superuser):

#     user = User.objects.get(email='superuser@algo.com')
#     client = APIClient()
#     client.force_authenticate(user=user)

#     return client


# @pytest.fixture
# def staffuser():
#     user = User.objects.create_user(
#         'staffuser@algo.com', 
#         '12345',
#         is_staff=True,      
#         )
#     staffuser = UserProfile.objects.create(
#         user=user,
#         name='Mohamed', 
#         )

#     return staffuser