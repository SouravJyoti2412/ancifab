from django.urls import path
from Products.views import *
urlpatterns = [
    path("category/",CategoryList.as_view()),
    path('subcategory/',SubcategoryList.as_view()),
    # path('maincategory/',MainCategoryList.as_view())
    #for fronend dropdown
    # path("categoryFrontend/",CategoryList.as_view()),
    # path('subcategoryFrontend/',SubcategoryList.as_view())
]
