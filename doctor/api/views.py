from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .utils import create_doctor, update_doctor
from .serializers import(
    CreateDoctorSerializer,
    UpdateDoctorSerializer,
    DoctorSerializer,
    )

from user.api.permissions import IsActive, IsDoctor
from user.api.serializers import PasswordSerializer


class CreateDoctorApi(APIView):
    
    def post(self, request):
        serializer = CreateDoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        doctor_object = create_doctor(data['email'], data['password_1'], data['password_2'], data['full_name'], data['bio'], data['fees'], data['phone'], data['address'], data['specialty'])
 
        # Generate Token
        refresh = RefreshToken.for_user(doctor_object[0])

        data = DoctorSerializer(doctor_object[1]).data
        data['refresh'], data['access'] = str(refresh), str(refresh.access_token)

        return Response(data, status=status.HTTP_201_CREATED)


class UpdateDoctorApi(APIView):

    permission_classes = [
        IsAuthenticated, IsDoctor, IsActive
        ]
    
    def put(self, request):
        serializer = UpdateDoctorSerializer(data=request.data)
        password_serializer = None
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if 'password_1' in request.data or 'password_2' in request.data:
            password_serializer = PasswordSerializer(data=request.data)
            password_serializer.is_valid(raise_exception=True)

            data['password_1'] = password_serializer.validated_data['password_1']
            data['password_2'] = password_serializer.validated_data['password_2']

        company_object = update_doctor(request.user, **data)

        data = DoctorSerializer(company_object).data
        
        return Response(data, status=status.HTTP_200_OK)
