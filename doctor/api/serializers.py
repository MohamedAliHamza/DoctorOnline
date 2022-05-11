from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from user.api.serializers import CreateUserSerializer, UpdateUserSerializer
from common.api.serializers import BaseSerializer
from core import settings


class CreateDoctorSerializer(CreateUserSerializer):
    bio = serializers.CharField(max_length=150)
    fees = serializers.DecimalField(max_digits=5, decimal_places=2)
    phone = PhoneNumberField()
    specialty = serializers.CharField(max_length=60)
    address = serializers.CharField(max_length=60)


class UpdateDoctorSerializer(UpdateUserSerializer):
    bio = serializers.CharField(max_length=150, required=False)
    fees = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    phone = PhoneNumberField(required=False)
    specialty = serializers.CharField(max_length=60, required=False)
    address = serializers.CharField(max_length=60, required=False)
    avatar = serializers.ImageField(required=False)
    background_image = serializers.ImageField(required=False)
    facebook_url = serializers.URLField(required=False)
    twitter_url = serializers.URLField(required=False)
    linkedin_url = serializers.URLField(required=False)
    website_url = serializers.URLField(required=False)


class DoctorSerializer(BaseSerializer):  
    full_name = serializers.CharField(read_only=True)
    bio = serializers.CharField(read_only=True)
    fees = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2)
    phone = PhoneNumberField(read_only=True)
    specialty = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    facebook_url = serializers.URLField(read_only=True)
    twitter_url = serializers.URLField(read_only=True)
    linkedin_url = serializers.URLField(read_only=True)
    website_url = serializers.URLField(read_only=True)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        data['avatar'] = f'{settings.DOMAIN_URL}{instance.avatar.url}'
        data['background_image'] = f'{settings.DOMAIN_URL}{instance.background_image.url}'
        data['email'] = instance.user.email
        data['is_active'] = instance.user.is_active
        data['is_doctor'] = True

        return data
