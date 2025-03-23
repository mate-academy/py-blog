from django.contrib import admin
from django.contrib.auth.models import Group

from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("created_time", "owner")
    search_fields = ("title", "owner__username")
    date_hierarchy = "created_time"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    list_filter = ("created_time", "user")
    search_fields = ("content", "user__username")
