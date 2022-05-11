from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .utils import create_patient, update_patient
from .serializers import(
    CreatePatientSerializer,
    UpdatePatientSerializer,
    PatientSerializer,
    )

from user.api.permissions import IsActive, IsPatient
from user.api.serializers import PasswordSerializer


class CreatePatientApi(APIView):
    
    def post(self, request):
        serializer = CreatePatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        patient_object = create_patient(data['email'], data['password_1'], data['password_2'], data['full_name'], data['age'], data['gender'], data.get('length'), data.get('weight'))
 
        # Generate Token
        refresh = RefreshToken.for_user(patient_object[0])

        data = PatientSerializer(patient_object[1]).data
        data['refresh'], data['access'] = str(refresh), str(refresh.access_token)

        return Response(data, status=status.HTTP_201_CREATED)


class UpdatePatientApi(APIView):

    permission_classes = [
        IsAuthenticated, IsPatient, IsActive
        ]
    
    def put(self, request):
        serializer = UpdatePatientSerializer(data=request.data)
        password_serializer = None
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if 'password_1' in request.data or 'password_2' in request.data:
            password_serializer = PasswordSerializer(data=request.data)
            password_serializer.is_valid(raise_exception=True)

            data['password_1'] = password_serializer.validated_data['password_1']
            data['password_2'] = password_serializer.validated_data['password_2']

        patient_object = update_patient(request.user, **data)

        data = PatientSerializer(patient_object).data
        
        return Response(data, status=status.HTTP_200_OK)
