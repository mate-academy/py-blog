from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    list_filter = ["created_time"]
    search_fields = ["title"]
    search_help_text = "Search post by title"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_time"]
    list_filter = ["created_time"]
    search_fields = ["user__username"]
    search_help_text = "Search comments by username"


admin.site.unregister(Group)
admin.site.register(User)
