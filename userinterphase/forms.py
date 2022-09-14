from django import forms
from django.forms import ModelForm
from .models import About_us, Faqs,Terms_and_Condition,Return_refund_policy,contact_details_section,home_carousel,home_collection_banner,banners,Blog, Blogcomment ,Aboutus_heading,Privacy_policy
class aboutusForm(ModelForm):
    class Meta:
        model = About_us
        fields = '__all__'
class Aboutus_headingForm(ModelForm):
    class Meta:
        model = Aboutus_heading
        fields = '__all__'
class FaqsForm(ModelForm):
    class Meta:
        model =  Faqs
        fields = '__all__'
        
class Privacy_policyForm(ModelForm):
    class Meta:
        model =  Privacy_policy
        fields = '__all__'
class Terms_and_ConditionForm(ModelForm):
    class Meta:
        model =  Terms_and_Condition
        fields = '__all__'
class Return_refund_policyForm(ModelForm):
    class Meta:
        model =  Return_refund_policy
        fields = '__all__'
class contact_details_sectionForm(ModelForm):
    class Meta:
        model =  contact_details_section
        fields = '__all__'
class home_carouselForm(ModelForm):
    class Meta:
        model =  home_carousel
        fields = '__all__'       
class bannersForm(ModelForm):
    class Meta:
        model =  banners
        fields = '__all__'
class home_collection_bannerForm(ModelForm):
    class Meta:
        model =  home_collection_banner
        fields = '__all__'
class home_collection_bannerForm(ModelForm):
    class Meta:
        model =  home_collection_banner
        fields = '__all__'
class BlogForm(ModelForm):
    class Meta:
        model =  Blog
        fields = '__all__'


