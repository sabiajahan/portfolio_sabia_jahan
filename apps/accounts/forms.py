from django import forms
from .models import UserProfile
from allauth.account.forms import SignupForm
from .validators import StrongPasswordValidator
from .validators import validate_bangladesh_phone_number

class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(
        required=True,
        help_text="Enter your phone number in local format (e.g., 01799925246)."
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Validate the local format and convert to international
        phone_number = validate_bangladesh_phone_number(phone_number)
        return phone_number

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        # Validate password strength
        validator = StrongPasswordValidator()
        validator.validate(password)
        return password

    def save(self, request):
        user = super().save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
    
class UserProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30, 
        required=False, 
        label="First Name",
        widget=forms.TextInput(attrs={ 'class': 'w-full custom-input', 'placeholder': 'First Name' })
    )
    last_name = forms.CharField(
        max_length=30, 
        required=False, 
        label="Last Name",
        widget=forms.TextInput(attrs={ 'class': 'w-full custom-input', 'placeholder': 'Last Name' })
    )
    phone_number = forms.CharField(
        max_length=15, 
        required=False, 
        label="Phone Number",
        widget=forms.TextInput(attrs={ 'class': 'w-full custom-input', 'placeholder': 'Phone Number' })
    )

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'birth_date', 'address', 'first_name', 'last_name', 'phone_number']
        widgets = {
            'profile_picture': forms.FileInput(attrs={ 'class': 'w-full custom-input' }),
            'bio': forms.Textarea(attrs={ 'class': 'w-full custom-input', 'placeholder': 'Tell us about yourself...', 'rows': 4 }),
            'birth_date': forms.DateInput(attrs={ 'class': 'w-full custom-input', 'placeholder': 'YYYY-MM-DD', 'type': 'date' }),
            'address': forms.TextInput(attrs={ 'class': 'w-full custom-input', 'placeholder': 'Your Address' }),
        }

    def __init__(self, *args, **kwargs):
        # Access the linked user instance for initial field population
        user = kwargs.get('instance').user if 'instance' in kwargs else None
        if user:
            kwargs.setdefault('initial', {}).update({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number': user.phone_number,
            })
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # Save the user-specific fields (first name, last name, phone number)
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.phone_number = self.cleaned_data.get('phone_number', '')

        if commit:
            user.save()
            profile.save()
        return profile