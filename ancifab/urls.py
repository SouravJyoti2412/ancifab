"""ancifab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ancifab import views
from django.conf import settings
from django.conf.urls.static import static
from ancifab.settings import MEDIA_ROOT
from django.urls import path,include
from .middleware.auth import auth_middleware
urlpatterns = [
    path('admins/',include('admins.urls')),
    
    #api to blogpost of comment
    path("blogcomment/",views.blogcomment,name= "blog_comment"),
    path("blog/blog-details/<slug>",views.blog_details, name = "blog_details"),
    path('admin/', admin.site.urls),
    # path('header.html', include('socialShare.urls')),
    path("",views.home , name = "home"),
    path("about/",views.about),
    path("blog/",views.blog),
    path("faq/",views.faq),
    path("contact/",views.contact),
    path("privacy/",views.privacy),
    path("register/",views.register, name="register"),
    path("login/",views.login , name = 'login'),
    path("terms/",views.terms),
    path("products/productdetail/<slug>",views.productdetails),
    path("products/",views.allproducts),
    path("plus_cart/",views.plus_cart),
    path("minus_cart/",views.minus_cart),
    # path("cart/",auth_middleware(views.cart)),
    path("add_to_cart/",views.add_to_carts,name="add_to_cart"),
    path("cart/",views.show_cart,name="show_cart"),
    path("cart_delete/<int:id>",views.cart_delete,name = "cart_delete"),
    path("return-refund/",views.return_refund),
    
    path("checkout/",auth_middleware(views.checkout)),
    path("logout/",views.handellogout),
    path("forget-password/",views.forgetpassword),
    # path("reset-password/",views.resetpassword , name = "resetpass"),
    path("getpasword/",views.getpasword_in_email ,name="getpasswordbyemail"),
    path("updatepassword/",views.update_password , name ="updatepass"),
    path("profile/",auth_middleware(views.profile)),
    path("subcategorywiseview/<int:Sno>",views.subcategorywiseview,name = "subcategorywiseview"),
    path("categorywiseview/<int:Sno>",views.categorywiseview,name = "categorywiseview"),
    path("maincategorywiseview/<int:id>",views.maincategorywiseview,name = "maincategorywiseview"),
    path("productreview/",views.productreviews,name = "productreview"),
    path("generalquery/",views.generalquery,name = "generalquery"),
    path("productquery/",views.productquery,name = "productquery"),
    path("passwordrest/<int:id>",views.passwordreset_byEmail,name= "passwordresetbyemail"),
    path("resetpasswordlink_in_email/",views.resetpasswordlink_in_email),
    path("selectpaymentmethod/",views.selectpaymentmethod),
    # path("addcartproduct/",views.addcartproduct)
    path("cashpayment/",views.cashpayment),
    path("orderstatus/",views.orderstatus ,name = 'orderstatus'),
    path("onlinepayment/",views.onlinepayment ,name ="onlinepay"),
    path("order_product_summary/<int:id>",views.order_product_summary,name = 'view_order_summary'),
    path("order-tracking/<str:order_id>",views.ordertracking , name = "ordertracking"),
    path("Products/",include('Products.urls')),
    path("cancelorderlist/",views.cancelorderlist,name= "cancelorderlist"),
    path("returnorders/",views.returnorders,name = "returnorders"),
    # path('paymentpage/',views.paymentpage, name ="paymentpage")
   path("return_product_summary/<int:id>",views.return_product_summary,name = 'return_product_summary'),
   path("cancel_product_summary/<int:id>",views.cancel_product_summary,name = 'cancel_product_summary'),
   path("returnordertracking/<str:order_id>",views.returnordertracking , name = "returnordertracking"), 
   path("coupon_apply/",views.coupon_apply,name ="coupon_apply" ),
   path("remove_coupon",views.remove_coupon,name ="remove_coupon")
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    
    
    