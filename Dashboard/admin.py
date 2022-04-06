from django.contrib import admin
from .models import product,order
from django.contrib.auth.models import Group


admin.site.site_header='Inventory Dashboard'

class productadmin(admin.ModelAdmin):
    list_display=('name','quantity','category',)
    list_filter=['category']
# Register your models here.
admin.site.register(product,productadmin)
# admin.site.unregister(Group)
admin.site.register(order)