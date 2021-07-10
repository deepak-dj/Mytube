from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class register_form(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']

class profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
class user_form(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']