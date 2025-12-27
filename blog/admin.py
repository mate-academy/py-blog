from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Commentary

admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_time", "commentaries_count")
    search_fields = ("title", "content")
    list_filter = ("author", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_time")
    search_fields = ("content",)
    list_filter = ("author", "created_time")
