from rest_framework.exceptions import APIException
from rest_framework import status


class UserExist(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'This email already exists'


class UserNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'This user does not exists'


class PasswordNotMatch(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Passwords not matched'


class WrongPassword(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Wrong Password'