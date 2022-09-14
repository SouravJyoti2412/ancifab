from distutils.command import upload
from wsgiref.validate import validator
from django.db import models
from django.core.exceptions import ValidationError
def validates_image(image):
    file_size = image.file.size
    limit_kb = 10
    if file_size > limit_kb * 1024:
         raise ValidationError("Max size of file is %s KB" % limit_kb)  
def validates_image20(image):
    file_size = image.file.size
    limit_kb = 20
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
    
    
class LogoField(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo field'
    heading_logo = models.ImageField(upload_to = 'logo/',)
    Footer_logo = models.ImageField(upload_to = 'logo/',)
    
    
class Slogan(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Website slogan'
        verbose_name_plural = 'Website slogans'
    slogan  = models.CharField(max_length =250)
    
    def __str__(self):
        return self.slogan
    
    
    


    

    

