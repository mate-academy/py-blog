from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_time")
    search_fields = ("title", "content")
    list_filter = ("created_time",)


@admin.register(Comment)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_time")
    list_filter = ("created_time",)
    search_fields = ("content", "author__username")


admin.site.register(User)
admin.site.unregister(Group)
