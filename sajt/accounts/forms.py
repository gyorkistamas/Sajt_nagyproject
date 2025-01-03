from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']