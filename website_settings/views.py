from email.mime import message
from django.shortcuts import redirect, render
from website_settings.models import LogoField
from website_settings.forms import LogoFieldForm
from django.contrib import messages
# def logofield(request):
#     logo = LogoField.objects.all()
    
#     return render(request,'dashboards/website_settings/system_settings/logos.html',{'logo':logo})

# def updatelogoField(request,id):
#     logo = LogoField.objects.get(pk=id)
#     form = LogoFieldForm(request.POST ,request.FILES,instance=logo)
#     if form.is_valid():
#         form.save()
#         messages.success(request,"Logo update sucessfully",extra_tags="upload_success")
#         return redirect ('/admins/logofield/')
#     else:
#         logo = LogoField.objects.get(pk=id)
#         form = LogoFieldForm(instance=logo)
#         messages.error(request,"Logo not updated",extra_tags="upload_failed")
        
    
#     return render(request, 'dashboards/website_settings/system_settings/logoupdate.html',{'form':form})
    
    
    
    
# def productsize_update(request,Sno):
    
#     data = ProductSize.objects.get(pk=Sno)
#     form = ProductSizeForm(request.POST ,request.FILES,instance=data)
#     if form.is_valid():
#         form.save()
#         messages.success(request,"size update sucessfully",extra_tags="upload_success")
#         return redirect('/admins/addproductssize/')
#     else :
#         data = ProductSize.objects.get(pk=Sno)
#         form = ProductSizeForm(instance=data)
#     return render(request,'dashboards/Product_Size_update.html',{'form':form})
    