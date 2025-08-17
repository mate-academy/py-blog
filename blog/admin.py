from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time")
    list_filter = ("owner", "created_time")
    search_fields = ("title", "content", "owner__username")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    list_filter = ("user", "post", "created_time")
    search_fields = ("content", "user__username", "user__email")


admin.site.unregister(Group)
