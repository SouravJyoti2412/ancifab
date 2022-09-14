
from django.db import models
from django.forms import ImageField, ValidationError
def validates_image(image):
    file_size = image.file.size
    limit_kb = 20
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
def validate_image(image):
    file_size = image.file.size
    limit_kb = 10
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)    
class WebsiteLogo(models.Model):
    HeaderLogo = models.ImageField( upload_to='logo/',validators=[validate_image],help_text=("Please we recommended dimensions: , 10 KB MAX"))
    Logoname1 = models.CharField(max_length=20, null = True)
    Logoname2 = models.CharField(max_length=20, null = True)
    footerLogo = models.ImageField( upload_to='logo/',validators=[validates_image],help_text=("Please we recommended dimensions: , 20 KB MAX"))
    
