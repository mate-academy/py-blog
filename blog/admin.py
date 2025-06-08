from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary

admin.site.unregister(Group)


# Register your models here.
@admin.register(User)
class UserAdministrator(UserAdmin):
    list_filter = UserAdmin.list_filter + (
        "username", "first_name", "last_name"
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {
            "fields": ("first_name", "last_name", "email")
        })
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "owner")
    list_filter = ("owner", "title", "created_time")
    search_fields = ("title",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_time")
    list_filter = ("content", "post", "created_time")
    search_fields = ("content",)
