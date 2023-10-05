from django.db import models
from Patient.models import Patient
from Doctor.models import Doctor
import datetime

from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
class Prescription(models.Model):
    prescriptionID = models.AutoField(primary_key=True)
    medicationName = models.CharField(max_length=40, default='NA')
    dosage = models.FloatField(default=0)
    frequency = models.FloatField(default=0)
    startDate = models.DateField(default=datetime.date.today())
    endDate = models.DateField(default=datetime.date.today())
    patientID = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    doctorID = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)



# @receiver(pre_save, sender=Prescription)
# def ensure_referential_integrity(sender, instance, **kwargs):
#     if instance.doctorID is None or instance.patientID is None:
#         # You can raise an exception, log an error, or handle this case as needed.
#         raise ValueError("Both doctorID and patientID must be set before saving an Appointment.")

    # prescriptionID = models.AutoField(primary_key=True)
    # medicationName = models.CharField(max_length=40)
    # dosage = models.FloatField()
    # frequency = models.FloatField()
    # startDate = models.DateField()
    # endDate = models.DateField()
    # patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)