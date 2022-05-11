from rest_framework import serializers

from ..constants import GENDER_CHOICES

from user.api.serializers import CreateUserSerializer, UpdateUserSerializer
from common.api.serializers import BaseSerializer
from core import settings


class CreatePatientSerializer(CreateUserSerializer):
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    length = serializers.FloatField(required=False)
    weight = serializers.FloatField(required=False)


class UpdatePatientSerializer(UpdateUserSerializer):
    age = serializers.IntegerField(required=False)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, required=False)
    length = serializers.FloatField(required=False)
    weight = serializers.FloatField(required=False)    
    avatar = serializers.ImageField(required=False)


class PatientSerializer(BaseSerializer):  
    full_name = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    length = serializers.FloatField(read_only=True)
    weight = serializers.FloatField(read_only=True)    
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        data['avatar'] = f'{settings.DOMAIN_URL}{instance.avatar.url}'
        data['gender'] = instance.get_gender_display()
        data['email'] = instance.user.email
        data['is_active'] = instance.user.is_active
        data['is_patient'] = True

        return data
