from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "first_name", "last_name", )
    search_fields = ("username", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('owner__username', 'title')
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'content')
    list_filter = ("created_time",)


admin.site.unregister(Group)
