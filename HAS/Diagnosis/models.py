from django.db import models

# Create your models here.
class Diagnosis(models.Model):
    diagnosisID = models.AutoField(primary_key=True)
