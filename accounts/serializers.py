from rest_framework import serializers

from .models import Doctor, Contact


class DoctorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('__all__')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')
