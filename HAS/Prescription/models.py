from django.db import models

# Create your models here.
class Prescription(models.Model):
    prescriptionID = models.AutoField(primary_key=True)
