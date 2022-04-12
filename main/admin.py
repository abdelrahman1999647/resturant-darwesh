from django.contrib import admin
from .models import Category, Product






class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(Category,CategoryAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display=('id','product','price','is_popular')
admin.site.register(Product,ProductAdmin)
