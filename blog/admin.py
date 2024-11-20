from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Commentary


# Register your models here.
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    list_filter = ["username"]
    search_fields = ["username"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ["created_time"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    list_filter = ["created_time"]
    search_fields = ["user"]
