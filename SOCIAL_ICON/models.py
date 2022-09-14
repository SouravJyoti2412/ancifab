from email.policy import default
from wsgiref.validate import validator
from django.db import models
from django.core.exceptions import ValidationError
def validate_image(image):
    file_size = image.file.size
    limit_kb = 10
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)

class Social_icon_adding(models.Model):
    social_icon_name = models.CharField(max_length = 30)
    social_icon_image =models.ImageField(upload_to='social_icon/', default=None, null =True,blank=False,validators=[validate_image],help_text=("Please we recommended dimensions: 16 x 16 PX, 10 KB MAX and use tranparent logo"))
    social_icon_link_except_http = models.CharField(max_length = 30)
    class Meta:
         verbose_name = "Social Icon"