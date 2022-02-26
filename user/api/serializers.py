from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
       email = serializers.EmailField(max_length=150)
       password = serializers.CharField(min_length=5, write_only=True, required=True)
       confirm_password = serializers.CharField(min_length=5, write_only=True, required=True)
       full_name = serializers.CharField(max_length=255)
 

class UpdateUserSerializer(serializers.Serializer):
       email = serializers.EmailField(max_length=150,required=False)
       old_password = serializers.CharField(write_only=True, required=False)
       new_password = serializers.CharField(min_length=5, write_only=True, required=False)
       full_name = serializers.CharField(max_length=255, required=False)
       avatar = serializers.ImageField(required=False)


class DetailUserSerializer(serializers.Serializer):
       id = serializers.IntegerField(read_only=True)
       email = serializers.EmailField(read_only=True)
       full_name = serializers.CharField(read_only=True)
       avatar = serializers.ImageField(read_only=True)
