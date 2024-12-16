from django import forms
from .models import ElectricityConnectionRequest

class ElectricityConnectionForm(forms.ModelForm):
    class Meta:
        model = ElectricityConnectionRequest
        fields = ['firstname', 'lastname', 'date_of_birth', 'aadhar_number', 'aadhar_card', 'subject']