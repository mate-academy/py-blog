from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Commentary, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "content", "owner__username")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "content", "created_time")
    list_filter = ("created_time", "user")
    search_fields = ("content", "user__username", "post__title")


admin.site.unregister(Group)
