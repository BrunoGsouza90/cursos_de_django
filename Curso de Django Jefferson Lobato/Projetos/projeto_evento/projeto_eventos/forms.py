from django import forms
from django.forms import ModelForm
from projeto_eventos.models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee 
        fields = ['name', 'email', 'profile_photo']

    profile_photo = forms.ImageField(
        label="Employee Profile Photo",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )