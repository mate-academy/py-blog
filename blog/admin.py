from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_time")
    search_fields = ("title", "content", "author__username")
    list_filter = ("created_time",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_time")
    search_fields = ("content", "author__username")
    list_filter = ("created_time",)
