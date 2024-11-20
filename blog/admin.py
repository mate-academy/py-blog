from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "content", "created_time"]
    search_fields = ["title"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_time", "content"]


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.unregister(Group)
