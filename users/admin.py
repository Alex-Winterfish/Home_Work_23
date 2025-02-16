from django.contrib import admin
from users.models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "username")
    list_filter = ["email"]
    search_help_text = ("email",)
