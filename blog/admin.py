from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_attribute', 'view_count')
    list_filter = ['title']
    search_fields = ('title', 'publish_attribute')