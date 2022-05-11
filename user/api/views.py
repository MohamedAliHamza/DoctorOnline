from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginUserSerializer


# class DetailUserApi(APIView):

#     permission_classes = [
#         IsAuthenticated,
#         ]

#     def get(self, request): 
#         user = request.user
#         data = None
#         if user.is_customer:
#             data = CompanySerializer(user.company).data
#         else:
#             ...
#             # data = AdminSerializer(user.profile).data

#         return Response(data, status=status.HTTP_200_OK)   


class LoginUserApi(APIView):

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(email=request.data['email'].lower(), password=request.data['password'])
        if not user:
            raise serializers.ValidationError({'detail':'Incorrect email or password'})

        # Generate Token
        refresh = RefreshToken.for_user(user)

        data = None
        # if user.is_company:
        #     data = CompanySerializer(user.company).data
        # else:
        #     ...
        #     # data = AdminSerializer(user.profile).data

        # data['refresh'], data['access'] = str(refresh), str(refresh.access_token)    

        return Response(data, status=status.HTTP_200_OK)
