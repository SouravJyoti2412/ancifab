from django.contrib import admin
from django.utils.html import format_html
from userinterphase.models import About_us,Faqs,Terms_and_Condition,Return_refund_policy,contact_details_section,home_carousel,home_collection_banner,banners,Blog,Blogcomment,comments,Aboutus_heading,Privacy_policy

class faqsAdmin(admin.ModelAdmin):
    list_display=('title','content','action',)
    list_display_links= None
    def action(self, obj):
        return format_html(f'<button style="background-color:green;"><a href="/admin/userinterphase/faqs/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')
class Terms_and_ConditionAdmin(admin.ModelAdmin):
    list_display=('title','content','action')
    list_display_links= None
    def action(self, obj):
        return format_html(f'<button style="background-color:green;"><a href="/admin/userinterphase/terms_and_condition/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')
class Return_refund_policyAdmin(admin.ModelAdmin):
    list_display=('title','content','action')
    list_display_links= None
    def action(self, obj):
        return format_html(f'<button style="background-color:green;"><a href="/admin/userinterphase/return_refund_policy/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')
class home_carouselAdmin(admin.ModelAdmin):
    list_display = ('Image_Preview','small_heading_optional','big_heading_optional','offer_optional','image_button_link','action')
    list_display_links = None
    def Image_Preview(self, obj):
        return format_html(f'<img src= "/media/{obj.image_1920X1080px}"style ="width:100px; height:auto;"')
    def action(self, obj):
        return format_html(f'<button style="background-color:green;"><a href="/admin/userinterphase/home_carousel/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')
    # def has_delete_permission(self, request, obj=id) :
    #     return False

    
admin.site.register(home_carousel, home_carouselAdmin)



class About_us_admin(admin.ModelAdmin):
    list_display = ('content_title','content_des','action',)
    list_display_links= None
    # def has_add_permission(self, request):
    #     return False
    def action(self, obj):
        return format_html(f'<button style="background-color:green;padding:5px 5px 5px 5px"><a href="/admin/userinterphase/about_us/{obj.id}/change/" class="default" style ="color:white;">edit</a></button>')
# class About_usTabularInline(admin.TabularInline):
#     model = About_us
class contact_address_Admin(admin.ModelAdmin):
    list_display = ('phone','email','address','side_image_preview','action')
    list_display_links= None
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None) :
        return False
    def side_image_preview(self, obj):
        return format_html(f'<img src= "/media/{obj.side_image_375X230}"style ="width:50px; height:auto;"')
    def action(self, obj):
        return format_html(f'<button style="background-color:green;padding:5px 5px 5px 5px"><a href="/admin/userinterphase/contact_details_section/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')

class home_collection_admin(admin.ModelAdmin):
    
    list_display = ('BIG_LEFT_BANNER_PREVIEW','SMALL_FIRST_BANNER_PREVIEW','BUTTON_LINK_OF_SMALL_FIRST_IMAGE','HEADING_OF_SMALL_FIRST_IMAGE','SMALL_SECOND_BANNER_PREVIEW','BUTTON_LINK_OF_SMALL_SECOND_IMAGE','HEADING_OF_SMALL_SECOND_IMAGE','RIGHT_DOWN_BANNER_PREVIEW','HEADING_OF_RIGHT_DOWN_IMAGE','BUTTON_LINK_OF_IMAGE_RIGHT_DOWN','MIDDLE_SIDE_BANNER_PREVIEW','HEADING_OF_MIDDLE_SIDE_IMAGE','BUTTON_LINK_OF_MIDDLE_SIDE_IMAGE', 'ACTION')
    list_display_links: None
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None) :
        return False
    def BIG_LEFT_BANNER_PREVIEW(self, obj):
        return format_html(f'<img src= "/media/{obj.IMAGE_BIG_LEFT_870X800px}"style ="width:150px; height:auto;"')
    def SMALL_FIRST_BANNER_PREVIEW(self, obj):
        return format_html(f'<img src= "/media/{obj.IMAGE_SMALL_FIRST_425X390px}"style ="width:150px; height:auto;"')
    def SMALL_SECOND_BANNER_PREVIEW(self, obj):
        return format_html(f'<img src= "/media/{obj.IMAGE_SMALL_SECOND_425X390px}"style ="width:150px; height:auto;"')
    def RIGHT_DOWN_BANNER_PREVIEW(self, obj):
        return format_html(f'<img src= "/media/{obj.IMAGE_RIGHT_DOWN_870X390px}"style ="width:150px; height:auto;"')
    def MIDDLE_SIDE_BANNER_PREVIEW(self, obj):
        return format_html(f'<img src= "/media/{obj.MIDDLE_SIDE_IMAGE_1920X1080px}"style ="width:150px; height:auto;"')
    def ACTION(self, obj):
        return format_html(f'<button style="background-color:green;padding:5px 5px 5px 5px"><a href="/admin/userinterphase/home_collection_banner/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')

class bannerAdmin(admin.ModelAdmin):
    list_display = ('Banner_Name','Banner_Preview','Action')
    list_display_links = None
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None) :
        return False
    def Banner_Preview(self, obj):
        return format_html(f'<img src= "/media/{obj.Banner_Image}"style ="width:150px; height:auto;"')
    def Action(self, obj):
        return format_html(f'<button style="background-color:green;"><a href="/admin/userinterphase/banners/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('Blog_title','Blog_banner_Image','Blog_first_Image','Blog_second_Image','category','author','content','created_at')


class Blogcommentadmin(admin.ModelAdmin):
    list_display_links= None
    list_display= ('comment', 'user','Action')
    def Action(self, obj):
        return format_html(f'<button style="background-color:red;padding:3px 2px 3px 2px;"><a href="/admin/userinterphase/blogcomment/{obj.sno}/delete/" class="default"style ="color:white;">Delete</a></button>')
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Blogcomment,Blogcommentadmin)

# admin.site.register(comments)
admin.site.register(About_us,About_us_admin)

admin.site.register(Faqs,faqsAdmin)
admin.site.register(Terms_and_Condition,Terms_and_ConditionAdmin)
admin.site.register(Return_refund_policy,Return_refund_policyAdmin)
admin.site.register(contact_details_section, contact_address_Admin)
# admin.site.register(home_carousel)
admin.site.register(home_collection_banner,home_collection_admin)
admin.site.register(banners, bannerAdmin)
admin.site.register(Aboutus_heading)
admin.site.register(Privacy_policy)
# admin.site.register(Blog)
# class EventAdminSite(admin.AdminSite):


