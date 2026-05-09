from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, User, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ["-created_time"]
    list_display = ("pk", "title", "created_time",)
    search_fields = ("title",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "created_time")
    list_filter = ("post",)
    search_fields = ("content",)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("pk", "username", "email", "is_staff", "is_superuser")
    search_fields = ("username",)


admin.site.unregister(Group)
