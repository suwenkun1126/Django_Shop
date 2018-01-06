from django.contrib import admin
from .models import Category,Product

class CagegoryAdimin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CagegoryAdimin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','available','created','updated',]
    list_filter=['available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,ProductAdmin)



