from dataclasses import fields
from tkinter import W
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput())
    password = forms.CharField(label='password1', widget=forms.PasswordInput())





class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput())
    email = forms.EmailField(label='email', widget=forms.EmailInput())
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'
        