from ast import Return
import datetime
from distutils import text_file
from distutils.command import upload
from tabnanny import verbose
from tkinter import CASCADE
from turtle import color
from django.utils.timezone import now
import uuid
# from typing_extensions import Self
# import typing_extensions
from weakref import proxy
from autoslug import AutoSlugField
from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from requests import request
# from .managers import categoryManager,sub_categoryManager,main_categoryManager
# from admins.views import customer
from customer_login.models import Singup
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
# from taggit.models import (
#     CommonGenericTaggedItemBase,
#     GenericTaggedItemBase,
#     GenericUUIDTaggedItemBase,
#     ItemBase,
#     Tag,
#     TagBase,
#     TaggedItem,
#     TaggedItemBase,
# )
def validate_image(image):
    file_size = image.file.size
    limit_kb = 100
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
def validate_image200kb(image):
    file_size = image.file.size
    limit_kb = 200
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
def validates_image(image):
    file_size = image.file.size
    limit_kb = 10
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
def validates20_image(image):
    file_size = image.file.size
    limit_kb = 20
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)    

class maincategory(models.Model):
    sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)
    Thrmbnil_image  =models.ImageField(verbose_name= "Thrumbnil Image (362X470px)", upload_to='social_icon/', default=None, null =True,blank=False,validators=[validate_image],help_text=("Please we recommended dimensions: 362 X 470px, 100 KB MAX and use tranparent logo"))
    slug = AutoSlugField(populate_from='name',unique=True,null=True, blank=False,default=None)
    def __str__(self):
        return self.name
class Category(models.Model):
    Sno =models.AutoField(primary_key=True)
    Category_name = models.CharField(max_length=20)
    maincategory = models.ForeignKey(maincategory ,on_delete=models.CASCADE, default=None,related_name="category")
    slug = AutoSlugField(populate_from='Category_name',unique=True,null=True, blank=False,default=None)
    def __str__(self) -> str:
        return self.Category_name 
class Sub_Category(models.Model):
    Sno =models.AutoField(primary_key=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None,related_name="subcategory")
    Sub_Category_name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='Sub_Category_name',unique=True,null=True, blank=False,default=None)
    def __str__(self):
        return self.Sub_Category_name
class ProductColor(models.Model):
    Sno =models.AutoField(primary_key=True)
    Color_name = models.CharField(max_length=20)
    Color_Swatch =models.ImageField( upload_to='color_swatches/', default=None, null =True,blank=False,validators=[validates_image],help_text=("Please we recommended dimensions: , 10 KB MAX"))
    def __str__(self):
        return self.Color_name

class ProductSize(models.Model):
    Sno =models.AutoField(primary_key=True)
    Size_name = models.CharField(max_length=20)
    Size_mesurment =  models.CharField(max_length=30)
    def __str__(self):
        return self.Size_name
        
        
        
        


 
    
class addproduct(models.Model):
    main_category = models.ForeignKey(maincategory, on_delete=models.CASCADE, default=None,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None,)
    sub_category =models.ForeignKey(Sub_Category,on_delete=models.CASCADE ,default=None,) 
    name =  models.CharField(max_length=50)
    product_code = models.CharField(max_length=50)
    product_des = RichTextField()
    color = models.ManyToManyField(ProductColor ,related_name='color')
    size = models.ManyToManyField(ProductSize, related_name='size')
    price = models.IntegerField(null= True,blank= True)
    discount = models.BooleanField(default=False)
    discount_price = models.IntegerField()
    Thrumnil =models.ImageField( upload_to='products/',validators=[validate_image200kb],help_text=("recommended dimensions:800X960px,200 KB MAX"))
    Thrumnil2 =models.ImageField( upload_to='products/',validators=[validate_image200kb],help_text=("recommended dimensions:800X960px,200 KB MAX"))
    Image1 =models.ImageField( upload_to='products/',validators=[validate_image200kb],help_text=("recommended dimensions:800X960px,200 KB MAX"))
    Image2=models.ImageField( blank=True, null= True,upload_to='products/',validators=[validate_image200kb],help_text=("recommended dimensions:800X960px,200 KB MAX"))
    Image3=models.ImageField( blank=True, null= True,upload_to='products/',validators=[validate_image200kb],help_text=("recommended dimensions:800X960px,200 KB MAX"))
    Image4 =models.ImageField( blank =True,null=True, upload_to='products/',validators=[validate_image200kb],help_text=("recommended dimensions:800X960px,200 KB MAX"))
    Image5 =models.ImageField( blank= True,null=True,upload_to='products/',validators=[validate_image200kb],help_text=("recommended dimensions:800X960px,200 KB MAX"))
    Image6 =models.ImageField( blank = True, null=True,upload_to='products/',validators=[validate_image200kb],help_text=("recommended dimensions:800X960px,200 KB MAX"))
    Meta_name = models.CharField(max_length=255, default =None,null = True)
    Meta_description = models.TextField()
    product_slug = AutoSlugField(populate_from='name',unique=True,null=True, blank=False,default=None)
    active = models.BooleanField(default= True)
    stock = models.BooleanField(default=True)
    # views = models.IntegerField(default =0)
    trending= models.BooleanField(default=False)
    def __str__(self):
        return   self.name + " (" + self.product_code +")"
    @staticmethod
    def get_Products_by_id(ids):
        return addproduct.objects.filter(id__in=ids)
    @staticmethod
    def get_all_products():
        return addproduct.objects.all()
    
    @staticmethod
    def get_allproduct_bysubcategorySno(sub_category_Sno) :
        if sub_category_Sno :
            return addproduct.objects.filter(sub_category=sub_category_Sno)
        else:
            pass


class Orderplace(models.Model):
    product = models.ForeignKey(addproduct,on_delete=models.CASCADE) 
    customer = models.ForeignKey(Singup,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    firstname = models.CharField(max_length= 30)
    lastname = models.CharField(max_length= 30)
    company_name = models.CharField(max_length=50 , blank = True, null=True )
    country = models.CharField(max_length= 30)
    Street_adress = models.TextField()
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    number = models.IntegerField(default = None)
    data = models.DateField(default=datetime.datetime.today)


class add_to_cart(models.Model):
    customer = models.ForeignKey(Singup,on_delete=models.CASCADE)
    cartProduct =models.ForeignKey(addproduct,on_delete=models.CASCADE, default=None)
    size = models.CharField(max_length=30,null =True,blank=True)
    quantity = models.IntegerField(default=1,)
class productreview(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'review'
        verbose_name_plural = 'product reviews'
    sno = models.AutoField(primary_key=True)
    rating = models.IntegerField(default=0)
    review_title = models.CharField(max_length=100)
    messege = models.TextField()
    user = models.ForeignKey(Singup, on_delete=models.CASCADE)
    product = models.ForeignKey(addproduct,on_delete=models.CASCADE)
    Parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
    Timestamp = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    
    
class generalQuery(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    subject = models.CharField(max_length=100,null = True, blank = True)
    mesege =  models.TextField()
    slug = AutoSlugField(populate_from='name',unique=True,null=True, blank=False,default=None)
    view = models.BooleanField(default=False)
    
    
class productQuery(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    productname = models.CharField( max_length=100)
    productcode = models.CharField( max_length=100,null = True, blank = True)
    mesege =  models.TextField()
    slug = AutoSlugField(populate_from='name',unique=True,null=True, blank=False,default=None)
    view = models.BooleanField(default=False)
    
    
    
    
# class productname(models.Model):
#     name  = models.CharField(max_length=50)
# class productqunty (models.Model):
#     quantity = models.CharField(max_length=50)
# class productprice (models.Model):
#     price = models.CharField(max_length=50)
    

class AllOrders(models.Model):
    
    
    customer = models.ForeignKey(Singup,on_delete=models.CASCADE)
    emailid = models.EmailField()
    firstname = models.CharField(max_length= 30)
    lastname = models.CharField(max_length= 30)
    company_name = models.CharField(max_length=50 , blank = True, null=True )
    country = models.CharField(max_length= 30)
    Street_adress = models.TextField()
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)
    number = models.CharField(max_length=10,default = None)
    date = models.DateField(default=datetime.datetime.today)
    paid = models.BooleanField(default = False)
    gst = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    shipping = models.CharField(default=0,null =True,blank=True ,max_length=2)
    order_id = models.CharField(default=uuid.uuid4, editable=False, max_length=20)
    payment_mood = models.CharField(max_length=10,null =True,blank=True ,)
    Orderplaced = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
    out_delivery = models.BooleanField(default=False)
    deliverd = models.BooleanField(default=False)
    
    
    
# class orderItem (models.Model):
    
#     product = models.ForeignKey(addproduct,on_delete=models.CASCADE) 
#     quantity = models.IntegerField(default=1)
#     price = models.IntegerField()
#     producttotal = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='orderitem/')   
#     orderid = models.ForeignKey(AllOrders, on_delete=models.CASCADE)  
    
class ALlorderItem (models.Model):
    
    product = models.ForeignKey(addproduct,on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    producttotal = models.CharField(max_length=50)
    image = models.ImageField(upload_to='orderitem/')   
    orderid = models.ForeignKey(AllOrders, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, default=None ,null =True,blank = True)
class TotalOrders(models.Model):
    
    
    customer = models.ForeignKey(Singup,on_delete=models.CASCADE)
    emailid = models.EmailField()
    firstname = models.CharField(max_length= 30)
    lastname = models.CharField(max_length= 30)
    company_name = models.CharField(max_length=50 , blank = True, null=True )
    country = models.CharField(max_length= 30)
    Street_adress = models.TextField()
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)
    number = models.CharField(max_length=10,default = None)
    date = models.DateField(default=datetime.datetime.today)
    paid = models.BooleanField(default = False)
    gst = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    shipping = models.CharField(default=0,null =True,blank=True ,max_length=2)
    order_id = models.CharField(default=uuid.uuid4, editable=False, max_length=250)
    orderitem = models.ForeignKey(ALlorderItem,on_delete= models.CASCADE)
    
    
class Size_chart(models.Model):
    short_des = models.TextField()
    description = RichTextField()
    
    
class product_return(models.Model):
    description = RichTextField()
    
    
class CancelAllOrders(models.Model):
    customer = models.ForeignKey(Singup,on_delete=models.CASCADE)
    emailid = models.EmailField()
    firstname = models.CharField(max_length= 30)
    lastname = models.CharField(max_length= 30)
    paid = models.BooleanField(default = False)
    gst = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    shipping = models.CharField(default=0,null =True,blank=True ,max_length=2)
    order_id = models.CharField(default=uuid.uuid4, editable=False, max_length=20)
    payment_mood = models.CharField(max_length=10,null =True,blank=True ,)
    bank_details = models.TextField(null = True,blank = True)
    reson_cancel = models.CharField(default=None,max_length=250 ,null = True)
    date = models.DateField(default=datetime.datetime.today)
    payment_confirm = models.BooleanField(default=False)
class cancelordersItem(models.Model):
    product = models.ForeignKey(addproduct,on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    producttotal = models.CharField(max_length=50)
    image = models.ImageField(upload_to='orderitem/')   
    size = models.CharField(max_length=10, default=None ,null =True,blank = True)
    cancelid = models.ForeignKey(CancelAllOrders, on_delete=models.CASCADE)
    
    
    
    
    
    
    
class ReturnAllOrders(models.Model):
    customer = models.ForeignKey(Singup,on_delete=models.CASCADE)
    emailid = models.EmailField()
    firstname = models.CharField(max_length= 30)
    lastname = models.CharField(max_length= 30)
    paid = models.BooleanField(default = False)
    gst = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    shipping = models.CharField(default=0,null =True,blank=True ,max_length=2)
    order_id = models.CharField(default=uuid.uuid4, editable=False, max_length=20)
    payment_mood = models.CharField(max_length=10,null =True,blank=True ,)
    bank_details = models.TextField(null = True,blank = True)
    reson_cancel = models.CharField(default=None,max_length=250 ,null = True)
    cancelproductImage = models.ImageField(upload_to ='orderitem/')
    date = models.DateField(default=datetime.datetime.today)
    address = models.TextField(default = None)
    Pickup_request = models.BooleanField(default=False)
    # pick_up_done = models.BooleanField(default=False)
    Return_Confirm = models.BooleanField(default=False)
    payment_confirm = models.BooleanField(default=False)
    
class ReturnordersItem(models.Model):
    product = models.ForeignKey(addproduct,on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    producttotal = models.CharField(max_length=50)
    image = models.ImageField(upload_to='orderitem/')   
    size = models.CharField(max_length=10, default=None ,null =True,blank = True)
    cancelid = models.ForeignKey(ReturnAllOrders, on_delete=models.CASCADE)
    
    
class WebsiteLogos(models.Model):
    HeaderLogo = models.ImageField( upload_to='logo/',validators=[validates_image],help_text=("Please we recommended dimensions: , 10 KB MAX"))
    footerLogo = models.ImageField( upload_to='logo/',validators=[validates20_image],help_text=("Please we recommended dimensions: , 20 KB MAX"))
    name = models.CharField(max_length=50, default= None, null = True)
    
    
    
class CouponSystem(models.Model):
    coupon = models.CharField(max_length=100)
    
    
    
    
    
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    discount = models.IntegerField(validators=[MinValueValidator(0)])
    active = models.BooleanField(default=True)