


from django.db import models

# from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from autoslug import AutoSlugField
from customer_login.models import Singup
from ckeditor.fields import RichTextField
# def validate_minimum_size(width=None, height=None):
#     def validator(image):
#         error = False
#         if width is not None and image.width < width:
#             error = True
#         if height is not None and image.height < height:
#             error = True
#         if error:
#             raise ValidationError(
#                 [f'Size should be at least {width} x {height} pixels.']
#             )
#         return validator
# ,validators=[validate_minimum_size(width=870, height=800)],
def validate_image(image):
    file_size = image.file.size
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
def validate_images(image):
    file_size = image.file.size
    limit_kb = 100
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
class About_us(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'About us content'
        verbose_name_plural = 'About us all content'
    content_title  = models.CharField(max_length =30, default=None,null=False)
    content_des =  RichTextField(default=None,null=False)
class Aboutus_heading(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'About us heading'
        verbose_name_plural = 'About us headings'
    title  = models.CharField(max_length =30)
    sub_title  = models.CharField(max_length =30)
    content =  RichTextField()
    side_image= models.FileField(upload_to='about_us/')
       
class Faqs(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'
    title  = models.CharField(max_length =100)
    content =  RichTextField()
    def __str__(self):
        return self.title
class Terms_and_Condition(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Terms and Condition'
        verbose_name_plural = 'Terms and Conditions'
    title  = models.CharField(max_length =100)
    content =  RichTextField()
    def __str__(self):
        return self.title

class Return_refund_policy(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Return and refund policy'
        verbose_name_plural = 'Return and refund policies'
    title  = models.CharField(max_length =100)
    content =  RichTextField()
    def __str__(self):
        return self.title
    
    
class Privacy_policy(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Privacy policy'
        verbose_name_plural = 'Privacy policies'
    title  = models.CharField(max_length =100)
    content =  RichTextField()
    def __str__(self):
        return self.title
class contact_details_section(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'contact address'
        verbose_name_plural = 'contact address'
    phone   = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length = 300)
    side_image_375X230 = models.FileField(upload_to='contact/', default = None)
    # def __str__(self):
    #     return self.title

class home_carousel(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Home Carousal'
        verbose_name_plural = 'Home Carousals'
    image_1920X1080px = models.FileField(upload_to='home/home_carousel/',)
    small_heading_optional =models.CharField(max_length = 20,blank= True)
    big_heading_optional = models.CharField(max_length = 30, blank=True)
    offer_optional = models.CharField(max_length = 50,blank=True)
    image_button_link = models.CharField(max_length = 255)
    
class home_collection_banner(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Home Collection Banner'
        verbose_name_plural = 'Home Collection Banners'

    IMAGE_BIG_LEFT_870X800px = models.ImageField(upload_to='home/home_all_banner/',validators=[validate_image])
    IMAGE_SMALL_FIRST_425X390px = models.ImageField(upload_to='home/home_all_banner/',validators=[validate_image])
    BUTTON_LINK_OF_SMALL_FIRST_IMAGE = models.CharField(max_length = 255)
    HEADING_OF_SMALL_FIRST_IMAGE = models.CharField(max_length = 30)
    IMAGE_SMALL_SECOND_425X390px = models.ImageField(upload_to='home/home_all_banner/',validators=[validate_image])
    BUTTON_LINK_OF_SMALL_SECOND_IMAGE = models.CharField(max_length = 255)
    HEADING_OF_SMALL_SECOND_IMAGE = models.CharField(max_length = 30)
    IMAGE_RIGHT_DOWN_870X390px =  models.ImageField(upload_to='home/home_all_banner/',validators=[validate_image])
    HEADING_OF_RIGHT_DOWN_IMAGE = models.CharField(max_length = 30)
    BUTTON_LINK_OF_IMAGE_RIGHT_DOWN =models.CharField(max_length = 255)
    MIDDLE_SIDE_IMAGE_1920X1080px = models.ImageField(upload_to='home/home_all_banner/',validators=[validate_image])
    HEADING_OF_MIDDLE_SIDE_IMAGE =models.CharField(max_length = 30)
    BUTTON_LINK_OF_MIDDLE_SIDE_IMAGE =models.CharField(max_length = 255)


class banners(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'All Banner'
        verbose_name_plural = 'All Banners'
    Banner_Name =models.CharField(max_length=255)
    Banner_Image =models.ImageField(upload_to ='all_banner_except_home/',validators=[validate_image],verbose_name="Banner Image (1920X464px)",help_text=("Please use our recommended dimensions: 1920 x 464 PX, 150 KB MAX"))


class Blog(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
    Blog_title =models.CharField(max_length=255)
    Blog_banner_Image =models.ImageField(upload_to ='Blog_image/',validators=[validate_image],verbose_name="Blog Banner Image(868x510px)",help_text=("Please use our recommended dimensions: 868x510px, 150 KB MAX"))
    Blog_first_Image =models.ImageField(upload_to ='Blog_image/',validators=[validate_images],verbose_name="Blog first image",help_text=("Please use our recommended dimensions: 424x300px, 100 KB MAX"))
    Blog_second_Image =models.ImageField(upload_to ='Blog_image/',validators=[validate_images],verbose_name="Blog second image",help_text=("Please use our recommended dimensions: 424x300px, 100 KB MAX"))
    category = models.CharField(max_length=30,help_text=("please mention your blog is in which category"))
    author = models.CharField(max_length=30,default ="annynomus" ,null=True , verbose_name= "Author name (optional)",help_text=("please mention your name"))
    created_at = models.DateTimeField(auto_now_add=True )
    title_slug = AutoSlugField(populate_from='Blog_title',unique=True,null=True,default=None)
    content = RichTextField()
class Blogcomment(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(Singup, on_delete=models.CASCADE)
    Blogpost = models.ForeignKey(Blog,on_delete=models.CASCADE)
    Parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
    Timestamp = models.DateTimeField(auto_now_add=True)
    # def __str__(self) :
    #     return self
    
    
class comments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(Singup,on_delete=models.CASCADE)
    blog_detail = models.ForeignKey(Blog,on_delete=models.CASCADE)
    
    
    