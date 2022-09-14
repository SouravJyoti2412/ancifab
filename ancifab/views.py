from ast import For
# from pyexpat import model
from re import A, L
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from pymysql import NULL
from pytz import timezone
from requests import Session, delete, post
from Products.forms import CouponForm
from admins.views import customer, subcategory
from customer_login.models import Singup
# from passlib.hash import pbkdf2_sha256 
from django.contrib.auth.hashers import make_password ,check_password 
from django.contrib import messages
from settings.models import WebsiteLogo
from userinterphase.models import About_us, Faqs,Terms_and_Condition,Return_refund_policy, comments,contact_details_section,home_carousel,home_collection_banner,banners,Blog, Blogcomment,Aboutus_heading,Privacy_policy
from ADVATISMENT.models import product_add_slot
from SOCIAL_ICON.models import Social_icon_adding
from website_settings.models import LogoField
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from userinterphase.templatetags import extras
from django.core.paginator import Paginator
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import 
from Products.models import Coupon, ProductColor,ProductSize,Category,Sub_Category,maincategory,addproduct,Orderplace,add_to_cart,productreview,generalQuery,productQuery,AllOrders,ALlorderItem,Size_chart,product_return,CancelAllOrders,cancelordersItem,ReturnAllOrders,ReturnordersItem
# from customer_login.forms import Singupform
from django.db.models import Q
from django.http import JsonResponse
from settings.models import WebsiteLogo
from django.db.models import Avg
import razorpay
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.utils import timezone
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))

all_data ={
'social_icon':Social_icon_adding.objects.all(),
# 'exist_customer':Singup.request.session.get("customer_fname"),
'main_category':maincategory.objects.all(),
'ProductColor':ProductColor.objects.all(),
'ProductSize':ProductSize.objects.all(),
'logo':WebsiteLogo.objects.all()
# 'addproduct':addproduct.objects.all(),


}
# def cartproduct(request):
#     ids =list(request.session.get('cart').keys())
#     products = addproduct.get_Products_by_id(ids)
#     print(products)
def encrypt(pas):
    try:        
        pas = str(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii") 
        return encrypt_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(pas):
    try:
        pas = base64.urlsafe_b64decode(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        decod_pass = cipher_pass.decrypt(pas).decode("ascii")     
        return decod_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


        
def about(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                    amount += tempamount
                    if amount >=2000:
                        shipping_amount =0.0
                        gst = amount * (18/100)
                        total_amount = amount +gst
                    else :
                        shipping_amount= 80
                        gst = amount * (18/100)
                        total_amount = amount +gst+shipping_amount  
    
    about_heading = About_us.objects.all()
     
    # about_content = About_us_content.objects.all()
    about_data = {
        'about_head': about_heading,
        # 'about_content':about_content,
        'about_head_main': Aboutus_heading.objects.all(),
        'about_banner':banners.objects.all()[:1],
        'data':all_data,
       'customer_name' :(request.session.get("customer_fname")),
     
       'cart':cart,
     'total':total_amount
    }
    return render(request,"about_us.html",about_data)
def blog(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount 
    
    data={
    'blog_banner':banners.objects.all()[1:2] ,
    'data':all_data ,
     'blogdetails':Blog.objects.all(),
     'customer_name' :(request.session.get("customer_fname")), 
     'cart':cart,
     'total':total_amount
    }
    return render(request,"blog.html",data)
def blog_details(request,slug):
    
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount 
    # blogdetails ={
    #     'blogdetails':Blog.objects.filter(title_slug=slug).first(),
    #     'blogcomment':Blogcomment.objects.filter(Blogpost=Blog.objects.get(title_slug=slug))
    # }
    blogdetail = Blog.objects.filter(title_slug=slug).first()
    blogcomment= Blogcomment.objects.filter(Blogpost =blogdetail,Parent=None).order_by('-sno')
    replycomment= Blogcomment.objects.filter(Blogpost =blogdetail).exclude(Parent=None)
    replyDict={}
    for reply in replycomment:
        if reply.Parent.sno not in replyDict.keys():
            replyDict[reply.Parent.sno]=[reply]
        else:
            replyDict[reply.Parent.sno].append(reply)
    
    blogdetails={
        'blogdetail':blogdetail,
        'blogcomment':blogcomment,
        'replycomment':replyDict,
        'customer_name' :(request.session.get("customer_fname")),
        'cart':cart,
     'total':total_amount ,
     'data':all_data
        
    }
    
    return render(request,"blog-details.html",blogdetails)

def blogcomment(request):
    customer = request.session.get('customer')
    if request.method == "POST":
        comment = request.POST.get("comment")
        # user= request.user
        postSno = request.POST.get("postSno")
        post = Blog.objects.get(id=postSno)
        parentSno = request.POST.get("parentSno")
        print ()
        if parentSno == "":
        
        # Parent = request.POST.get
            comment = Blogcomment(comment=comment,user=Singup(id=customer),Blogpost=post)
            comment.save()
            messages.success(request,"your comment post sucessfully",extra_tags="comment_success")
        else:
            Parent =Blogcomment.objects.get(sno=parentSno)
            comment = Blogcomment(comment=comment,user=Singup(id=customer),Blogpost=post,Parent=Parent)
            comment.save()
            messages.success(request,"your reply post sucessfully",extra_tags="comment_success")
    return redirect(f"/blog/blog-details/{post.title_slug}")

    # data = request.session.get("customer_f_name") 
    
# def postblogcomment(request):
#     customer = request.session.get('customer')
#     blog = Blog.objects.all().first()
#     if request.method == "POST":
#         comment = request.POST["comment"]
#         print(customer, blog,comment)
#         commentdata = comments(comment = comment,user = Singup(id=customer),blog_detail = blog)
#         commentdata.save()
    
    
# def blogcomment(request,slug):
#     customer = request.session.get('customer')
#     blog = Blog.objects.filter(title_slug=slug).first()
#     if request.method == "POST":
#         comment = request.POST.get("comment")
        
#     comment = Blogcomment(comment=comment,user=Singup(id=customer),Blogpost=blog) 
#     comment.save()
#     messages.success(request,"your comment post sucessfully",extra_tags="comment_success")
#     # return redirect(f"/blog/{{blog.title_slug}}") 
#     return redirect("/")
    
    
    
# def cart(request):
#     ids =list(request.session.get('cart').keys())
#     products = addproduct.get_Products_by_id(ids)
#     print(products)
    
#     data={
#     'data':all_data,
#     'cart_banner':banners.objects.all()[2:3] ,
#     'products':products
#     }
#     return render(request,"cart.html",data)
def cart_delete(request, id):
    if request.method == 'POST':
        data1 = add_to_cart.objects.get(pk=id)
        data1.delete()
    return redirect('/cart')
def checkout(request):
    
    # cart = request.session.get('cart')
    # ids =list(request.session.get('cart').keys())
    # products = addproduct.get_Products_by_id(ids)
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    print(cart)
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount  
    data={
    'data':all_data,
    'checkout_banner':banners.objects.all()[7:8] , 
    # 'products':products,
    'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,
    'customer_name' :(request.session.get("customer_fname")), 
    }
    if request.method == "POST":
       cart = add_to_cart.objects.filter(customer=Singup(id=customer))
       customer = request.session.get('customer')
       carts = request.session.get('cart')
       firstname = request.POST.get('name')
       lastname = request.POST.get('lname')
       company_name =request.POST.get('cname')
       country = request.POST.get('country')
       Street_adress = request.POST.get('address')
       town = request.POST.get('town')
       state = request.POST.get('state')
       pincode = request.POST.get('pin')
       number = request.POST.get('number')
    #    print(product ,customer ,carts,firstname,lastname, company_name, country, Street_adress, town, state , pincode, number)
       for c in cart :
           order = Orderplace(product = c.cartProduct,
                              customer =Singup(id =customer),
                              price = c.cartProduct.discount_price,
                              quantity = c.quantity,
                              firstname =firstname,
                              lastname=lastname,
                              company_name=company_name,
                              country=country,
                              Street_adress=Street_adress,
                              town=town,
                              state=state,
                              pincode=pincode,
                              number=number)
           order.save()
          
    return render(request,"checkout.html",data)

def home(request):
    sub_category =Sub_Category.objects.all()
    maincat = maincategory.objects.all()[1:]
    maincat1 = maincategory.objects.all()[:1]
    trendproduct = addproduct.objects.all()    
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount 
    
    
    
    
    # maincat = maincategory.objects.all()[:5]
    
    # mainviewproduct={}
    # maincatid = request.GET.get('maincatid')
    # maincategoryview = maincategory.objects.get(sno=maincatid)
    # mainviewproduct = addproduct.objects.filter(main_category = maincategoryview)
    
    # subcategorySno = request.GET.get('Sub_Category')
    # if subcategorySno:
    #     products =addproduct.get_allproduct_bysubcategorySno(subcategorySno)
    # print(mainviewproduct)
    data = {
    'customer_name' :(request.session.get("customer_fname")), 
    'home_carsole': home_carousel.objects.all(),
    'home_banner':home_collection_banner.objects.all(),
    'data':all_data,
    # 'product':products,
    'sub_category':sub_category,
    'trendproduct':trendproduct ,
    'customer_name' :(request.session.get("customer_fname")), 
    'cart':cart,
    'total':total_amount,
    'maincat':maincat,
    'maincat1':maincat1,
    # 'maincategory':maincategories,
    # 'maincategorthumb':maincategorthumb
    # 'mainviewproduct':mainviewproduct
    }
    return render(request,"index.html",data)






def contact(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount 
    data= {
    'contact_section':contact_details_section.objects.all(),
    'contact_banner':banners.objects.all()[3:4],
     'data':all_data,
     'customer_name' :(request.session.get("customer_fname")),
     'total':total_amount ,
     'cart':cart 
    }
    return render(request,"contact.html",data)
def faq(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount  
    faq =Faqs.objects.all()
    faq_banner=banners.objects.all()[4:5]
    return render(request,"faq.html",{'faq':faq,'faq_banner':faq_banner,'data':all_data,'total':total_amount,'cart':cart,'customer_name' :(request.session.get("customer_fname")), })
def privacy(request):
    
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount 
    return render(request,"privacy_policy.html",{'cart':cart,'total':total_amount,'data':all_data,'privacy':Privacy_policy.objects.all(),'customer_name' :(request.session.get("customer_fname")) })
def profile(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount 
    ids = (request.session.get('customer'))
    # user = Singup.get_singup_detail_byid(ids)
    # ids =list(request.session.get('cart').keys())
    
    data = {
     
    'customer_name' :(request.session.get("customer_fname"))  ,
    'lname':(request.session.get('customer_lname')),
    'ph_number':(request.session.get('customer_number')),
    'email':(request.session.get('customer_email'))  ,
    'data':all_data,
    'customer_name' :(request.session.get("customer_fname")), 
    'total':total_amount,'cart':cart
    # 'user':ids
    }
    if request.method =="POST":
        name= request.POST.get('fname',)
        lname = request.POST.get('lname')
        number = request.POST.get('ph_number')
        print(name,lname,number)
        user1 = Singup(id=ids,firstname =name,lastname=lname,number=number ,email_id =(request.session.get('customer_email')), password =(request.session.get('customer_pass')))
        user1.password =encrypt((request.session.get('customer_pass')))
        #   updateuser = isinstance()
        # form = Singupform(request.POST,)
    #     user.firstname =name
    #     user.
        user1.save()
        del request.session['customer']
        redirect('/login')
        messages.success(request,"details updated ,please login again", extra_tags="update")
    
    return render(request,"my-profile.html",data)
def terms(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount 
    terms = Terms_and_Condition.objects.all()
    
    return render(request,"terms.html",{'terms':terms,'data':all_data,'customer_name' :(request.session.get("customer_fname")),'total':total_amount ,'cart':cart })

def register(request):

    if request.method == "POST":

        fname = request.POST["fname"]
        lname = request.POST["lname"]
        phonenumber = request.POST["number"]
        emailid = request.POST["email"]
        password = request.POST["pass"]
        reppass = request.POST["cpass"]
        
        
        
        get_data = Singup(firstname=fname , lastname=lname , number=phonenumber , email_id=emailid , password=password )
        if password == reppass:
            if get_data.email_exists():
                messages.error(request,"email id already exsists", extra_tags="email_exist")
                return redirect("/register")
            else:
                # get_data.password =make_password(get_data.password)
                # key = Fernet.generate_key()
                get_data.password = encrypt(password)
                # get_data.password = password
                # get_data.password = fernet.encrypt(get_data.password.encode())
                get_data.save()
                messages.success(request,"singup sucessfully and please login ", extra_tags="singup_sucess")
                return redirect ( '/login')     
        else:
            messages.error(request,"password not matched" , extra_tags='singuperror')
            return redirect("/register")
    data ={
            'register_banner':banners.objects.all()[5:6] ,
            'data':all_data   ,
            'customer_name' :(request.session.get("customer_fname")), 
            }
    
    return render(request,"register.html",data)

    

def login(request):
    # return_url= None
    login.return_url= request.GET.get('return_url')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass']
        customer = Singup.get_customer_details_by_email(email)
        if customer :

            # key = Fernet.generate_key()
            
            customer.password = decrypt(customer.password)
            # customer.password = str(fernet.decrypt(bytes(customer.password, 'utf-8')), 'utf-8')
            if password == customer.password:
            # if check_password(password, customer.password)== True :
                request.session["customer"] = customer.id 
                request.session["customer_email"] = customer.email_id
                request.session["customer_fname"]= customer.firstname
                request.session["customer_lname"] = customer.lastname
                request.session["customer_number"]= customer.number
                request.session["customer_pass"]= customer.password
                if login.return_url:
                    HttpResponseRedirect(login.return_url)
                else:  
                    login.return_url =None
                    messages.success(request,"login sucessfully", extra_tags='login_sucess')  
                    return redirect('/')
            


            else:
                messages.error(request, "password was not correct",extra_tags= 'loginerror' )
                return redirect('/login')
        else:
            messages.error(request, "email was not correct",extra_tags= 'loginerror' )
            return redirect('/login')  
    # print(request.session.get("customer_fname"))
    data={
        'login_banner':banners.objects.all()[6:7] , 
        'data':all_data,
        'customer_name' :(request.session.get("customer_fname")), 
    }  
    return render(request,"sign_in.html",data)
def handellogout(request):
    del request.session['customer']
    return redirect('/')




def productdetails(request,slug):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount 
    product = addproduct.objects.get(product_slug=slug)
    productrating= productreview.objects.filter( product=product,Parent=None).order_by('-sno')
    rating_avg= productrating.aggregate(Avg('rating'))["rating__avg"]
    if rating_avg == None:
        rating_avg =0
        
    # print(round(rating_avg))
    # totalcount =productrating.count 
    # product_reviewCount= productreview.objects.filter( product=product,Parent=None).values_list('', flat=True).distinct()
    
    # totalratingvalue=  rating*int(totalcount)
    # product.views= product.views+1
    product.save()
    # print(totalcount)
    # print(product_reviewCount)
    # products = addproduct.objects.all
    data={
        # 'data':data,
        'data':all_data,
        'product':product ,
        'productrating':productrating,
        # 'totalratingvalue':totalratingvalue
        # 'totalcount':totalcount
        # 'rating':rating,
        'rating_avg':round(rating_avg),
        'customer_name' :(request.session.get("customer_fname")), 
        'cart':cart,
        'total':total_amount,
        'sizechart':Size_chart.objects.all(),
        'product_return':product_return.objects.all()
    }
    return render(request,"product-details.html",data)
def allproducts(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
        for p in cart_product:  
            if p.cartProduct.discount == False :
                tempamount =(p.quantity * p.cartProduct.discount_price)
            else:
                tempamount =(p.quantity * p.cartProduct.price)
            amount += tempamount
            if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
            else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    maincatid = request.GET.get('maincategory')
    colorid =  request.GET.get('color')
    catid = request.GET.get('category')
    sizeid = request.GET.get('size')
    stock = request.GET.get('stock')
    subcatid = request.GET.get('subcategory')
    productdata = request.GET.get('productname')
    

    
    all_product = addproduct.objects.filter(active = True).order_by('-id')
    
    
    if maincatid:
        all_product = addproduct.objects.filter(main_category__slug =maincatid).order_by('-id')
        
             
    elif catid:
        all_product = addproduct.objects.filter(category__slug = catid).order_by('-id')
    elif subcatid:
        all_product = addproduct.objects.filter(sub_category__slug =subcatid).order_by('-id')
        
    elif colorid:
        all_product = addproduct.objects.filter(color__Color_name=colorid).order_by('-id')
    
    elif sizeid :
        all_product = addproduct.objects.filter(size__Size_name = sizeid).order_by('-id')
    elif stock :
        all_product = addproduct.objects.filter(stock = stock).order_by('-id')
    else:
        all_product = addproduct.objects.filter(active = True).order_by('-id')
    
    
    if request.method =="GET":
        productdata = request.GET.get('productname')
        
        if productdata != None:
            all_product = addproduct.objects.filter(name__icontains=productdata)
            
    item_per_page  =21
    Paginators = Paginator(all_product,item_per_page)
    page_number=request.GET.get("page")
    product_paginator= Paginators.get_page(page_number)
    totalpages =product_paginator.paginator.num_pages
    
    data ={
        'data':all_data,
        'customer_name' :(request.session.get("customer_fname")), 
        # 'allproduct':all_product,
        'cart':cart,
        'total':total_amount,
        'sizechart':Size_chart.objects.all(),
        'product_return':product_return.objects.all(),
        'allproduct':product_paginator,'lastpage':totalpages 
         ,'allpages':[n+1 for n in range(totalpages)],
         'num_pages': Paginators.num_pages,
         'maincatid':maincatid,
         'data1':product_add_slot.objects.all()
    }
    return render(request,"products.html",data)

def plus_cart(request):  
    customer = request.session.get('customer')
    coupon_discount =(request.session.get("coupon_discount"))
    if request.method  == "GET":
        product_id = request.GET["product_id"]
        print(product_id)
        c= add_to_cart.objects.get(Q(cartProduct=product_id) & Q(customer=Singup(id=customer)))
        c.quantity+=1
        c.save()
        amount =0.0
        shipping_amount = 0.0
        total_amount =0.0
        gst=0.0
        discount =0.0
        cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
        if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                    else:
                        total_amount
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                    else:
                        total_amount
            
        data ={
                'quantity':c.quantity,
                'amount':amount,
                'totalamount':total_amount,
                'gst':gst,
                'shipping_amount':shipping_amount,
                'customer_name' :(request.session.get("customer_fname")), 
                'discount':discount
            }
        return JsonResponse(data)
   
def minus_cart(request):  
    customer = request.session.get('customer')
    coupon_discount =(request.session.get("coupon_discount"))
    if request.method  == "GET":
        product_id = request.GET["product_id"]
        print(product_id)
        c= add_to_cart.objects.get(Q(cartProduct=product_id) & Q(customer=Singup(id=customer)))
        if c.quantity == 1:
            c.quantity = 1
        else:
            c.quantity-=1
        
        c.save()
        amount =0.0
        shipping_amount = 0.0
        total_amount =0.0
        gst=0.0
        discount =0.0
        
        cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
        if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                    else:
                        total_amount
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                    else:
                        total_amount
            
        data ={
                'quantity':c.quantity,
                'amount':amount,
                'totalamount':total_amount,
                'gst':gst,
                'shipping_amount':shipping_amount,
                'customer_name' :(request.session.get("customer_fname")), 
                'discount':discount
            }
        return JsonResponse(data)   
    
    
        
def add_to_carts(request):
    
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    
    
    customer = request.session.get('customer')
    if request.method =="GET":
        
        Productid = request.GET.get('productid')
        product= addproduct.objects.get(id=Productid)
        size = request.GET.get('size')
        # id = add_to_cart.objects.get(cart.id)
        quantity = request.GET.get('quantity')
        if quantity == None:
            quantity =1
        
        data= add_to_cart(customer=Singup(id=customer),cartProduct=product ,size =size , quantity=quantity)
        data.save()
        return redirect('/cart')

def show_cart(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    coupon_discount =(request.session.get("coupon_discount"))
    print(cart)
    gst_percentage = 18
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    discount = 0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (gst_percentage/100)
                    total_amount = amount +gst
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                    else:
                        total_amount
                    
                else :
                    shipping_amount= 80
                    gst = amount * (gst_percentage/100)
                    total_amount = amount +gst+shipping_amount
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                    else:
                        total_amount 
                
       
            return render(request,"cart.html",{'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,'customer_name' :(request.session.get("customer_fname")),'data':all_data ,'discount':discount,'coupon_discount':coupon_discount,'gst_percentage':gst_percentage})
    else:
        return render(request,'empty_cart.html',{'cart':cart,'data':all_data, 'customer_name' :(request.session.get("customer_fname")), })   
    

def return_refund(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    return_policy = Return_refund_policy.objects.all()
    data ={
        "return_policy":return_policy,
        'customer_name' :(request.session.get("customer_fname")), 
        'cart':cart,
        'total':total_amount,
        'data':all_data
    }
    return render(request,"return&refund.html", data)

def forgetpassword(request):
    return render(request,"forgetpassword.html")
# def resetpassword(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         customer = Singup.get_customer_details_by_email(email)
#         if customer :
#             if email == customer.email_id:
#                  request.session["customer"] = customer.id 
#                  request.session["customer_password"]=customer.password
#                  return redirect("/updatepassword")
            
#             else:
#                 messages.error(request,"can't find your emailid in database ", extra_tags="wronemailerror")
#                 return redirect("/reset-password")
#         else:
#             messages.error(request,"can't find your emailid in database ", extra_tags="wronemailerror")
#             return redirect("/reset-password")
#     return render(request,"reset_password.html")
def getpasword_in_email(request):
    if request.method == "POST":
        email = request.POST["email"]
        customer = Singup.get_customer_details_by_email(email)
        if customer :
            if email == customer.email_id:
                request.session["customer"] = customer.id 
                request.session["customer_email"] = customer.email_id
                request.session["customer_fname"]= customer.firstname
                request.session["customer_password"]= customer.password
                name = (request.session.get("customer_fname"))
                # email = (request.session.get("customer_email"))
                decryppass=decrypt(request.session.get("customer_password"))
                # encryp_password =(request.session.get("customer_password"))
                # password = check_password(password, hasing_password)
                # decryppass = decrypt(encryp_password)
                print(decryppass)
                email = send_mail(
                f'password of ancifab login account ',
                f'hello {name}  your ancifab account password is{decryppass}',
                'astrologertheindian@gmail.com',
               [f'{request.session.get("customer_email")}'],
                fail_silently=False,)
                del request.session['customer']
                messages.success(request,"your password send into in your register email",extra_tags="sucess_send_pass_email")

                return redirect("/login")
        else:
            messages.error(request, "can't find email address in database",extra_tags="wrong_mail")
        return render(request,"get_password_by_email.html")

    return render(request,"get_password_by_email.html")
def update_password(request):
        request.session.set_expiry(60)
        if request.method == "POST":
            password = request.POST["pass"]
            repass = request.POST["cpass"]
            email = request.POST["email"]
            customer = Singup.get_customer_details_by_email(email)
            if customer :
                if email == customer.email_id:
                    request.session["customer"] = customer.id 
                #     request.session["customer_email"] = customer.email_id
                #     request.session["customer_fname"]= customer.firstname
                    request.session["customer_password"]= customer.password
                    request.session["customer_number"]= customer.number
                    if password ==repass:
                        
                # user=  Singup(id=customer)
                        user1 = Singup.objects.get(id=customer.id)

                        # print(user1.id)
                        # user = user1.customer.password.set_password(password)
                        # user.save()
        #                 # request.session.get["customer_password"] = password 
                        get_data = Singup(Singup,password=customer.number,pk=user1.id)
                        get_data.save(update_fields=["password"]) 
       
        return render(request,"update_password_form.html")


def subcategorywiseview(request,Sno):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    subcategoryview = Sub_Category.objects.get(Sno=Sno)
    colorid = request.GET.get("color")
    print(colorid)
    data = {
        'subcatview':addproduct.objects.filter(sub_category=subcategoryview).order_by('-id'),
        'data':all_data,
        'customer_name' :(request.session.get("customer_fname")), 
            'customer_name' :(request.session.get("customer_fname")), 
            'cart':cart,
            'total':total_amount
            }     
        
    
    return render(request,"productsbysubcategory.html",data)


def categorywiseview(request, Sno):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    categoryview = Category.objects.get(Sno=Sno)
    if categoryview:
        viewbycategory = addproduct.objects.filter(category=categoryview).order_by('-id')
    
   
    return render(request,"productsviewsCategory.html",{'categoryview':viewbycategory,'data':all_data,'customer_name' :(request.session.get("customer_fname")),'total' :total_amount,'cart':cart} )
def maincategorywiseview(request, id):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    maincategoryview = maincategory.objects.get(sno=id)
    colorid = request.GET.get("color")
    print(colorid)
    colorview = addproduct.objects.all()
    viewbymaincategory = addproduct.objects.filter(main_category = maincategoryview).order_by('-id')
 
        
       
    return render(request,"maincategorywiseview.html",{'maincategoryview':viewbymaincategory,'data':all_data,'customer_name' :(request.session.get("customer_fname")), 'cart':cart,'total':total_amount ,'colorview': colorview} )

def productreviews(request):
    
    customer = request.session.get('customer')
    if request.method=="POST":
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        messege = request.POST.get("message")
        productid = request.POST.get("productid")
        product = addproduct.objects.get(id=productid)
       
    # comment = Blogcomment(comment=comment,user=Singup(id=customer),Blogpost=post)
        review = productreview(rating=rating,review_title=review,messege=messege,user=Singup(id=customer),product=product)
        review.save()
    return redirect(f"/products/productdetail/{product.product_slug}")


def generalquery(request):
    
    if request.method =="POST":
        name =  request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        sub = request.POST.get('subject')
        messege = request.POST.get('message')
        
        generalqueries = generalQuery(name=name,email=email,number= number,subject=sub,mesege=messege)
        generalqueries.save()
        # messages.success(request, "your messege send our admin", extra_tags="genarel_success")
        email = send_mail(
                f'Genreal query of {name}',
                f'this is query from {name} , {name} email id is {email } , {name} phone number is {number},{name} talk about {sub} and {name} messege is {messege}',
                'astrologertheindian@gmail.com',
               [f'souravjoyti@gmail.com'],
                fail_silently=False,)
               
        messages.success(request, "your messege send our admin", extra_tags="genarel_success")     
        return redirect("/contact")
        
def productquery(request):
    if request.method =="POST":
        name =  request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        p_name= request.POST.get('p_name')
        p_code = request.POST.get('p_code')
        messege = request.POST.get('message')
        print(name, email, number,p_name,p_code, messege)
        productqueries = productQuery(name=name,email=email,number= number,productname=p_name,productcode=p_code,mesege=messege)
        productqueries.save()
        messages.success(request, "your product query send our admin", extra_tags="Product_success")
        email = send_mail(
                f'Product query of {name} and query product is {p_name}',
                f'this is query from {name} , {name} email id is {email } , {name} phone number is {number} , {name} enquery product is {p_name} product code is {p_code} and {name} messege is {messege} ',
                'astrologertheindian@gmail.com',
               [f'souravjoyti@gmail.com'],
                fail_silently=False,)
        return redirect("/contact")
        

def resetpasswordlink_in_email(request):
    if request.method == "POST":
        email = request.POST["email"]
        customer = Singup.get_customer_details_by_email(email)
        if customer :
            if email == customer.email_id and customer.block == False:
                request.session["customer"] = customer.id 
                request.session["customer_email"] = customer.email_id
                request.session["customer_fname"]= customer.firstname
                name = (request.session.get("customer_fname"))
                id = (request.session.get("customer"))
                count_passchange = Singup.objects.get(id = id)
                count_passchange.forgetpass =  count_passchange.forgetpass+1
                count_passchange.save(update_fields=['forgetpass'])
                if count_passchange.forgetpass >= 3:
                    customer = Singup.objects.get(id = id)
                    customer.block = True
                    customer.save(update_fields=['block'])
                    messages.error(request,"you can't change password in 24 hours",extra_tags="error_forget_pass")
                else:
                       
                    email = send_mail(
                    f'password of ancifab login account ',
                    f'hello {name}  your ancifab account password reset link is http://127.0.0.1:8000/passwordrest/{id}',
                    'astrologertheindian@gmail.com',
                    [f'{request.session.get("customer_email")}'],
                    fail_silently=False,)
                    messages.success(request,"your password reset link send into in your register email",extra_tags="sucess_send_pass_email")
                del request.session['customer']
                # if emailcount =(request.session.get("customer_email".count())
                # print(email.count())
                    

                return redirect("/resetpasswordlink_in_email")
            else:
                messages.error(request, "can't find email address in database or block your account",extra_tags="wrong_mail")
                return redirect("/resetpasswordlink_in_email")
            
    return render(request,"reset_password.html")
    
    
def passwordreset_byEmail(request,id):
    if request.method == 'POST':
        password = request.POST.get('pass')
        data1 = Singup.objects.get(pk=id)
        data1.password = encrypt(password)
        data1.save(update_fields=['password'])
        return redirect("/")
    return render(request,"passwordreset.html" )

def checkout(request):
    
    # cart = request.session.get('cart')
    # ids =list(request.session.get('cart').keys())
    # products = addproduct.get_Products_by_id(ids)
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    coupon_discount =(request.session.get("coupon_discount"))
    gst_percentage = 18
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    discount = 0.0
    
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (gst_percentage/100)
                    total_amount = amount +gst
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                    else:
                        total_amount
                    
                else :
                    shipping_amount= 80
                    gst = amount * (gst_percentage/100)
                    total_amount = amount +gst+shipping_amount
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                    else:
                        total_amount 
    data={
    'data':all_data,
    'checkout_banner':banners.objects.all()[7:8] , 
    # 'products':products,
    'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,
    'customer_name' :(request.session.get("customer_fname")), 
    'gst_percentage':gst_percentage,
    'discount':discount,
    'coupon_discount':coupon_discount
    }
    
    return render(request,"checkout.html",data)


def selectpaymentmethod(request):
    context ={
        
    }
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    coupon_discount =(request.session.get("coupon_discount"))
    gst_percentage = 18
    print(cart)
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    quantity =0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (gst_percentage/100)
                    total_amount = amount +gst
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                        quantity = p.quantity
                    else:
                        total_amount
                        quantity = p.quantity
                    
                else :
                    shipping_amount= 80
                    gst = amount * (gst_percentage/100)
                    total_amount = amount +gst+shipping_amount
                    if coupon_discount:
                        discount = total_amount*(coupon_discount/100)
                        total_amount = total_amount - discount
                        quantity = p.quantity
                    else:
                        total_amount 
                        quantity = p.quantity
    if request.method == "POST":
       customer_id =Singup(id =customer)
       email = request.session.get('customer_email')
       fname = request.POST.get('name')
       lname = request.POST.get('lname')
       cname =request.POST.get('cname')
       country = request.POST.get('country')
       Street_adress = request.POST.get('address')
       town = request.POST.get('town')
       state = request.POST.get('state')
       pincode = request.POST.get('pin')
       number = request.POST.get('number')
       shipping = shipping_amount
       gst = gst
       total = total_amount
       razorpaytotal  = total*100 
       
   
    context ={'customer':customer_id,'email':email,'fname':fname,'lname':lname,'cname':cname,'country':country,'Street_adress':Street_adress,'town':town,'state':state,'pincode':pincode,'number':number,'shipping':shipping,'gst':gst,'total':total,'quantity':quantity,'data':all_data
        ,'cart':cart,'razorpaytotal':razorpaytotal
    }
   
    
    
    
    return render( request,"select-payment-method.html",context)

# @csrf_exempt
def cashpayment(request):
  
    
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    code = request.session.get('coupon_code')
    customer_id =Singup(id =customer)
    email = request.POST.get('email')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    cname =request.POST.get('cname')
    country = request.POST.get('country')
    Street_adress = request.POST.get('Street_adress')
    town = request.POST.get('town')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')
    number = request.POST.get('number')
    shipping = request.POST.get('shipping')
    gst = request.POST.get('gst')
    total = request.POST.get('total')
    # print(customer_id,email,fname,lname,cname,country,Street_adress,town,state,pincode,number,shipping,gst,total,number)
    order = AllOrders(customer=customer_id,emailid= email, firstname=fname,lastname=lname
                     ,company_name = cname, country=country,Street_adress=Street_adress
                   ,town=town, state=state,pincode=pincode,number =number,shipping=shipping,gst=gst,total=total,payment_mood= "cod" )
    order.save()
    if request.session.get("coupon_discount"):
        del request.session["coupon_code"]
    
    for c in cart :
        if c.cartProduct.discount == False:
            totalprice = c.quantity*c.cartProduct.discount_price
            price = c.cartProduct.discount_price
        else:
            totalprice = c.quantity*c.cartProduct.price
            price = c.cartProduct.price
        orderitem = ALlorderItem(product = c.cartProduct,
                              price = price,
                              quantity = c.quantity,
                              image = c.cartProduct.Thrumnil,
                              producttotal = totalprice,
                              orderid = AllOrders.objects.get(id = order.id),
                              size = c.size
                              )
        
        orderitem.save()
        c.delete()
    
    return redirect("/orderstatus")

def onlinepayment(request):
    # payment = client.order.create({
    #     'amount':500,
    #     'currency':"INR",
    #     'payment_capture':"1"
    # })
    # context ={
    #     'order_id':order_id,
    #     'payment':payment
    # }
    # # print(payment)
    # order_id = payment['id']
    # context ={
    #     'order_id':order_id,
    #     'payment':payment
    # }
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    customer_id =Singup(id =customer)
    email = request.POST.get('email')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    cname =request.POST.get('cname')
    country = request.POST.get('country')
    Street_adress = request.POST.get('Street_adress')
    town = request.POST.get('town')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')
    number = request.POST.get('number')
    shipping = request.POST.get('shipping')
    gst = request.POST.get('gst')
    total = request.POST.get('total')
    order_id = request.POST.get('order_id')
    razorpaytotal =request.POST.get('razorpaytotal')
    # print(customer_id,email,fname,lname,cname,country,Street_adress,town,state,pincode,number,shipping,gst,total,number)
    order = AllOrders(customer=customer_id,emailid= email, firstname=fname,lastname=lname
                     ,company_name = cname, country=country,Street_adress=Street_adress
                   ,town=town, state=state,pincode=pincode,number =number,shipping=shipping,gst=gst,total=total,payment_mood= "online" 
    ,paid= True)
    
    order.save()
    
    for c in cart :
        if c.cartProduct.discount == False:
            totalprice = c.quantity*c.cartProduct.discount_price
            price = c.cartProduct.discount_price
        else:
            totalprice = c.quantity*c.cartProduct.price
            price = c.cartProduct.price
        orderitem = ALlorderItem(product = c.cartProduct,
                              price = price,
                              quantity = c.quantity,
                              image = c.cartProduct.Thrumnil,
                              producttotal = totalprice,
                              orderid = AllOrders.objects.get(id = order.id),
                              size = c.size
                              )
        
        orderitem.save()
        c.delete()
    
    return redirect(f"/orderstatus")

def orderstatus(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    returnorder = ReturnAllOrders.objects.filter(customer=Singup(id=customer)).order_by('-id')
    
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    order ={
     'order' :AllOrders.objects.filter(customer=customer).order_by('-id'),
     'cancel_order':CancelAllOrders.objects.filter(customer=customer).order_by('-id'),
     'data':all_data, 'returnorder':returnorder,
    'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,
    'customer_name' :(request.session.get("customer_fname")), 
    
    }
   
    return render(request,'oder-status.html',order )


def order_product_summary(request,id):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    oderItem = ALlorderItem.objects.filter(orderid =id)
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    order ={
     'order' :AllOrders.objects.get(id= id),
     'allorderitem':oderItem,
     'data':all_data, 
    'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,
    'customer_name' :(request.session.get("customer_fname")), 
    
    }
   
    return render(request,'product_summary.html',order )

def paymentpage(request):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    razorpaytotal =request.POST.get('razorpaytotal')
    return render(request,'paymentpage.html',{'razorpaytotal':razorpaytotal})
    
    
def ordertracking(request,order_id):
    allorder =AllOrders.objects.get(order_id= order_id)
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer)) 
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    order={
        'allorder':allorder, 'data':all_data, 
        
    'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,
    'customer_name' :(request.session.get("customer_fname")), 
    }
    return render(request,'ordertracking.html',order) 




def cancelorderlist(request):
    if request.method =="POST":
        id = request.POST["id"]
        customer = request.session.get('customer')
        emailid = request.POST["emailid"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        paid = request.POST["paid"]
        gst = request.POST["gst"]
        total = request.POST["total"]
        shipping = request.POST["shipping"]
        order_id = request.POST["order_id"]
        payment_mood = request.POST["payment_mood"]
        bank_details = request.POST["bank_details"]
        reson_cancel = request.POST["reson_cancel"]
        cancelorder = CancelAllOrders(customer=Singup(id =customer),
                                      emailid=emailid,
                                      firstname=firstname,
                                      lastname=lastname,
                                      paid=paid,
                                      gst=gst,
                                      total=total,
                                      shipping=shipping,
                                      order_id=order_id,
                                      payment_mood=payment_mood,
                                      bank_details=bank_details,
                                      reson_cancel=reson_cancel)
        cancelorder.save()
        
        ordercancelproduct = ALlorderItem.objects.filter(orderid = id)
        for p in ordercancelproduct:
            cancelorderitem = cancelordersItem(product = p.product,
                              price = p.price,
                              quantity = p.quantity,
                              image = p.image,
                              producttotal = p.producttotal,
                              cancelid = CancelAllOrders.objects.get(id = cancelorder.id),
                              size = p.size
                              )
            cancelorderitem.save()
            p.delete()
        orderdelete = AllOrders.objects.get(order_id=order_id)
        orderdelete.delete()
    return redirect('/orderstatus')
def cancel_product_summary(request,id):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    oderItem = cancelordersItem.objects.filter(cancelid =id)
   
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    order ={
     'order' :CancelAllOrders.objects.get(id= id),
     'allorderitem':oderItem,
     'data':all_data, 
    'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,
    'customer_name' :(request.session.get("customer_fname")), 
    
    }
   
    return render(request,'returnproductSummary.html',order )        
        
def returnorders(request):
    if request.method =="POST":
        id = request.POST["id"]
        customer = request.session.get('customer')
        emailid = request.POST.get("emailid")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        paid = request.POST.get("paid")
        gst = request.POST.get("gst")
        total = request.POST.get("total")
        shipping = request.POST.get("shipping")
        order_id = request.POST.get("order_id")
        payment_mood = request.POST.get("payment_mood")
        bank_details = request.POST.get("bank_details")
        reson_cancel = request.POST.get("reson_cancel")
        productImage = request.FILES.get("productimage")
        address = request.POST.get("address")
        cancelorder = ReturnAllOrders(customer=Singup(id =customer),
                                      emailid=emailid,
                                      firstname=firstname,
                                      lastname=lastname,
                                      paid=paid,
                                      gst=gst,
                                      total=total,
                                      shipping=shipping,
                                      order_id=order_id,
                                      payment_mood=payment_mood,
                                      bank_details=bank_details,
                                      reson_cancel=reson_cancel,
                                      cancelproductImage =productImage,
                                      address=address)
        cancelorder.save()
        
        ordercancelproduct = ALlorderItem.objects.filter(orderid = id)
        for p in ordercancelproduct:
            cancelorderitem = ReturnordersItem(product = p.product,
                              price = p.price,
                              quantity = p.quantity,
                              image = p.image,
                              producttotal = p.producttotal,
                              cancelid = ReturnAllOrders.objects.get(id = cancelorder.id),
                              size = p.size
                              )
            cancelorderitem.save()
            p.delete()
        orderdelete = AllOrders.objects.get(order_id=order_id)
        orderdelete.delete()
    
        
        
    return redirect('/orderstatus')


def return_product_summary(request,id):
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    oderItem = ReturnordersItem.objects.filter(cancelid =id)
    print(oderItem)
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    order ={
     'order' :ReturnAllOrders.objects.get(id= id),
     'allorderitem':oderItem,
     'data':all_data, 
    'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,
    'customer_name' :(request.session.get("customer_fname")), 
    
    }
   
    return render(request,'returnproductSummary.html',order )


def returnordertracking(request,order_id):
    allorder =ReturnAllOrders.objects.get(order_id= order_id)
    customer = request.session.get('customer')
    cart = add_to_cart.objects.filter(customer=Singup(id=customer))
    
    print()
    amount =0.0
    shipping_amount = 0.0
    total_amount =0.0
    gst=0.0
    cart_product =[p for p in add_to_cart.objects.all() if p.customer==Singup(id=customer)]
    #    print(cart_product)
    if cart_product:
            for p in cart_product:  
                if p.cartProduct.discount == False :
                    tempamount =(p.quantity * p.cartProduct.discount_price)
                else:
                    tempamount =(p.quantity * p.cartProduct.price)
                amount += tempamount
                if amount >=2000:
                    shipping_amount =0.0
                    gst = amount * (18/100)
                    total_amount = amount +gst
                else :
                    shipping_amount= 80
                    gst = amount * (18/100)
                    total_amount = amount +gst+shipping_amount
    order={
        'allorder':allorder, 'data':all_data, 
        
    'cart':cart,'total':total_amount,'amount':amount,'gst':gst,'shipping':shipping_amount,
    'customer_name' :(request.session.get("customer_fname")), 
    }
    return render(request,'returnordertrack.html',order) 



def coupon_apply(request):
    now = timezone.now()
    # form = CouponForm(request.POST)
    if request.method == "POST":
        code = request.POST["coupon"]
        
        try:
            coupon = Coupon.objects.get(code__iexact = code,
                                        valid_from__lte = now,
                                        valid_to__gte = now, active = True)
            request.session['coupon_id']=coupon.id
            request.session['coupon_code'] = coupon.code
            request.session['coupon_discount'] = coupon.discount
            print((request.session.get("coupon_discount")))
            messages.success(request,"Coupon Applied",extra_tags="valid_coupon")
        except Coupon.DoesNotExist:
            request.session['coupon_id']= None
            messages.error(request,"invalid coupon",extra_tags="invalid_coupon")
        return redirect('/cart')
    return(request,'cart.html')
def remove_coupon(request):
    del request.session["coupon_code"]
    del request.session["coupon_discount"]
    return redirect('/cart')
    
    


    