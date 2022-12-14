
# from os import name
from django.conf.urls import url
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
from .views import login_view, register_user
# from website_settings.views import logofield
urlpatterns = [ 
path('login/', login_view, name="login"),
path('register/', register_user, name="register"),
path("logout/", views.logoutview, name="logout") ,
path("dashboard/",views.dashboard),
path("general-query/<str:slug>",views.generalqueries_view, name = "generalquery"),
path("generelqueryedit/<int:id> ",views.generalqueries_edit,name="generalqueries_edit"),
path("product-query/<str:slug>",views.productqueries_view, name = "generalquery"),
path("productqueryedit/<int:id> ",views.productqueries_edit,name="productqueries_edit"),
path("addproductssize/" ,views.productsize,name = 'addsize'),
path("productsize_delete/<int:Sno>/",views.productsize_delete,name ='productsize_delete'),
path("productsize_update/<int:Sno>/",views.productsize_update,name ='productsize_update'),
path("add_colors/" ,views.color_name,name = 'addcolor'), 
path("color_delete/<int:Sno>/",views.color_delete,name ='color_deletes'),
path("color_update/<int:Sno>/",views.color_update,name ='color_updates'),
path("subcategory/" ,views.subcategory,name = 'subcategory'), 
path("updatesubcategory/<int:Sno>" ,views.subcat_update,name = 'updatesubcategory'), 
path("subcategory_delete/<int:Sno>" ,views.subcategory_delete,name = 'subcategory_delete'), 
path("category/" ,views.category,name = 'category'),
path("category_edit/<int:Sno>" ,views.category_update,name = 'category_update'),
path("category_delete/<int:Sno>",views.category_delete,name = "category_delete") ,      
path("maincategory/" ,views.maincategories,name = 'maincategory'), 
path("maincategories_update/<int:sno>",views.maincategories_update,name = 'maincategory_update_data'),
path("maincategory_delete/<int:sno>",views.maincategory_delete,name = 'maincategory_delete'),
path("productupload/",views.productupload,name ="productupload"),
path("product_manage/",views.productmanage),
path("deleteProduct/<int:id>/",views.product_delete, name ="product_delete"),
path("productPending/<int:id>",views.product_pending,name = "product_pending"),
path("product_active/<int:id>",views.product_active,name = "product_active"),
path("product_out_of_stock/<int:id>",views.product_out_of_stock,name = "product_out_of_stock"),
path("product_in_stock/<int:id>",views.product_in_stock,name = "product_in_stock"),
path("product_update/<int:id>",views.product_update,name = "product_update"),

path("mark_as_trending/<int:id>",views.mark_as_trending,name= "mark_as_trending"),
path("mark_as_normal/<int:id>",views.mark_as_normal,name= "mark_as_normal"),
# path("product_upload_asDraft/", views.productupload_asDraft, name='save_as_draft'),
path("customer/", views.customer, name = "manage_customer"),
path("delete/<int:id>/", views.Customer_delete_data, name = "Customer_delete_data"),
path("aboutus/", views.aboutus, name = "aboutus"),
path("about_delete/<int:id>/", views.About_delete_data, name = "about_delete_data"),
path("<int:id>/", views.About_update_data, name = "about_update_data"),
path("About_heading_update/<int:id>/", views.About_heading_update_data, name = "About_heading_update"),
path("faq/", views.faq, name = "faq"),
path("faq_delete/<int:id>/", views.faq_delete_data, name = "faq_delete_data"),
path("faq/<int:id>/", views.faq_update_data, name = "faq_update_data"),
path("contactus/", views.contact, name = "contactus"),
path("contact/<int:id>/", views.contact_update_data, name = "contact_update_data"),
path("productreviews/",views.productreviews,name ="productreviews"),
path('review_delete/<int:sno>',views.review_delete,name="review_delete"),
path("queries/",views.queries,name ="queries"),
path("generalqueries_delete/<int:id>/", views.generalqueries_delete, name = "generalqueries_delete"),
path("productqueries_delete/<int:id>/", views.productqueries_delete, name = "productqueries_delete"),
path("terms/", views.terms, name = "terms"),
path("terms_delete/<int:id>/", views.terms_delete_data, name = "terms_delete_data"),
path("terms/<int:id>/", views.terms_update_data, name = "terms_update_data"),
path("returnpolicy/", views.returnpolicy, name = "returnpolicy"),
path("returnpolicy_delete/<int:id>/", views.returnpolicy_delete_data, name = "returnpolicy_delete_data"),
path("returnpolicy/<int:id>/", views.returnpolicy_update_data, name = "returnpolicy_update_data"),
path("addblog/", views.addblog, name = "addblog"),
path("manageblog/", views.manageblog, name = "manageblog"),
path("blog_delete/<int:id>/", views.blog_delete_data, name = "blog_delete_data"),
path("blogcomment/",views.Blogcomment_view,name ="Blogcomment_view"),
path('Blogcomment_delete/<int:sno>',views.Blogcomment_delete,name="Blogcomment_delete"),
path("homecarsoule/", views.homecarsoule, name = "homecarsoule"),
path("homecarasoule_delete_data/<int:id>/", views.homecarasoule_delete_data, name = "homecarasoule_delete_data"),
path("homecarsoule_update_data/<int:id>/", views.homecarsoule_update_data, name = "homecarsoule_update_data"),
# path("blog_update_data/<int:id>/", views.blog_update_data, name = "blog_update_data"),
# re_path(r'^.*\.*', views.pages, name='pages'),
path("homecollection/", views.homecollection, name = "homecollection"),
path("homecollection_update_data/<int:id>/", views.homecollection_update_data, name = "homecollection_update_data"),
path("allbanners/", views.allbanners, name = "allbanners"),
path("allbanners_update_data/<int:id>/", views.allbanners_update_data, name = "allbanners_update_data"),

path("advatisment/", views.advatisment, name = "allbanners"),
path("advatisment_update_data/<int:id>/", views.advatisment_update_data, name = "advatisment_update_data"),
path("social_icon/", views.social_icon, name = "social_icon"),
path("social_icon_delete/<int:id>/", views.social_icon_delete_data, name = "social_icon_delete_data"),
path("social_icon_update_data/<int:id>/", views.social_icon_update_data, name = "social_icon_update_data"),

path("Privacy/", views.Privacy, name = "Privacy"),
path("Privacy_delete/<int:id>/", views.Privacy_delete_data, name = "Privacy_delete_data"),
path("Privacy_update/<int:id>/", views.Privacy_update_data, name = "Privacy_update_data"),
path("Size_chart/",views.Sizechart),
path("Sizechart/<int:id>",views.Sizechart_update,name = "Sizechart_update"),
path("Productreturn_update_data/<int:id>",views.Productreturn_update_data,name ="Productreturn_update_data"),
path("recived_orders/",views.recived_orders),
path("order_placed/<int:id>",views.order_placed,name = "order_placed"),
path("oder_summary/<int:id>",views.oder_summary,name = "oder_summary"),
path("forget_password/",views.forget_password),
path('forget_password_block/<int:id>',views.forget_password_block, name ="forget_password_block"),
path('forget_password_unblock/<int:id>',views.forget_password_unblock, name ="forget_password_unblock"),
path('track_orders/',views.track_orders,name = "track_orders"),
path("order_shipped/<int:id>",views.order_shipped,name ="order_shipped"),
path("order_out_delivery/<int:id>",views.order_out_delivery,name ="order_out_delivery"),
path("order_deliverd/<int:id>",views.order_deliverd,name ="order_deliverd"),
path("cancelorders/",views.cancelorders,name = "cancelorders"),
path("canceloder_summary/<int:id>",views.canceloder_summary,name = "canceloder_summary"),
path("Return_order_list/",views.Return_order_list,name = "Return_order_list"),

path("return_oder_summary/<int:id>",views.return_oder_summary,name = "return_oder_summary"),
path("Pickup_request/<int:id>",views.Pickup_request,name = "Pickup_request"),
path("refundOfRetun_orders/",views.refundOfRetun_orders,name = "refundOfRetun_orders"),
path("return_confirm/<int:id>",views.return_confirm,name ="return_confirm"),
path("Payment_confirm/<int:id>",views.Payment_confirm,name ="Payment_confirm"),
path("cancel_order_payment_confirm/<int:id>",views.cancel_order_payment_confirm,name ="cancel_order_payment_confirm"),
path("logofield/",views.websitelogo,), #this view has in website_settings
path("updatelogoField/<int:id>/", views.updatelogoField, name = "updatelogoField"),

path('slogan/',views.slogan,name ="slogan"),
path('sloganupdate/<int:id>/',views.sloganupdate,name ="sloganupdate")

]