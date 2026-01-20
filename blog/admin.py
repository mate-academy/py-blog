from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Post, User, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name",)}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "created_time"]
    list_filter = ["title", "created_time"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "created_time"]
    list_filter = ["user", "created_time"]


admin.site.unregister(Group)
