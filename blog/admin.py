from blog.models import User, Post, Commentary
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        "owner",
        "created_time",
    )
    list_filter = ["owner"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time"]
    list_filter = ["post", "user"]


admin.site.unregister(Group)
