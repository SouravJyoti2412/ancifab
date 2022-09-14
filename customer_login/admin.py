from email.policy import default
from django.contrib import admin
from django.utils.html import format_html
from django.views import View
from customer_login.models import Singup
class SingupAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','number','email_id','password','forgetpass','block','action')
    list_display_links= None
    def has_add_permission(self, request):
        return False
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(SingupAdmin, self).changeform_view(request, object_id, extra_context=extra_context)
    def action(self, obj):
        return format_html(f'<button style ="background-color:red"><a href="/admin/customer_login/singup/{obj.id}/delete/" class="default"style ="color:white">delete</a></button>')
admin.site.register(Singup, SingupAdmin)
# Register your models here.
