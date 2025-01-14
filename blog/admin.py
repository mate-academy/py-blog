from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "owner", "content", "created_time"]
    ordering = ("-created_time", "title")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["user", "post", "created_time", "content"]
    ordering = ("-created_time", )
