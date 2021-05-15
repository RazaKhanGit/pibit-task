# forms.py
from django import forms
from django.urls import conf
from .models import *
  
class ImageForm(forms.Form):
    image = forms.ImageField()

class EditForm(forms.ModelForm):
    class Meta:
        model = ImageM
        fields = ['title', 'info']
    
       

    