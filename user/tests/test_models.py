from user.models import User, Doctor, Patient
import pytest

@pytest.mark.django_db
class TestDoctor():

       @pytest.fixture
       def setup(self):
              User.objects.create_doctor(email="doctor1@doctoronline.com", password="12345")
              User.objects.create_doctor(email="doctor2@doctoronline.com", password="12345")
              User.objects.create_doctor(email="doctor3@doctoronline.com", password="12345")
           

       def test_create_doctor(self, setup):
              assert Doctor.objects.all().count() == 3
              assert Doctor.objects.get(id=3).email == "doctor3@doctoronline.com"


@pytest.mark.django_db
class TestPatient():

       @pytest.fixture
       def setup(self):
              User.objects.create_patient(email="patient1@doctoronline.com", password="12345")
              User.objects.create_patient(email="patient2@doctoronline.com", password="12345")
              User.objects.create_patient(email="patient3@doctoronline.com", password="12345")
           

       def test_create_patient(self, setup):
              assert Patient.objects.all().count() == 3
              assert Patient.objects.get(id=2).email != "patient3@example.com"