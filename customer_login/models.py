from tabnanny import verbose
from django.db import models
import email
from passlib.hash import pbkdf2_sha256
from django.db import models
class Singup(models.Model):
    firstname = models.CharField(max_length=30,editable=False)
    lastname = models.CharField(max_length=30,editable=False)
    number =models.CharField(max_length=15,editable=False)
    email_id=models.EmailField(editable=False)
    password =models.CharField(max_length=255,editable=False)
    forgetpass = models.IntegerField(default = 0,null =True,blank = True)
    block = models.BooleanField(default=False)
    def verify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)
    class Meta:
         verbose_name = "User"
    @staticmethod
    def get_singup_detail_byid(ids):
        return Singup.objects.filter(id=ids)
# Create your models here.
    def email_exists(self) :
        if Singup.objects.filter(email_id =self.email_id):
            return True
        return False
    
    @staticmethod
    def get_customer_details_by_email(email_id):
        try:
            return Singup.objects.get(email_id = email_id)
        except:
            return False

    def __str__(self):
        return  self.firstname     

# Create your models here.
