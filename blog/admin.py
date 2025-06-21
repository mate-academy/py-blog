from django.contrib import admin
from .models import Commentary, User, Post
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content")
    list_filter = ("created_time", "owner")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("content",)
    list_filter = ("created_time", "user", "post")
