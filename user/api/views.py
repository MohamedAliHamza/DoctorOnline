from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..models import User
from .serializers import(
    CreateUserSerializer,
    UpdateUserSerializer,
    DetailUserSerializer,
    )
from .exceptions import(
    PasswordNotMatch,
    WrongPassword,
    UserExist, 
    )

from utility.utils import object_exist


class CreatePatientApi(APIView):
    
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        # Fetch the data
        email = data['email'].lower()
        password = data['password']
        confirm_password = data['confirm_password']

        # Check unique email
        if object_exist(User, email=email):
            raise UserExist()

        # Check valid password    
        if password != confirm_password:
            raise PasswordNotMatch()
           
        # Create new patient object if data are valid    
        User.objects.create_user(
            email,
            password,
            is_patient=True,
            )
        return Response(status=status.HTTP_201_CREATED)


class UpdateUserApi(APIView):

    permission_classes = [
        IsAuthenticated,
        ]
    
    def put(self, request):
        serializer = UpdateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        if data: 
            user = request.user
            user_data = {}

            # Fetch the data
            if 'email' in data:
                email = data['email'].lower()
                if object_exist(User, email=email):
                    raise UserExist()
                user.email = email
                user_data['email'] = ''

            if 'old_password' in data or 'new_password' in data:
                old_password = data.get('old_password')
                new_password = data.get('new_password')

                if old_password and not user.check_password(old_password):
                    raise WrongPassword()

                if ((old_password and not new_password) or 
                (not old_password and new_password) or 
                (old_password != new_password)):
                    raise PasswordNotMatch()

                user.set_password(new_password)
                data.pop('old_password')
                data.pop('new_password')
                user_data['password'] = ''
                
            if 'avatar' in data:
                user.avatar = data['avatar']
                user_data['avatar'] = ''

            user.full_name = data.get('full_name')
            user_data['updated_at'] = ''

            # Call the save method to update only a provided data
            user.save(update_fields=[field for field in user_data.keys()])

        return Response(status=status.HTTP_200_OK)


class DetailUserApi(APIView):
    permission_classes = [
        IsAuthenticated,
        ]

    def get(self, request): 
        user = request.user
        user_data = DetailUserSerializer(user).data

        return Response(user_data)
        