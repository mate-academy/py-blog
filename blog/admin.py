from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_time"]
    list_filter = ["owner"]
    search_fields = ["title"]


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Info", {"fields": ("first_name", "last_name",)}),)


admin.site.register(Commentary)
admin.site.unregister(Group)
