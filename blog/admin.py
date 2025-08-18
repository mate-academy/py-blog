from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary
from django.contrib.auth.models import Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "created_time"]
    search_fields = ("title",)
    list_filter = ["owner", "title", "created_time"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    search_fields = ("user", "post")
    list_filter = ["created_time"]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
