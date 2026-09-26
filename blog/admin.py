from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]
    list_filter = ["created_time"]


class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_filter = ["created_time"]


admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Commentary, CommentaryAdmin)

admin.site.unregister(Group)
