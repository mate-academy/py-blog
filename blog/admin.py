from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Comment


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "content", "created_time", ]
    list_filter = ["title", "created_time"]
    search_fields = ["title", "author__username"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", "content", ]
    list_filter = ["user", "post", "created_time"]
    search_fields = ["user__username", "post__title", "content"]


admin.site.unregister(Group)
