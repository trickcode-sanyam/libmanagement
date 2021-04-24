from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta: #it needs to be named this
        model = User
        fields = ['username','email','password1', 'password2']
