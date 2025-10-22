from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'profile_pic', 'username', 'email',
            'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'user_type'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-select'}),
        }
