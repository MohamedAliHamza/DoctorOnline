from .models import Clinic, ClinicDate
from rest_framework import serializers
from user.models import User

class ClinicDateSerializers(serializers.ModelSerializer):
       class Meta:
              model = ClinicDate
              fields = ['day','start_time', 'end_time']


class ClinicSerializers(serializers.ModelSerializer):
       doctor = serializers.StringRelatedField(required=False)
       date = ClinicDateSerializers(many=True, required=False)
       class Meta:
              model = Clinic 
              fields = ['name', 'price', 'doctor', 'date']

       def create(self, validated_data):
              dates_data = None
              if 'date' in validated_data:
                  dates_data = validated_data.pop('date')
              user =  self.context['request'].user
              clinic = Clinic.objects.create(doctor=user, **validated_data)
              if dates_data != None:
                 for date_data in dates_data:
                     dt = ClinicDate.objects.create(**date_data)
                     clinic.date.add(dt)
                     clinic.save()
              return clinic

       def update(self, instance, validated_data):
              instance.name = validated_data.get('name', instance.name)
              instance.price = validated_data.get('price', instance.price)

              if 'date' in validated_data: 
                     nested_serializer = validated_data.pop('date')
                     # print(nested_serializer[0]['day'])

              instance.save()
              return instance      