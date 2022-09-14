from django.contrib import admin
from django.utils.html import format_html
from SOCIAL_ICON.models import Social_icon_adding
class Social_icon_addingAdmin(admin.ModelAdmin):
    list_display = ('social_icon_name','Social_icon_Preview','social_icon_link_except_http','Action')
    list_display_links = None
    def Social_icon_Preview(self, obj):
        return format_html(f'<img src= "/media/{obj.social_icon_image}"style ="width:30px; height:auto;"')
    def Action(self, obj):
        return format_html(f'<button style="background-color:green; padding:3px 10px 3px 10px; margin-right:5px"><a href="/admin/SOCIAL_ICON/social_icon_adding/{obj.id}/change/" class="default"style ="color:white;">Edit</a></button> ' f'<button style="background-color:red;padding:3px 2px 3px 2px;"><a href="/admin/SOCIAL_ICON/social_icon_adding/{obj.id}/delete/" class="default"style ="color:white;">Delete</a></button>')
       
admin.site.register(Social_icon_adding, Social_icon_addingAdmin)

