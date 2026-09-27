from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog.models import User, Post, Commentary
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["created_time"]
    list_display = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]
    list_filter = ["created_time"]
    list_display = ["user"]


admin.site.unregister(Group)
