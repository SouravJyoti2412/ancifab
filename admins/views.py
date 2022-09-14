from pyexpat.errors import messages
from tkinter import ACTIVE
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from customer_login.models import Singup
from settings.forms import WebsiteLogoForm
from settings.models import WebsiteLogo
from userinterphase.models import About_us, Faqs,Terms_and_Condition,Return_refund_policy,contact_details_section,home_carousel,home_collection_banner,banners,Blog, Blogcomment ,Aboutus_heading,Privacy_policy
from taggit.models import Tag
from django.template.defaultfilters import slugify
from Products.models import WebsiteLogos, addproduct
from userinterphase.forms import aboutusForm, FaqsForm,Terms_and_ConditionForm,Return_refund_policyForm,contact_details_sectionForm,home_carouselForm,home_collection_bannerForm,bannersForm,BlogForm ,Aboutus_headingForm,Privacy_policyForm
from .forms import LoginForm, SignUpForm
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from Products.models import ProductSize,ProductColor,maincategory,Category,Sub_Category,addproduct,productreview,generalQuery,productQuery,Size_chart,product_return,AllOrders,ALlorderItem,CancelAllOrders,cancelordersItem,ReturnAllOrders,ReturnordersItem
from Products.forms import ProductColorForm,ProductSizeForm,CatagoryForm,Sub_CategoryForm, WebsiteLogosForm,maincategoryForm,productaddingForm,Size_chartForm,product_returnForm
from django.core.paginator import Paginator
from ADVATISMENT.models import product_add_slot
from ADVATISMENT.forms import product_add_slotForm
from SOCIAL_ICON.models import Social_icon_adding
from SOCIAL_ICON.forms import Social_icon_addingForm
from django.http import HttpResponse
from website_settings.models import LogoField, Slogan
from website_settings.forms import LogoFieldForm, SloganForm
import json
from django.contrib.auth import logout as auth_logout
# def get_subcategory(request):
#     Sno = request.GET.get('Sno', '')
#     result = list(Sub_Category.objects.filter(
#     category_Sno=int(Sno)).values('Sno', 'name'))
#     return HttpResponse(json.dumps(result), content_type="application/json")


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/admins/dashboard")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
        
    return render(request, "dashboards/accounts/login.html", {"form": form, "msg": msg})
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "dashboards/accounts/register.html", {"form": form, "msg": msg, "success": success})

# def logout(request):
    



@login_required(login_url="admins/login/")
def productsize(request):
    form = ProductSizeForm
    context = {'form':form,'size':ProductSize.objects.all()}
    if request.method =="POST":
        form= ProductSizeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"your product size upload sucessfully",extra_tags="upload_success")
            return redirect('/admins/addproductssize')
        else :
            messages.error(request,"your product size not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/addproductssize')
    html_template = loader.get_template('dashboards/Product_Size.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="admins/login/")
def productsize_delete(request,Sno):
    if request.method == 'POST':
        data1 = ProductSize.objects.get(pk=Sno)
        data1.delete()
        messages.success(request,"size delete sucessfully",extra_tags="upload_success")
        return redirect('/admins/addproductssize/')
@login_required(login_url="admins/login/")
def productsize_update(request,Sno):
    
    data = ProductSize.objects.get(pk=Sno)
    form = ProductSizeForm(request.POST ,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,"size update sucessfully",extra_tags="upload_success")
        return redirect('/admins/addproductssize/')
    else :
        data = ProductSize.objects.get(pk=Sno)
        form = ProductSizeForm(instance=data)
    return render(request,'dashboards/Product_Size_update.html',{'form':form}) 




@login_required(login_url="admins/login/")
def productupload(request):
    # addproducts = addproduct.objects.all()
    # common_tags =addproduct.Meta_name.most_common()[:4]
    form = productaddingForm
    context = {'form':form}
    if request.method =="POST":
        form = productaddingForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,"your product upload sucessfully",extra_tags="upload_success")
            return redirect('/admins/productupload')
        else :
            messages.error(request,"your product not uploaded",extra_tags="upload_unsuccess")
            return HttpResponseRedirect('/admins/productupload')
    html_template = loader.get_template('dashboards/products/productUpload/product_upload.html')
    return HttpResponse(html_template.render(context, request))




@login_required(login_url="admins/login/")
def productmanage(request):
    # productsearch = addproduct.objects.all()
    
            
            
    # addproducts = addproduct.objects.all()
    # common_tags =addproduct.Meta_name.most_common()[:4]
    form = productaddingForm
    product = addproduct.objects.all().order_by('-id')
    if request.method =="GET":
        productdata = request.GET.get('productname')
    if productdata != None:
        product = addproduct.objects.filter(name__icontains = productdata)
    
    allproductcount = addproduct.objects.all().count()
    draftProductcount = addproduct.objects.filter(active=False).count()
    activeProductcount = addproduct.objects.filter(active=True).count()
    trendingcount = addproduct.objects.filter(trending=True).count()
    item_per_page =10
    Paginators = Paginator(product,item_per_page)
    page_number=request.GET.get("page")
    product_paginator= Paginators.get_page(page_number)
    totalpages =product_paginator.paginator.num_pages
    
    
    context = {'form':form,
                      'product':product_paginator,'lastpage':totalpages 
                      ,'allpages':[n+1 for n in range(totalpages)],
                      'num_pages': Paginators.num_pages,
                      'allproductcount' : allproductcount,
                      'draftProductcount':draftProductcount,
                      'active_productcount':activeProductcount,
                      'trendingcount':trendingcount,
                     
                     }
    
    html_template = loader.get_template('dashboards/products/productUpload/productmanage.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="admins/login/")
def product_delete(request,id):
    if request.method == 'POST':
        data1 = addproduct.objects.get(pk=id)
        data1.delete()
        messages.success(request,"product delete sucessfully",extra_tags="delete_success")
        return redirect('/admins/product_manage/')
@login_required(login_url="admins/login/")
def product_pending(request,id):
    if request.method == 'POST':
        data1 = addproduct.objects.get(pk=id)
        data1.active = False 
        data1.save(update_fields=['active'])
        messages.success(request,"product pending sucessfully",extra_tags="pending_success")
        return redirect('/admins/product_manage/')
@login_required(login_url="admins/login/")
def product_active(request,id):
    if request.method == 'POST':
        data1 = addproduct.objects.get(pk=id)
        data1.active = True 
        data1.save(update_fields=['active'])
        messages.success(request,"product active sucessfully",extra_tags="active_success")
        return redirect('/admins/product_manage/')
@login_required(login_url="admins/login/")
def product_out_of_stock(request,id):
    if request.method == 'POST':
        data1 = addproduct.objects.get(pk=id)
        data1.stock= False 
        data1.save(update_fields=['stock'])
        messages.success(request,"product out of stock sucessfully",extra_tags="out_of_stock_success")
        return redirect('/admins/product_manage/')
@login_required(login_url="admins/login/")
def product_in_stock(request,id):
    if request.method == 'POST':
        data1 = addproduct.objects.get(pk=id)
        data1.stock= True
        data1.save(update_fields=['stock'])
        messages.success(request,"product in stock sucessfully",extra_tags="in_stock_success")
        return redirect('/admins/product_manage/')
    
def product_update(request,id):
    data = addproduct.objects.get(pk=id)
    form = productaddingForm
    
    if request.method =="POST":
        form= productaddingForm(request.POST, request.FILES,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"your product update sucessfully",extra_tags="Product_update_success")
            return redirect('/admins/product_manage')
        else :
            data = addproduct.objects.get(pk=id)
            form = productaddingForm(instance=data)
        return render(request,'dashboards/products/productUpload/product_update.html',{'form':form})
def mark_as_trending(request,id):
    if request.method == 'POST':
        data1 = addproduct.objects.get(pk=id)
        data1.trending= True
        data1.save(update_fields=['trending'])
        messages.success(request,"product is trending now",extra_tags="trending_success")
        return redirect('/admins/product_manage/') 
def mark_as_normal(request,id):
    if request.method == 'POST':
        data1 = addproduct.objects.get(pk=id)
        data1.trending= False
        data1.save(update_fields=['trending'])
        messages.success(request,"product is normal now",extra_tags="normal_success")
        return redirect('/admins/product_manage/')     


@login_required(login_url="admins/login/")
def color_name(request):
    form = ProductColorForm
    
    context = {'form':form,
               'color':ProductColor.objects.all()}
    if request.method =="POST":
        form= ProductColorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"your product color adding sucessfully",extra_tags="upload_success")
            return redirect('/admins/add_colors')
        else :
            messages.error(request,"your product color not added",extra_tags="upload_unsuccess")
            return redirect('/admins/add_colors')
    html_template = loader.get_template('dashboards/productsColor.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="admins/login/")
def color_delete(request,Sno):
    if request.method == 'POST':
        data1 = ProductColor.objects.get(pk=Sno)
        data1.delete()
        messages.success(request,"color delete sucessfully",extra_tags="upload_success")
        return redirect('/admins/add_colors')
@login_required(login_url="admins/login/")
def color_update(request,Sno):
    
    data = ProductColor.objects.get(pk=Sno)
    form = ProductColorForm(request.POST ,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,"color update sucessfully",extra_tags="upload_success")
        return redirect('/admins/add_colors')
    else :
        data = ProductColor.objects.get(pk=Sno)
        form = ProductColorForm(instance=data)
    return render(request,'dashboards/productscolor_update.html',{'form':form}) 








@login_required(login_url="admins/login/")
def maincategories(request):
    
    form = maincategoryForm
    context = {'form':form, 'main_category':maincategory.objects.all().order_by('-sno')}
    if request.method =="POST":
        form= maincategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"your product main category upload sucessfully",extra_tags="upload_success")
            return redirect('/admins/maincategory')
        else :
            messages.error(request,"your product main category not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/maincategory')
    html_template = loader.get_template('dashboards/products/main_category/maincategory.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def maincategory_delete(request,sno):
    if request.method == 'POST':
        data1 = maincategory.objects.get(pk=sno)
        data1.delete()
        messages.success(request,"main category delete sucessfully",extra_tags="upload_success")
        return redirect('/admins/maincategory')
@login_required(login_url="admins/login/")
def maincategories_update(request,sno):
    
    data = maincategory.objects.get(pk=sno)
    form = maincategoryForm(request.POST ,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,"your product main category update sucessfully",extra_tags="upload_success")
        return redirect('/admins/maincategory')
    else :
        data = maincategory.objects.get(pk=sno)
        form = maincategoryForm(instance=data)
    return render(request,'dashboards/products/main_category/maincategory_update.html',{'form':form}) 

@login_required(login_url="admins/login/")
def category(request):
    
    form = CatagoryForm
    context = {'form':form ,'category':Category.objects.all().order_by('-Sno')}
    if request.method =="POST":
        form= CatagoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"your product category add sucessfully",extra_tags="upload_success")
            return redirect('/admins/category')
        else :
            messages.error(request,"your product category not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/category')
    html_template = loader.get_template('dashboards/products/category/category.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="admins/login/")
def category_update(request , Sno):
    data = Category.objects.get(pk=Sno)
    form = CatagoryForm(request.POST ,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,"Category update sucessfully",extra_tags="upload_success")
        return redirect('/admins/category')
    else :
        data = Category.objects.get(pk=Sno)
        form = CatagoryForm(instance=data)
    return render(request,'dashboards/products/category/updatecategory.html',{'form':form}) 

@login_required(login_url="admins/login/")
def category_delete(request , Sno):
    if request.method == 'POST':
        data1 = Category.objects.get(pk=Sno)
        data1.delete()
        messages.success(request,"category delete sucessfully",extra_tags="upload_success")
        return redirect('/admins/category')
    
@login_required(login_url="admins/login/")
def subcategory(request):
    
    form = Sub_CategoryForm
    context = {'form':form , 'subcategory':Sub_Category.objects.all().order_by('-Sno')}
    if request.method =="POST":
        form= Sub_CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"your product size upload sucessfully",extra_tags="upload_success")
            return redirect('/admins/subcategory')
        else :
            messages.error(request,"your product size not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/subcategory')
    html_template = loader.get_template('dashboards/products/subcategory/sub_category.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="admins/login/")
def subcat_update(request , Sno):
    data = Sub_Category.objects.get(pk=Sno)
    form = Sub_CategoryForm(request.POST ,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,"Sub category update sucessfully",extra_tags="upload_success")
        return redirect('/admins/subcategory')
    else :
        data = Sub_Category.objects.get(pk=Sno)
        form = Sub_CategoryForm(instance=data)
    return render(request,'dashboards/products/subcategory/updatesubcategory.html',{'form':form}) 

@login_required(login_url="admins/login/")
def subcategory_delete(request , Sno):
    if request.method == 'POST':
        data1 = Sub_Category.objects.get(pk=Sno)
        data1.delete()
        messages.success(request,"subcategory delete sucessfully",extra_tags="upload_success")
        return redirect('/admins/subcategory')




@login_required(login_url="admins/login/")
def dashboard(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('dashboards/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="admins/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/dashboard')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
        
        html_template = loader.get_template('dashboards/index.html')
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('dashboards/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('dashboards/page-500.html')
        return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def customer(request):
    context = {'customer':Singup.objects.all()}

    html_template = loader.get_template('dashboards/user/customer.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def Customer_delete_data(request, id):
    if request.method == 'POST':
        data1 = Singup.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/customer')
@login_required(login_url="admins/login/")
def aboutus(request):
    form = aboutusForm
    context = {'aboutus':About_us.objects.all(),
               'aboutus_heading':Aboutus_heading.objects.all(),
               'form':form}
    if request.method =="POST":
        form= aboutusForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"about us details added sucessfully",extra_tags="upload_success")
            return redirect('/admins/aboutus')
        else :
            messages.error(request,"about us details not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/aboutus')

    html_template = loader.get_template('dashboards/userinterface/about_us.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="admins/login/")
def About_heading_update_data(request, id):
    if request.method == 'POST':
        data1 = Aboutus_heading.objects.get(pk=id)
        fm = Aboutus_headingForm(request.POST ,request.FILES,instance=data1)
        if fm.is_valid():
            fm.save()
            messages.success(request,"about us heading details update sucessfully",extra_tags="update_success")
            return redirect('/admins/aboutus')
        else :
            data1 = Aboutus_heading.objects.get(pk=id)
            fm = Aboutus_headingForm(instance=data1)
            
            
        messages.error(request,"about us details not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/aboutus_heading_update.html',{'form':fm})







@login_required(login_url="admins/login/")
def About_delete_data(request, id):
    if request.method == 'POST':
        data1 = About_us.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/aboutus')
@login_required(login_url="admins/login/")
def About_update_data(request, id):
    if request.method == 'POST':
        data1 = About_us.objects.get(pk=id)
        fm = aboutusForm(request.POST ,request.FILES,instance=data1)
        if fm.is_valid():
            fm.save()
            messages.success(request,"about us details update sucessfully",extra_tags="update_success")
            return redirect('/admins/aboutus')
        else :
            data1 = About_us.objects.get(pk=id)
            fm = aboutusForm(instance=data1)
            
            
        messages.error(request,"about us details not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/aboutus_update.html',{'form':fm})
    
@login_required(login_url="admins/login/")
def faq(request):
    form = FaqsForm
    context = {'aboutus':Faqs.objects.all(),
               'form':form}
    if request.method =="POST":
        form= FaqsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"faq details added sucessfully",extra_tags="upload_success")
            return redirect('/admins/faq')
        else :
            messages.error(request,"faqdetails not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/faq')

    html_template = loader.get_template('dashboards/userinterface/faqs/faq.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def faq_delete_data(request, id):
    if request.method == 'POST':
        data1 = Faqs.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/faq')
@login_required(login_url="admins/login/")
def faq_update_data(request, id):
    if request.method == 'POST':
        data = Faqs.objects.get(pk=id)
        fm = FaqsForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"faq details update sucessfully",extra_tags="update_success")
            return redirect('/admins/faq')
        else :
            data = Faqs.objects.get(pk=id)
            fm = FaqsForm(instance=data)
            
            
        messages.error(request,"faqdetails not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/faqs/faq_update.html',{'form':fm})
    
    
    
    
    
    
    
    
@login_required(login_url="admins/login/")
def Privacy(request):
    form = Privacy_policyForm
    context = {'aboutus':Privacy_policy.objects.all(),
               'form':form}
    if request.method =="POST":
        form= Privacy_policyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Privacy details added sucessfully",extra_tags="upload_success")
            return redirect('/admins/Privacy')
        else :
            messages.error(request,"Privacy details not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/Privacy')

    html_template = loader.get_template('dashboards/userinterface/Privacy/Privacy_policy.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def Privacy_delete_data(request, id):
    if request.method == 'POST':
        data1 = Privacy_policy.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/Privacy')
@login_required(login_url="admins/login/")
def Privacy_update_data(request, id):
    if request.method == 'POST':
        data = Privacy_policy.objects.get(pk=id)
        fm = Privacy_policyForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Privacy details update sucessfully",extra_tags="update_success")
            return redirect('/admins/Privacy')
        else :
            data = Privacy_policy.objects.get(pk=id)
            fm = Privacy_policyForm(instance=data)
            
            
        messages.error(request,"privacydetails not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/Privacy/Privacy_policy_update.html',{'form':fm})
    
    
    
    
    
    
    
@login_required(login_url="admins/login/")
def contact(request):
    context = {'aboutus':contact_details_section.objects.all(),
               }

    html_template = loader.get_template('dashboards/userinterface/contact_us/contactUs.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def contact_update_data(request, id):
    if request.method == 'POST':
        data = contact_details_section.objects.get(pk=id)
        fm = contact_details_sectionForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Contact details update sucessfully",extra_tags="update_success")
            return redirect('/admins/contactus')
        else :
            data = contact_details_section.objects.get(pk=id)
            fm = contact_details_sectionForm(instance=data)
            
            
        messages.error(request,"contactdetails not update",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/contact_us/contact_update.html',{'form':fm})    
    
@login_required(login_url="admins/login/")
def productreviews(request):
    
    context ={
        'review': productreview.objects.all()
    }
    return render(request,'dashboards/products/productsreview/productreview.html',context)

@login_required(login_url="admins/login/")
def review_delete(request,sno):
    if request.method == 'POST':
        data1 = productreview.objects.get(pk=sno)
        data1.delete()
        
    return redirect("/admins/productreviews")



@login_required(login_url="admins/login/")
def queries(request):
    genarel_query =  generalQuery.objects.all().order_by('-id')
    unreadcount = generalQuery.objects.filter(view=False).count()
    productunreadcount =productQuery.objects.filter(view=False).count()
    
    product_query =productQuery.objects.all().order_by('-id')
    item_per_page = 10
    Paginators = Paginator(genarel_query,item_per_page)
    page_number=request.GET.get("page")
    general_query_paginator = Paginators.get_page(page_number)
    totalpages =general_query_paginator.paginator.num_pages
    
    # product_query =productQuery.objects.all(),
    product_Paginators = Paginator(product_query,10)
    page=request.GET.get("pages")
    product_query_paginator = product_Paginators.get_page(page)
    totalpaginatorpages =product_query_paginator.paginator.num_pages
    
    
    
    context ={
        # 'genarelquery': genarel_query,
        
        'genarelquery':general_query_paginator,
        'allpages':[n+1 for n in range(totalpages)],
        'num_pages': Paginators.num_pages,
        
        'unreadcount':unreadcount,
        'productunreadcount':productunreadcount,
        'productquery':product_query_paginator,
        'allpage':[j+1 for j in range(totalpaginatorpages)],
        'num_of_pages':product_Paginators.num_pages
        
    }
    return render(request,'dashboards/products/queries/queries.html',context)
    
@login_required(login_url="admins/login/")
def generalqueries_delete(request,id):
    if request.method == 'POST':
        data1 = generalQuery.objects.get(pk=id)
        data1.delete()
    return redirect("/admins/queries/")
@login_required(login_url="admins/login/")
def generalqueries_view(request,slug):
    genarelquery = generalQuery.objects.filter(slug=slug).first()
    genralquires={
   'genralqurey' : genarelquery
       }
    return render(request,'dashboards/products/queries/genrelqureyview.html',genralquires)   
@login_required(login_url="admins/login/")
def generalqueries_edit(request,id):
    if request.method == 'POST':
        data1 = generalQuery.objects.get(pk=id)
        data1.view = True 
        data1.save(update_fields=['view'])
    return redirect(f'/admins/general-query/{data1.slug}')     
    
@login_required(login_url="admins/login/")
def productqueries_delete(request,id):
    if request.method == 'POST':
        data1 = productQuery.objects.get(pk=id)
        data1.delete()
    return redirect("/admins/queries/")

@login_required(login_url="admins/login/")
def productqueries_view(request,slug):
    productquery = productQuery.objects.filter(slug=slug).first()
    productquires={
   'productquery' : productquery
       }
    return render(request,'dashboards/products/queries/productqureyview.html',productquires)   
@login_required(login_url="admins/login/")
def productqueries_edit(request,id):
    if request.method == 'POST':
        data1 = productQuery.objects.get(pk=id)
        data1.view = True 
        data1.save(update_fields=['view'])
    return redirect(f'/admins/product-query/{data1.slug}') 

@login_required(login_url="admins/login/")
def terms(request):
    form = Terms_and_ConditionForm
    context = {'aboutus':Terms_and_Condition.objects.all(),
               'form':form}
    if request.method =="POST":
        form= Terms_and_ConditionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"terms and condition details added sucessfully",extra_tags="upload_success")
            return redirect('/admins/terms')
        else :
            messages.error(request,"terms and condition not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/terms')

    html_template = loader.get_template('dashboards/userinterface/terms/terms.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def terms_delete_data(request, id):
    if request.method == 'POST':
        data1 = Terms_and_Condition.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/terms')
@login_required(login_url="admins/login/")
def terms_update_data(request, id):
    if request.method == 'POST':
        data = Terms_and_Condition.objects.get(pk=id)
        fm = Terms_and_ConditionForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"terms and condition details update sucessfully",extra_tags="update_success")
            return redirect('/admins/terms')
        else :
            data = Terms_and_Condition.objects.get(pk=id)
            fm = Terms_and_ConditionForm(instance=data)
            
            
        messages.error(request,"termsdetails not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/terms/terms_update.html',{'form':fm})
@login_required(login_url="admins/login/")
def returnpolicy(request):
    form = Return_refund_policyForm
    context = {'aboutus':Return_refund_policy.objects.all(),
               'product_return':product_return.objects.all(),
               'form':form}
    if request.method =="POST":
        form= Return_refund_policyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"return policy details added sucessfully",extra_tags="upload_success")
            return redirect('/admins/returnpolicy')
        else :
            messages.error(request,"return policy not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/returnpolicy')

    html_template = loader.get_template('dashboards/userinterface/returnpolicy/returnpolicy.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def returnpolicy_delete_data(request, id):
    if request.method == 'POST':
        data1 = Return_refund_policy.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/returnpolicy')
@login_required(login_url="admins/login/")
def returnpolicy_update_data(request, id):
    if request.method == 'POST':
        data = Return_refund_policy.objects.get(pk=id)
        fm = Return_refund_policyForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"return policy details update sucessfully",extra_tags="update_success")
            return redirect('/admins/returnpolicy')
        else :
            data = Return_refund_policy.objects.get(pk=id)
            fm = Return_refund_policyForm(instance=data)
            
            
        messages.error(request,"returnpolicydetails not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/returnpolicy/returnpolicy_update.html',{'form':fm})

@login_required(login_url="admins/login/")
def Productreturn_update_data(request, id):
    if request.method == 'POST':
        data = product_return.objects.get(pk=id)
        fm = product_returnForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"product return policy details update sucessfully",extra_tags="update_success")
            return redirect('/admins/returnpolicy')
        else :
            data = product_return.objects.get(pk=id)
            fm = product_returnForm(instance=data)
            
            
        messages.error(request,"returnpolicydetails not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/returnpolicy/product_returnpolicy_update.html',{'form':fm})       
        
        
        
@login_required(login_url="admins/login/")
def addblog(request):
    form = BlogForm
    context = {'aboutus':Blog.objects.all(),
               'form':form}
    if request.method =="POST":
        form= BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"blog details added sucessfully",extra_tags="upload_success")
            return redirect('/admins/addblog')
        else :
            messages.error(request,"blogdetails not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/addblog')

    html_template = loader.get_template('dashboards/userinterface/blogs/add_blogs.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def manageblog(request):
    context = {'blog':Blog.objects.all(),
               }

    html_template = loader.get_template('dashboards/userinterface/blogs/manage_blogs.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="admins/login/")
def blog_delete_data(request, id):
    if request.method == 'POST':
        data1 = Blog.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/manageblog')
# @login_required(login_url="admins/login/")
# def blog_update_data(request, id):
#     if request.method == 'POST':
#         data = Blog.objects.get(pk=id)
#         fm = BlogForm(request.POST ,request.FILES,instance=data)
#         if fm.is_valid():
#             fm.save()
#             messages.success(request,"return policy details update sucessfully",extra_tags="update_success")
#             return redirect('/admins/returnpolicy')
#         else :
#             data = Blog.objects.get(pk=id)
#             fm = BlogForm(instance=data)
            
            
#         messages.error(request,"returnpolicydetails not uploaded",extra_tags="update_unsuccess")
#         return render(request,'dashboards/userinterface/returnpolicy/returnpolicy_update.html',{'form':fm})



@login_required(login_url="admins/login/")
def Blogcomment_view(request):
    
    context ={
        'blogcomment': Blogcomment.objects.all()
    }
    return render(request,'dashboards/userinterface/blogs/blogcomment.html',context)

@login_required(login_url="admins/login/")
def Blogcomment_delete(request,sno):
    if request.method == 'POST':
        data1 = Blogcomment.objects.get(pk=sno)
        data1.delete()
        
    return redirect("/admins/blogcomment")





@login_required(login_url="admins/login/")
def homecarsoule(request):
    form = home_carouselForm
    context = {'aboutus':home_carousel.objects.all(),
               'form':form}
    if request.method =="POST":
        form= home_carouselForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"homecarsoule added sucessfully",extra_tags="upload_success")
            return redirect('/admins/homecarsoule')
        else :
            messages.error(request,"home carsoule not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/homecarsoule')

    html_template = loader.get_template('dashboards/userinterface/home/homecarsoule/homecarsoule.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def homecarasoule_delete_data(request, id):
    if request.method == 'POST':
        data1 = home_carousel.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/homecarsoule')
@login_required(login_url="admins/login/")
def homecarsoule_update_data(request, id):
    if request.method == 'POST':
        data = home_carousel.objects.get(pk=id)
        fm = home_carouselForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"home carasoule update sucessfully",extra_tags="update_success")
            return redirect('/admins/homecarsoule')
        else :
            data = home_carousel.objects.get(pk=id)
            fm = home_carouselForm(instance=data)
            
            
        messages.error(request,"home carasoule not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/home/homecarsoule/homecarsoule_update.html',{'form':fm})

  
  
  
      

      
@login_required(login_url="admins/login/")
def homecollection(request):
    context = {'homecollection':home_collection_banner.objects.all(),
               }
    

    html_template = loader.get_template('dashboards/userinterface/home/homecollection/homecollection.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="admins/login/")
def homecollection_update_data(request, id):
    if request.method == 'POST':
        data = home_collection_banner.objects.get(pk=id)
        fm = home_collection_bannerForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"home collection banner update sucessfully",extra_tags="update_success")
            return redirect('/admins/homecollection')
        else :
            data = home_collection_banner.objects.get(pk=id)
            fm = home_collection_bannerForm(instance=data)
            
            
        messages.error(request,"homecollection banner not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/home/homecollection/homecollection_update.html',{'form':fm})

@login_required(login_url="admins/login/")
def allbanners(request):
    context = {'banners':banners.objects.all(),
               }
    

    html_template = loader.get_template('dashboards/userinterface/allbanners/allbanners.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="admins/login/")
def allbanners_update_data(request, id):
    if request.method == 'POST':
        data = banners.objects.get(pk=id)
        fm = bannersForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"banners update sucessfully",extra_tags="update_success")
            return redirect('/admins/allbanners')
        else :
            data = banners.objects.get(pk=id)
            fm = bannersForm(instance=data)
            
            
        messages.error(request,"banners not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/userinterface/allbanners/allbanners_update.html',{'form':fm})

@login_required(login_url="admins/login/")
def advatisment(request):
    context = {'ad':product_add_slot.objects.all(),
               }
    

    html_template = loader.get_template('dashboards/advatisment/advatisment.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="admins/login/")
def advatisment_update_data(request, id):
    if request.method == 'POST':
        data = product_add_slot.objects.get(pk=id)
        fm = product_add_slotForm(request.POST ,request.FILES,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"advatisment update sucessfully",extra_tags="update_success")
            return redirect('/admins/advatisment')
        else :
            data = product_add_slot.objects.get(pk=id)
            fm = product_add_slotForm(instance=data)
            
            
        messages.error(request,"ad field uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/advatisment/advatisment_update.html',{'form':fm})
    
    
@login_required(login_url="admins/login/")
def social_icon(request):
    form = Social_icon_addingForm
    context = {'socialicon':Social_icon_adding.objects.all(),
               'form':form}
    if request.method =="POST":
        form= Social_icon_addingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Social icon added sucessfully",extra_tags="upload_success")
            return redirect('/admins/social_icon')
        else :
            messages.error(request,"Social icon not uploaded",extra_tags="upload_unsuccess")
            return redirect('/admins/social_icon')

    html_template = loader.get_template('dashboards/social_icon/social_icon.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="admins/login/")
def social_icon_delete_data(request, id):
    if request.method == 'POST':
        data1 = Social_icon_adding.objects.get(pk=id)
        data1.delete()
        return redirect('/admins/social_icon')
@login_required(login_url="admins/login/")
def social_icon_update_data(request, id):
    if request.method == 'POST':
        data1 = Social_icon_adding.objects.get(pk=id)
        fm = Social_icon_addingForm(request.POST ,request.FILES,instance=data1)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Social icon update sucessfully",extra_tags="update_success")
            return redirect('/admins/social_icon')
        else :
            data1 = Social_icon_adding.objects.get(pk=id)
            fm = Social_icon_addingForm(instance=data1)
            
            
        messages.error(request,"Social icon  not uploaded",extra_tags="update_unsuccess")
        return render(request,'dashboards/social_icon/social_icon_update.html',{'form':fm})
    
    
@login_required(login_url="admins/login/")
def Sizechart(request):
    
    
    context = {'sizechart':Size_chart.objects.all()}
   
    html_template = loader.get_template('dashboards/products/sizechart/Size_chart.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="admins/login/")
def Sizechart_update(request,id):
    
    data = Size_chart.objects.get(pk=id)
    form = Size_chartForm(request.POST ,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,"your product size chart update sucessfully",extra_tags="upload_success")
        return redirect('/admins/Size_chart')
    else :
        data = Size_chart.objects.get(pk=id)
        form = Size_chartForm(instance=data)
    return render(request,'dashboards/products/sizechart/Size_chart_update.html',{'form':form}) 


@login_required(login_url="admins/login/")
def recived_orders(request):
     
    
    order ={
    'ordercount' :AllOrders.objects.all().count(),
     'order' :AllOrders.objects.all(),
     'pendingcount' :AllOrders.objects.filter(Orderplaced=False).count(),
     'placeordercount':AllOrders.objects.filter(Orderplaced=True).count(),
    #  'allorder':ALlorderItem.objects.get(orderid =)
    
    }
    
    return render(request,'dashboards/orders/recived_order/recived_order.html',order) 


@login_required(login_url="admins/login/")
def order_placed(request,id):
    if request.method == 'POST':
        data1 = AllOrders.objects.get(pk=id)
        data1.Orderplaced = True 
        data1.save(update_fields=['Orderplaced'])
        messages.success(request,"product placed sucessfully",extra_tags="active_success")
        return redirect('/admins/recived_orders/')
                
                
                
                
                
                
@login_required(login_url="admins/login/")
def oder_summary(request,id):
     
    
    order ={
     'order' :AllOrders.objects.get(id=id),
     'allorderitem':ALlorderItem.objects.filter(orderid =id)
    
    }
    
    return render(request,'dashboards/orders/recived_order/view_order_summary.html',order)


@login_required(login_url="admins/login/")
def forget_password(request):
     
    
    forgetpasslist ={
     'forgetpass' :Singup.objects.all()
     
    
    }
    
    return render(request,'dashboards/forgetpasswordlist/forgetpass.html',forgetpasslist)


@login_required(login_url="admins/login/")
def forget_password_block(request,id):
     
    
    if request.method == 'POST':
        data1 = Singup.objects.get(pk=id)
        data1.block = True
        data1.save(update_fields=['block'])
    
    return redirect('/admins/forget_password')

@login_required(login_url="admins/login/")
def forget_password_unblock(request,id):
     
    
    if request.method == 'POST':
        data1 = Singup.objects.get(pk=id)
        data1.block = False
        data1.save(update_fields=['block'])
        data1.forgetpass = 0
        data1.save(update_fields=['forgetpass'])
        
    
    return redirect('/admins/forget_password')



@login_required(login_url="admins/login/")
def track_orders(request):
     
    
    order ={
     'order' :AllOrders.objects.filter(Orderplaced=True),
     'placeorder_count' :AllOrders.objects.filter(Orderplaced=True).count(),
     'shipped_ordercount':AllOrders.objects.filter(shipped=True).count(),
     'out_deliverycount':AllOrders.objects.filter(out_delivery=True).count(),
     'deliverdorder_count':AllOrders.objects.filter(deliverd=True).count(),
    #  'allorder':ALlorderItem.objects.get(orderid =)
    
    }
    
    return render(request,'dashboards/orders/tracking_order/track_order.html',order) 
@login_required(login_url="admins/login/")
def order_shipped(request,id):
    
    if request.method == 'POST':
        data1 = AllOrders.objects.get(pk=id)
        data1.shipped = True
        data1.save(update_fields=['shipped'])
    
    return redirect('/admins/track_orders')

@login_required(login_url="admins/login/")    
def order_out_delivery(request,id):
    
    if request.method == 'POST':
        data1 = AllOrders.objects.get(pk=id)
        data1.out_delivery = True
        data1.save(update_fields=['out_delivery'])
    
    return redirect('/admins/track_orders')
@login_required(login_url="admins/login/")
def order_deliverd(request,id):
    
    if request.method == 'POST':
        data1 = AllOrders.objects.get(pk=id)
        data1.deliverd = True
        data1.save(update_fields=['deliverd'])
    
    return redirect('/admins/track_orders')


@login_required(login_url="admins/login/")
def cancelorders(request):
    cancelorder = CancelAllOrders.objects.all()
    cancelAllorders ={
        'cancelorder':cancelorder
    }
    
    return render(request,'dashboards/orders/cancel_order/cancelorders.html',cancelAllorders)

@login_required(login_url="admins/login/")    
def cancel_order_payment_confirm(request,id):
    
    if request.method == 'POST':
        data1 = CancelAllOrders.objects.get(pk=id)
        data1.payment_confirm = True
        data1.save(update_fields=['payment_confirm'])

    return redirect("/admins/cancelorders/")

@login_required(login_url="admins/login/")
def canceloder_summary(request,id):
     
    
    order ={
     'order' :CancelAllOrders.objects.get(id=id),
     'allorderitem':cancelordersItem.objects.filter(cancelid =id)
    
    }
    
    return render(request,'dashboards/orders/cancel_order/view_cancelorder_summary.html',order)



@login_required(login_url="admins/login/")
def Return_order_list(request):
    return_order ={
        'returnoders':ReturnAllOrders.objects.all()

    }

    return render(request,'dashboards/orders/Return_order/returnorder.html',return_order) 


@login_required(login_url="admins/login/")
def return_oder_summary(request,id):
     
    
    order ={
     'order' :ReturnAllOrders.objects.get(id=id),
     'allorderitem':ReturnordersItem.objects.filter(cancelid =id)
    
    }
    
    return render(request,'dashboards/orders/Return_order/view_returnorder_summary.html',order)

@login_required(login_url="admins/login/")
def Pickup_request(request,id):
    
    if request.method == 'POST':
        data1 = ReturnAllOrders.objects.get(pk=id)
        data1.Pickup_request = True
        data1.save(update_fields=['Pickup_request'])
    return redirect('/admins/Return_order_list/')


@login_required(login_url="admins/login/")
def refundOfRetun_orders(request):
     
    
    order ={
     'returnorder' :ReturnAllOrders.objects.filter(Pickup_request=True),
     
    #  'allorder':ALlorderItem.objects.get(orderid =)
    
    }

    return render(request,'dashboards/orders/Return_order/retunordertracking.html',order)

@login_required(login_url="admins/login/")
def return_confirm(request,id):
    
    if request.method == 'POST':
        data1 = ReturnAllOrders.objects.get(pk=id)
        data1.Return_Confirm = True
        data1.save(update_fields=['Return_Confirm'])
    
    return redirect('/admins/refundOfRetun_orders/')

@login_required(login_url="admins/login/")    
def Payment_confirm(request,id):
    
    if request.method == 'POST':
        data1 = ReturnAllOrders.objects.get(pk=id)
        data1.payment_confirm = True
        data1.save(update_fields=['payment_confirm'])

    return redirect("/admins/refundOfRetun_orders/")

# @login_required(login_url="admins/login/")
# def logofield(request):
#     form = LogoFieldForm
#     context = {'form':form, 'logo':LogoField.objects.all()}
#     if request.method =="POST":
#         form= LogoFieldForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"your  logo upload sucessfully",extra_tags="upload_success")
#             return redirect('/admins/logofield/')
#         else :
#             messages.error(request,"your logo not uploaded",extra_tags="upload_unsuccess")
#             return redirect('/admins/logofield/')
#     return render(request,'dashboards/website_settings/system_settings/logos.html',context)

# @login_required(login_url="admins/login/")
# def updatelogoField(request,id):
    
#     data = LogoField.objects.get(pk=id)
#     fm = LogoFieldForm(request.POST ,request.FILES,instance=data)
#     if fm.is_valid():
#         fm.save()
#         messages.success(request,"your product size chart update sucessfully",extra_tags="upload_success")
#         return redirect('/admins/logofield/')
#     else :
#         data = LogoField.objects.get(pk=id)
#         fm = LogoFieldForm(instance=data)
#     return render(request,'dashboards/website_settings/system_settings/logoupdate.html',{'form':fm}) 

@login_required(login_url="admins/login/")
def slogan(request):
    slogan = Slogan.objects.all()

    return render(request,'dashboards/website_settings/system_settings/slogan.html',{'slogan':slogan})

@login_required(login_url="admins/login/")
def sloganupdate(request,id):
    data1 = Slogan.objects.get(id=id)
    form = SloganForm(request.POST ,instance = data1)
    if form.is_valid():
        form.save()
        messages.success(request,"your Website slogan update sucessfully",extra_tags="upload_success")
        return redirect('/admins/slogan')

    else:
        data = Slogan.objects.get(pk=id)
        form = SloganForm(instance=data)
    return render(request,'dashboards/website_settings/system_settings/slogan_update.html',{'form':form})




@login_required(login_url="admins/login/")
def websitelogo(request):
   
    context = {'websitelogo':WebsiteLogo.objects.all()}
        
    html_template = loader.get_template('dashboards/website_settings/system_settings/logos.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="admins/login/")
def updatelogoField(request,id):
    
    data = WebsiteLogo.objects.get(pk=id)
    form = WebsiteLogoForm(request.POST ,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,"size update sucessfully",extra_tags="upload_success")
        return redirect('/admins/logofield/')
    else :
        data = WebsiteLogo.objects.get(pk=id)
        form = WebsiteLogoForm(instance=data)
    return render(request,'dashboards/website_settings/system_settings/logoupdate.html',{'form':form}) 
def logoutview(request):
    auth_logout(request) 
    return redirect('/admins/login')
    