from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')
    list_filter = ('category_name')
    search_fields = ('category_name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('')
