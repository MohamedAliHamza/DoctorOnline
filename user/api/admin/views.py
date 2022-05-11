from django.db.models import Q

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import CreateAdminSerializer, UpdateAdminSerializer, AdminSerializer
from ..serializers import CustomerSerializer, PasswordSerializer
from ..utils import _create_user, _update_user
from ..permissions import IsSuperuser, IsStaff
from ...models import UserProfile


class CreateAdminApi(APIView):
    ''' Add new staff or superuser, availbale only for superuser '''

    permission_classes = [
        IsAuthenticated,
        IsSuperuser,
        ]

    def post(self, request):
        serializer = CreateAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user_object = _create_user(data['email'], data['name'], data['password'], data['confirm_password'], is_staff=True, is_superuser=data.get('is_superuser'))

        data = AdminSerializer(user_object[1]).data

        return Response(data, status=status.HTTP_201_CREATED)


class UpdateAdminApi(APIView):
    ''' update admin info for superuser '''

    permission_classes = [
        IsAuthenticated,
        IsSuperuser
        ]
    
    def put(self, request):
        serializer = UpdateAdminSerializer(data=request.data)
        password_serializer = None
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if 'password' in request.data or 'confirm_password' in request.data:
            password_serializer = PasswordSerializer(data=request.data)
            password_serializer.is_valid(raise_exception=True)

            data['password'] = password_serializer.validated_data['password']
            data['confirm_password'] = password_serializer.validated_data['confirm_password']

        try:
            profile = UserProfile.objects.select_related('user').get(
                (Q(user__is_staff=True) | Q(user__is_superuser=True)) & 
                Q(id=data.pop('admin_id')))
            user_object = _update_user(request.user, profile, **data)
            data = AdminSerializer(user_object[1]).data 
            return Response(data, status=status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            return Response({'detail':'This admin does not exist'}, status=status.HTTP_404_NOT_FOUND)


class ListAdminApi(APIView, LimitOffsetPagination):

    permission_classes = [
        IsAuthenticated,
        IsSuperuser | IsStaff
        ]

    def get(self, request):

        admins = UserProfile.objects.filter(Q(user__is_superuser=True) | Q(user__is_staff=True)).select_related('user')

        results = self.paginate_queryset(admins, request, view=self)

        serializer = AdminSerializer(results, many=True)

        return self.get_paginated_response(serializer.data)


class ListCustomerApi(APIView, LimitOffsetPagination):

    permission_classes = [
        IsAuthenticated,
        IsSuperuser | IsStaff
        ]

    def get(self, request):

        customers = UserProfile.objects.filter(user__is_customer=True).select_related('user')

        results = self.paginate_queryset(customers, request, view=self)

        serializer = CustomerSerializer(results, many=True)

        return self.get_paginated_response(serializer.data)
