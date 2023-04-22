from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title",)
    list_filter = ("owner",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time")
    search_fields = ("post",)
    list_filter = ("user",)


admin.site.unregister(Group)
