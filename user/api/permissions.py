from rest_framework.permissions import BasePermission


denial_message = 'You do not have permission to perform this action'


class IsSuperuser(BasePermission):
    message = denial_message

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsStaff(BasePermission):
    message = denial_message

    def has_permission(self, request, view):
        return request.user.is_staff


class IsPatient(BasePermission):
    message = denial_message

    def has_permission(self, request, view):
        return request.user.is_patient


class IsDoctor(BasePermission):
    message = denial_message

    def has_permission(self, request, view):
        return request.user.is_doctor


