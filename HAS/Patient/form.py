from django.forms import ModelForm
from django import forms
from .models import Patient

class Patient(ModelForm):
    sexType = forms.CharField(widget=forms.ChoiceField)

    email = models.CharField(max_length=100, primary_key=True, null=False)
    password = models.CharField(max_length=20, null=False)
    firstName = models.CharField(max_length=100, null=False)
    middleName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=False)
    birthDate = models.DateField(null=False)
    sex = models.CharField(max_length=1, null=False, choices=sexType)
    phone = models.CharField(max_length=11, null=True)
    user = models.CharField(max_length=1, null=False, choices=userType)
    class Meta:
        model = Patient
        fields = ['participants','date','event']

class RoomForm(ModelForm):
    roomName = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Room
        fields = ['roomID','roomName']
