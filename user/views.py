from .serializer import UserSerializer, UserUpdateSerializer, DoctorTokenSerializer, PatientTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User

class UserRegistrationView(generics.CreateAPIView):
    ''' Register User AS A PATIENT Or DOCTOR '''
    serializer_class = UserSerializer


class DoctorTokenView(TokenObtainPairView):
    ''' Login Doctor'''
    serializer_class = DoctorTokenSerializer

class PatientTokenView(TokenObtainPairView):
    ''' Login Patient'''
    serializer_class = PatientTokenSerializer

class UserView(generics.RetrieveAPIView):
    ''' Get User Info'''
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]


class UpdateUserView(generics.UpdateAPIView):
    ''' Update User Info'''
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
