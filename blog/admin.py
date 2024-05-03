from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time")
    list_filter = ("title", "created_time")
    search_fields = ("title", "content")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    list_filter = ("user", "created_time")


admin.site.unregister(Group)
