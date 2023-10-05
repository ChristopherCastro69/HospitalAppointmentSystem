from django.db import models
from User.models import User

# Create your models here.
class Doctor(User):
    shifts = (('M','Morning'),('A','Afternoon'))

    # doctorID = models.AutoField(primary_key=True)
    specialization = models.CharField(max_length=200,null=False,default='NA')
    shiftType = models.CharField(max_length=1, null=False, choices=shifts,default='N')


