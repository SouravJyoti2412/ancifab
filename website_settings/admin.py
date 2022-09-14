from django.contrib import admin
from website_settings.models import LogoField,Slogan



# class LogoFieldAdmin(admin.ModelAdmin):
#     # list_editable: Sequence[str]

# admin.site.register(LogoField, LogoFieldAdmin)

# Register your models here.

admin.site.register(LogoField)
admin.site.register(Slogan)