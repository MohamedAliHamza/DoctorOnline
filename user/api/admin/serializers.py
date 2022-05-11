from rest_framework import serializers

from ..serializers import CreateUserSerializer, UpdateUserSerializer

from core import settings


class CreateAdminSerializer(CreateUserSerializer):
    is_superuser = serializers.BooleanField(required=False)


class UpdateAdminSerializer(UpdateUserSerializer):
    admin_id = serializers.IntegerField()
    is_superuser = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)


class AdminSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    avatar = serializers.ImageField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['avatar'] = f'{settings.DOMAIN_URL}{instance.avatar.url}'
        data['email'] = instance.user.email
        data['is_staff'] = instance.user.is_staff
        data['is_superuser'] = instance.user.is_superuser

        return data
