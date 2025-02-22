from django import forms
from .models import SoftwareInfo

class SoftwareInfoForm(forms.ModelForm):
    class Meta:
        model = SoftwareInfo
        fields = [
            'software_name', 'software_title', 'software_dev_by', 'software_logo', 'software_favicon', 
            'software_email', 'software_contact', 'software_address', 'status', 
        ]
        widgets = {
            'software_name': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter software name' }),
            'software_title': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter software title' }),
            'software_dev_by': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter developer name' }),
            'software_logo': forms.FileInput(attrs={ 'class': 'form-control' }),
            'software_favicon': forms.FileInput(attrs={ 'class': 'form-control' }),
            'software_email': forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter email address' }),
            'software_contact': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter contact number' }),
            'software_address': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter address'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }