from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import WebUser, PanelAdmin
from django.contrib.auth.password_validation import validate_password
from django import forms
from django.contrib.auth.hashers import make_password

from .models import WebUser, PanelAdmin,Admin

class AdminRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Admin
        fields = ['name', 'email', 'password']

    def save(self, commit=True):
        admin = super().save(commit=False)
        admin.set_password(self.cleaned_data["password"])
        if commit:
            admin.save()
        return admin

class WebUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = WebUser
        fields = ['email', 'name', 'contact_no', 'address', 'city', 'state', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200',
                'placeholder': 'Enter your password'
            }),
        }
    def save(self, commit=True):
        # Save the form instance but do not commit it to the database yet.
        user = super().save(commit=False)
        
        # Hash the password before saving
        user.password = make_password(self.cleaned_data["password"])
        
        # Save the instance if commit=True
        if commit:
            user.save()
        return user

class PanelAdminRegistrationForm(forms.ModelForm):
    class Meta:
        model = PanelAdmin
        fields = ['email', 'name', 'contact_no', 'address', 'city', 'state', 'password']


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200',
            'placeholder': 'Enter your email',
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200',
            'placeholder': 'Enter your password',
        })
    )