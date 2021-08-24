from rest_framework.permissions import BasePermission
from user.models import User

class IsDoctor(BasePermission):
    message = "Only doctors can add clinics"

    def has_permission(self, request, view):
        return request.user.type == User.DOCTOR

class IsPatient(BasePermission):
    message = "Only patient can add reservation"

    def has_permission(self, request, view):
        return request.user.type == User.PATIENT

class IsOwner(BasePermission):
    message = "You do not have access to this page"

    def has_object_permission(self, request, view, obj):
        return obj.doctor == request.user

class IsOwnerReservation(BasePermission):
    message = "You do not have access to this page"

    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user

class IsOwnerClinic(BasePermission):
    message = "You do not have access to this page"

    def has_object_permission(self, request, view, obj):
        return obj.doctor == request.user
