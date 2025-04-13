from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_time")
    search_fields = ("title", "content", "created_time")
    list_filter = ("title", "content", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_time")
    search_fields = ("content", "created_time")
    list_filter = ("user", "content", "created_time")


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "email")
