from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..serializers import CreateUserSerializer, DetailUserSerializer
from ..permissions import IsSuperuser, IsStaff
from ..utils import create_user
from ...models import User


class CreateAdminApi(APIView):
    ''' Add new admin user endpoint, availbale only for admin user '''

    permission_classes = [
        IsAuthenticated,
        IsSuperuser | IsStaff
        ]

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        create_user(
            data['email'].lower(),
            data['password'],
            data['confirm_password'],
            full_name=data['full_name'],
            is_staff=True,
            )
       

        return Response(status=status.HTTP_201_CREATED)


class CreateDoctorApi(APIView):
    ''' Add new doctor endpoint, availbale only for admin user '''

    permission_classes = [
        IsAuthenticated,
        IsSuperuser | IsStaff
        ]

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        create_user(
            data['email'].lower(),
            data['password'],
            data['confirm_password'],
            full_name=data['full_name'],
            is_doctor=True,
            )

        return Response(status=status.HTTP_201_CREATED)


class ListAdminApi(APIView):
    ''' List admin endpoint for admin '''

    permission_classes = [
        IsAuthenticated,
        IsSuperuser | IsStaff
        ]

    def get(self, request):

        admins = User.objects.filter(Q(is_superuser=True) | Q(is_staff=True))

        admins_data = DetailUserSerializer(admins, many=True).data

        return Response(admins_data)


class ListPatientApi(APIView):
    ''' List patients endpoint for admin '''

    permission_classes = [
        IsAuthenticated,
        IsSuperuser | IsStaff
        ]

    def get(self, request):

        patients = User.objects.filter(is_patient=True)

        patients_data = DetailUserSerializer(patients, many=True).data

        return Response(patients_data)


class ListDoctorApi(APIView):
    ''' List doctors endpoint for admin '''

    permission_classes = [
        IsAuthenticated,
        IsSuperuser | IsStaff
        ]

    def get(self, request):

        doctors = User.objects.filter(is_doctor=True)

        doctors_data = DetailUserSerializer(doctors, many=True).data

        return Response(doctors_data)

