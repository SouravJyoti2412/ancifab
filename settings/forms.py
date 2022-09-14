
from django import forms
from django.forms import ModelForm

# from admins.views import productsize
from .models import WebsiteLogo

class WebsiteLogoForm(ModelForm):
    class Meta:
        model = WebsiteLogo
        fields = '__all__'