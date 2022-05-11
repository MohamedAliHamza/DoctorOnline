from rest_framework.exceptions import APIException
from rest_framework import status


class SpecialtyExist(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'This specialty title already exists'


class SpecialtyNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'This specialty does not exists'


