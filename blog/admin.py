from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time",)
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
