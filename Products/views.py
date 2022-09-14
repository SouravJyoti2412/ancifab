from django.http import JsonResponse
from Products.models import maincategory,Category
from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.permissions import IsAuthenticated

# class MainCategoryList(APIView):
#     permission_classes =[IsAuthenticated]
#     def post(self,request,format=None):
#         # maincategories = request.data['maincategories']
#         maincategories = maincategory.objects.all()
#         maincat = { p.name:p.sno for p in maincategories}
        
#         # category ={}
#         # if maincategories:
            
#         #     categories = maincategory.objects.get(sno=maincategories).category.all()
#         #     category = { p.Category_name:p.Sno for p in categories}
#         return JsonResponse(data = maincat ,safe= False)


class CategoryList(APIView):
    permission_classes =[IsAuthenticated]
    def post(self,request,format=None):
        maincategories = request.data['maincategories']
        category ={}
        if maincategories:
            
            categories = maincategory.objects.get(sno=maincategories).category.all()
            category = { p.Category_name:p.Sno for p in categories}
        return JsonResponse(data = category ,safe= False)
    
    
class SubcategoryList(APIView):
    permission_classes =[IsAuthenticated]
    def post(self,request,format=None):
        categories = request.data['categories']
        subcategory ={}
        if categories:
            categories = Category.objects.get(Sno=categories).subcategory.all()
            subcategory = { p.Sub_Category_name:p.Sno for p in categories}
        return JsonResponse(data = subcategory ,safe= False)