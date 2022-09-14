from django.contrib import admin
from ADVATISMENT.models import product_add_slot
from django.utils.html import format_html

class product_add_slotAdmin(admin.ModelAdmin):
    list_display = ('Graphic_ad_preview','PRODUCT_ADD_lINK','action')
    list_display_links= None
    def Graphic_ad_preview(self, obj):
        return format_html(f'<img src= "/media/{obj.PRODUCT_ADD_SLOT_274X366px}"style ="width:auto; height:150px;"')
    def action(self, obj):
        return format_html(f'<button style="background-color:green;"><a href="/admin/ADVATISMENT/product_add_slot/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')



admin.site.register(product_add_slot,product_add_slotAdmin)
