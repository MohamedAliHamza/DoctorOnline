from rest_framework import generics
from .models import Reservation
from .serializer import ReservationSerializer
from utility.permissions import IsDoctor, IsOwnerReservation, IsPatient
from rest_framework.permissions import IsAuthenticated
from user.models import User
from specialty.models import Clinic

class CreateReservationView(generics.CreateAPIView):
       serializer_class = ReservationSerializer
       permission_classes = [IsAuthenticated, IsPatient]

class ListReservationView(generics.ListAPIView):
       serializer_class = ReservationSerializer
       permission_classes = [IsAuthenticated]

       def get_queryset(self):
              user = self.request.user
              if user.type == User.PATIENT:
                     return user.patient_reservation.all()
              if user.type == User.DOCTOR:
                     return user.doctor_reservation.all()

class UpdateDeleteReservationView(generics.RetrieveUpdateDestroyAPIView):
       serializer_class = ReservationSerializer
       permission_classes = [IsAuthenticated, IsOwnerReservation]
       queryset = Reservation.objects.all()