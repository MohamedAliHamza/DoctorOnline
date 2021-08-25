from utilities.permissions import IsDoctor, IsOwner, IsPatient, IsOwnerClinic, IsOwner
from rest_framework.permissions import IsAuthenticated
from .serializers import ClinicSerializers
from .models import Clinic, ClinicDate
from rest_framework import generics

class ClinicListView(generics.ListAPIView):
       ''' All Available Clinics '''
       queryset = Clinic.objects.all()
       serializer_class = ClinicSerializers

class ClinicDoctorosListView(generics.ListAPIView):
       ''' All Clinics That Belong To Specific Doctor '''
       def get_queryset(self):
              user = self.request.user
              return user.doctor_clinic.all()
       serializer_class = ClinicSerializers
       permission_classes = [IsAuthenticated, IsOwner]


class ClinicCreateView(generics.CreateAPIView):
       ''' Create Clinics Only For Doctors '''
       serializer_class = ClinicSerializers
       permission_classes = [IsAuthenticated, IsDoctor]


class ClinicUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
       ''' Update Clinics Only For Doctors '''
       serializer_class = ClinicSerializers
       queryset = Clinic.objects.all()
       permission_classes = [IsAuthenticated, IsOwnerClinic]