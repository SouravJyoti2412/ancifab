from dataclasses import fields
from importlib.metadata import files
from turtle import color
from django import forms
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
# from admins.views import productsize
from .models import Coupon, ProductColor,ProductSize,Category,Sub_Category, WebsiteLogos,maincategory,addproduct,Size_chart,product_return

class maincategoryForm(ModelForm):
    class Meta:
        model = maincategory
        fields = '__all__'
class CatagoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields ='__all__'
        # widgets = {
        #     'Category_name' : forms.TextInput(attrs = {'placeholder': 'Category'}),
        #     # 'maincategory'    : forms.(attrs = {'class':'form-control'}),
        # }
class Sub_CategoryForm(ModelForm):
    
    class Meta:
        model = Sub_Category
        fields ='__all__'
        
class ProductColorForm(ModelForm):
    
    class Meta:
        model = ProductColor
        fields ='__all__'
    
class ProductSizeForm(ModelForm):
    
    class Meta:
        model = ProductSize
        fields ='__all__'
class productaddingForm(forms.ModelForm):
   
    color = forms.ModelMultipleChoiceField(
            queryset=ProductColor.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            )
    size = forms.ModelMultipleChoiceField(
            queryset=ProductSize.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            )
    class Meta:
        model = addproduct
        fields ='__all__'
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['category'].queryset = Category.objects.none()
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['sub_category'].queryset = Sub_Category.objects.none()
   

    
class Size_chartForm(ModelForm):
    
    class Meta:
        model = Size_chart
        fields ='__all__'
        
        
class product_returnForm(ModelForm):
    class Meta:
        model = product_return
        fields ="__all__"
        
        
        
class WebsiteLogosForm(ModelForm):
    class Meta:
        model = WebsiteLogos
        fields ="__all__"
        
class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields= "__all__"