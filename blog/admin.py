from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time", )
    search_fields = ("title", )
    list_filter = ("owner", "created_time", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("post", "created_time", )
    list_display = ("user", "post", "content", "created_time", )
    search_fields = ("content", )


admin.site.unregister(Group)
