from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from .enums import DoctorSpecialties, Gender


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[MinValueValidator(23)])
    specialty = models.CharField(max_length=20, choices=[(s.name, s.value) for s in DoctorSpecialties])

    def __str__(self):
        return f"{self.user}"


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[MinValueValidator(23)])
    gender = models.CharField(max_length=8, choices=[(g.name, g.value) for g in Gender])

    def __str__(self):
        return f"{self.user}"









