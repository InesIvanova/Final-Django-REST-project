from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS, IsAdminUser

from .models import Doctor


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return obj.user == request.user


class DoctorPermission(BasePermission):

    def has_permission(self, request, view):
        if (request.method == "DELETE" or request.method == "POST") and not request.user.is_superuser:
            return False

        try:
            doctor = Doctor.objects.get(user__pk=request.user.id)
        except Doctor.DoesNotExist:
            doctor = None

        if doctor or request.user.is_superuser:
            return True
        return False
