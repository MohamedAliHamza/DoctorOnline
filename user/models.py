from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .manager import UserManager

from utility.models import TimeStamp


class User(AbstractBaseUser, PermissionsMixin, TimeStamp):
    email = models.EmailField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='media/users/', default='media/users/default.png')
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'