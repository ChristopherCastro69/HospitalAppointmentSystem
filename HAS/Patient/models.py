from django.db import models
from User.models import User


# Create your models here.
class Patient(User):
    address = models.CharField(max_length=50)
    emergencyContactName = models.CharField(max_length=30)
    emergencyContactNumber = models.IntegerField(max_length=11)
    allergy = models.CharField(max_length=20)

class MedicalHistory(models.Model):
    medHistoryID = models.AutoField(primary_key = True)
    medicalCondition = models.CharField(max_length=20)
    date = models.DateField()
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

class Prescriptions(models.Model):
    prescriptionID = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    dosage = models.CharField(max_length=10)
    frequency = models.CharField(max_length=10)
    startDate = models.DateField()
    endDate = models.DateField()
    currentState = models.CharField(max_length= 1, choices=(('F','Filled'), ('R','Refilled'), ('C', 'Cancelled'), ('E', 'Expired')), default = 'F' )
    medicalHistory = models.ForeignKey('MedicalHistory', on_delete=models.CASCADE)

class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key = True)
    type = models.CharField(choices=(('C','Consultation'), ('P','Procedure')), default = 'C')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE())
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE())

    class Meta:
        unique_together =['patient','doctor', 'type']

class Diagnosis(models.Model):
    diagnosisID = models.AutoField(primary_key = True)
    description = models.CharField(max_length= 150)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE())
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE())
    class Meta:
        unique_together =['patient','doctor', 'description']

class Treatment(models.Model):
    treatment = models.AutoField(primary_key = True)
    description = models.CharField(max_length= 250)
    status = models.CharField(max_length=1, choices=(('O','Ongoing'),('C','Completed'),('D','Discontinued')), default = 'O')
    cost = models.FloatField(max_length=15)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE())
    Doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE())
    medicalHistory = models.ForeignKey(MedicalHistory)
    class Meta:
        unique_together =['patient','doctor', 'description']
class PatientDoctor(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE())
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE())

    class Meta:
        unique_together =['patient','doctor']

