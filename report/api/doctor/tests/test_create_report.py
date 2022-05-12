import pytest

from django.urls import reverse

from rest_framework import status

from report.models import Report


@pytest.mark.django_db
def test_patient_id_not_exist(authenticate_doctor):
    data = {
        "patient_id": 2,
        "content": "Report Content", 
    }

    response = authenticate_doctor.post(reverse('doctor_report:create'), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['detail'] == 'Patient is not exist'


@pytest.mark.django_db
def test_create_ok(authenticate_doctor, patient):
    data = {
        "patient_id": patient.id,
        "content": "Report Content", 
    }

    assert Report.objects.count() == 0

    response = authenticate_doctor.post(reverse('doctor_report:create'), data=data)
    
    assert response.status_code == status.HTTP_201_CREATED
    assert Report.objects.count() == 1
    assert Report.objects.get(id=1).content == 'Report Content'
