from clinic.serializers import ClinicSerializers
from django.shortcuts import get_object_or_404
from user.serializer import UserSerializer
from rest_framework import serializers
from clinic.models import Clinic
from .models import Reservation
from user.models import User
from utilities.utility import choice_day

class ReservationSerializer(serializers.Serializer):
       patient = serializers.StringRelatedField(read_only=True)
       doctor = serializers.StringRelatedField(read_only=True)
       clinic = serializers.StringRelatedField(read_only=True)
       clinic_id = serializers.IntegerField(required=True, write_only=True)
       day = serializers.ChoiceField(choices=choice_day, required=True)
       start_time = serializers.DateTimeField(required=True)

       def create(self, validated_data):
              patient =  self.context['request'].user
              clinic_id = validated_data.pop('clinic_id')
              clinic = get_object_or_404(Clinic, id=clinic_id)
              reservation = Reservation.objects.create(clinic=clinic,patient=patient, doctor=clinic.doctor, **validated_data)
              return reservation

       def update(self, instance, validated_data):
              instance.day = validated_data.get('day', instance.day)
              instance.start_time = validated_data.get('start_time', instance.start_time)       
              instance.save()
              return instance