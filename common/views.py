from rest_framework import generics
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from.serializers import AppointmentSerializer, AppointmentCreateSerializer
from .permissions import AppointmentPermission, IsOwnerOrReadOnly


class MethodSerializerView(object):
    '''
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('GET', ): MyModelListViewSerializer,
        ('PUT', 'PATCH'): MyModelCreateUpdateSerializer
    }
    '''
    method_serializer_classes = None

    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
            'Expected view %s should contain method_serializer_classes '
            'to get right serializer class.' %
            (self.__class__.__name__, )
        )
        for methods, serializer_cls in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)


class AppointmentList(MethodSerializerView, generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    method_serializer_classes = {
        ('GET',): AppointmentSerializer,
        ('POST'): AppointmentCreateSerializer
    }

    permission_classes = (IsAuthenticated, AppointmentPermission)


class AppointmentDetail(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()


    method_serializer_classes = {
        ('GET'): AppointmentSerializer,
        ('PUT', 'PATCH'): AppointmentCreateSerializer,

    }

    permission_classes = [IsAuthenticated, AppointmentPermission, IsOwnerOrReadOnly]


