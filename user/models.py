from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import PermissionsMixin
from utilities.utility import upload_avatar
from django.db import models


class UserManager(BaseUserManager):
    def create_doctor(self, email, password=None, **extra_fields):
       if not email:
            raise ValueError('Doctor must have an email address')            
       user = self.model(
            email=self.normalize_email(email),
             **extra_fields
       )
       user.set_password(password)
       user.type = User.DOCTOR
       user.save()
       return user

    def create_patient(self, email, password=None, **extra_fields):
       if not email:
            raise ValueError('Patient must have an email address')            
       user = self.model(
            email=self.normalize_email(email),
             **extra_fields
       )
       user.set_password(password)
       user.type = User.PATIENT
       user.save()
       return user

    def create_superuser(self, email, password, **extra_fields):
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_superuser', True)

       if not email:
            raise ValueError('Admin must have an email address')            
       user = self.model(
            email=self.normalize_email(email),
             **extra_fields
       )
       user.set_password(password)
       user.type = User.ADMIN
       user.save()
       return user


class User(AbstractBaseUser, PermissionsMixin):
    DOCTOR = 'DOCTOR'
    PATIENT = 'PATIENT'
    ADMIN = 'ADMIN'
    user_types = [
       (DOCTOR, 'Doctor'),
       (PATIENT, 'Patient'),
       (ADMIN, 'Admin'),
    ]
    type = models.CharField(max_length=15, choices=user_types)  
    email = models.EmailField(max_length=50, blank=True, null=True, unique=True)
    mobile = PhoneNumberField(max_length=11, unique=True, blank=True, null=True, help_text='Contact phone number')                            
    full_name = models.CharField(max_length=25, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.FileField(blank=True, null=True, upload_to=upload_avatar)
    address = models.CharField(max_length=25,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
       verbose_name = 'User'
       verbose_name_plural = 'Users'

    def __str__(self):
       return self.email


class DoctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.DOCTOR)

class PatientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.PATIENT)


class Doctor(User):
    objects = DoctorManager()

    class Meta:
       proxy = True

class Patient(User):
    objects = PatientManager()

    class Meta:
       proxy = True