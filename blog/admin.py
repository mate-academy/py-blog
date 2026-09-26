from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time")
    list_filter = ("owner", "created_time")
    search_fields = ("owner__username", "title")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    list_filter = ("user", "created_time")
    search_fields = ("user__username",)
