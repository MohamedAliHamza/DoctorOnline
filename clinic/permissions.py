from rest_framework.permissions import BasePermission
from user.models import User

class IsDoctor(BasePermission):
    message = "You do not have access to this page"

    def has_object_permission(self, request, view, obj):
       #return obj.client == request.user
       return request.user.type == User.DOCTOR
