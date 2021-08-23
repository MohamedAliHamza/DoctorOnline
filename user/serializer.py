from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
       ''' Register User Serializer ''' 
       email = serializers.EmailField(required=True,max_length=50)
       password = serializers.CharField(min_length=5, write_only=True, required=True)
       type = serializers.ChoiceField(choices=User.user_types) 
       mobile = serializers.CharField(max_length=11, required=False)
       full_name = serializers.CharField(max_length=11, required=False)
 
       def create(self, validated_data):
              password = validated_data.pop('password', None)
              type = validated_data.pop('type', None)

              if type == User.DOCTOR:
                     user = User.objects.create_doctor(**validated_data)
                     user.set_password(password)
                     user.save()
                     return user

              if type == User.PATIENT:
                     user = User.objects.create_patient(**validated_data)
                     user.set_password(password)
                     user.save()
                     return user

class UserUpdateSerializer(serializers.Serializer):
       ''' Update User Serializer ''' 
       email = serializers.EmailField(max_length=50,required=False)
       old_password = serializers.CharField(write_only=True, required=False)
       new_password = serializers.CharField(min_length=5, write_only=True, required=False)
       mobile = serializers.CharField(max_length=11, required=False)
       full_name = serializers.CharField(max_length=11, required=False)

       def validate(self, attrs):
              user = self.context['request'].user
              old_password = attrs.get('old_password', None)
              new_password = attrs.get('new_password', None)
              if old_password != None and new_password == None:
                     raise serializers.ValidationError({"detail":"You need to enter the new password!"})
              if old_password == None and new_password != None:
                     raise serializers.ValidationError({"detail":"You need to enter the old password!"})        
              if old_password != None and not user.check_password(old_password):
                     raise serializers.ValidationError({"detail":"Your old password  was entered incorrectly. Please enter it again!"})                        
              return attrs    
       def update(self, instance, validated_data):
              instance.email = validated_data.get('email', instance.email)
              instance.mobile = validated_data.get('mobile', instance.mobile)
              instance.full_name = validated_data.get('full_name', instance.full_name)
              instance.save()
              return instance       

       def save(self, **kwargs):
              password = self.validated_data['new_password']
              user = self.context['request'].user
              user.set_password(password)
              user.save()
              return user
              
class DoctorTokenSerializer(TokenObtainPairSerializer):
    ''' Token Doctor Serializer ''' 
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.type != User.DOCTOR:
              raise serializers.ValidationError({"detail":"You are not a doctor"})    
       return token

class PatientTokenSerializer(TokenObtainPairSerializer):
    ''' Token Patient Serializer ''' 
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.type != User.PATIENT:
              raise serializers.ValidationError({"detail":"You are not a patient"})    
       return token