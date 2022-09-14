from dataclasses import fields
from importlib.metadata import files
from turtle import color
from django import forms
from django.forms import ModelForm
from .models import Social_icon_adding


class Social_icon_addingForm(ModelForm):
    
    class Meta:
        model = Social_icon_adding
        fields ='__all__'