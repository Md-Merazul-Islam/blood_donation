from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['blood_group','name',  'phone_number', 'address']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter donor name'}),
            'blood_group': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter present address'}),
        }
