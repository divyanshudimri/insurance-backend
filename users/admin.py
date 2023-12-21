from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("is_superuser",)
    list_display = ("username", "is_active", "is_superuser")
