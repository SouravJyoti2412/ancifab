from django import forms
from django.forms import ModelForm
from .models import LogoField,Slogan

class LogoFieldForm(ModelForm):
    class Meta:
        model = LogoField
        fields = '__all__'
        
        
        
        
class SloganForm(ModelForm):
    class Meta:
        model = Slogan
        fields = '__all__'
