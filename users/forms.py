from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    phone=forms.CharField()

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2','phone']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    phone=forms.CharField()

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','phone']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','birthdate','contact']
