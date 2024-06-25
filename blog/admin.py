from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_filter = ("is_staff", "is_superuser",)
    search_fields = ("is_staff", "is_superuser",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time",)
    list_filter = ("owner",)
    search_fields = ("title", "content",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content",)
    list_filter = ("user", "post",)
    search_fields = ("content",)
