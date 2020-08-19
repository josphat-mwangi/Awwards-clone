from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django import forms
from django.contrib.auth.models import User
from .models import Profile,Project

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic","bio"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['author', 'title', 'image','description','link']

  
