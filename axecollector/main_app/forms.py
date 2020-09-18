from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Maintenance

class RegistrationForm(UserCreationForm):
  first_name = forms.CharField(max_length=50, required=True)
  last_name = forms.CharField(max_length=50, required=True)
  email = forms.CharField(max_length=50, required=True)
  
  class Meta:
    model = User
    fields = ["username", "password1", "password2", "first_name", "last_name", "email"]

class MaintenanceForm(ModelForm):
  class Meta:
    model = Maintenance
    fields = ['date', 'service', 'technician']