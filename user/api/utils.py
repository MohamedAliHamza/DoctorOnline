from utility.utils import object_exist

from ..models import User
from .exceptions import(
    PasswordNotMatch,
    WrongPassword,
    UserExist, 
    )


def create_user(email, password, confirm_password, **kwargs):

    # Check unique email
    if object_exist(User, email=email):
        raise UserExist()

    # Check valid password    
    if password != confirm_password:
        raise PasswordNotMatch()

    user = User.objects.create_user(email, password, **kwargs)

    return user


def update_user(user, **kwargs):
    
    if 'email' in kwargs:
        email = kwargs['email'].lower()
        if object_exist(User, email=email):
            raise UserExist()
        user.email = email

    if 'old_password' in kwargs and not user.check_password(kwargs['old_password']):
        raise WrongPassword()

    if 'new_password' in kwargs and not 'old_password' in kwargs:
        raise PasswordNotMatch()

    elif not 'new_password' in kwargs and 'old_password' in kwargs:
        raise PasswordNotMatch()    

    elif 'new_password' and 'old_password' in kwargs:
        user.set_password(kwargs['new_password'])
        kwargs.pop('old_password')
        kwargs.pop('new_password')
        kwargs['password'] = ''
        
    user.avatar = kwargs.get('avatar')
    user.full_name = kwargs.get('full_name')
    kwargs['updated_at'] = ''

    # Call the save method to update only a provided data
    user.save(update_fields=[field for field in kwargs.keys()])

    return user
