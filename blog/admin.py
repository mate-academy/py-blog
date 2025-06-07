from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post


# Register your models here.
@admin.register(User)
class UserAdministrator(UserAdmin):
    list_filter = UserAdmin.list_filter + ("username", 'first_name', 'last_name')
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {'fields': ('first_name', 'last_name', 'email')})
    ),


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "owner")
    list_filter = ("owner", "title", "created_time")
    search_fields = ("title",)
