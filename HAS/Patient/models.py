from django.db import models
from User.models import User

# Create your models here.
class Patient(User):
    patientID = models.AutoField(primary_key=True)
