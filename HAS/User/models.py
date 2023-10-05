from django.db import models

# Create your models here.
class User(models.Model):
    sexType = (('M', 'Male'), ('F', 'Female'), ('I', 'Intersex'))
    userType = (('P', 'Patient'), ('D', 'Doctor'))

    email = models.CharField(max_length=100, primary_key=True, null=False)
    password = models.CharField(max_length=20, null=False)
    firstName = models.CharField(max_length=100, null=False)
    middleName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=False)
    birthDate = models.DateField(null=False)
    sex = models.CharField(max_length=1, null=False, choices=sexType)
    phone = models.CharField(max_length=11, null=True)
    user = models.CharField(max_length=1, null=False, choices=userType)

