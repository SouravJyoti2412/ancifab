from dataclasses import fields
from importlib.metadata import files
from turtle import color
from django import forms
from django.forms import ModelForm
from .models import product_add_slot


class product_add_slotForm(ModelForm):
    
    class Meta:
        model = product_add_slot
        fields ='__all__'