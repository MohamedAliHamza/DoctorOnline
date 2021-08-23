from .models import Clinic, ClinicDate
from rest_framework import serializers
from user.models import User

class ClinicDateSerializers(serializers.ModelSerializer):
       class Meta:
              model = ClinicDate
              fields = ['day','start_time', 'end_time']


class ClinicSerializers(serializers.ModelSerializer):
       doctor = serializers.StringRelatedField(required=False)
       date = ClinicDateSerializers(many=True)
       class Meta:
              model = Clinic
              fields = ['name', 'price', 'doctor', 'date']

       def create(self, validated_data):
              dates_data = validated_data.pop('date')
              user =  self.context['request'].user
              clinic = Clinic.objects.create(doctor=user, **validated_data)
              for date_data in dates_data:
                     dt = ClinicDate.objects.create(**date_data)
                     clinic.date.add(dt)
              return clinic