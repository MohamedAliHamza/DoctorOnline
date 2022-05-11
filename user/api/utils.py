from typing import Optional

from rest_framework import serializers

from ..models import User

from common.utils import _object_exist


def _clean_email(email: str):
    if _object_exist(User, email=email):
            raise serializers.ValidationError({'detail':'This email already exists'})
    ...


def _clean_password_match(password_1: str, password_2: str):
    if password_1 != password_2:
            raise serializers.ValidationError({'detail':'Passwords do not match'})
    ...


def _clean_old_password(user: User, old_password: str):
    if not user.check_password(old_password):
            raise serializers.ValidationError({'detail':'Incorrect Old Password'})
    ...


def _create_user(email: str, password_1: str, password_2: str, **kwargs):
    email = email.lower()
    # Validate
    _clean_email(email)
    _clean_password_match(password_1, password_2)

    # Create
    user = User.objects.create_user( email, password_1, **kwargs)

    return user


def _update_user(user: User, email: Optional[str] = None, password_1: Optional[str] = None, password_2: Optional[str] = None):

    user_fields = []

    # Validate
    if email != None:
        email = email.lower()
        _clean_email(email)
        user_fields.append('email')

    if password_1 != None:
        _clean_old_password(user, password_1)
        user.set_password(password_2)
        user_fields.append('password')

    return user_fields
