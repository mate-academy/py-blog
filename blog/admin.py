from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Comment


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_time")
    list_filter = ("author", "created_time")
    search_fields = ("title", "content")


@admin.register(Comment)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_time")
    list_filter = ("author", "created_time")
    search_fields = ("content",)
