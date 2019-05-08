from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Patient


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return obj.patient.user == request.user and obj.status == 'P'


class AppointmentPermission(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True

        patient = Patient.objects.filter(user__pk=request.user.id).exists()

        if patient or (request.user.is_superuser and not request.method == 'POST'):
            return True
        return False