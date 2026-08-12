from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post, User


@admin.register(User)
class BlogUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time",)
    search_fields = ("title", "content", "owner__username")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time")
    list_filter = ("created_time",)
    search_fields = ("content", "user__username", "post__title")


admin.site.unregister(Group)
