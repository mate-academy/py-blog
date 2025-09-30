from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "content", "owner__username")
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "content", "created_time")
    list_filter = ("user", "created_time")
    search_fields = ("user__username",)
    ordering = ("-created_time",)


admin.site.unregister(Group)
