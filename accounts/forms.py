from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'profile_image', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
