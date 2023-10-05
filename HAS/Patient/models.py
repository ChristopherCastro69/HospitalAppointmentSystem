from django.db import models
from User.models import User

# Create your models here.
class Patient(User):
    #patientID = models.AutoField(primary_key=True)
    pass

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.CharField(max_length=20)