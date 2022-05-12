from ...models import Report

from patient.api.utils import clean_patient_id
from doctor.models import Doctor


def create_report(doctor: Doctor, patient_id: int, content: str):

    clean_patient_id(patient_id)

    report = Report.objects.create(
        doctor=doctor,
        patient_id=patient_id,
        content=content
        )

    return report
