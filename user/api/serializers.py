from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):
    password_1= serializers.CharField(write_only=True, min_length=5)
    password_2 = serializers.CharField(write_only=True, min_length=5)


class CreateUserSerializer(PasswordSerializer):
    email = serializers.EmailField(max_length=150)
    full_name = serializers.CharField(max_length=150)


class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=150, required=False)
    full_name = serializers.CharField(max_length=150, required=False)
    

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(write_only=True)
    