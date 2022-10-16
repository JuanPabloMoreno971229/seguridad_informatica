from core.models import data_login
from django.contrib import admin

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    readonly_fields = ('mail', 'password')

admin.site.register(data_login, DataAdmin)


    