from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import CreateUserSerializer, UpdateUserSerializer, DetailUserSerializer
from .utils import create_user, update_user


class CreatePatientApi(APIView):
    
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        create_user(
            data['email'].lower(),
            data['password'],
            data['confirm_password'],
            full_name=data['full_name'],
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
            update_user(request.user, **data)

        return Response(status=status.HTTP_200_OK)


class DetailUserApi(APIView):
    permission_classes = [
        IsAuthenticated,
        ]

    def get(self, request): 
        user = request.user
        user_data = DetailUserSerializer(user).data

        return Response(user_data)
        