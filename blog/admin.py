from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Commentary, User, Post


admin.site.unregister(Group)


admin.site.register(User, UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "content", "owner__username")
    list_filter = ("owner", "created_time")
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "user", "post", "created_time")
    search_fields = ("content", "user__username", "post__title")
    list_filter = ("user__username", "created_time")
    ordering = ("-created_time",)
