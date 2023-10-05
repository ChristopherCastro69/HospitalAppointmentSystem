from django.db import models
from django.utils import timezone

# Create your models here.
class Diagnosis(models.Model):
    diagnosisID = models.AutoField(primary_key=True)
    diagnosisName = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    dateCreated = models.DateTimeField(default=timezone.now)
    patientID = models.ForeignKey('Patient.Patient', on_delete=models.CASCADE, default="NA")
    doctorID = models.ForeignKey('Doctor.Doctor', on_delete=models.CASCADE, default="NA")
