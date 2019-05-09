from rest_framework import views, generics, response, status
from rest_framework.permissions import IsAuthenticated

from .models import Doctor, Contact
from .serializers import DoctorSerializer, ContactSerializer
from .permissions import DoctorPermission, IsOwnerOrReadOnly
from .tasks import email_to_customer, email_to_admin




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


class Contact(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        email_to_customer.delay(self.request.user.username, request.data['customer'])
        email_to_admin.delay(request.data['customer'], request.data['content'])
        return response.Response(serializer.data,
                                 status=status.HTTP_201_CREATED, headers=headers)

    permission_classes = [IsAuthenticated,]








