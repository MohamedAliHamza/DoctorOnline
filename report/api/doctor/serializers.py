from rest_framework import serializers

from patient.api.serializers import PatientSerializer
from common.api.serializers import BaseSerializer


class CreateReportSerializer(serializers.Serializer):
    patient_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1000)


class ListReportSerializer(BaseSerializer):  
    content = serializers.CharField(read_only=True)
    patient = PatientSerializer(read_only=True)
