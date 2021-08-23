from rest_framework.permissions import IsAuthenticated
from .serializer import ClinicSerializers
from .models import Clinic, ClinicDate
from rest_framework import generics
from .permissions import IsDoctor

class ClinicListView(generics.ListAPIView):
       ''' All Available Clinics '''
       queryset = Clinic.objects.all()
       serializer_class = ClinicSerializers

# class ClinicDoctorosListView(generics.ListAPIView):
#        ''' All Clinics That Belong To Specific Doctor '''
#        queryset = Clinic.objects.all()
#        serializer_class = ClinicSerializers


class ClinicCreateView(generics.CreateAPIView):
       ''' Create Clinics Only For Doctors '''
       serializer_class = ClinicSerializers
       #permission_classes = [IsAuthenticated, IsDoctor]

class ClinicUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
       ''' Update Clinics Only For Doctors '''
       serializer_class = ClinicSerializers
       def get_queryset(self):
              user = self.request.user
              return user.doctor_clinic.all() # related_name from models.py file
       permission_classes = [IsAuthenticated, IsDoctor]