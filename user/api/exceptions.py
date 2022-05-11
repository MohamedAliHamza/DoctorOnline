from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework import status


class UserExist(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('This email already exists')


class UserNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('This user does not exists')


class PasswordNotMatch(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Passwords do not match')
    