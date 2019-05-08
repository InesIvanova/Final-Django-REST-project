from rest_framework import views, generics
from rest_framework.permissions import IsAuthenticated

from .models import Doctor
from .serializers import DoctorSerializer
from .permissions import DoctorPermission, IsOwnerOrReadOnly


class DoctorList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        specialty = self.request.query_params.get('specialty', None)

        if specialty is not None:
            queryset = Doctor.objects.filter(specialty=specialty)
            return queryset

        queryset = Doctor.objects.all()
        return queryset

    permission_classes = [IsAuthenticated, DoctorPermission]


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    permission_classes = [IsAuthenticated, DoctorPermission, IsOwnerOrReadOnly]




