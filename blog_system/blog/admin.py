from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User

from .models import Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("owner", "title", "content", "created_time")
    list_filter = ("owner", "created_time")
    search_fields = ("title", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time", "content")
    list_filter = ("post", "created_time")
    search_fields = ("content", )
