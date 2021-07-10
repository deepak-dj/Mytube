from django import forms
from .models import display
from django.contrib.auth.models import User
class display_form(forms.ModelForm):
    class Meta:
        model = display
        fields = ['date_posted','title','video']

