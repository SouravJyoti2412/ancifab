from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models

# from .managers import main_categoryManager,categoryManager,sub_categoryManager
from Products.models import AllOrders, Category, Coupon,Sub_Category,ProductColor,ProductSize, WebsiteLogos,addproduct,maincategory,Orderplace,add_to_cart,productreview,generalQuery,productQuery,AllOrders,ALlorderItem,Size_chart,product_return,CancelAllOrders,cancelordersItem,ReturnAllOrders,ReturnordersItem
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(ProductColor)
admin.site.register(ProductSize)
admin.site.register(Orderplace)
class add_to_cartAdmin(admin.ModelAdmin):
    list_display = ('customer','cartProduct','quantity')

admin.site.register(add_to_cart, add_to_cartAdmin)
admin.site.register(productreview)
admin.site.register(generalQuery)
admin.site.register(productQuery)
admin.site.register(AllOrders)
admin.site.register(ALlorderItem)
admin.site.register(Size_chart)
admin.site.register(product_return)
admin.site.register(WebsiteLogos)
admin.site.register(maincategory)



class addproductAdmin(admin.ModelAdmin):
    class Media:
        js =("assets/js/newajax.js",)
admin.site.register(addproduct,addproductAdmin)
# class CancelAllOrdersAdmin(admin.ModelAdmin):


admin.site.register(CancelAllOrders)
admin.site.register(cancelordersItem)
admin.site.register(ReturnAllOrders)
admin.site.register(ReturnordersItem)
admin.site.register(Coupon)
    


