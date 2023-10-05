from django.db import models


# Create your models here.
class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key=True)

