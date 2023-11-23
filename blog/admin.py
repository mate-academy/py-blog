from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post, Commentary, User

admin.site.register(User)
admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]
    list_filter = ["created_time"]
