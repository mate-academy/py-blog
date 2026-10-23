from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Commentary


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_time")
    list_filter = ("created_time", "user")
    search_fields = ("content",)
