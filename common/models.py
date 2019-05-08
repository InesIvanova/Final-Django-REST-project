from django.db import models

from .enums import TreatmentEnum, StatusEnum

from accounts.enums import DoctorSpecialties
from accounts.models import Patient, Doctor


class Cardboard(models.Model):
    creation_date = models.DateField(auto_now=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)


class Visitation(models.Model):
    date = models.DateField(auto_now=True)
    description = models.TextField()
    treatment = models.CharField(max_length=20, choices=[(t.name, t.value) for t in TreatmentEnum])
    cardboard = models.ForeignKey(Cardboard, on_delete=models.CASCADE)


class Appointment(models.Model):
    date = models.DateField()
    reason = models.TextField()
    doctor_type = models.CharField(max_length=20, choices=[(s.name, s.value) for s in DoctorSpecialties])
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=10, choices=[(s.name, s.value) for s in StatusEnum], default=StatusEnum.P)

    @property
    def is_archived(self):
        from datetime import datetime
        if datetime.now() > self.date:
            return True
        return False
