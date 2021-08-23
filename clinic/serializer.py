from .models import Clinic, ClinicDate
from rest_framework import serializers
from user.models import User

class ClinicDateSerializers(serializers.ModelSerializer):
       #clinic = serializers.PrimaryKeyRelatedField(many=True, read_only=True)       
       class Meta:
              model = ClinicDate
              fields = ['day','start_time', 'end_time']

class ClinicSerializers(serializers.ModelSerializer):
       #doctor = serializers.StringRelatedField()
       date = ClinicDateSerializers(many=True)
       #date = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
       class Meta:
              model = Clinic
              fields = ['name', 'price', 'doctor', 'date']

       def create(self, validated_data):
              user =  self.context['request'].user
              return Clinic.objects.create(**validated_data, doctor=user)       
